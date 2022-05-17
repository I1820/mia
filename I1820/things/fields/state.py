from ...exceptions.thing import ThingInvalidAccessException
from ...services.master import service_master
from ..base import Thing
from .base import Field


class State(Field):
    field_name = 'states'

    def __init__(self):
        super().__init__()

    def __get__(self, obj: Thing, _):
        with service_master.service('log_service') as log_service:
            value = log_service.retrieve_last(
                self.name, obj.agent_id, obj.device_id)
        return value

    def __set__(self, obj: Thing, value):
        if isinstance(value, dict):
            with service_master.service('log_service') as log_service:
                log_service.create(self.name, obj.agent_id,
                                   obj.device_id,
                                   value['time'], value['value'])
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)
