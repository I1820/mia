# In The Name Of God
# ========================================
# [] File Name : handler.py
#
# [] Creation Date : 14-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..controller.ws import WebSocketController


async def handler(websocket, path):
    WebSocketController().connect(websocket)
