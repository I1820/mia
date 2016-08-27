# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 27-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import KaaRestBase, KaaRestError

import requests
from requests.exceptions import HTTPError
import json


class KaaRestNotification(KaaRestBase):
    """
    This class provide a rest way for interfacing with kaa notifications
    """

    def __init__(self, address, username, password):
        super(KaaRestNotification, self).__init__(address, username, password)

    def send_notification(self, application_id: int,
                          schema_id: int, topic_id: int, message: dict):
        notification = {'applicationId': application_id, 'schemaId': schema_id,
                        'topicId': topic_id, 'type': 'USER'}

        files = {'file':
                 ('message.json', json.dumps(message), 'application/json'),
                 'notification':
                 ('', json.dumps(notification), 'application/json')}

        response = requests.post(self.url_prefix + 'sendNotification',
                                 files=files)
        print(response.text)
