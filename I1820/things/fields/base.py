import abc


class Field:
    '''
    Field represnts a measurement/actuation on a device.
    for example when we have lamp we can have on/off actuation on it.
    '''
    field_name: str = ""

    def __init__(self):
        self.name: str = ""
