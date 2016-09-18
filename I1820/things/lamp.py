# In The Name Of God
# ========================================
# [] File Name : lamp.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .actuator import ActuatorThing


class Lamp(ActuatorThing):
    """
    This class represents Lamp actuator
    """
    name = "lamp"

    def __init__(self, rpi_id, device_id):
        self.rpi_id = rpi_id
        self.device_id = device_id

    @property
    def on(self):
        """
        On property is used as a trigger for lamp status.
        """
        raise ValueError('Actuator settings are not readable')

    @on.setter
    def on(self, on: bool):
        message = {'id': self.device_id, 'settings': {'on': on},
                   'type': 'lamp'}
        print(message)
