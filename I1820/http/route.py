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


@app.route('/test')
def test_handler():
    return "18.20 is leaving us"


# Thing Side


@app.route('/log', methods=['POST'])
def log_handler():
    data = flask.request.get_json(force=True)
    log = I1820LogDictDecoder.decode(data)

    try:
        thing = Things.get(log.type).get_thing(log.endpoint, log.device)
    except ImportError as e:
        return ('%s is not one of our things: %s' % (log.type, str(e)),
                400, {})
    except KeyError:
        return ('%s is not one of our RPis' % log.endpoint, 404, {})
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
    """
    @api {get} /discovery Get avaiable things and rpis
    @apiName Discovery
    @apiGroup Thing

    @apiDescription Get avaiable things and rpis until when
    you requested.

    @apiSuccess {json} response List of rpis and their attached things
    @apiSuccessExample {json} Discovery Example:
        {
            "b07882d6-5c28-597b-89f9-d250f74b0bad": {
                "time": "2016-09-20 18:05:56.124096",
                "things": [
                    {
                        "id": "0",
                        "attributes": {},
                        "type": "lamp"
                    },
                    {
                        "id": "1",
                        "attributes": {},
                        "type": "temperature"
                    }
                ],
                "ip": "192.168.1.4"
            }
        }
    """
    discovery = DiscoveryController()
    return json.dumps(discovery.rpis)


@app.route('/thing', methods=['POST', 'PUT'])
def thing_handler():
    """
    @api {post} /thing Get thing states or Change thing settings
    @apiName Thing
    @apiGroup Thing

    @apiDescription Read or Update thing states and settings
    respectively based on I1820 Information Model.

    @apiErrorExample {string} Thing Not Found:
        HTTP/1.1 400 Bad Request
        humidity is not one of things
    @apiErrorExample {string} RPi Not Discovered:
        HTTP/1.1 404 Not Found
        aa60d333-42ee-4311-87fc-ac08b1dd8773 is not one of our RPi's

    @apiParam {json} request Thing requested states or Thing target settings
    @apiParamExample {json} States Request Example:
        {
            "type": "temperature",
            "device_id": 0,
            "rpi_id": "cdede389-2315-419c-b1d5-ee9a9b43be2a",
            "states": [
                "temperature"
            ]
        }
    @apiParamExample {json} Settings Target Example:
        {
            "type": "lamp",
            "device_id": 0,
            "rpi_id": "cdede389-2315-419c-b1d5-ee9a9b43be2a",
            "settings": {
                "on": true
            }
        }

    @apiSuccess {json} response Value of thing requested states or New value of thing target settings
    @apiSuccessExample {json} States Request Example:
        {
            "temperature": 10
        }
    """
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
