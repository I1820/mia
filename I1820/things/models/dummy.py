from ..fields.state import State
from ..sensor import SensorThing


class Dummy(SensorThing):
    """
    This class represents Dummy sensor
    """
    name = "dummy"

    chert = State()
