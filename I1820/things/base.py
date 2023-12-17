'''
fundamental classes for dynamic managements of things models
using python code and without having any external source of description
like JSON or YAML.
'''
from __future__ import annotations

import re
import abc
import importlib
import typing

from ..exceptions.thing import (ThingNotFoundException,
                                ThingTypeNotImplementedException)
from .fields.base import Field


class Things():
    '''
    Things class manages loaded things so we can get them by their name.
    '''
    things: dict[str, type[Thing]] = {}

    @classmethod
    def set(cls, name: str, thing: type[Thing]):
        '''
        Provide a thing class with its name for future
        referencing.
        '''
        cls.things[name] = thing

    @classmethod
    def get(cls, name: str) -> type[Thing]:
        '''
        Return the thing class by its name property.
        It will load these classes on-demand from the
        models package.
        '''
        if name not in cls.things:
            try:
                importlib.import_module(f'I1820.things.models.{name}')
            except ImportError as exception:
                raise ThingTypeNotImplementedException(name, exception) \
                    from exception
        return cls.things[name]


class AbstractThing(abc.ABCMeta):
    '''
    Abstract class for things which controls the instantiation
    of the Thing classes.
    '''
    @typing.override
    def __new__(mcs, name, bases, namespace):
        instance = abc.ABCMeta.__new__(
            mcs, name, bases, namespace)

        # Thing itself should need to be defined, so treat
        # it as normal.
        try:
            Thing
        except NameError:
            return instance

        # Thing sub-classes can use abstract to remove themselves from
        # things tree.
        if namespace.get("abstract", False):
            return instance
        
        # meta class is used only for thing so every instances should
        # be thing or its sub-classes.

        if 'name' not in namespace or not isinstance(namespace['name'], str) \
                or namespace['name'] == "":
            # convert class name from camel case to snake case.
            namespace['name'] = re.sub(r'(?<!^)(?=[A-Z])', '_', name).lower()
            instance.name = namespace['name']

        assert isinstance(instance, type(Thing))
        Things.set(namespace['name'], instance)
        instance.registered_things[namespace['name']] = {}


        for _, value in namespace.items():
            if isinstance(value, Field):
                if hasattr(instance, value.field_name):
                    getattr(instance, value.field_name).append(value)
                else:
                    setattr(instance, value.field_name, [value])
        return instance


class Thing(metaclass=AbstractThing):
    '''
    Thing class has all of the instances of that class.
    For example Lamp is a thing and for each lamp we will have
    a record in the registered_things map based on the agent_id
    and device_id.

    registered thing is defined over the thing class and it is shared between
    all the instances.
    '''
    registered_things: dict[str, dict[tuple[str, str], Thing]] = {}
    name: str = ""

    # these properties filled by `field_name` of the fields.
    statistics: list[Field] = []
    settings: list[Field] = []
    events: list[Field] = []
    states: list[Field] = []

    @classmethod
    def to_dict(cls) -> dict:
        '''
        create a dict representation of the thing properties.
        '''
        response: dict[str, list[str] | str] = {}
        response['type'] = cls.name
        response['master'] = [str(c) for c in cls.__bases__]
        response['statistics'] = [s.name for s in cls.statistics]
        response['settings'] = [s.name for s in cls.settings]
        response['states'] = [s.name for s in cls.states]
        response['events'] = [e.name for e in cls.events]
        return response

    def __init__(self, agent_id: str, device_id: str):
        self.agent_id = agent_id
        self.device_id = device_id

    @classmethod
    def get_thing(cls, agent_id: str, device_id: str) -> Thing:
        try:
            thing = cls.registered_things[cls.name][(agent_id, device_id)]
        except (KeyError, ValueError) as exception:
            raise ThingNotFoundException(agent_id, device_id, cls.name,
                                         exception) from exception
        return thing

    @classmethod
    def new_thing(cls, agent_id: str, device_id: str):
        if (agent_id, device_id) not in cls.registered_things[cls.name]:
            cls.registered_things[cls.name][(agent_id, device_id)] = \
                    cls(agent_id, device_id)

    @classmethod
    def del_thing(cls, agent_id: str, device_id: str):
        if cls.name in cls.registered_things:
            if (agent_id, device_id) in cls.registered_things[cls.name]:
                del cls.registered_things[cls.name][(agent_id, device_id)]

    @classmethod
    def has_thing(cls, agent_id: str, device_id: str):
        if cls.name in cls.registered_things:
            if (agent_id, device_id) in cls.registered_things[cls.name]:
                return True
        return False
