from __future__ import annotations

import abc
import threading


class Controller():
    '''
    controllers must be signleton. this parent class create single controller
    instance on their first call and then return it always.
    '''

    instances: dict[type[Controller], Controller] = {}
    lock = threading.Lock()

    @classmethod
    def __call__(cls):
        with cls.lock:
            if cls not in cls.instances:
                cls.instances[cls] = cls()
        return cls.instances[cls]
