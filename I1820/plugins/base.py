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

from ..things.base import Things


class Plugins(abc.ABCMeta):
    plugins = {}

    def __new__(cls, name, bases, namespace):
        instance = abc.ABCMeta.__new__(
            cls, name, bases, namespace)
        if isinstance(instance.name, str):
            cls.plugins[instance.name] = instance
        return instance

    @classmethod
    def get(cls, name):
        if name not in cls.plugins.keys():
            importlib.import_module('I1820.plugins.%s' % name)
        return cls.plugins[name]


class Plugin(metaclass=Plugins):
    def __init__(self, ident):
        self.ident = ident

    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

    def notify(self, rpi_id, device_id, type, settings):
        thing = Things.get(type).get_thing(rpi_id, device_id)

        for key, value in settings.items():
            setattr(thing, key, value)

    @abc.abstractmethod
    def on_log(self, log):
        raise NotImplemented()
