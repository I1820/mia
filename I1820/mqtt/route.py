# In The Name Of God
# ========================================
# [] File Name : route.py
#
# [] Creation Date : 12-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from . import client
from ..conf.config import cfg
from ..controllers.event import EventController
from ..services.master import service_master
from ..domain.log import I1820Log
from ..domain.event import I1820Event
from ..domain.agent import I1820Agent
from ..things.base import Things
from ..exceptions.thing import ThingNotFoundException
from ..exceptions.format import InvalidLogFormatException, \
     InvalidAgentFormatException

import logging
import json

logger = logging.getLogger(__name__)


def on_log(client, userdata, message):
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
        logger.warning("[%s]: %s" % (message.topic, str(e)))
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
        logger.warning("[%s]: %s" % (message.topic, str(e)))
        return

    for state in log.states:
        setattr(thing, state['name'], {'value': state['value'],
                                       'time': log.timestamp})

    logger.info("[%s]" % message.topic)


def on_new_discovery(client, userdata, message):
    '''
    Handles discovery messages that come from I1820 Agents.
    These messages are used as Broadcast for finding free I1820.

    : client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param age: recived message that contains topic, payload, qos, retain.
    :type message: MQTTMessage
    '''
    try:
        agent = I1820Agent.from_json(message.payload.decode('ascii'))
    except InvalidAgentFormatException as e:
        logger.warning("[%s]: %s" % (message.topic, str(e)))
        return
    resp = {
        'id': agent.ident,
        'master': cfg.endpoint
    }
    client.publish('I1820/discovery-ack', json.dumps(resp))


def on_discovery(client, userdata, message):
    '''
    Handles discovery messages that come from I1820 Agents.
    These messages are used as Raspberry PI heart beat.

    : client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param age: recived message that contains topic, payload, qos, retain.
    :type message: MQTTMessage
    '''
    try:
        agent = I1820Agent.from_json(message.payload.decode('ascii'))
    except InvalidAgentFormatException as e:
        logger.warning("[%s]: %s" % (message.topic, str(e)))
        return

    with service_master.service('discovery_service') as discovery_service:
        discovery_service.ping(agent)

    logger.info("[%s]" % message.topic)


def on_connect(client, userdata, flags, rc):
    '''
    Called when the broker responds to our connection request.
    It subscribes to thing side channels based on things API token

    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param flags: response flags sent by the broker
    :param rc: the connection result
    '''
    # New added things
    client.subscribe('I1820/discovery')
    client.message_callback_add('I1820/discovery', on_new_discovery)

    client.subscribe('I1820/%s/discovery' % cfg.endpoint)
    client.message_callback_add('I1820/%s/discovery' % cfg.endpoint, on_discovery)
    client.subscribe('I1820/%s/log' % cfg.endpoint)
    client.message_callback_add('I1820/%s/log' % cfg.endpoint, on_log)


# provides on connect handler
client.on_connect = on_connect
