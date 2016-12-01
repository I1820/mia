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
                 agent_id: str, device_id: str, type: str, settings: dict):
        self.type = type
        self.settings = settings
        self.agent_id = agent_id
        self.device_id = device_id
        super().__init__(ident)

    def on_log(self, log):
        self.notify(self.agent_id, self.device_id, self.type, self.settings)
