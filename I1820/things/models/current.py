from ..fields.state import State
from ..sensor import SensorThing


class Dummy(SensorThing):
    """
    This class represents Current sensor
    """
    name = "current"

    current = State()
