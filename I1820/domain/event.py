# In The Name Of God
# ========================================
# [] File Name : event.py
#
# [] Creation Date : 30-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import json


class I1820Event:
    '''
    The I1820Event object contains information that is used to
    send realtime events to humans.

    :param type: type of event [Discovery, Log, Event]
    :type type: str
    :param data: event's data with following form:
    {
        rpi_id: RPi Identification
        device_id: device number relative to RPi
        type: device type
        state: {
            'temperature': 10
        }
    }
    '''
    def __init__(self, type: str, data: dict):
        self.type = type
        self.data = data

    def to_json(self):
        result = self.data
        result['event'] = self.type
        return json.dumps(result)
