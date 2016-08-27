# In The Name Of God
# ========================================
# [] File Name : lamp.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import Thing
from ..pykaa.rest.notif import KaaRestNotification


class Lamp(Thing):
    """
    This class represents Lamp !
    """
    name = "lamp"

    @classmethod
    def list(cls):
        pass

    @classmethod
    def handle(cls, data: dict):
        message = {'id': '00', 'interval': 10}
        krn = KaaRestNotification('192.168.1.5:8080', 'devuser', 'devuser123')
        krn.send_notification(32768, 32771, 32769, message)
        return "Hello World of {}".format(data)
