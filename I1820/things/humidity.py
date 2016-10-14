# In The Name Of God
# ========================================
# [] File Name : humidity.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing


class Humidity(SensorThing):
    """
    This class represents Humidity sensor
    """
    name = "humidity"
    allowed_states = ['humidity']

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
