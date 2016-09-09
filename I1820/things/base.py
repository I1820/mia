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
        if isinstance(cls.name, str):
            metaclass.things[cls.name] = cls
        return cls

    @classmethod
    def get(cls, name):
        if name not in cls.things:
            importlib.import_module('I1820.things.%s' % name)
        return cls.things[name]


class Thing(metaclass=Things):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

    @abc.abstractmethod
    def get_thing(self, rpi_id, device_id):
        pass

    @abc.abstractmethod
    def new_thing(self, rpi_id, device_id):
        pass
