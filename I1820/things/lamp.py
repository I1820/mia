# In The Name Of God
# ========================================
# [] File Name : lamp.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .actuator import ActuatorThing
from ..pykaa.rest.notif import KaaRestNotification
from ..conf.config import cfg


class Lamp(ActuatorThing):
    """
    This class represents Lamp actuator
    """
    name = "lamp"

    def __init__(self, rpi_id, device_id):
        self.id = 10

    @property
    def on(self):
        """
        On property is used as a trigger for lamp status.
        """
        raise ValueError('Actuator settings are not readable')

    @on.setter
    def on(self, on: bool):
        message = {'id': self.id, 'settings': {'on': on}, 'type': 'lamp'}
        krn = KaaRestNotification('%s:%s' % (cfg.kaa_host, cfg.kaa_port),
                                  cfg.kaa_user_developer,
                                  cfg.kaa_passwd_developer)
        krn.send_notification(cfg.app_uid, cfg.notif_uid, 32770, message)
