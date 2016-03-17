# In The Name Of God
# ========================================
# [] File Name : app.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from .base import KaaRestBase
from domain.app import Application, ApplicationDictDecoder

import requests
import json


class KaaRestApplication(KaaRestBase):
    def __int__(self, address, username, password):
        super(KaaRestApplication, self).__init__(address, username, password)

    def get_all_applications(self) -> [Application]:
        applications = []
        response = requests.get(self.url_prefix + "applications")
        response = json.loads(response.text)
        for obj in response:
            application = ApplicationDictDecoder.decode(obj)
            applications = applications.append(application)
        return applications
