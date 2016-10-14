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
        self._rpis = dict()

    @property
    def rpis(self):
        rpis = {}
        for rpi in self._rpis:
            rpis[rpi] = {}
            rpis[rpi]['time'] = self._rpis[rpi]['time']
            rpis[rpi]['things'] = []
            for thing in self._rpis[rpi]['things']:
                rpis[rpi]['things'].append({'type': thing[0], 'id': thing[1]})
        return rpis

    def ping(self, message: dict):
        message['things'] = {tuple(t) for t in message['things']}

        if message['rpi_id'] not in self._rpis:
            self._rpis[message['rpi_id']] = {
                'time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                'things': set()
            }
        else:
            self._rpis[message['rpi_id']]['time'] = \
                    datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        to_be_add = message['things'] - self._rpis[message['rpi_id']]['things']
        to_be_del = self._rpis[message['rpi_id']]['things'] - message['things']

        for thing in to_be_del:
            Things.get(thing[0]).del_thing(message['rpi_id'], thing[1])
            self._rpis[message['rpi_id']]['things'].remove(thing)

        for thing in to_be_add:
            Things.get(thing[0]).new_thing(message['rpi_id'], thing[1])
            self._rpis[message['rpi_id']]['things'].add(thing)
