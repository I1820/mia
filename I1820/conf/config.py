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

from ..pykaa.rest.app import KaaRestApplication
from ..pykaa.rest.notif import KaaRestNotification


class I1820Kaa:
    def __init__(self, name, kaa):
        # Application
        self.app = {}
        kra = KaaRestApplication('%s:%s' % (kaa['host'], kaa['port']),
                                 kaa['user_developer'],
                                 kaa['passwd_developer'])
        apps = kra.get_all_applications()
        for app in apps:
            if app.name == name:
                self.app['name'] = app.name
                self.app['token'] = app.application_token
                self.app['uid'] = app.id
        # Notification
        self.notif = {}
        krn = KaaRestNotification('%s:%s' % (kaa['host'], kaa['port']),
                                  kaa['user_developer'],
                                  kaa['passwd_developer'])
        notifss = krn.get_all_notification_schemas(self.app['token'])
        notifss.sort(reverse=True)
        notifs = notifss[0]

        self.notif['name'] = notifs.name
        self.notif['uid'] = notifs.id
        self.notif['version'] = notifs.version


class I1820Config:
    def __init__(self, path):
        with open(path, 'r') as ymlfile:
            cfg = yaml.load(ymlfile)
        self.cfg = cfg
        self.kaa = None

    def __getattr__(self, name):
        section, field = name.split('_', maxsplit=1)
        if section == 'kaa' or section == 'mongodb':
            return self.cfg[section][field]
        elif section == 'app':
            if self.kaa is None:
                self.kaa = I1820Kaa(cfg['app']['name'], cfg['kaa'])
            return self.kaa.app[field]
        elif section == 'notif':
            if self.kaa is None:
                self.kaa = I1820Kaa(cfg['app']['name'], cfg['kaa'])
            return self.kaa.notif[field]


I1820_CONFIG_PATH = os.path.join(os.path.dirname(__file__), "1820.yml")
cfg = I1820Config(I1820_CONFIG_PATH)
