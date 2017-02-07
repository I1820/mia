from ..sensor import SensorThing
from ..fields import State


class Accelerometer(SensorThing):
    """
    This class represents Accelerometer sensor
    """
    name = "accelerometer"

    accelerate = State()
