# In The Name Of God
# ========================================
# [] File Name : sdk.py
#
# [] Creation Date : 3/18/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from .base import KaaRestBase

from kaa.domain.sdk import SDKProfile, SDKProfileDictDecoder

import requests
import json


class KaaRestSDKProfile(KaaRestBase):
    def __int__(self, address, username, password):
        super(KaaRestSDKProfile, self).__init__(address, username, password)

    def get_all_sdk_profiles(self, application_id: int) -> [SDKProfile]:
        sdk_profiles = []
        response = requests.get(self.url_prefix + "sdkProfiles/{}".format(application_id))
        response = json.loads(response.text)
        for obj in response:
            sdk_profile = SDKProfileDictDecoder.decode(obj)
            sdk_profiles.append(sdk_profile)
        return sdk_profiles
