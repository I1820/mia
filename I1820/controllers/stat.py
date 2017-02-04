# In The Name Of God
# ========================================
# [] File Name : stat.py
#
# [] Creation Date : 22-11-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .base import I1820Controller

import datetime


class StatController(I1820Controller):
    def __init__(self):
        print(" * I1820 controllers: Stat Controller")
        self.start_time = datetime.datetime.now()

    def uptime(self):
        return datetime.datetime.now() - self.start_time
