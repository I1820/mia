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
    allowed_settings = ['on']

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
