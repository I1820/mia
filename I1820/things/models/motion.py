from ..fields.event import Event
from ..sensor import SensorThing


class Motion(SensorThing):
    """
    This class represents Motion detector
    """
    name = "motion"

    motion = Event()
