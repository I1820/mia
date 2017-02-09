from ..actuator import ActuatorThing
from ..fields import Setting


class Alarm(ActuatorThing):
    """
    This class represents Alarm actuator
    """

    name = "alarm"

    on = Setting()
