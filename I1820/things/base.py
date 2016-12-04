# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc
import importlib

from .types import Event, Setting, State, Statistic
from ..exceptions.thing import \
     ThingNotFoundException, ThingTypeNotImplementedException


class Things(abc.ABCMeta):
    things = {}

    def __new__(cls, name, bases, namespace):
        instance = abc.ABCMeta.__new__(
            cls, name, bases, namespace)

        if isinstance(instance.name, str):
            cls.things[instance.name] = instance
            instance.things[instance.name] = {}

        for k, v in namespace.items():
            if isinstance(v, State):
                v.name = k
                if hasattr(instance, 'states'):
                    instance.states.append(k)
                else:
                    instance.states = [k]
            if isinstance(v, Event):
                v.name = k
                if hasattr(instance, 'events'):
                    instance.events.append(k)
                else:
                    instance.events = [k]
            if isinstance(v, Setting):
                v.name = k
                if hasattr(instance, 'settings'):
                    instance.settings.append({
                        'name': k,
                        'type': v.type
                    })
                else:
                    instance.settings = [{
                        'name': k,
                        'type': v.type
                    }]
            if isinstance(v, Statistic):
                v.name = k
                if hasattr(instance, 'statistics'):
                    instance.statistics.append(k)
                else:
                    instance.statistics = [k]
        return instance

    @classmethod
    def get(cls, name):
        if name not in cls.things:
            try:
                importlib.import_module('I1820.things.models.%s' % name)
            except ImportError as e:
                raise ThingTypeNotImplementedException(name, e)
        return cls.things[name]


class Thing(metaclass=Things):
    things = {}

    def __init__(self, agent_id, device_id):
        self.agent_id = agent_id
        self.device_id = device_id

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

    @classmethod
    def get_thing(cls, agent_id, device_id):
        try:
            thing = cls.things[cls.name][(agent_id, device_id)]
        except (KeyError, ValueError) as e:
            raise ThingNotFoundException(agent_id, device_id, cls.name, e)
        return thing

    @classmethod
    def new_thing(cls, agent_id, device_id):
        cls.things[cls.name][(agent_id, device_id)] = cls(agent_id, device_id)

    @classmethod
    def del_thing(cls, agent_id, device_id):
        del cls.things[cls.name][(agent_id, device_id)]

    @classmethod
    def has_thing(cls, agent_id, device_id):
        if cls.name in cls.things:
            if (agent_id, device_id) in cls.things[cls.name]:
                return True
        return False
