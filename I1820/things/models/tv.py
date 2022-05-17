from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Tv(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    name = "tv"

    on: Setting[bool] = Setting()
