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


def ping():
    '''
    ping simulate an agent with the given id and hard-coded thing.
    '''
    agent = Agent('dummy', things={
                      RawThing(type='dummy', id='0')
                  }, actions=[])
    client.publish(f'I1820/{TENANT_ID}/agent/ping', agent.to_json())


if __name__ == '__main__':
    client.connect('127.0.0.1', int(1883))
    client.loop_start()
    i = 2
    while True:
        i = (i ** 2) % 1024
        ping()
        log = I1820Log(type='dummy', device='0', agent='dummy',
                       states=[
                           {'name': 'chert', 'value': str(i)}
                       ])
        client.publish(f'I1820/{TENANT_ID}/log/send', log.to_json())
        time.sleep(1)
