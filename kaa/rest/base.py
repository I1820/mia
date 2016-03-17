# In The Name Of God
# ========================================
# [] File Name : base.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================


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
        self.url_prefix = 'http://{0}:{1}@{2}/kaaAdmin/rest/api/'.format(username, password, address)
