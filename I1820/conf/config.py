# In The Name Of God
# ========================================
# [] File Name : config.py
#
# [] Creation Date : 01-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import os
import configparser


class I1820Config:
    def __init__(self, path):
        cfg = configparser.ConfigParser()

        # File based configurations
        cfg.read(path)

        self.cfg = cfg

    def __getattr__(self, name):
        if '_' in name:
            section, field = name.split('_', maxsplit=1)
        else:
            section = name
        if section == 'appenders':
            if '_' in field:
                db, field = field.split('_', maxsplit=1)
                return self.cfg['%s.appenders.i1820.org' % db][field]
            else:
                return self.cfg['appenders.i1820.org'][field]
        elif section == 'mqtt':
            return self.cfg['mqtt.i1820.org'][field]
        elif section == 'endpoints':
            return self.cfg['things.i1820.org']['endpoints'].split(' ')


I1820_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "1820.ini")
cfg = I1820Config(I1820_CONFIG_PATH)
