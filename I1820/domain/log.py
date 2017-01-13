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
    '''
    The I1820Log object contains information that is used to
    report end device states into I1820.

    :param type: type of target end device.
    :type type: str
    :param device: identification of target end device.
    :type device: str
    :param states: states of target device.
    :type states: dict
    :param agent: identification of target end device agent [Raspberry PI].
    :type agent: str
    '''
    def __init__(self, type: str, device: str,
                 states: dict,
                 agent: str,
                 timestamp: datetime.datetime = None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()

        self.states = states
        self.type = type
        self.device = device
        self.timestamp = timestamp
        self.agent = agent

    def bson_encode(self):
        return {
                'timestamp': self.timestamp.timestamp(),
                'type': self.type,
                'device': self.device,
                'states': self.states,
                'agent': self.agent
        }

    def bson_init(self, raw_values):
        self.states = raw_values['states']
        self.type = raw_values['type']
        self.device = raw_values['device']
        self.agent = raw_values['agent']
        self.timestamp = datetime.datetime.fromtimestamp(
            raw_values['timestamp'])


bson.import_class(I1820Log)
