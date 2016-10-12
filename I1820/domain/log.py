# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import datetime
import bson


class I1820Log(bson.BSONCoding):
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

    def bson_encode(self):
        return {
                'timestamp': self.timestamp.timestamp(),
                'type': self.type,
                'device': self.device,
                'states': self.states,
                'endpoint': self.endpoint
        }

    def bson_init(self, raw_values):
        self.states = raw_values['states']
        self.type = raw_values['type']
        self.device = raw_values['device']
        self.endpoint = raw_values['endpoint']
        self.timestamp = datetime.datetime.fromtimestamp(
            raw_values['timestamp'])
