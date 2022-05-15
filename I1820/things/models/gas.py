from ..fields.state import State
from ..sensor import SensorThing


class Gas(SensorThing):
    """
    This class represents Gas sensor
    """
    name = "gas"

    gas = State()
