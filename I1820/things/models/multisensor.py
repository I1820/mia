# In The Name Of God
# ========================================
# [] File Name : multisensor.py
#
# [] Creation Date : 21-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..sensor import SensorThing
from ..types import State, Event, Statistic


class MultiSensor(SensorThing):
    """
    This class represents Mutli Sensor
    """
    name = "multisensor"

    temperature = State()
    humidity = State()
    light = State()

    battery = Statistic()

    motion = Event()

    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
