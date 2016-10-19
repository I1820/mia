# In The Name Of God
# ========================================
# [] File Name : gas.py
#
# [] Creation Date : 17-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing
from .types import State

class Gas(SensorThing):
    """
    This class represents Gas sensor
    """
    name = "gas"

    gas = State('gas')

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
