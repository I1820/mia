# In The Name Of God
# ========================================
# [] File Name : discovery.py
#
# [] Creation Date : 22-02-2017
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from ..things.base import Things
from ..domain.agent import I1820Agent

from datetime import datetime
from threading import Lock
from pelix.ipopo.decorators import ComponentFactory, Property, Provides, \
     Validate, Invalidate, Instantiate


@ComponentFactory("discovery_factory")
@Provides("discovery_service")
@Property("default")
@Instantiate("default_discovery_instance")
class DiscoveryService:
    def __init__(self):
        self._agents = {}
        self.lck = Lock()

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
        '''
        Retrieves I1820 agent information from redis.
        '''
        result = {}

        with self.lck:
            for agent_id, agent in self._agents.items():
                result[agent_id] = {}
                result[agent_id]['time'] = datetime\
                    .fromtimestamp(agent['time'])\
                    .strftime('%Y-%m-%dT%H:%M:%SZ')
                result[agent_id]['things'] = []
                for t_type, t_id in agent['things']:
                    result[agent_id]['things'].append(
                        {'type': t_type, 'id': t_id})
        return result

    def ping(self, agent: I1820Agent):
        '''
        Agent pings I1820, this method saves it's status and things.
        '''
        # Agent attached things set
        s = {(t['type'], t['id']) for t in agent.things}

        # Let's create our agent
        to_add = {}
        to_del = {}
        with self.lck:
            if agent.ident not in self._agents:
                self._agents[agent.ident] = {}
                self._agents[agent.ident]['things'] = s
                self._agents[agent.ident]['time'] = \
                    datetime.utcnow().timestamp()
                to_add = s
            else:
                self._agents[agent.ident]['time'] = \
                            datetime.utcnow().timestamp()
                if self._agents[agent.ident]['things'] == s:
                    return
                else:
                    to_del = self._agents[agent.ident]['things'] - s
                    to_add = s - self._agents[agent.ident]['things']

        # Add things into local things storage
        for (t_type, t_id) in to_add:
            Things.get(t_type).new_thing(agent.ident, t_id)

        # Remove things from local things storage
        for (t_type, t_id) in to_del:
            Things.get(t_type).del_thing(agent.ident, t_id)

    def pong(self, agent_id: str):
        '''
        Removes given agent (based on it's identification) from agent storage.
        '''
        with self.lck:
            if agent_id in self._agents:
                result = 1
                for t_type, t_id in self._agents[agent_id]['things']:
                    Things.get(t_type).del_thing(agent_id, t_id)
                del self._agents[agent_id]
            else:
                result = 0
        return result
