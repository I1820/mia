# In The Name Of God
# ========================================
# [] File Name : motion.py
#
# [] Creation Date : 10-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..sensor import SensorThing
from ..types import Event


class Motion(SensorThing):
    """
    This class represents Motion detector
    """
    name = "motion"

    motion = Event()
