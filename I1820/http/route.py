# In The Name Of God
# ========================================
# [] File Name : route.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
import flask
import flask_cors
import json
import jsonschema

from . import app
from ..domain.schemas.schema import log_request_schema
from ..domain.schemas.schema import notif_request_schema
from ..things.base import Things
from ..services.master import service_master
from ..controllers.discovery import DiscoveryController
from ..exceptions.thing import \
     ThingNotFoundException, ThingTypeNotImplementedException, \
     ThingInvalidAccessException


@app.route('/about')
def about_handler():
    return "18.20 is leaving us"


# I1820-UI


@app.route('/<path:path>', methods=['GET'])
def ui_handler(path):
    return flask.send_from_directory('../I1820-UI/dist', path)


@app.route('/', methods=['GET'])
def root_handler():
    return flask.send_file('../I1820-UI/dist/index.html')


# Human Side


# Models


@app.route('/model/<string:thing>', methods=['GET'])
def model_handler(thing):
    with service_master.service('model_service') as model_service:
        return json.dumps(model_service.get_model(thing))


# Agents


@app.route('/agent', methods=['GET'])
def agent_get_handler():
    discovery = DiscoveryController()
    return json.dumps(discovery.agents)


@app.route('/agent/<string:agent>', methods=['DELETE'])
def agent_remove_handler(agent):
    discovery = DiscoveryController()
    return json.dumps(discovery.pong(agent))


# Things


@app.route('/thing', methods=['POST'])
@flask_cors.cross_origin()
def thing_read_handler():
    data = flask.request.get_json(force=True)

    jsonschema.validate(data, log_request_schema)

    agent_id = data['agent_id']
    device_id = data['device_id']
    things = []
    if isinstance(data['device_id'], str):
        device_id = data['device_id']
        things.append(Things.get(data['type']).get_thing(agent_id, device_id))
    elif isinstance(data['device_id'], list):
        for device_id in data['device_id']:
            things.append(
                Things.get(data['type']).get_thing(agent_id, device_id))
    result = {}

    # Handling the requested states :)
    if 'states' in data.keys():
        for thing in things:
            if len(data['states']) == 0:
                data['states'] = [state.name for state in thing.states]
            for key in data['states']:
                result[key] = getattr(thing, key)

    # Even handling setting but I think it's not okey !
    if 'settings' in data.keys():
        for thing in things:
            for key in data['settings']:
                result[key] = getattr(thing, key)

    # Handling the statistics for having more fucking fun ...
    if hasattr(thing, 'statistics'):
        for thing in things:
            for key in [statistic.name for statistic in thing.statistics]:
                result[key] = getattr(thing, key)

    return json.dumps(result)


@app.route('/thing', methods=['PUT'])
@flask_cors.cross_origin()
def thing_write_handler():
    data = flask.request.get_json(force=True)

    jsonschema.validate(data, notif_request_schema)

    agent_id = data['agent_id']
    things = []
    if isinstance(data['device_id'], str):
        device_id = data['device_id']
        things.append(Things.get(data['type']).get_thing(agent_id, device_id))
    elif isinstance(data['device_id'], list):
        for device_id in data['device_id']:
            things.append(
                Things.get(data['type']).get_thing(agent_id, device_id))

    if 'settings' in data.keys():
        for thing in things:
            for key, value in data['settings'].items():
                setattr(thing, key, value)

    return json.dumps(data)


# Stats


@app.route('/stat/uptime', methods=['GET'])
def stat_uptime_handler():
    with service_master.service('stat_service') as stat_service:
        return str(stat_service.uptime())


# Error Side :P

@app.errorhandler(jsonschema.ValidationError)
def handle_invalid_request(error):
    return (str(error), 400, {})


@app.errorhandler(ThingNotFoundException)
def handle_invalid_usage(error):
    return (str(error), 404, {})


@app.errorhandler(ThingTypeNotImplementedException)
def handle_not_implemented_thing(error):
    return (str(error), 400, {})


@app.errorhandler(ThingInvalidAccessException)
def handle_invalid_access(error):
    return (str(error), 403, {})
