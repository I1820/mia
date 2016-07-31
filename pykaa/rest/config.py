# In The Name Of God
# ========================================
# [] File Name : config.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from pykaa.domain.config import Config, ConfigDictDecoder

import requests
from requests.exceptions import HTTPError


class T1820RestConfig:
    """
    This class provide a rest way for interfacing with 18.20 configs
    :type url_prefix: str
    """

    def __init__(self, address):
        self.url_prefix = 'http://{}/'.format(address)

    def get_last_configuration(self) -> Config:
        response = requests.get(self.url_prefix + "config")
        try:
            response.raise_for_status()
        except HTTPError as e:
            if response.status_code == 404:
                raise T1820RestConfigError("18.20 server not found", e) from e
            if response.status_code == 500:
                raise T1820RestConfigError(
                    "An unexpected error occurred on the server side", e) \
                    from e
        response = response.json()
        config = ConfigDictDecoder.decode(response[str(len(response) - 1)])
        return config


class T1820RestConfigError(Exception):
    """
    This class wraps server HTTP errors for 1820 configs
    :type message: str
    :type exception: HTTPError
    """

    def __init__(self, message, exception):
        super(T1820RestConfigError, self).__init__()
        self.message = message
        self.exception = exception

    def __str__(self) -> str:
        return "{0}: {1}".format(self.exception, self.message)
