from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Projector(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    name = "projector"

    on = Setting()
    input = Setting()
