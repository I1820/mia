# In The Name Of God
# ========================================
# [] File Name : event.py
#
# [] Creation Date : 30-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..domain.event import I1820Event
from ..mqtt import client
from ..conf.config import cfg


class EventController(I1820Controller):
    '''
    The NotificationController controls notifications. these notifications
    base on :class:`I1820Notification`.
    '''
    def __init__(self):
        pass

    def notify(self, event: I1820Event):
        for t in cfg.endpoints:
            client.publish('I1820/%s/event/%s' % t, None)
