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
from ..exceptions.thing import \
     ThingNotFoundException, ThingTypeNotImplementedException, \
     ThingInvalidAccessException


@app.route('/test')
def test_handler():
    return "18.20 is leaving us"


# I1820-UI

@app.route('/<path:path>', methods=['GET'])
def ui_handler(path):
    return flask.send_from_directory('../I1820-UI', path)


@app.route('/', methods=['GET'])
def root_handler():
    return flask.send_file('../I1820-UI/index.html')

# Thing Side


@app.route('/log', methods=['POST'])
def log_handler():
    data = flask.request.get_json(force=True)
    log = I1820LogDictDecoder.decode(data)

    thing = Things.get(log.type).get_thing(log.endpoint, log.device)

    for key, value in log.states.items():
        setattr(thing, key, {'value': value, 'time': log.timestamp})

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


@app.route('/thing', methods=['POST'])
def thing_read_handler():
    data = flask.request.get_json(force=True)
    rpi_id = data['rpi_id']
    device_id = data['device_id']
    result = {}

    thing = Things.get(data['type']).get_thing(rpi_id, device_id)

    if 'states' in data.keys():
        for key in data['states']:
            result[key] = getattr(thing, key)
    if 'statistics' in data.keys():
        for key in data['statistics']:
            result[key] = getattr(thing, key)

    return json.dumps(result)


@app.route('/thing', methods=['PUT'])
def thing_write_handler():
    data = flask.request.get_json(force=True)
    rpi_id = data['rpi_id']
    device_id = data['device_id']
    result = {}

    thing = Things.get(data['type']).get_thing(rpi_id, device_id)

    if 'settings' in data.keys():
        for key, value in data['settings'].items():
            setattr(thing, key, value)
            result[key] = value

    return json.dumps(result)


# Error Side :P

@app.errorhandler(ThingNotFoundException)
def handle_invalid_usage(error):
    return (str(error), 404, {})


@app.errorhandler(ThingTypeNotImplementedException)
def handle_invalid_request(error):
    return (str(error), 400, {})


@app.errorhandler(ThingInvalidAccessException)
def handle_invalid_access(error):
    return (str(error), 403, {})
