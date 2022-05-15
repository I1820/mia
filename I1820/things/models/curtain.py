from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Curtain(ActuatorThing):
    """
    This class represents Curtain actuator
    """

    name = "curtain"

    height: Setting[int] = Setting()
