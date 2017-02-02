from ...exceptions.thing import ThingInvalidAccessException
from ...controllers.log import LogController
from .base import Field


class State(Field):
    field_name = 'states'

    def __get__(self, obj, objtype):
        value = LogController().last(
            self.name, obj.agent_id, obj.device_id)
        return value

    def __set__(self, obj, value):
        if isinstance(value, dict):
            LogController().save(self.name, obj.agent_id,
                                 obj.device_id,
                                 value['time'], value['value'])
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)
