# In The Name Of God
# ========================================
# [] File Name : ws.py
#
# [] Creation Date : 14-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller


class WebSocketController(I1820Controller):
    def __init__(self):
        self.connected = []

    def send(self, message):
        pass

    def connect(self, socket):
        self.connected.append(socket)
