import datetime
import typing

from .base import LogAppender


class LogService:
    def __init__(self, appender: LogAppender):
        self.appender: LogAppender = appender

    def create(self, measurement, agent_id: str,
               device_id: str, time: datetime.datetime, value: typing.Any):
        return self.appender.create(measurement, agent_id,
                                    device_id, time, value)

    def retrieve_last(self, measurement, agent_id: str, device_id: str):
        return self.appender.retrieve_last(measurement, agent_id, device_id)
