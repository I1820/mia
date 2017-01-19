# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 28-11-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc
import datetime


class I1820LogAppender:
    @abc.abstractmethod
    def save(self, measurement, agent_id, device_id, time: datetime.datetime,
             value):
        raise NotImplemented()

    @abc.abstractmethod
    def last(self, measurement, agent_id, device_id):
        raise NotImplemented()

    @abc.abstractmethod
    def since(self, measurement, agent_id, device_id, since, limit):
        raise NotImplemented()
