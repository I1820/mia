# In The Name Of God
# ========================================
# [] File Name : master.py
#
# [] Creation Date : 04-03-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import json


class I1820Master:
    '''
    The I1820Master object contains information that is used to
    master selecting process.

    :param master: identification of master [I1820].
    :type master: str
    :param agent: identification of target end device agent [Raspberry PI].
    :type agent: str
    '''
    def __init__(self, master: str, agent: str):
        self.agent = agent
        self.master = master

    def to_json(self):
        result = {
                'master': self.master,
                'agent': self.agent
        }
        return json.dumps(result)

    @classmethod
    def from_json(cls, raw):
        raw_values = json.loads(raw)

        master = raw_values['master']
        agent = raw_values['agent']
        return cls(master, agent)
