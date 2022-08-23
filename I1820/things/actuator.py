from .base import Thing


class ActuatorThing(Thing):
    def __init__(self, agent_id: str, device_id: str):
        super().__init__(agent_id, device_id)
