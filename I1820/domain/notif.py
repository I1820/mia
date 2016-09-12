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
    def __init__(self, type: str, device: str,
                 settings: dict,
                 endpoint: str):
        self.type = type
        self.device = device
        self.settings = settings
        self.endpoint = endpoint


class I1820NotificatioJSONEncoder(json.JSONEncoder):
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
                                 obj['states'], obj['endpoint'])
