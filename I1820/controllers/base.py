from __future__ import annotations

import abc
import threading
import typing


class ControllerMeta(abc.ABCMeta):
    instances: dict[type[Controller], Controller] = {}
    lock = threading.Lock()

    def __call__(cls, *args, **kwargs):
        cls = typing.cast(type[Controller], cls)

        with cls.lock:
            if cls not in cls.instances:
                cls.instances[cls] = super().__call__(*args, **kwargs)
        return cls.instances[cls]


class Controller(metaclass=ControllerMeta):
    """
    controllers must be signleton. this parent class create single controller
    instance on their first call and then return it always.
    """
