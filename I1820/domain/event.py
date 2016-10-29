# In The Name Of God
# ========================================
# [] File Name : event.py
#
# [] Creation Date : 30-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


class I1820Event:
    '''
    The I1820Event object contains information that is used to
    send realtime events to humans.

    :param type: type of event [Discovery, Log, Event]
    :type type: str
    '''
    def __init__(self, type: str):
        self.type = type
