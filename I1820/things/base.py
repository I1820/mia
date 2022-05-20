'''
fundamental classes for dynamic managements of things models.
'''
from __future__ import annotations

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
        cls.things[name] = thing

    @classmethod
    def get(cls, name: str) -> type[Thing]:
        '''
        return the thing class by its name property.
        it will load these classes on-demand.
        '''
        if name not in cls.things:
            try:
                importlib.import_module(f'I1820.things.models.{name}')
            except ImportError as exception:
                raise ThingTypeNotImplementedException(name, exception) \
                    from exception
        return cls.things[name]


class AbstractThing(abc.ABCMeta):
    def __new__(cls, name, bases, namespace):
        instance = abc.ABCMeta.__new__(
            cls, name, bases, namespace)

        # here we are wrongly consider all subclasses
        # of AbstractThing are Thing
        # please ignore the type error
        if 'name' in namespace and isinstance(namespace['name'], str) \
                and namespace['name'] != "":
            instance = typing.cast(type[Thing], instance)
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
