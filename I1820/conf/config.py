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
        try:
            ymlfile = open(path, 'r')
        except IOError:
            cfg = {}
            cfg['influxdb'] = {}
            cfg['influxdb']['host'] = os.getenv(
                'I1820_INFLUXDB_HOST', '0.0.0.0')
            cfg['influxdb']['port'] = os.getenv(
                'I1820_INFLUXDB_PORT', '8086')
            cfg['influxdb']['db'] = os.getenv(
                'I1820_INFLUXDB_DB', 'I1820')
            cfg['influxdb']['user'] = os.getenv(
                'I1820_INFLUXDB_USER', 'root')
            cfg['influxdb']['passwd'] = os.getenv(
                'I1820_INFLUXDB_PASSWD', 'root')
            cfg['endpoints'] = os.getenv('I1820_ENDPOINTS', '').split(' ')
        else:
            with ymlfile:
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
