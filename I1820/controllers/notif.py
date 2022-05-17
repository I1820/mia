from ..domain.notif import I1820Notification
from ..mqtt import MQTTService
from .base import Controller


class NotificationController(Controller):
    '''
    The NotificationController controls notifications. these notifications
    base on :class:`I1820Notification`.
    '''

    mqtt_service: MQTTService

    def __init__(self):
        pass

    def notify(self, notification: I1820Notification):
        self.mqtt_service.publish(notification.to_json())
