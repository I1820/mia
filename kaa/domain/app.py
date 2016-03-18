# In The Name Of God
# ========================================
# [] File Name : app.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

import json


class Application:
    """
    This object represents a Kaa application
    :type application_token: str
    :type app_id: str
    :type name: str
    :type sequence_number: int
    :type tenant_id: str
    """

    def __init__(self, application_token, app_id, name, sequence_number, tenant_id):
        self.application_token = application_token
        self.id = app_id
        self.name = name
        self.sequence_number = sequence_number
        self.tenant_id = tenant_id

    def __str__(self):
        json.dumps(self, indent=4, cls=ApplicationJSONEncoder)


class ApplicationJSONEncoder(json.JSONEncoder):
    def default(self, obj: Application):
        if obj is Application:
            return {
                'applicationToken': obj.application_token,
                'id': obj.id,
                'name': obj.name,
                'sequenceNumber': obj.sequence_number,
                'tenantId': obj.tenant_id
            }
        else:
            raise TypeError("UserJsonEncoder got {} instead of Application.".format(type(obj)))


class ApplicationDictDecoder:
    @staticmethod
    def decode(obj: dict) -> Application:
        return Application(application_token=obj['applicationToken'], app_id=obj['id'], name=obj['name'],
                           sequence_number=int(obj['sequenceNumber']), tenant_id=obj['tenantId'])
