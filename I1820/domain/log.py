# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 04-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..exceptions.format import InvalidLogFormatException

import datetime
import json
import jsonschema
import os

schema = json.load(open(os.path.join(os.path.dirname(__file__),
                                     os.path.join("schemas", "log.json"))))


class I1820Log:
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
                 states: list,
                 agent: str,
                 timestamp: datetime.datetime = None):
        if timestamp is None:
            timestamp = datetime.datetime.utcnow()

        for state in states:
            if 'name' not in state or 'value' not in state:
                raise ValueError(
                    'states must be an array of names and values.')

        self.states = states
        self.type = type
        self.device = device
        self.timestamp = timestamp
        self.agent = agent

    def to_json(self):
        result = {
                'timestamp': self.timestamp.timestamp(),
                'type': self.type,
                'device': self.device,
                'states': self.states,
                'agent': self.agent
        }
        return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        # validate input json
        try:
            jsonschema.validate(raw_values, schema)
        except jsonschema.ValidationError as e:
            raise InvalidLogFormatException(e)

        states = raw_values['states']
        type = raw_values['type']
        device = raw_values['device']
        agent = raw_values['agent']
        timestamp = datetime.datetime.fromtimestamp(
            raw_values['timestamp'])
        return cls(type, device, states, agent, timestamp)
