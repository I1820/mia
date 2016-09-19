# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 13-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import requests

from .base import I1820Controller
from ..domain.notif import I1820Notification, I1820NotificationJSONEncoder
from .discovery import DiscoveryController


class NotificationController(I1820Controller):
    def __init__(self):
        pass

    def notify(self, notification: I1820Notification):
        ip = DiscoveryController.rpis[notification['endpoint']]['ip']
        requests.post('http://%s:1820/event' % ip,
                      data=I1820NotificationJSONEncoder().encode(notification))
