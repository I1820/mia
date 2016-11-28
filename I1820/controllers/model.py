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
        response = {}
        response['type'] = thing
        if ActuatorThing in thing_cls.__bases__:
            response['master'] = 'actuator'
            response['settings'] = thing_cls.settings
        elif SensorThing in thing_cls.__bases__:
            response['master'] = 'sensor'
            response['states'] = thing_cls.states \
                if hasattr(thing_cls, 'states') else []
            response['events'] = thing_cls.events \
                if hasattr(thing_cls, 'events') else []
        else:
            pass
        return response
