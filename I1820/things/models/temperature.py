from ..fields.state import State
from ..sensor import SensorThing


class Temperature(SensorThing):
    """
    This class represents Temperature sensor
    """
    name = "temperature"

    temperature = State()
