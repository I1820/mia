# In The Name Of God
# ========================================
# [] File Name : filter.py
#
# [] Creation Date : 01-12-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import Plugin


class FilterPlugin(Plugin):
    name = 'filter'

    def __init__(self, ident: int,
                 agent_id: str, device_id: str, type: str, state: str,
                 op: str, value):
        self.type = type
        self.state = state
        self.agent_id = agent_id
        self.device_id = device_id
        self.value = value
        self.op = op
        super().__init__(ident)

    def on_log(self, log):
        if self.agent_id != '*' and log.agent != self.agent_id:
            return False
        if self.device_id != '*' and log.device != self.device_id:
            return False
        if self.type != '*' and log.type != self.type:
            return False

        if self.op == '==':
            return log.states[self.state] == self.value
        elif self.op == '!=':
            return log.states[self.state] != self.value
        elif self.op == '>':
            return log.states[self.state] > self.value
        elif self.op == '<':
            return log.states[self.state] < self.value
        elif self.op == '>=':
            return log.states[self.state] >= self.value
        elif self.op == '<=':
            return log.states[self.state] <= self.value
        else:
            return False
