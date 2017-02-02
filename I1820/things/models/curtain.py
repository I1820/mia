from ..actuator import ActuatorThing
from ..types import Setting


class Curtain(ActuatorThing):
    """
    This class represents Curtain actuator
    """

    name = "curtain"

    height = Setting(type="integer")
