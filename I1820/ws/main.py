# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 14-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import websockets
import asyncio

from .handler import handler


def main():
    start_server = websockets.serve(handler, '0.0.0.0', 8765)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()
