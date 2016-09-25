# In The Name Of God
# ========================================
# [] File Name : humidity.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .sensor import SensorThing


class Motion(SensorThing):
    """
    This class represents Motion detector
    """
    name = "motion"

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)

    @property
    def allowed_states(self):
        return []

    @property
    def allowed_events(self):
        return ['motion']
