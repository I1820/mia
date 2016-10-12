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
from ..domain.log import I1820LogDictDecoder
from ..things.base import Things

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
    data = bson.loads(message.payload)
    log = I1820LogDictDecoder.decode(data)

    thing = Things.get(log.type).get_thing(log.endpoint, log.device)

    for key, value in log.states.items():
        setattr(thing, key, {'value': value, 'time': log.timestamp})

    return ""


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
client.connect(cfg.mqtt_host, int(cfg.mqtt_port), 60)
