# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from requests.exceptions import HTTPError


class KaaRestBase:
    """
    This class provide basis for all Kaa Rest modules
    :type username : str
    :type password : str
    :type address : str
    """

    def __init__(self, address, username, password):
        self.username = username
        self.password = password
        self.url_prefix = 'http://{0}:{1}@{2}/kaaAdmin/rest/api/'.format(
            username, password, address)


class KaaRestError(Exception):
    """
    This class provide basis for all Kaa Rest modules errors

    :type message: str
    :type exception: HTTPError
    """

    def __init__(self, message, exception):
        super(KaaRestError, self).__init__()
        self.message = message
        self.exception = exception

    def __str__(self) -> str:
        return "{0}: {1}".format(self.exception, self.message)
