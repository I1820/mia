# In The Name Of God
# ========================================
# [] File Name : lamp.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .actuator import ActuatorThing
from ..domain import I1820Notification
from ..controller import NotificationController


class Lamp(ActuatorThing):
    """
    This class represents Lamp actuator
    """
    name = "lamp"

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)

    @property
    def on(self):
        """
        On property is used as a trigger for lamp status.
        """
        raise ValueError('Actuator settings are not readable')

    @on.setter
    def on(self, on: bool):
        message = I1820Notification('lamp', self.device_id, {'on': on},
                                    self.rpi_id)
        NotificationController().notify(message)
