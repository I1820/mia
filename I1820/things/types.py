# In The Name Of God
# ========================================
# [] File Name : types.py
#
# [] Creation Date : 19-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..exceptions.thing import ThingInvalidAccessException
from ..controllers.log import LogController
from ..controllers.notif import NotificationController
from ..controllers.event import EventController
from ..domain.notif import I1820Notification
from ..domain.event import I1820Event


class Event:
    def __init__(self):
        self.name = None
        self.storage = {}

    def __get__(self, obj, objtype):
        time = self.storage.get((obj.agent_id, obj.device_id), None)
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")\
            if time is not None else None

    def __set__(self, obj, value):
        if isinstance(value, dict):
            self.storage[(obj.agent_id, obj.device_id)] = value['time']


class State:
    def __init__(self):
        self.name = None

    def __get__(self, obj, objtype):
        value = LogController().last(
            self.name, obj.agent_id, obj.device_id)
        return value

    def __set__(self, obj, value):
        if isinstance(value, dict):
            LogController().save(self.name, obj.agent_id,
                                 obj.device_id,
                                 value['time'], value['value'])
            data = {
                'rpi_id': obj.agent_id,
                'device_id': obj.device_id,
                'state': {
                    self.name: {
                        'value': value['value'],
                        'time': value['time'].strftime("%Y-%m-%dT%H:%M:%SZ")
                    }
                }
            }
            EventController().event(I1820Event('log', data))
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)


class Statistic:
    def __init__(self):
        self.name = None
        self.storage = {}

    def __get__(self, obj, objtype):
        time = self.storage.get((obj.agent_id, obj.device_id), None)
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")\
            if time is not None else None

    def __set__(self, obj, value):
        if isinstance(value, dict):
            self.storage[(obj.agent_id, obj.device_id)] = value['time']


class Setting:
    def __init__(self):
        self.name = None

    def __get__(self, obj, objtype):
        pass

    def __set__(self, obj, value):
        message = I1820Notification(obj.name, obj.device_id,
                                    {self.name: value}, obj.agent_id)
        NotificationController().notify(message)
