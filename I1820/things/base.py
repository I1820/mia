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


class Things(abc.ABCMeta):
    things = {}

    def __new__(metaclass, name, bases, namespace):
        cls = abc.ABCMeta.__new__(
            metaclass, name, bases, namespace)
        if not hasattr(cls, 'things'):
            # If class has no things list, so it must be a Thing :D
            cls.things = {}
        else:
            # Register the new thing :D
            if isinstance(cls.name, str):
                cls.things[cls.name] = {}
        if isinstance(cls.name, str):
            metaclass.things[cls.name] = cls
        return cls

    @classmethod
    def get(cls, name):
        if name not in cls.things:
            importlib.import_module('I1820.things.%s' % name)
        return cls.things[name]


class Thing(metaclass=Things):
    things = {}

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

    @classmethod
    def get_thing(cls, rpi_id, device_id):
        thing = cls.things[cls.name][(rpi_id, device_id)]
        return thing

    @classmethod
    def new_thing(cls, rpi_id, device_id):
        cls.things[cls.name][(rpi_id, device_id)] = cls(rpi_id, device_id)
