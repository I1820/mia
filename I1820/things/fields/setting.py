import typing

# from ...controllers.notif import NotificationController
from ...domain.notif import I1820Notification
from ..base import Thing
from .base import Field

T = typing.TypeVar('T')

class Setting(Field, typing.Generic[T]):
    field_name = 'settings'

    def __init__(self):
        super().__init__()
        self.storage: dict[tuple[str, str], T] = {}

    def __get__(self, obj: Thing, objtype) -> T:
        return self.storage[(obj.agent_id, obj.device_id)]

    def __set__(self, obj: Thing, value: T):
        I1820Notification(obj.name, obj.device_id,
                          [{'name': self.name, 'value': value}],
                          obj.agent_id)
        self.storage[(obj.agent_id, obj.device_id)] = value
        # NotificationController().notify(message)
