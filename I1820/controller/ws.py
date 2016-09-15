# In The Name Of God
# ========================================
# [] File Name : ws.py
#
# [] Creation Date : 14-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..http import socketio
from .base import I1820Controller


class WebSocketController(I1820Controller):
    def __init__(self):
        pass

    def send(self, message, namespace):
        socketio.send(message, json=True, namespace='/%s' % namespace)
