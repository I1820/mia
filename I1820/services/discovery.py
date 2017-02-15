from ..things.base import Things

from datetime import datetime
import time
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate, Requires


@ComponentFactory("discovery_factory")
@Provides("discovery_service")
@Property("default")
@Requires("_rs", "redis_service")
@Instantiate("default_discovery_instance")
class DiscoveryService:
    def __init__(self):
        self._agents = {}
        self._rs = None

    @Validate
    def validate(self, context):
        """
        The component is validated. This method is called right before the
        provided service is registered to the framework.
        """
        # All setup should be done here
        print(" * 18.20 Service: Discovery Service")

    @Invalidate
    def invalidate(self, context):
        """
        The component has been invalidated. This method is called right after
        the provided service has been removed from the framework.
        """
        pass

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
        self._rs.rconn.zadd('time:', time.time(),
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
