from ...domain.event import I1820Event
from ...controllers.event import EventController
from .base import Field


class Event(Field):
    field_name = 'events'

    def __init__(self):
        self.storage = {}

    def __get__(self, obj, objtype):
        time = self.storage.get((obj.agent_id, obj.device_id), None)
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")\
            if time is not None else None

    def __set__(self, obj, value):
        if isinstance(value, dict):
            self.storage[(obj.agent_id, obj.device_id)] = value['time']
            data = {
                'agent_id': obj.agent_id,
                'device_id': obj.device_id,
                'type': obj.name,
                'state': {
                    self.name: {
                        'value': value['value'],
                        'time': value['time'].strftime("%Y-%m-%dT%H:%M:%SZ")
                    }
                }
            }
            EventController().event(I1820Event('event', data))
