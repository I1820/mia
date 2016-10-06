# In The Name Of God
# ========================================
# [] File Name : config.py
#
# [] Creation Date : 01-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import yaml
import os


class I1820Config:
    def __init__(self, path):
        with open(path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.cfg = cfg

    def __getattr__(self, name):
        if '_' in name:
            section, field = name.split('_', maxsplit=1)
        else:
            section = name
        if section == 'influxdb':
            return self.cfg[section][field]
        elif section == 'endpoints':
            return self.cfg[section]


I1820_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "1820.yml")
cfg = I1820Config(I1820_CONFIG_PATH)
