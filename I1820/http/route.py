# In The Name Of God
# ========================================
# [] File Name : route.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import flask

from . import app
from ..things.base import Things


@app.route('/test')
def test_handler():
    return "18.20 is leaving us"


@app.route('/thing/<uuid:rpi_id>/<uuid:device_id>', methods=['POST', 'PUT'])
def thing_handler(rpi_id, device_id):
    data = flask.request.get_json(force=True)
    data['rpi_id'] = rpi_id
    data['device_id'] = device_id
    try:
        return Things.get(data['type']).handle(data)
    except ImportError as e:
        return ('%s is not one of our things: %s' % (data['type'], str(e)),
                400, {})
