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

import json


def on_log(client, userdata, message):
    '''
    Handles log messages that come from Raspberry PIs.
    These messages are used for report and status collecting.

    :param client: the client instance for this callback
    :param userdata: the private user data as set in Client() or userdata_set()
    :param message: recived message that contains topic, payload, qos, retain.
    :type message: MQTTMessage
    '''
    data = json.loads(message.payload)
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
    data = json.loads(message.payload)
    discovery = DiscoveryController()
    discovery.ping(data)


# subscribe to thing side channels based on things API token
for t in cfg.endpoints:
    client.subscribe('%s/discovery' % t)
    client.message_callback_add('%s/discovery' % t, on_discovery)
    client.subscribe('%s/log' % t)
    client.message_callback_add('%s/log' % t, on_log)

# connect to brocker
client.connect(cfg.mqtt_host, cfg.mqtt_port, 60)
