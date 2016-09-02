# In The Name Of God
# ========================================
# [] File Name : route.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import flask
import json

from . import app
from ..things.base import Things


@app.route('/test')
def test_handler():
    return "18.20 is leaving us"


@app.route('/service/<string:name>', methods=['POST'])
def service_handler(name):
    pass


@app.route('/thing/<uuid:rpi_id>/<uuid:device_id>', methods=['POST', 'PUT'])
def thing_handler(rpi_id, device_id):
    data = flask.request.get_json(force=True)
    result = {}
    try:
        thing = Things.get(data['type'])(rpi_id, device_id)
    except ImportError as e:
        return ('%s is not one of our things: %s' % (data['type'], str(e)),
                400, {})
    if 'settings' in data.keys():
        for key, value in data['settings'].items():
            setattr(thing, key, value)
            result[key] = value
    if 'status' in data.keys():
        for key in data['status']:
            result[key] = getattr(thing, key)

    return json.dumps(result)
