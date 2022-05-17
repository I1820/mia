# In The Name Of God
# Creation Date : 1/29/17
# Created By : Mahtab Farrokh (mahtab.farrokh@gmail.com)


from ..actuator import ActuatorThing
from ..fields.setting import Setting


class SmartLamp (ActuatorThing):
    """
    Colorful lamp which is built by Niligo.
    """

    name = "smartLamp"

    on = Setting()
    color: Setting[float] = Setting()
    fade: Setting[int] = Setting()
