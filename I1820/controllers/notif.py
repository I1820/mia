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


class NotificationController(I1820Controller):
    '''
    The NotificationController controls notifications. these notifications
    base on :class:`I1820Notification`.
    '''
    def __init__(self):
        pass

    def notify(self, notification: I1820Notification):
        client.publish('I1820/%s/notification' % cfg.endpoint,
                       notification.to_json())
