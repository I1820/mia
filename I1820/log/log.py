# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime


class I1820Logger:
    def __init__(self, timestamp: datetime.datetime,
                 data: dict, endpoint: str):
        self._status = data['status']
        for key, value in data['status'].items():
            setattr(self, key, value)
        self.timestamp = timestamp
        self.endpoint = endpoint

    def save(self):
        for key, value in self._status.items():
            pass

    @classmethod
    def last(cls, me):
        pass
