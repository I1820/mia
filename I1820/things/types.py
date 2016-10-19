# In The Name Of God
# ========================================
# [] File Name : types.py
#
# [] Creation Date : 19-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..controller.log import LogController
from ..exceptions.thing import ThingInvalidAccessException
from ..controller.notif import NotificationController
from ..domain.notif import I1820Notification


class Event:
    def __init__(self):
        self.name = None
        self.storage = {}

    def __get__(self, obj, objtype):
        time = self.storage.get((obj.rpi_id, obj.device_id), None)
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")\
            if time is not None else None

    def __set__(self, obj, value):
        if isinstance(value, dict):
            self.storage[(obj.rpi_id, obj.device_id)] = value['time']


class State:
    def __init__(self):
        self.name = None

    def __get__(self, obj, objtype):
        value = LogController().last(
            self.name, obj.rpi_id, obj.device_id)
        return value

    def __set__(self, obj, value):
        if isinstance(value, dict):
            LogController().save(self.name, obj.rpi_id,
                                 obj.device_id,
                                 value['time'], value['value'])
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)


class Setting:
    def __init__(self):
        self.name = None

    def __get__(self, obj, objtype):
        pass

    def __set__(self, obj, value):
        message = I1820Notification(obj.name, obj.device_id,
                                    {self.name: value}, obj.rpi_id)
        NotificationController().notify(message)
