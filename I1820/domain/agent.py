# In The Name Of God
# ========================================
# [] File Name : agent.py
#
# [] Creation Date : 22-02-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import json


class I1820Agent:
    '''
    The I1820Agent object contains information that is used to
    represents agent to I1820.

    :param ident: agent identification.
    :type ident: str
    :param things: list of agent attached things.
    :type things: list
    '''
    def __init__(self, ident: str, things: list):
        for thing in things:
            if 'type' not in thing or 'id' not in thing:
                raise ValueError(
                    'things must be an array of types and ids.')

        self.ident = ident
        self.things = things

    def to_json(self):
            result = {
                'id': self.ident,
                'things': self.things,
            }
            return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        ident = raw_values['type']
        things = raw_values['things']
        return cls(ident, things)
