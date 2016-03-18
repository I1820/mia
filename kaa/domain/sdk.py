# In The Name Of God
# ========================================
# [] File Name : sdk.py
#
# [] Creation Date : 3/18/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

import datetime
import json


class SDKProfile:
    """
    This object represents a Kaa SDK profile
    :type aef_map_ids: [str]
    :type application_id: str
    :type application_token: str
    :type configuration_schema_version: int
    :type log_schema_version: int
    :type notification_schema_version: int
    :type profile_schema_version: int
    :type created_time: datetime.datetime
    :type created_username: str
    :type endpoint_count: int
    :type sdk_id: str
    :type name: str
    :type token: str
    :type default_verifier_token: str
    """

    def __init__(self, aef_map_ids, application_id, application_token, default_verifier_token,
                 configuration_schema_version, log_schema_version, notification_schema_version, profile_schema_version,
                 created_time, created_username, endpoint_count, sdk_id, name, token):
        self.aef_map_ids = aef_map_ids
        self.application_id = application_id
        self.application_token = application_token
        self.configuration_schema_version = configuration_schema_version
        self.log_schema_version = log_schema_version
        self.notification_schema_version = notification_schema_version
        self.profile_schema_version = profile_schema_version
        self.created_time = created_time
        self.created_username = created_username
        self.endpoint_count = endpoint_count
        self.id = sdk_id
        self.name = name
        self.token = token
        self.default_verifier_token = default_verifier_token

    def __str__(self) -> str:
        return json.dumps(self, indent=4, cls=SDKProfileJSONEncoder)


class SDKProfileJSONEncoder(json.JSONEncoder):
    def default(self, obj: SDKProfile):
        if isinstance(obj, SDKProfile):
            return {
                "aefMapIds": obj.aef_map_ids,
                "applicationId": obj.application_id,
                "applicationToken": obj.application_token,
                "configurationSchemaVersion": obj.configuration_schema_version,
                "logSchemaVersion": obj.log_schema_version,
                "notificationSchemaVersion": obj.notification_schema_version,
                "profileSchemaVersion": obj.profile_schema_version,
                "createdTime": obj.created_time.second,
                "createdUsername": obj.created_username,
                "endpointCount": obj.endpoint_count,
                "id": obj.id,
                "name": obj.name,
                "token": obj.token,
                "defaultVerifierToken": obj.default_verifier_token
            }
        else:
            raise TypeError("SDKProfileJsonEncoder got {} instead of SDKProfile.".format(type(obj)))


class SDKProfileDictDecoder:
    @staticmethod
    def decode(obj: dict) -> SDKProfile:
        pass
