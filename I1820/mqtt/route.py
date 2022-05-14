import logging

from ..conf.config import Config
from ..controllers.event import EventController
from ..domain.agent import Agent
from ..domain.event import I1820Event
from ..domain.log import I1820Log
from ..exceptions.format import (InvalidAgentFormatException,
                                 InvalidLogFormatException)
from ..exceptions.thing import ThingNotFoundException
from ..things.base import Things
from ..things.discovery import DiscoveryService


class Handler():
    def __init__(self, discovery_service: DiscoveryService, cfg: Config):
        self.logger = logging.getLogger("mqtt.handler")
        self.discovery_service = discovery_service
        self.cfg = cfg

    def on_log(self, _client, _userdata, message):
        '''
        Handles log messages that come from I1820 Agents.
        These messages are used for report and status collecting.

        :param client: the client instance for this callback
        :param userdata: the private user data as set in Client() or userdata_set()
        :param message: recived message that contains topic, payload, qos, retain.
        :type message: MQTTMessage
        '''
        try:
            log = I1820Log.from_json(message.payload.decode('ascii'))
        except InvalidLogFormatException as e:
            self.logger.warning("[%s]: %s", message.topic, str(e))
            return

        # Sending raw data without any futher processing
        data = {
            'agent_id': log.agent,
            'device_id': log.device,
            'type': log.type,
            'states': {state['name']: state['value'] for state in log.states}
        }
        EventController().event(I1820Event('raw', data))

        try:
            thing = Things.get(log.type).get_thing(log.agent, log.device)
        except ThingNotFoundException as e:
            self.logger.warning("[%s]: %s", message.topic, str(e))
            return

        for state in log.states:
            setattr(thing, state['name'], {'value': state['value'],
                                           'time': log.timestamp})

        self.logger.info("[%s]", message.topic)


    def on_discovery(self, client, userdata, message):
        '''
        Handles discovery messages that come from I1820 Agents.
        These messages are used as Raspberry PI heart beat.

        : client: the client instance for this callback
        :param userdata: the private user data as set in Client() or userdata_set()
        :param age: recived message that contains topic, payload, qos, retain.
        :type message: MQTTMessage
        '''
        try:
            agent = Agent.from_json(message.payload.decode('ascii'))
        except InvalidAgentFormatException as e:
            self.logger.warning("[%s]: %s", message.topic, str(e))
            return

        self.discovery_service.ping(agent)

        self.logger.info("discovery on [%s]", agent.ident)


    def on_connect(self, client, userdata, flags, rc):
        '''
        Called when the broker responds to our connection request.
        It subscribes to thing side channels based on things API token

        :param client: the client instance for this callback
        :param userdata: the private user data as set in Client() or userdata_set()
        :param flags: response flags sent by the broker
        :param rc: the connection result
        '''
        # Discovery
        client.subscribe(f'I1820/{self.cfg.tenant}/agent/ping')
        client.message_callback_add(f'I1820/{self.cfg.tenant}/agent/ping',
                                    self.on_discovery)
        # Log
        client.subscribe(f'I1820/{self.cfg.tenant}/log/send')
        client.message_callback_add(f'I1820/{self.cfg.tenant}/log/send',
                                    self.on_log)
