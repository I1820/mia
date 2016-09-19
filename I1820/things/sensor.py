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


class SensorThing(Thing):

    def __init__(self, rpi_id, device_id):
        super().__init__(rpi_id, device_id)

    @property
    @abc.abstractmethod
    def allowed_states(self):
        raise NotImplemented()

    def __setattr__(self, name, value):
        if name in self.allowed_states:
            if isinstance(value, dict):
                LogController().save(name, self.name, self.rpi_id,
                                     self.device_id,
                                     value['time'], value['value'])
                return
            else:
                raise ValueError(
                    'Sensor states are not writeable by %s' % type(value))
        super().__setattr__(name, value)

    def __getattr__(self, name):
        if name not in self.allowed_states:
            raise ValueError(
                'There is no %s state on %s sensor' % (name, self.name))
        value = LogController().last(
            name, self.rpi_id, self.device_id)
        return value
