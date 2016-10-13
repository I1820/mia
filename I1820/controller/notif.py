# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 13-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..domain.notif import I1820Notification
from ..mqtt import client
from ..conf.config import cfg

import bson


class NotificationController(I1820Controller):
    def __init__(self):
        pass

    def notify(self, notification: I1820Notification):
        for t in cfg.endpoints:
            client.publish('I1820/%s/notification' % t, bson.dumps(notification))
