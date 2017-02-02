# In The Name Of God
# ========================================
# [] File Name : humidity.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..sensor import SensorThing
from ..types import State


class Light(SensorThing):
    """
    This class represents Light sensor
    """
    name = "light"

    light = State()
