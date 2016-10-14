# In The Name Of God
# ========================================
# [] File Name : model.py
#
# [] Creation Date : 14-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..things.base import Things
from ..things.sensor import SensorThing
from ..things.actuator import ActuatorThing


class ModelController(I1820Controller):
    def __init__(self):
        pass

    def get_model(self, thing):
        thing_cls = Things.get(thing)
        if isinstance(thing_cls, ActuatorThing):
            pass
        elif isinstance(thing_cls, SensorThing):
            pass
