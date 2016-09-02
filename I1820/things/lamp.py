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
from ..conf.config import cfg


class Lamp(Thing):
    """
    This class represents Lamp !
    :param on: shows the lamp is on or off
    :type on: bool
    """
    name = "lamp"

    def __init__(self, rpi_id, device_id):
        self.id = 10

    @property
    def on(self):
        pass

    @on.setter
    def on(self, on: bool):
        message = {'id': self.id, 'settings': {'on': on}, 'type': 'lamp'}
        krn = KaaRestNotification('%s:%s' % (cfg.kaa_host, cfg.kaa_port),
                                  cfg.kaa_user_developer,
                                  cfg.kaa_passwd_developer)
        krn.send_notification(cfg.app_uid, cfg.notif_uid, 32770, message)
