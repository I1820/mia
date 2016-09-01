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
    :type version: int
    """

    def __init__(self, notif_id, app_id, name, schema, version):
        self.id = notif_id
        self.app_id = app_id
        self.name = name
        self.schema = schema
        self.version = version

    def __lt__(self, other):
        return self.version < other.version

    def __le__(self, other):
        return self.version <= other.version


class NotificationJSONEncoder(json.JSONEncoder):
    def default(self, obj: Notification):
        if isinstance(obj, Notification):
            return {
            }
        else:
            raise TypeError(
                "NotificationJsonEncoder got {} instead of Notification".format(
                    type(obj))
