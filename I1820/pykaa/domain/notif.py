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
    """

    def __init__(self):
        pass


class NotificationJSONEncoder(json.JSONEncoder):
    def default(self, obj: Notification):
        if isinstance(obj, Notification):
            return {
            }
        else:
            raise TypeError(
                "NotificationJsonEncoder got {} instead of Notification".format(
                    type(obj))
