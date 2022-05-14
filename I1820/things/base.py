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
            instance.things[namespace['name']] = {}

        for key, value in namespace.items():
            if isinstance(value, Field):
                # set field name based on its name in the thing class
                value.name = key
                if hasattr(instance, value.field_name):
                    getattr(instance, value.field_name).append(value)
                else:
                    setattr(instance, value.field_name, [value])
        return instance

class Thing(metaclass=AbstractThing):
    things = {}
    name: str = ""

    def __init__(self, agent_id: str, device_id: str):
        self.agent_id = agent_id
        self.device_id = device_id

    @classmethod
    def get_thing(cls, agent_id, device_id):
        try:
            thing = cls.things[cls.name][(agent_id, device_id)]
        except (KeyError, ValueError) as exception:
            raise ThingNotFoundException(agent_id, device_id, cls.name,
                                         exception) from exception
        return thing

    @classmethod
    def new_thing(cls, agent_id, device_id):
        if (agent_id, device_id) not in cls.things[cls.name]:
            cls.things[cls.name][(agent_id, device_id)] = \
                    cls(agent_id, device_id)

    @classmethod
    def del_thing(cls, agent_id, device_id):
        if cls.name in cls.things:
            if (agent_id, device_id) in cls.things[cls.name]:
                del cls.things[cls.name][(agent_id, device_id)]

    @classmethod
    def has_thing(cls, agent_id, device_id):
        if cls.name in cls.things:
            if (agent_id, device_id) in cls.things[cls.name]:
                return True
        return False
