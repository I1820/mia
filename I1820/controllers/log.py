import datetime
import typing

from ..databases import LogService
from .base import Controller


class LogController(Controller):
    '''
    log controller stores the given logs into the storage.
    '''

    log_service: LogService

    def create(self, measurement, agent_id: str,
               device_id: str, time: datetime.datetime, value: typing.Any):
        return self.log_service.create(measurement, agent_id,
                                       device_id, time, value)

    def retrieve_last(self, measurement, agent_id: str, device_id: str):
        return self.log_service.retrieve_last(measurement, agent_id, device_id)
