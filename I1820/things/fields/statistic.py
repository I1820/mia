from .base import Field


class Statistic(Field):
    field_name = 'statistics'

    def __init__(self):
        self.storage = {}

    def __get__(self, obj, objtype):
        value = self.storage.get((obj.agent_id, obj.device_id), None)
        if value is not None:
            result = {}
            result['time'] = value['time'].strftime("%Y-%m-%dT%H:%M:%SZ")
            result['value'] = value['value']
            return result
        else:
            return None

    def __set__(self, obj, value):
        if isinstance(value, dict):
            self.storage[(obj.agent_id, obj.device_id)] = value
