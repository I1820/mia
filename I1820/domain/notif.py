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

    def to_json(self):
            result = {
                'type': self.type,
                'device': self.device,
                'settings': self.settings,
                'endpoint': self.endpoint
            }
            return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        type = raw_values['type']
        device = raw_values['device']
        settings = raw_values['settings']
        endpoint = raw_values['endpoint']
        return cls(type, device, settings, endpoint)
