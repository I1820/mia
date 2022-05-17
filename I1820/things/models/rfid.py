from ..fields.state import State
from ..sensor import SensorThing


class RFID(SensorThing):
    """
    This class represents Motion detector
    """
    name = "rfid"

    uid = State()
