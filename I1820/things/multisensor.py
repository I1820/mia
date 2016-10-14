# In The Name Of God
# ========================================
# [] File Name : multisensor.py
#
# [] Creation Date : 21-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing


class MultiSensor(SensorThing):
    """
    This class represents Mutli Sensor
    """
    name = "multisensor"
    allowed_states = ['temperature', 'humidity', 'light']
    allowed_events = ['motion']

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
