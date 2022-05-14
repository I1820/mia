from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Lamp(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    name = "lamp"

    on: Setting[bool] = Setting()
