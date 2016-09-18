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
    # TODO: Provide log analyzer

    @property
    @abc.abstractmethod
    def allowed_states(self):
        raise NotImplemented()

    def __setattr__(self, name, value):
        raise ValueError('Sensor states are not writeable')

    def __getattr__(self, name):
        if name not in self.allowed_states:
            raise ValueError(
                'There is no %s state on %s sensor' % (name, self.name))
        value = LogController().last(
            name, self.rpi_id, self.device_id)
        return value
