# In The Name Of God
# ========================================
# [] File Name : notifier.py
#
# [] Creation Date : 29-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import Plugin


class NotifierPlugin(Plugin):
    name = 'notifier'

    def __init__(self, ident: int,
                 sensor: str, value: dict, actuator: str, target: dict):
        self.sensor = sensor
        self.value = value
        self.actuator = actuator
        self.target = target
        super().__init__(ident)

    def on_log(self, log):
        send = True
        for (key, value) in self.value.items():
            if key in log.states:
                print(log.states[key])
                if log.states[key] != value:
                    send = False
            else:
                send = False
        if send is True:
            self.notify(log.endpoint, '1:1', self.actuator, self.target)
