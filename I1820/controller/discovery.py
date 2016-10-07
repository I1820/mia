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
from ..things.base import Things

import threading


class DiscoveryController(I1820Controller):
    def __init__(self):
        self._rpis = dict()
        self.lock = threading.Lock()

    def ping(self, message: dict, ip: str):
        self.rpis[message['rpi_id']] = {
            'time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
            'ip': ip,
            'things': message['things']
        }
        for thing in message['things']:
            if not Things.get(thing['type']).has_thing(message['rpi_id'],
                                                       thing['id']):
                Things.get(thing['type']).new_thing(
                    message['rpi_id'], thing['id'])

    @property
    def rpis(self):
        with self.lock:
            return self._rpis
