# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 27-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import KaaRestBase, KaaRestError
from ..domain.notif import NotificationSchema, NotificationSchemaDictDecoder

import requests
from requests.exceptions import HTTPError
import json


class KaaRestNotification(KaaRestBase):
    """
    This class provide a rest way for interfacing with kaa notifications
    """

    def __init__(self, address, username, password):
        super(KaaRestNotification, self).__init__(address, username, password)

    def get_all_notification_schemas(
            self, application_token) -> [NotificationSchema]:
        notification_schemas = []
        response = requests.get(
            self.url_prefix
            + 'notificationSchemasByAppToken/{}'.format(application_token))
        try:
            response.raise_for_status()
        except HTTPError as e:
            pass
        for obj in response.json():
            notification_schema = NotificationSchemaDictDecoder.decode(obj)
            notification_schemas.append(notification_schema)
        print(notification_schemas)
        return notification_schemas

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

    def create_notification_schema(self, application_id: int,
                                   name: str, description: str, schema: dict):
        print(schema)
        meta = {'applicationId': application_id, 'name': name,
                'description': description}
        files = {'file':
                 ('notification_schema.json', json.dumps(schema),
                  'application/json'),
                 'notificationSchema':
                 ('', json.dumps(meta), 'application/octet-stream')}
        response = requests.post(self.url_prefix + 'notificationSchema',
                                 files=files)
        print(response.text)


class KaaRestNotificationError(KaaRestError):
    pass
