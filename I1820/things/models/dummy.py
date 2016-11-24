# In The Name Of God
# ========================================
# [] File Name : dummy.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..sensor import SensorThing
from ..types import State


class Dummy(SensorThing):
    """
    This class represents Dummy sensor
    """
    name = "dummy"

    chert = State()

    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
