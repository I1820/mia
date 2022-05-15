from ..fields.state import State
from ..sensor import SensorThing


class Accelerometer(SensorThing):
    """
    This class represents Accelerometer sensor
    """
    name = "accelerometer"

    accelerate = State()
