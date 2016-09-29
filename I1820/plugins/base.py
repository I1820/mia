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
import requests


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
        if name not in cls.services.keys():
            importlib.import_module('I1820.plugins.%s' % name)
        return cls.plugins[name]


class Plugin(metaclass=Plugins):
    @property
    @abc.abstractmethod
    def name(self):
        raise NotImplemented()

    def notify(self, rpi_id, device_id, type, settings):
        data = {
            'type': type,
            'rpi_id': rpi_id,
            'device_id': device_id,
            'settings': settings
        }
        requests.put('thing', json=data)

    @abc.abstractmethod
    def on_log(self):
        raise NotImplemented()
