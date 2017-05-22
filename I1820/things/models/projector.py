# In The Name Of God
# ========================================
# [] File Name : lamp.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..actuator import ActuatorThing
from ..fields import Setting


class Projector(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    name = "projector"

    on = Setting()
    input = Setting()
