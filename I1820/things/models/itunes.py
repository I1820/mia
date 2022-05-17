from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Itunes(ActuatorThing):
    """
    This class represents Itunes controller
    """

    name = "itunes"

    play = Setting()
    direction = Setting()
