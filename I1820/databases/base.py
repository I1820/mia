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


class I1820LogAppender(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def create(self, measurement, agent_id, device_id, time: datetime.datetime,
               value):
        raise NotImplemented()

    @abc.abstractmethod
    def retrieve_last(self, measurement, agent_id, device_id):
        raise NotImplemented()

    @abc.abstractmethod
    def retrieve_since(self, measurement, agent_id, device_id, since, limit):
        raise NotImplemented()

    @abc.abstractmethod
    def update(self, measurement, agent_id, device_id,
               time: datetime.datetime):
        raise NotImplemented()
