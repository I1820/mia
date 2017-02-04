# In The Name Of God
# ========================================
# [] File Name : model.py
#
# [] Creation Date : 14-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..things.base import Things
from ..things.sensor import SensorThing
from ..things.actuator import ActuatorThing

from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
         Validate, Invalidate, Instantiate


@ComponentFactory("model_factory")
@Provides("model_service")
@Property("default")
@Instantiate("default_model_instance")
class ModelService:
    def __init__(self):
        pass

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Model Service")

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        pass

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
