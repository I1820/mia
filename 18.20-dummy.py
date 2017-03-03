#!/usr/bin/env python3

import paho.mqtt.client as mqtt
from socketIO_client import SocketIO, BaseNamespace
import time
import logging

from I1820.conf.config import cfg
from I1820.domain.log import I1820Log
from I1820.domain.agent import I1820Agent


tenant_id = cfg.tenant_id
client = mqtt.Client()
t = 0
logger = logging.getLogger('I1820.dummy')


class I1820Namespace(BaseNamespace):
    def on_raw(self, data):
        logger.info('raw: %s' % data)
        print(time.time() - t)

    def on_connect(self):
        logger.info('connect')


def ping(i):
    logger.info('i = %d' % i)
    agent = I1820Agent('dummy', [{'type': 'dummy', 'id': str(i)}])
    client.publish('I1820/%s/discovery' % tenant_id, agent.to_json())


if __name__ == '__main__':
    socketIO = SocketIO('localhost', 8080)
    socketIO.define(I1820Namespace, '/I1820')

    client.connect(cfg.mqtt_host, int(cfg.mqtt_port))
    client.loop_start()
    i = 0
    while True:
        i = (i + 1) % 2
        ping(i)
        log = I1820Log(type='dummy', device='0', agent='dummy',
                       states=[
                           {'name': 'chert', 'value': '1'}
                       ])
        client.publish('I1820/%s/log' % tenant_id, log.to_json())
        t = time.time()
        socketIO.wait(seconds=1)
        time.sleep(1)
