# In The Name Of God
# ========================================
# [] File Name : app.py
#
# [] Creation Date : 3/17/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from .base import KaaRestBase, KaaRestError
from pykaa.domain.app import Application, ApplicationDictDecoder

import requests
from requests.exceptions import HTTPError
import json


class KaaRestApplication(KaaRestBase):
    """
    This class provide a rest way for interfacing with kaa applications
    """

    def __int__(self, address, username, password):
        super(KaaRestApplication, self).__init__(address, username, password)

    def get_all_applications(self) -> [Application]:
        applications = []
        response = requests.get(self.url_prefix + "applications")
        try:
            response.raise_for_status()
        except HTTPError as e:
            if response.status_code == 401:
                raise KaaRestApplicationError(
                    "The user is not authenticated or"
                    " invalid credentials were provided", e) from e
            if response.status_code == 403:
                raise KaaRestApplicationError(
                    "The authenticated user does not have the required role"
                    " (TENANT_ADMIN, TENANT_DEVELOPER, or TENANT_USER)", e) \
                    from e
            if response.status_code == 500:
                raise KaaRestApplicationError(
                    "An unexpected error occurred on the server side", e) \
                    from e
        response = json.loads(response.text)
        for obj in response:
            application = ApplicationDictDecoder.decode(obj)
            applications.append(application)
        return applications

    def get_application_by_id(self, application_id: str) -> Application:
        response = requests.get(
            self.url_prefix + "application/{}".format(application_id))
        response = json.loads(response.text)
        application = ApplicationDictDecoder.decode(response)
        return application


class KaaRestApplicationError(KaaRestError):
    """
    This class wraps server HTTP errors for kaa applications
    """

    def __init__(self, message, exception):
        super(KaaRestApplicationError, self).__init__(message, exception)
