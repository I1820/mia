# In The Name Of God
# ========================================
# [] File Name : log.py
#
# [] Creation Date : 27-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import KaaRestBase, KaaRestError

import requests
from requests.exceptions import HTTPError
import json


class KaaRestLog(KaaRestBase):
    """
    This class provide a rest way for interfacing with kaa logs
    """

    def __init__(self, address, username, password):
        super(KaaRestLog, self).__init__(address, username, password)

    def create_log_schema(self, application_id: int,
                          name: str, description: str, schema: dict):
        meta = {'applicationId': application_id, 'name': name,
                'description': description}

        files = {'file':
                 ('schema.json', json.dumps(schema), 'application/json'),
                 'logSchema':
                 ('', json.dumps(meta), 'application/json')}

        try:
            response = requests.post(self.url_prefix + 'createLogSchema',
                                     files=files)
        except HTTPError:
            pass
        print(response.text)


class KaaRestLogError(KaaRestError):
    pass
