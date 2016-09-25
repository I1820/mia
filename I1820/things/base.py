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

from ..exceptions.thing import ThingNotFoundException


class Things(abc.ABCMeta):
    things = {}

    def __new__(cls, name, bases, namespace):
        instance = abc.ABCMeta.__new__(
            cls, name, bases, namespace)
        if isinstance(instance.name, str):
            cls.things[instance.name] = cls
            instance.things[instance.name] = {}
        return instance

    @classmethod
    def get(cls, name):
        if name not in cls.things:
            importlib.import_module('I1820.things.%s' % name)
        return cls.things[name]


class Thing(metaclass=Things):
    things = {}

    def __init__(self, rpi_id, device_id):
        self.rpi_id = rpi_id
        self.device_id = device_id

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

    @classmethod
    def get_thing(cls, rpi_id, device_id):
        try:
            thing = cls.things[cls.name][(rpi_id, device_id)]
        except KeyError as e:
            raise ThingNotFoundException(rpi_id, device_id, cls.name, e)
        return thing

    @classmethod
    def new_thing(cls, rpi_id, device_id):
        cls.things[cls.name][(rpi_id, device_id)] = cls(rpi_id, device_id)

    @classmethod
    def has_thing(cls, rpi_id, device_id):
        if cls.name in cls.things:
            if (rpi_id, device_id) in cls.things[cls.name]:
                return True
        return False
