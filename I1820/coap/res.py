# In The Name Of God
# ========================================
# [] File Name : res.py
#
# [] Creation Date : 22-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import aiocoap.resource as resource
import json
import aiocoap

from ..controller.discovery import DiscoveryController


class DiscoveryResource(resource.Resource):
    async def render_post(self, request):
        data = json.loads(request.payload.decode('ASCII'))
        discovery = DiscoveryController()
        print(request)
        discovery.ping(data, request.get_request_uri())
        return aiocoap.Message(code=aiocoap.ACK)


class LogResource(resource.Resource):
    pass
