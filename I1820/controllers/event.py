# In The Name Of God
# ========================================
# [] File Name : event.py
#
# [] Creation Date : 30-10-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller
from ..domain.event import I1820Event
from ..http import sio


class EventController(I1820Controller):
    '''
    The EventController controls human related events. these events
    base on :class:`I1820Event`.
    **Use Event for sending realtime information to humans.**
    '''
    def __init__(self):
        pass

    def event(self, event: I1820Event):
        sio.emit(event.type, data=event.to_json(), namespace='event')
