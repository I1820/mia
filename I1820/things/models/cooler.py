# In The Name Of God
# ========================================
# [] File Name : cooler.py
#
# [] Creation Date : 02-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..actuator import ActuatorThing
from ..types import Setting


class Cooler(ActuatorThing):
    """
    This class represents Cooler actuator
    """

    name = "cooler"

    on = Setting()

    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
