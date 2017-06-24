from ..actuator import ActuatorThing
from ..fields import Setting


class Valve(ActuatorThing):
    """
    This class represents Valve actuator
    """

    name = "valve"

    on = Setting()
