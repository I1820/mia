# In The Name Of God
# ========================================
# [] File Name : cooler.py
#
# [] Creation Date : 02-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .actuator import ActuatorThing


class Cooler(ActuatorThing):
    """
    This class represents Cooler actuator
    """

    name = "cooler"
    allowed_settings = ['on']

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
