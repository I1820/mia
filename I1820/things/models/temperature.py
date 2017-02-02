# In The Name Of God
# ========================================
# [] File Name : temperature.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..sensor import SensorThing
from ..types import State


class Temperature(SensorThing):
    """
    This class represents Temperature sensor
    """
    name = "temperature"

    temperature = State()
