# In The Name Of God
# ========================================
# [] File Name : route.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from flask import request

from . import app
from ..things.base import Things


@app.route('/<uuid:rpi_id>/<uuid:device_id>', methods=['POST', 'PUT'])
def thing_handler(rpi_id, device_id):
    data = request.get_json(force=True)
    data['rpi_id'] = rpi_id
    data['device_id'] = device_id
    return Things.get(data['type']).handle(data)
