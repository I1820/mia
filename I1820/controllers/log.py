import datetime
import typing

from .base import Controller


class AbstractLog(typing.Protocol):
    def create(self, measurement, agent_id: str,
               device_id: str, time: datetime.datetime, value: typing.Any):
        pass

    def retrieve_last(self, measurement, agent_id: str, device_id: str):
        pass


class LogController(Controller):
    '''
    log controller stores the given logs into the storage.
    '''

    log_service: typing.Optional[AbstractLog] = None

    def create(self, measurement, agent_id: str,
               device_id: str, time: datetime.datetime, value: typing.Any):
        assert self.log_service is not None
        return self.log_service.create(measurement, agent_id,
                                       device_id, time, value)

    def retrieve_last(self, measurement, agent_id: str, device_id: str):
        assert self.log_service is not None
        return self.log_service.retrieve_last(measurement, agent_id, device_id)
