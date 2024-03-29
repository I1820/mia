import datetime
from threading import Lock

from I1820.domain.agent import Agent, RawThing
from I1820.things.base import Things
from I1820.logger import logger


class DiscoveryService:
    """
    DiscoveryService manages agents. agent may have multiple things.
    """

    def __init__(self):
        self._agents: dict[str, Agent] = {}
        self.lck = Lock()
        self.logger = logger.getChild("discovery")
        print(" * Mia Service: Discovery Service")

    @property
    def agents(self) -> dict[str, dict]:
        """
        retrieves agent information from memory.
        """
        result: dict[str, dict] = {}

        with self.lck:
            for agent_id, agent in self._agents.items():
                result[agent_id] = {}

                result[agent_id]["time"] = agent.last_seen.strftime(
                    "%Y-%m-%dT%H:%M:%SZ"
                )

                result[agent_id]["things"] = []
                for thg in agent.things:
                    result[agent_id]["things"].append(
                        {"type": thg.type, "id": thg.id}
                    )
        return result

    def ping(self, agent: Agent):
        """
        agent pings mia platform, this method saves their status and things.
        for saving things we are using Thing class devices field.
        """
        # Let's create our agent
        to_add: set[RawThing] = set()
        to_del: set[RawThing] = set()
        with self.lck:
            if agent.ident not in self._agents:
                self._agents[agent.ident] = agent
                self._agents[agent.ident].last_seen = datetime.datetime.now(datetime.UTC)
                to_add = agent.things
            else:
                agent.last_seen = datetime.datetime.now(datetime.UTC)
                if self._agents[agent.ident] == agent.things:
                    return
                to_del = self._agents[agent.ident].things - agent.things
                to_add = agent.things - self._agents[agent.ident].things
                self._agents[agent.ident].things = agent.things

        # Add things into local things storage
        for thg in to_add:
            Things.get(thg.type).new_thing(agent.ident, thg.id)
            self.logger.info("thing %s was registered", thg.id)

        # Remove things from local things storage
        for thg in to_del:
            Things.get(thg.type).del_thing(agent.ident, thg.id)
            self.logger.info("thing %s was removed", thg.id)

    def pong(self, agent_id: str):
        """
        Removes given agent (based on it's identification) from agent storage.
        """
        with self.lck:
            if agent_id in self._agents:
                result = 1
                for thg in self._agents[agent_id].things:
                    Things.get(thg.type).del_thing(agent_id, thg.id)
                del self._agents[agent_id]
            else:
                result = 0
        return result
