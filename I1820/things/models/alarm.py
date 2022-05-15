from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Alarm(ActuatorThing):
    """
    This class represents Alarm actuator
    """

    name = "alarm"

    on: Setting[bool] = Setting()
