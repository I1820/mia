from ..fields.state import State
from ..sensor import SensorThing


class Light(SensorThing):
    """
    This class represents Light sensor
    """
    name = "light"

    light = State()
