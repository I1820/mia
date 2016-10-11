# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 12-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import json


class I1820Notification:
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


class I1820NotificationJSONEncoder(json.JSONEncoder):
    def default(self, obj: I1820Notification):
        if isinstance(obj, I1820Notification):
            return {
                'type': obj.type,
                'device': obj.device,
                'settings': obj.settings,
                'endpoint': obj.endpoint
            }
        else:
            raise TypeError(
                ("I1820NotificationEncoder got"
                 " {} instead of I1820Notification").format(
                    type(obj)))


class I1820NotificationDictDecoder:
    @staticmethod
    def decode(obj: dict) -> I1820Notification:
        return I1820Notification(obj['type'], obj['device'],
                                 obj['settings'], obj['endpoint'])
