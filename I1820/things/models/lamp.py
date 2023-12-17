from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Lamp(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    on: Setting[bool] = Setting()
