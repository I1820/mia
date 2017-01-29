# In The Name Of God 
# Creation Date : 1/29/17
# Created By : Mahtab Farrokh (mahtab.farrokh@gmail.com)


from ..actuator import ActuatorThing
from ..types import Setting

class SmartLamp (ActuatorThing) :
    """
    This class represents smart lamp actuator
    """

    name = "smartLamp"

    color = Setting(type = 'string')

    def __init__(self, agent_id, device_id):
        super().__init__(agent_id, device_id)
