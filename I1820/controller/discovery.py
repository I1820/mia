# In The Name Of God
# ========================================
# [] File Name : discovery.py
#
# [] Creation Date : 09-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..things.base import Things

from datetime import datetime


class DiscoveryController(I1820Controller):
    def __init__(self):
        self.rpis = dict()

    def ping(self, message: dict):
        message['things'] = {tuple(t) for t in message['things']}

        if message['rpi_id'] not in self.rpis:
            self.rpis[message['rpi_id']] = {
                'time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                'things': set()
            }
        else:
            self.rpis[message['rpi_id']]['time'] = \
                    datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        to_be_add = message['things'] - self.rpis[message['rpi_id']]['things']
        to_be_del = self.rpis[message['rpi_id']]['things'] - message['things']

        for thing in to_be_del:
            Things.get(thing[0]).del_thing(message['rpi_id'], thing[1])
            self.rpis[message['rpi_id']]['things'].remove(thing)

        for thing in to_be_add:
            Things.get(thing[0]).new_thing(message['rpi_id'], thing[1])
            self.rpis[message['rpi_id']]['things'].add(thing)
