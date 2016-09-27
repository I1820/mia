# In The Name Of God
# ========================================
# [] File Name : dummy.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing


class Dummy(SensorThing):
    """
    This class represents Dummy sensor
    """
    name = "dummy"

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)

    @property
    def allowed_states(self):
        return ['chert']
