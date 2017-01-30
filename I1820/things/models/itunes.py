from ..actuator import ActuatorThing
from ..types import Setting


class Itunes(ActuatorThing):
    """
    This class represents Itunes controller
    """

    name = "itunes"

    play = Setting()
    direction = Setting()

    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
