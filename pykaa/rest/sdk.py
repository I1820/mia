# In The Name Of God
# ========================================
# [] File Name : sdk.py
#
# [] Creation Date : 3/18/16
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================

from .base import KaaRestBase

from pykaa.domain.sdk import SDKProfile, SDKProfileDictDecoder, \
    SDKProfileTargetPlatform

import requests
import json


class KaaRestSDKProfile(KaaRestBase):
    def __init__(self, address, username, password):
        super(KaaRestSDKProfile, self).__init__(address, username, password)

    def get_all_sdk_profiles(self, application_token: sdk) -> [SDKProfile]:
        sdk_profiles = []
        response = requests.get(
            self.url_prefix + "sdkProfilesByAppToken/{}".format(application_token))
        response = json.loads(response.text)
        for obj in response:
            sdk_profile = SDKProfileDictDecoder.decode(obj)
            sdk_profiles.append(sdk_profile)
        return sdk_profiles

    def generate_endpoint_sdk(self, profile_sdk_id: str,
                              target_platform: SDKProfileTargetPlatform,
                              filename: str):
        params = {
            'sdkProfileId': profile_sdk_id,
            'targetPlatform': target_platform.value
        }
        response = requests.post(self.url_prefix + "sdk", data=params)
        with open(filename, 'wb') as fd:
            for chunk in response.iter_content(512):
                fd.write(chunk)
