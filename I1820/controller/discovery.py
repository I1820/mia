# In The Name Of God
# ========================================
# [] File Name : discovery.py
#
# [] Creation Date : 09-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from datetime import datetime
from .base import I1820Controller


class DiscoveryController(I1820Controller):
    def __init__(self):
        self.rpis = dict()

    def ping(self, message: dict):
        if message['rpi_id'] not in self.rpis.keys():
            self.rpis[message['rpi_id']] = {'time': str(datetime.now()),
                                            'things': message['things']}
            # TODO: handle new things
        else:
            self.rpis[message['rpi_id']]['time'] = datetime.now()
