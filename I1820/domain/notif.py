# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 12-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import bson


class I1820Notification(bson.BSONCoding):
    '''
    The I1820Notification object contains information that is used to
    send notification into end devices.

    :param type: type of target end device.
    :type type: str
    :param device: identification of target end device.
    :type device: str
    :param settings: configurations wanted to apply on target end device.
    :type settings: dict
    :param endpoint: identification of target end device Raspberry PI.
    :type endpoint: str
    '''
    def __init__(self, type: str, device: str,
                 settings: dict,
                 endpoint: str):
        self.type = type
        self.device = device
        self.settings = settings
        self.endpoint = endpoint

    def bson_encode(self):
            return {
                'type': self.type,
                'device': self.device,
                'settings': self.settings,
                'endpoint': self.endpoint
            }

    def bson_init(self, raw_values):
        self.type = raw_values['type']
        self.device = raw_values['device']
        self.settings = raw_values['settings']
        self.endpoint = raw_values['endpoint']


bson.import_class(I1820Notification)
