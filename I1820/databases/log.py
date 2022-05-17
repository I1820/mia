import datetime
import importlib
import typing

from .base import LogAppender


class LogService:
    def __init__(self, appender_name: str, renew: bool):
        self.renew = renew

        appender_module = importlib.import_module(
            'I1820.databases.%s' % appender_name)
        appender_cls = getattr(
            appender_module, f"{appender_name.title()}LogAppender")

        print(f" * Mia Log Appender based on {appender_name.title()}")

        self.appender: LogAppender = appender_cls()

    def create(self, measurement, agent_id: str, device_id: str, time: datetime.datetime, value: typing.Any):
        last_value = None
        if self.renew is True:
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
