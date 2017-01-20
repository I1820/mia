#!/usr/bin/env python3

import paho.mqtt.client as mqtt
import time
import json

from I1820.conf.config import cfg
from I1820.domain.log import I1820Log


token = '83DB8F6299E0A303730B5F913B6A3DF420EBC2C2'
client = mqtt.Client()


def ping():
    message = {
        'agent_id': 'dummy',
        'things': [['dummy', '0']]
    }
    client.publish('I1820/%s/discovery' % token, json.dumps(message))

if __name__ == '__main__':
    client.connect(cfg.mqtt_host, int(cfg.mqtt_port))
    client.loop_start()
    while True:
        ping()
        log = I1820Log(type='dummy', device='0', agent='dummy',
                       states=[
                           {'name': 'chert', 'value': '1'}
                       ])
        client.publish('I1820/%s/log' % token, log.to_json())
        time.sleep(20)
