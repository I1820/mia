from .actuator import ActuatorThing
from .base import Things
from .sensor import SensorThing


class ModelService:
    '''
    model service loads things models
    '''
    def __init__(self):
        print(" * 18.20 Service: Model Service")

    def get_model(self, thing):
        thing_cls = Things.get(thing)
        response = {}
        response['type'] = thing
        response['statistics'] = [s.name for s in thing_cls.statistics] \
            if hasattr(thing_cls, 'statistics') else []
        if ActuatorThing in thing_cls.__bases__:
            response['master'] = 'actuator'
            response['settings'] = [{'name': s.name, 'type': s.type}
                                    for s in thing_cls.settings]
        elif SensorThing in thing_cls.__bases__:
            response['master'] = 'sensor'
            response['states'] = [s.name for s in thing_cls.states] \
                if hasattr(thing_cls, 'states') else []
            response['events'] = [e.name for e in thing_cls.events] \
                if hasattr(thing_cls, 'events') else []
        else:
            pass
        return response
