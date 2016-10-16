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
from ..controller.discovery import DiscoveryController
from ..controller.plugin import PluginController
from ..domain.log import I1820Log
from ..things.base import Things
from ..exceptions.thing import ThingNotFoundException

import bson


def on_log(client, userdata, message):
    '''
    Handles log messages that come from Raspberry PIs.
    These messages are used for report and status collecting.

    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param message: recived message that contains topic, payload, qos, retain.
    :type message: MQTTMessage
    '''
    log = bson.loads(message.payload)

    if not isinstance(log, I1820Log):
        return

    try:
        thing = Things.get(log.type).get_thing(log.endpoint, log.device)
    except ThingNotFoundException as e:
        print("%s -- []: %s" % (message.topic, str(e)))
        return

    for key, value in log.states.items():
        setattr(thing, key, {'value': value, 'time': log.timestamp})

    PluginController().on_log(log)

    print("%s -- []" % (message.topic))


def on_discovery(client, userdata, message):
    '''
    Handles discovery messages that come from Raspberry PIs.
    These messages are used as Raspberry PI heart beat.

    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param message: recived message that contains topic, payload, qos, retain.
    :type message: MQTTMessage
    '''
    data = bson.loads(message.payload)
    discovery = DiscoveryController()
    discovery.ping(data)

    print("%s -- []" % (message.topic))


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
