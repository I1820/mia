from ...exceptions.thing import ThingInvalidAccessException
from ...controllers.log import LogController
from .base import Field


class State(Field):
    field_name = 'states'

    def __init__(self):
        super().__init__()
        self.storage = {}

    def __get__(self, obj, objtype):
        value = LogController().last(
            self.name, obj.agent_id, obj.device_id)
        return value

    def __set__(self, obj, value):
        if isinstance(value, dict):
            # TODO: checks last cached value with new value
            # caches last value for renewing instead of inserting
            self.storage[(obj.agent_id, obj.device_id)] = value
            LogController().save(self.name, obj.agent_id,
                                 obj.device_id,
                                 value['time'], value['value'])
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)
