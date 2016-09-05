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


class Services(abc.ABCMeta):
    services = {}

    def __new__(metaclass, name, bases, namespace):
        cls = abc.ABCMeta.__new__(
            metaclass, name, bases, namespace)
        if isinstance(cls.name, str):
            metaclass.services[cls.name] = cls
        return cls

    @classmethod
    def get(cls, name):
        if name not in cls.things:
            importlib.import_module('I1820.services.%s' % name)
        return cls.things[name]
