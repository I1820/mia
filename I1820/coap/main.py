# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 22-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import aiocoap.resource as resource
import asyncio
import aiocoap

from .res import DiscoveryResource, LogResource


def main():
    # Event loop creation
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    # Resource tree creation
    root = resource.Site()
    root.add_resource(('discovery',), DiscoveryResource())
    root.add_resource(('log',), LogResource())
    asyncio.async(aiocoap.Context.create_server_context(root))

    # Run the event loop
    asyncio.get_event_loop().run_forever()
