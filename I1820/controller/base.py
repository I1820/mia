# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 09-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import abc


class ControllerMeta(abc.ABCMeta):
    instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self.instances:
            self.instances[self] = super(ControllerMeta,
                                         self).__call__(*args, **kwargs)
        return self.instances[self]


class I1820Controller(metaclass=ControllerMeta):
    pass
