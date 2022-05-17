from ...controllers import LogController
from ...exceptions.thing import ThingInvalidAccessException
from ..base import Thing
from .base import Field


class State(Field):
    field_name = 'states'

    def __get__(self, obj: Thing, _):
        value = LogController().retrieve_last(
                self.name, obj.agent_id, obj.device_id)
        return value

    def __set__(self, obj: Thing, value):
        if isinstance(value, dict):
            LogController().create(self.name, obj.agent_id,
                                   obj.device_id,
                                   value['time'], value['value'])
        else:
            raise ThingInvalidAccessException(obj.name, self.name)
