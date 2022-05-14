# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 10-03-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime
import importlib

from ..conf.config import Config
from .base import LogAppender


class LogService:
    def __init__(self, cfg: Config):
        self.cfg = cfg
        print(" * Mia Log Appender Service")

        appender_name = cfg.appenders.name
        appender_module = importlib.import_module(
            'I1820.databases.%s' % appender_name)
        appender_cls = getattr(
            appender_module, "%sLogAppender" % appender_name.title())

        print(f" * Mia Log Appender based on {appender_name.title()}")

        self.appender: LogAppender = appender_cls()

    def create(self, measurement, agent_id: str, device_id: str, time: datetime.datetime, value):
        last_value = None
        if self.cfg.appenders.renew is True:
            last_value = self.appender.retrieve_last(measurement,
                                                     agent_id,
                                                     device_id)['value']

        if last_value is not None and value == last_value:
            return self.appender.update(measurement,
                                        agent_id,
                                        device_id, time)
        return self.appender.create(measurement, agent_id,
                                    device_id, time, value)

    def retrieve_last(self, measurement, agent_id: str, device_id: str):
        return self.appender.retrieve_last(measurement, agent_id, device_id)
