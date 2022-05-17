import typing

from ..domain.notif import I1820Notification
from .base import Controller


class AbstractNotification(typing.Protocol):
    def publish(self, body: str):
        pass


class NotificationController(Controller):
    '''
    The NotificationController controls notifications. these notifications
    base on :class:`I1820Notification`.
    '''

    mqtt_service: typing.Optional[AbstractNotification] = None

    def notify(self, notification: I1820Notification):
        assert self.mqtt_service is not None
        self.mqtt_service.publish(notification.to_json())
