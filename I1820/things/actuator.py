# In The Name Of God
# ========================================
# [] File Name : actuator.py
#
# [] Creation Date : 07-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc

from .base import Thing
from ..domain.notif import I1820Notification
from ..controller.notif import NotificationController
from ..exceptions.thing import ThingInvalidAccessException


class ActuatorThing(Thing):
    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)

    @property
    @abc.abstractmethod
    def allowed_settings(self):
        raise NotImplemented()

    def __setattr__(self, name, value):
        if name in self.allowed_settings:
            message = I1820Notification(self.name, self.device_id,
                                        {name: value}, self.rpi_id)
            NotificationController().notify(message)
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name in self.allowed_settings:
            raise ThingInvalidAccessException(self.name, name)
