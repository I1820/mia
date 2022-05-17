from ..fields.event import Event
from ..fields.state import State
from ..fields.statistic import Statistic
from ..sensor import SensorThing


class MultiSensor(SensorThing):
    """
    Mutli-Sensor which is buit by Sepehr Hashtroudi in Aolab @ 2016
    """
    name = "multisensor"

    temperature = State()
    humidity = State()
    light = State()

    battery = Statistic()

    motion = Event()
