# In The Name Of God
# Creation Date : 1/29/17
# Created By : Mahtab Farrokh (mahtab.farrokh@gmail.com)


from ..actuator import ActuatorThing
from ..fields import Setting


class SmartLamp (ActuatorThing):
    """
    This class represents smart lamp actuator
    """

    name = "smartLamp"

    on = Setting()
    color = Setting(type='string')
    fade = Setting(type='integer')
