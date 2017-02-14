# In The Name Of God
# ========================================
# [] File Name : discovery.py
#
# [] Creation Date : 09-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..things.base import Things
from ..services.master import service_master

from datetime import datetime
import time


class DiscoveryController(I1820Controller):
    def __init__(self):
        self._agents = {}

    @property
    def agents(self):
        agents = {}
        for agent in self._agents:
            agents[agent] = {}
            agents[agent]['time'] = self._agents[agent]['time']
            agents[agent]['things'] = []
            for thing in self._agents[agent]['things']:
                agents[agent]['things'].append(
                    {'type': thing[0], 'id': thing[1]})
        return agents

    def ping(self, message: dict):
        with service_master.service('redis_service') as redis_service:
            redis_service.rconn.zadd('time:',
                                     time.time(),
                                     'agent: %s' % message['agent_id'])

        message['things'] = {tuple(t) for t in message['things']}

        if message['agent_id'] not in self._agents:
            self._agents[message['agent_id']] = {
                'time': datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ"),
                'things': set()
            }
        else:
            self._agents[message['agent_id']]['time'] = \
                    datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")

        to_be_add = message['things'] - \
            self._agents[message['agent_id']]['things']
        to_be_del = self._agents[message['agent_id']]['things'] - \
            message['things']

        for thing in to_be_del:
            Things.get(thing[0]).del_thing(message['agent_id'], thing[1])
            self._agents[message['agent_id']]['things'].remove(thing)

        for thing in to_be_add:
            Things.get(thing[0]).new_thing(message['agent_id'], thing[1])
            self._agents[message['agent_id']]['things'].add(thing)

    def pong(self, agent_id: str):
        agent = self._agents.pop(agent_id, None)
        result = {}
        if agent is not None:
            result['time'] = agent['time']
            result['things'] = []
            for thing in agent['things']:
                result['things'].append({'type': thing[0], 'id': thing[1]})
        return result
