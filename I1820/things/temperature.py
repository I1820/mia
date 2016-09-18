# In The Name Of God
# ========================================
# [] File Name : temperature.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing


class Temperature(SensorThing):
    """
    This class represents Temperature sensor
    """
    name = "temperature"

    def __init__(self, rpi_id, device_id):
        self.rpi_id = rpi_id
        self.device_id = device_id
        self.allowed_states = ['temperature']
