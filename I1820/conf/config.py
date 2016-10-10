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

        # Environment based configurations
        env_cfg = {}
        env_cfg['InfluxDB'] = {}
        env_cfg['InfluxDB']['host'] = os.getenv('I1820_INFLUXDB_HOST',
                                                '0.0.0.0')
        env_cfg['InfluxDB']['port'] = os.getenv('I1820_INFLUXDB_PORT', '8086')
        env_cfg['InfluxDB']['db'] = os.getenv('I1820_INFLUXDB_DB', 'I1820')
        env_cfg['InfluxDB']['user'] = os.getenv('I1820_INFLUXDB_USER', 'root')
        env_cfg['InfluxDB']['passwd'] = os.getenv('I1820_INFLUXDB_PASSWD',
                                                  'root')
        env_cfg['Things'] = {}
        env_cfg['Things']['endpoints'] = os.getenv('I1820_ENDPOINTS', '')
        cfg.read_dict(env_cfg)

        # File based configurations
        cfg.read(path)

        self.cfg = cfg

    def __getattr__(self, name):
        if '_' in name:
            section, field = name.split('_', maxsplit=1)
        else:
            section = name
        if section == 'influxdb':
            return self.cfg['InfluxDB'][field]
        elif section == 'endpoints':
            return self.cfg['Things']['endpoints'].split(' ')


I1820_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "1820.ini")
cfg = I1820Config(I1820_CONFIG_PATH)
