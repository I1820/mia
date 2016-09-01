# In The Name Of God
# ========================================
# [] File Name : notif.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import json


class NotificationSchema:
    """
    This object represnets a Kaa notification schema
    :type app_id: str
    :type name: str
    :type id: str
    :type schema: str
    :type description: str
    :type version: int
    """

    def __init__(self, notif_id, app_id, name,
                 schema, version, description):
        self.id = notif_id
        self.app_id = app_id
        self.name = name
        self.schema = schema
        self.version = version
        self.description = description

    def __lt__(self, other):
        return self.version < other.version

    def __le__(self, other):
        return self.version <= other.version

    def __eq__(self, other):
        return self.version == other.version

    def __ne__(self, other):
        return self.version != other.version

    def __gt__(self, other):
        return self.version > other.version

    def __ge__(self, other):
        return self.version >= other.version


class NotificationSchemaJSONEncoder(json.JSONEncoder):
    def default(self, obj: NotificationSchema):
        if isinstance(obj, NotificationSchema):
            return {
                'id': obj.id,
                'applicationId': obj.app_id,
                'name': obj.name,
                'schema': obj.schema,
                'version': obj.version,
                'description': obj.description
            }
        else:
            raise TypeError(
                "NotificationJsonEncoder got {} instead of NotificationSchema"
                .format(type(obj)))


class NotificationSchemaDictDecoder:
    @staticmethod
    def decode(obj: dict) -> NotificationSchema:
        return NotificationSchema(notif_id=obj['id'], name=obj['name'],
                                  app_id=obj['applicationId'],
                                  schema=obj['schema'],
                                  version=int(obj['version']),
                                  description=obj['description'])
