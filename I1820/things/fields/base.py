import abc


class Field:
    def __init__(self):
        self.name = None

    @property
    @abc.abstractmethod
    def field_name(self):
        raise NotImplemented()
