# In The Name Of God
# ========================================
# [] File Name : coap-client.py
#
# [] Creation Date : 22-09-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import logging
import asyncio
import json
import aiocoap

logging.basicConfig(level=logging.INFO)


async def main():
    protocol = await aiocoap.Context.create_client_context()

    request = aiocoap.Message(code=aiocoap.POST,
                              payload=json.dumps(
                                  {'rpi_id': '1',
                                   'time': 10,
                                   'things': []}).encode('ASCII'))
    request.set_request_uri('coap://localhost/discovery')

    try:
        response = await protocol.request(request).response
    except Exception as e:
        print('Failed to fetch resource:')
        print(e)
    else:
        print('Result: %s\n%r' % (response.code, response.payload))

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(main())
