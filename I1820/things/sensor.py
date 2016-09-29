# In The Name Of God
# ========================================
# [] File Name : sensor.py
#
# [] Creation Date : 07-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc

from .base import Thing
from ..controller.log import LogController
from ..exceptions.thing import ThingInvalidAccessException


def make_event_setter(event):
    def event_setter(self, value):
        if isinstance(value, dict):
            setattr(self, "_%s" % event, value['time'])
    return event_setter


def make_event_getter(event):
    def event_getter(self):
        time = getattr(self, "_%s" % event)
        return time.strftime("%Y-%m-%dT%H:%M:%SZ")
    return event_getter


class SensorThing(Thing):

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)
        for allowed_event in self.allowed_events:
            setattr(type(self), allowed_event,
                    property(make_event_getter(allowed_event),
                             make_event_setter(allowed_event), None))

    @property
    @abc.abstractmethod
    def allowed_states(self):
        raise NotImplemented()

    @property
    def allowed_events(self):
        return []

    def __setattr__(self, name, value):
        if name in self.allowed_states:
            if isinstance(value, dict):
                LogController().save(name, self.name, self.rpi_id,
                                     self.device_id,
                                     value['time'], value['value'])
                return
            else:
                raise ThingInvalidAccessException(self.name, name)
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name not in self.allowed_states:
            raise ThingInvalidAccessException(self.name, name)
        value = LogController().last(
            name, self.rpi_id, self.device_id)
        return value
