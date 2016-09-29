#!/usr/bin/env python3

import requests
import logging
import time
import datetime


log = logging.getLogger('ping')


def ping():
    message = {
        'rpi_id': 'dummy',
        'things': [{'type': 'dummy', 'id': '0', 'attributes': {}}]
    }
    try:
        requests.post('http://127.0.0.1:8080/discovery', json=message)
    except Exception as e:
        log.error('Ping request failed: %s' % e)

if __name__ == '__main__':
    while True:
        ping()
        log = {
            'type': 'dummy',
            'device': '0',
            'endpoint': 'dummy',
            'timestamp': datetime.datetime(
                1995, 2, 20, 12, 00, 00).timestamp(),
            'states': {
                'chert': '1'
            }
        }
        requests.post('http://127.0.0.1:8080/log', json=log)
        time.sleep(20)