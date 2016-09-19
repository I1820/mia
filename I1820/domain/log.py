# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime
import json


class I1820Log:
    def __init__(self, type: str, device: str,
                 states: dict,
                 endpoint: str,
                 timestamp: datetime.datetime = None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()

        self.states = states
        self.type = type
        self.device = device
        self.timestamp = timestamp
        self.endpoint = endpoint


class I1820LogJSONEncoder(json.JSONEncoder):
    def default(self, obj: I1820Log):
        if isinstance(obj, I1820Log):
            return {
                'timestamp': obj.timestamp.timestamp(),
                'type': obj.type,
                'device': obj.device,
                'states': obj.states,
                'endpoint': obj.endpoint
            }
        else:
            raise TypeError(
                "I1820LogJSONEncoder got {} instead of I1820Log.".format(
                    type(obj)))


class I1820LogDictDecoder:
    @staticmethod
    def decode(obj: dict) -> I1820Log:
        return I1820Log(obj['type'], obj['device'],
                        obj['states'], obj['endpoint'],
                        datetime.datetime.fromtimestamp(
                            obj['timestamp']))
