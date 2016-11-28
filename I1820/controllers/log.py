# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import importlib

from .base import I1820Controller
from ..conf.config import cfg


class LogController(I1820Controller):
    def __init__(self):
        appender_name = cfg.appenders_appender
        appender_module = importlib.import_module(
            'I1820.appenders.%s' % appender_name)
        appender_cls = getattr(
            appender_module, "%sLogAppender" % appender_name.title())
        self.appender = appender_cls()

    def save(self, measurement, agent_id, device_id, time, value):
        return self.appender.save(measurement, agent_id,
                                  device_id, time, value)

    def last(self, measurement, agent_id, device_id):
        return self.appender.last(measurement, agent_id, device_id)
