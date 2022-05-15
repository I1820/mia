from ..actuator import ActuatorThing
from ..fields.setting import Setting


class Cooler(ActuatorThing):
    """
    This class represents Cooler actuator
    """

    name = "cooler"

    on: Setting[bool] = Setting()
    temperature: Setting[int] = Setting()
