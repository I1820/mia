from I1820.discovery import DiscoveryService
from I1820.domain.agent import Agent
from I1820.logger import logger

# from ..domain.event import I1820Event
from I1820.domain.log import I1820Log
from I1820.exceptions.format import (
    InvalidAgentFormatException,
    InvalidLogFormatException,
)
from I1820.exceptions.thing import ThingNotFoundException
from I1820.things.base import Things


class Handler:
    def __init__(self, discovery_service: DiscoveryService, tenant: str):
        self.discovery_service = discovery_service
        self.logger = logger.getChild("mqtt")
        self.tenant = tenant

    def on_log(self, _client, _userdata, message):
        """
        Handles log messages that come from I1820 Agents.
        These messages are used for report and status collecting.

        :param client: the client instance for this callback
        :param userdata: the private user data as set in
        Client() or userdata_set()
        :param message: recived message that contains topic, payload,
        qos, retain.
        :type message: MQTTMessage
        """
        try:
            log = I1820Log.from_json(message.payload.decode("ascii"))
        except InvalidLogFormatException as e:
            self.logger.warning("%s: %s", message.topic, str(e))
            return

        # Sending raw data without any futher processing
        # data = {
        #     'agent_id': log.agent,
        #    'device_id': log.device,
        #     'type': log.type,
        #     'states': {state['name']: state['value'] for state in log.states}
        # }
        # EventController().event(I1820Event('raw', data))

        try:
            thing = Things.get(log.type).get_thing(log.agent, log.device)
        except ThingNotFoundException as e:
            self.logger.warning("%s: %s", message.topic, str(e))
            return

        for state in log.states:
            setattr(
                thing,
                state["name"],
                {"value": state["value"], "time": log.timestamp},
            )

        self.logger.info(
            "recived log on %s from agent: %s, device: %s, type: %s",
            message.topic,
            log.agent,
            log.device,
            log.type,
        )

    def on_discovery(self, client, userdata, message):
        """
        Handles discovery messages that come from I1820 Agents.
        These messages are used as Raspberry PI heart beat.

        : client: the client instance for this callback
        :param userdata: the private user data as set in
        Client() or userdata_set()
        :param age: recived message that contains topic, payload, qos, retain.
        :type message: MQTTMessage
        """
        try:
            agent = Agent.from_json(message.payload.decode("ascii"))
        except InvalidAgentFormatException as e:
            logger.warning("[%s]: %s", message.topic, str(e))
            return

        self.discovery_service.ping(agent)

        self.logger.info("discovery from %s", agent.ident)

    def publish(self, client, body):
        """
        publish the given body into the tenant.
        """
        client.publish(f"I1820/{self.tenant}/configuration/request", body)

    def on_connect(self, client, userdata, flags, rc):
        """
        Called when the broker responds to our connection request.
        It subscribes to thing side channels based on things API token

        :param client: the client instance for this callback
        :param userdata: the private user data as set in
        Client() or userdata_set()
        :param flags: response flags sent by the broker
        :param rc: the connection result
        """
        # Discovery
        client.subscribe(f"I1820/{self.tenant}/agent/ping")
        client.message_callback_add(
            f"I1820/{self.tenant}/agent/ping", self.on_discovery
        )
        # Log
        client.subscribe(f"I1820/{self.tenant}/log/send")
        client.message_callback_add(
            f"I1820/{self.tenant}/log/send", self.on_log
        )
