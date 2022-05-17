from ..fields.state import State
from ..sensor import SensorThing


class Humidity(SensorThing):
    """
    This class represents Humidity sensor
    """
    name = "humidity"

    humidity = State()
