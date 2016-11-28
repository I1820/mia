# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 09-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc
import threading


class ControllerMeta(abc.ABCMeta):
    instances = {}
    lock = threading.Lock()

    def __call__(self, *args, **kwargs):
        with self.lock:
            if self not in self.instances:
                self.instances[self] = super(ControllerMeta,
                                             self).__call__(*args, **kwargs)
        return self.instances[self]


class I1820Controller(metaclass=ControllerMeta):
    pass
