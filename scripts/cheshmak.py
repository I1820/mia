#!/usr/bin/env python3
# In The Name Of God
# Creation Date : 1/31/17
# Created By : Mahtab Farrokh (mahtab.farrokh@gmail.com)

import requests
import json
import time

url = 'http://127.0.0.1:8080/thing'



def makeCheshmak ()  :
    while True:
        post_data = {
            "type": "smartLamp",
            "agent_id": "3ae45bf0-8d7b-5e88-964c-ad785b7af0d5",
            "device_id": "1",
            "settings": {
                "color": "#ff0000",
                "on": True
            }
        }
        requests.put(url, data=json.dumps(post_data))
        time.sleep(1)
        post_data = {
            "type": "smartLamp",
            "agent_id": "3ae45bf0-8d7b-5e88-964c-ad785b7af0d5",
            "device_id": "1",
            "settings": {
                "color": "#0000ff",
                "on": True
            }
        }
        requests.put(url, data=json.dumps(post_data))
        time.sleep(1)

if __name__ == '__main__':
    makeCheshmak()


