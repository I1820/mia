from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Mode(ActuatorThing):
    """
    This class represents Lamp actuator
    """

    name = "mode"

    on: Setting[bool] = Setting()
