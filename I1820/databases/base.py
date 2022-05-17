import abc
import datetime
import typing


class LogAppender(metaclass=abc.ABCMeta):
    '''
    abstract log appender to implement different log storages.
    '''

    @abc.abstractmethod
    def create(self, measurement: typing.Any, agent_id: str, device_id: str, time: datetime.datetime,
               value: typing.Any):
        raise NotImplementedError()

    @abc.abstractmethod
    def retrieve_last(self, measurement: typing.Any, agent_id: str, device_id: str):
        raise NotImplementedError()

    @abc.abstractmethod
    def retrieve_since(self, measurement: typing.Any, agent_id: str, device_id: str, since: datetime.datetime, limit: int):
        raise NotImplementedError()

    @abc.abstractmethod
    def update(self, measurement, agent_id, device_id,
               time: datetime.datetime):
        raise NotImplementedError()
