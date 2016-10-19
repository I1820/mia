# In The Name Of God
# ========================================
# [] File Name : lamp.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .actuator import ActuatorThing
from .types import Setting


class Lamp(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    name = "lamp"

    on = Setting()

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
