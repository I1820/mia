from ...controllers.notif import NotificationController
from ...domain.notif import I1820Notification
from .base import Field


class Setting(Field):
    field_name = 'settings'

    def __init__(self, type='bool'):
        self.type = type

    def __get__(self, obj, objtype):
        pass

    def __set__(self, obj, value):
        message = I1820Notification(obj.name, obj.device_id,
                                    [{'name': self.name, 'value': value}],
                                    obj.agent_id)
        NotificationController().notify(message)
