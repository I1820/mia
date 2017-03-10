# In The Name Of God
# ========================================
# [] File Name : state.py
#
# [] Creation Date : 10-03-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ...exceptions.thing import ThingInvalidAccessException
from ...services.master import service_master
from .base import Field


class State(Field):
    field_name = 'states'

    def __init__(self):
        super().__init__()

    def __get__(self, obj, objtype):
        with service_master.service('log_service') as log_service:
            value = log_service.last(
                self.name, obj.agent_id, obj.device_id)
        return value

    def __set__(self, obj, value):
        if isinstance(value, dict):
            with service_master.service('log_service') as log_service:
                log_service.save(self.name, obj.agent_id,
                                 obj.device_id,
                                 value['time'], value['value'])
            return
        else:
            raise ThingInvalidAccessException(obj.name, self.name)
