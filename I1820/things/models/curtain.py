from ..actuator import ActuatorThing
from ..types import Setting


class Curtain(ActuatorThing):
    """
    This class represents Curtain actuator
    """

    name = "curtain"

    height = Setting(type="integer")

    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
