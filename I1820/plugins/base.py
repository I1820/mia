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


class Plugins(abc.ABCMeta):
    plugins = {}

    def __new__(metaclass, name, bases, namespace):
        cls = abc.ABCMeta.__new__(
            metaclass, name, bases, namespace)
        if isinstance(cls.name, str):
            metaclass.plugins[cls.name] = cls()
        return cls

    @classmethod
    def get(cls, name):
        if name not in cls.services.keys():
            importlib.import_module('I1820.services.%s' % name)
        return cls.plugins[name]


class Plugin(metaclass=Plugins):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()
