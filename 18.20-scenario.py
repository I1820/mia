#!/usr/bin/env python3

import requests

if __name__ == '__main__':
    f = {
        'type': 'filter',
        'chain': 1,
        'arguments': {
            'agent_id': '42f6a151-92bb-552d-ba69-bf1d25def01f',
            'device_id': '1',
            'type': 'current',
            'state': 'current',
            'value': '30',
            'op': '=='
        }
    }

    r = requests.post('http://127.0.0.1:8080/plugin', json=f)
    print(r.text)

    n = {
        'type': 'notifier',
        'chain': 1,
        'arguments': {
            'agent_id': '42f6a151-92bb-552d-ba69-bf1d25def01f',
            'device_id': '1:1',
            'type': 'lamp',
            'settings': {
                'on': True
            }
        }
    }

    r = requests.post('http://127.0.0.1:8080/plugin', json=n)
    print(r.text)
