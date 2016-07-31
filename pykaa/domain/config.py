# In The Name Of God
# ========================================
# [] File Name : app.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

import json


class Config:
    """
    This object represents a Configuration for connecting to Kaa
    :type name: str
    :type kaa_ip: str
    :type kaa_port: int
    :type kaa_admin_user: str
    :type kaa_admin_password: str
    :type kaa_developer_user: str
    :type kaa_developer_password: str
    """

    def __init__(self, name, kaa_ip, kaa_port,
                 kaa_admin_user, kaa_admin_password,
                 kaa_developer_user, kaa_developer_password):
        self.name = name
        self.kaa_ip = kaa_ip
        self.kaa_port = kaa_port
        self.kaa_admin_user = kaa_admin_user
        self.kaa_admin_password = kaa_admin_password
        self.kaa_developer_user = kaa_developer_user
        self.kaa_developer_password = kaa_developer_password

    def __str__(self) -> str:
        return json.dumps(self, indent=4, cls=ConfigJSONEncoder)


class ConfigJSONEncoder(json.JSONEncoder):
    def default(self, obj: Config):
        if isinstance(obj, Config):
            return {
                'name': obj.name,
                'kaa_ip': obj.kaa_ip,
                'kaa_port': obj.kaa_port,
                'kaa_admin_user': obj.kaa_admin_user,
                'kaa_admin_password': obj.kaa_admin_password,
                'kaa_developer_user': obj.kaa_developer_user,
                'kaa_devloper_password': obj.kaa_developer_password
            }
        else:
            raise TypeError(
                "ConfigJsonEncoder got {} instead of Config.".format(
                    type(obj)))


class ConfigDictDecoder:
    @staticmethod
    def decode(obj: dict) -> Config:
        return Config(name=obj['name'], kaa_ip=obj['kaa_ip'],
                      kaa_port=int(obj['kaa_port']),
                      kaa_admin_user=obj['kaa_admin_user'],
                      kaa_admin_password=obj['kaa_admin_password'],
                      kaa_developer_user=obj['kaa_developer_user'],
                      kaa_developer_password=obj['kaa_developer_password'])
