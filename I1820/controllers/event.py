from ..domain.event import I1820Event


class EventController():
    '''
    The EventController controls human related events. these events
    base on :class:`I1820Event`.
    **Use Event for sending realtime information to humans.**
    '''
    def __init__(self):
        pass

    def event(self, event: I1820Event):
        # sio.emit(event.type, data=event.to_json(), namespace='/I1820')
        pass
