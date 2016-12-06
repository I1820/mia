#!/usr/bin/env python3

import requests

if __name__ == '__main__':
    f = {
        'type': 'filter',
        'chain': 1,
        'parent': 'root',
        'arguments': {
            'agent_id': '*',
            'device_id': '*',
            'type': '*',
            'state': 'light',
            'value': '800',
            'op': '>'
        }
    }

    fr = requests.post('http://127.0.0.1:8080/plugin', json=f)
    print(fr.text)

    n = {
        'type': 'notifier',
        'chain': 1,
        'parent': fr.text + ':' + 'true',
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

    n = {
        'type': 'notifier',
        'chain': 1,
        'parent': r.text + ':' + 'true',
        'arguments': {
            'agent_id': '42f6a151-92bb-552d-ba69-bf1d25def01f',
            'device_id': '1:2',
            'type': 'lamp',
            'settings': {
                'on': True
            }
        }
    }

    r = requests.post('http://127.0.0.1:8080/plugin', json=n)
    print(r.text)

    n = {
        'type': 'notifier',
        'chain': 1,
        'parent': fr.text + ':' + 'false',
        'arguments': {
            'agent_id': '42f6a151-92bb-552d-ba69-bf1d25def01f',
            'device_id': '1:1',
            'type': 'lamp',
            'settings': {
                'on': False
            }
        }
    }

    r = requests.post('http://127.0.0.1:8080/plugin', json=n)
    print(r.text)

    n = {
        'type': 'notifier',
        'chain': 1,
        'parent': r.text + ':' + 'true',
        'arguments': {
            'agent_id': '42f6a151-92bb-552d-ba69-bf1d25def01f',
            'device_id': '1:2',
            'type': 'lamp',
            'settings': {
                'on': False
            }
        }
    }

    r = requests.post('http://127.0.0.1:8080/plugin', json=n)
    print(r.text)
