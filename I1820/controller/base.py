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

    @classmethod
    def __call__(cls, *args, **kwargs):
        if cls not in cls.instances:
            cls.instances[cls] = super(ControllerMeta,
                                       cls).__call__(*args, **kwargs)
            return cls.instances[cls]


class I1820Controller(metaclass=ControllerMeta):
    pass
