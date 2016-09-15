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
from . import socketio
from ..things.base import Things
from ..domain.log import I1820LogDictDecoder, I1820LogJSONEncoder
from ..controller.discovery import DiscoveryController
from ..controller.log import LogController


@app.route('/test')
def test_handler():
    return "18.20 is leaving us"


# Thing Side


@app.route('/log', methods=['POST'])
def log_handler():
    data = flask.request.get_json(force=True)
    log = I1820LogDictDecoder.decode(data)

    # InfluxDB
    LogController().save(log)

    # SocketIO
    socketio.emit('log', I1820LogJSONEncoder().encode(log))
    socketio.emit('log', I1820LogJSONEncoder().encode(log),
                  namespace='/%s' % log.type)
    return ""


@app.route('/discovery', methods=['POST'])
def discovery_thing_handler():
    data = flask.request.get_json(force=True)
    discovery = DiscoveryController()
    discovery.ping(data, flask.request.remote_addr)
    return ""


# Human Side


@app.route('/discovery', methods=['GET'])
def discovery_human_handler():
    discovery = DiscoveryController()
    return json.dumps(discovery.rpis)


@app.route('/thing', methods=['POST', 'PUT'])
def thing_handler():
    data = flask.request.get_json(force=True)
    rpi_id = data['rpi_id']
    device_id = data['device_id']
    result = {}
    try:
        thing = Things.get(data['type']).get_thing(rpi_id, device_id)
    except ImportError as e:
        return ('%s is not one of our things: %s' % (data['type'], str(e)),
                400, {})
    except KeyError:
        return ('%s is not one of our RPis' % rpi_id, 404, {})
    if 'settings' in data.keys():
        for key, value in data['settings'].items():
            setattr(thing, key, value)
            result[key] = value
    if 'states' in data.keys():
        for key in data['states']:
            result[key] = getattr(thing, key)

    return json.dumps(result)
