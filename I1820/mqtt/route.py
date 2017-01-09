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
from ..controllers.discovery import DiscoveryController
from ..controllers.event import EventController
from ..controllers.plugin import PluginController
from ..domain.log import I1820Log
from ..domain.event import I1820Event
from ..things.base import Things
from ..exceptions.thing import ThingNotFoundException

import bson
import logging

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
    log = bson.loads(message.payload)

    if not isinstance(log, I1820Log):
        return

    # Sending raw data
    data = {
        'agent_id': log.agent,
        'device_id': log.device,
        'type': log.type,
        'states': log.states
    }
    EventController().event(I1820Event('raw', data))

    try:
        thing = Things.get(log.type).get_thing(log.agent, log.device)
    except ThingNotFoundException as e:
        logger.warning("[%s]: %s" % (message.topic, str(e)))
        return

    PluginController().on_log(log)

    for key, value in log.states.items():
        setattr(thing, key, {'value': value, 'time': log.timestamp})

    logger.info("[%s]" % message.topic)


def on_discovery(client, userdata, message):
    '''
    Handles discovery messages that come from I1820 Agents.
    These messages are used as Raspberry PI heart beat.

    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param message: recived message that contains topic, payload, qos, retain.
    :type message: MQTTMessage
    '''
    data = bson.loads(message.payload)
    discovery = DiscoveryController()
    discovery.ping(data)

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
    for t in cfg.endpoints:
        client.subscribe('I1820/%s/discovery' % t)
        client.message_callback_add('I1820/%s/discovery' % t, on_discovery)
        client.subscribe('I1820/%s/log' % t)
        client.message_callback_add('I1820/%s/log' % t, on_log)

# connect to brocker
client.on_connect = on_connect
try:
    client.connect(cfg.mqtt_host, int(cfg.mqtt_port), 60)
    print(" * MQTT at %s:%d" % (cfg.mqtt_host, int(cfg.mqtt_port)))
except ConnectionError as e:
    print(" * MQTT at %s:%d had connection error." % (cfg.mqtt_host,
                                                      int(cfg.mqtt_port)))
    raise e
