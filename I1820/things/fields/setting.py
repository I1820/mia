from ...controllers.notif import NotificationController
from ...domain.notif import I1820Notification
from .base import Field


class Setting(Field):
    field_name = 'settings'

    def __init__(self, type='bool'):
        super().__init__()
        self.type = type
        self.storage = {}

    def __get__(self, obj, objtype):
        return self.storage[(obj.agent_id, obj.devivce_id)]

    def __set__(self, obj, value):
        message = I1820Notification(obj.name, obj.device_id,
                                    [{'name': self.name, 'value': value}],
                                    obj.agent_id)
        self.storage[(obj.agent_id, obj.device_id)] = value
        NotificationController().notify(message)
