'''
dummy agent is a simple agent implementation for the mia platform.
'''

import logging
import time

import paho.mqtt.client as mqtt

from I1820.domain.agent import Agent, RawThing
from I1820.domain.log import I1820Log

TENANT_ID = 'main'
client = mqtt.Client()
logger = logging.getLogger('mia.dummy')


def ping(ident: int):
    '''
    ping simulate an agent with the given id and hard-coded thing.
    '''
    logger.info('id = %d', ident)
    agent = Agent('dummy', things={
                      RawThing(type='dummy', id=str(ident))
                  }, actions=[])
    client.publish(f'I1820/{TENANT_ID}/agent/ping', agent.to_json())


if __name__ == '__main__':
    client.connect('127.0.0.1', int(1883))
    client.loop_start()
    i = 0
    while True:
        i = (i + 1) % 2
        ping(i)
        log = I1820Log(type='dummy', device='0', agent='dummy',
                       states=[
                           {'name': 'chert', 'value': '1'}
                       ])
        client.publish(f'I1820/{TENANT_ID}/log/send', log.to_json())
        time.sleep(1)
