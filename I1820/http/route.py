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

from . import app
from ..things.base import Things
from ..controllers.discovery import DiscoveryController
from ..controllers.plugin import PluginController
from ..controllers.model import ModelController
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


@app.route('/model/<string:thing>', methods=['GET'])
def model_handler(thing):
    model = ModelController()
    return json.dumps(model.get_model(thing))


@app.route('/agent', methods=['GET'])
def agent_get_handler():
    discovery = DiscoveryController()
    return json.dumps(discovery.agents)


@app.route('agent/<string:agent>', methods=['DELETE'])
def agent_remove_handler(agent):
    discovery = DiscoveryController(agent)
    return discovery.pong(agent)


@app.route('/thing', methods=['POST'])
@flask_cors.cross_origin()
def thing_read_handler():
    data = flask.request.get_json(force=True)
    agent_id = data['agent_id']
    device_id = data['device_id']
    result = {}

    thing = Things.get(data['type']).get_thing(agent_id, device_id)

    # Handling the requested states :)
    if 'states' in data.keys():
        if len(data['states']) == 0:
            data['states'] = thing.states
        for key in data['states']:
            result[key] = getattr(thing, key)

    # Handling the statistics for having more fucking fun ...
    if hasattr(thing, 'statistics'):
        for key in thing.statistics:
            result[key] = getattr(thing, key)

    return json.dumps(result)


@app.route('/thing', methods=['PUT'])
@flask_cors.cross_origin()
def thing_write_handler():
    data = flask.request.get_json(force=True)
    agent_id = data['agent_id']
    device_id = data['device_id']

    thing = Things.get(data['type']).get_thing(agent_id, device_id)

    if 'settings' in data.keys():
        for key, value in data['settings'].items():
            setattr(thing, key, value)

    return json.dumps(data)


@app.route('/plugin', methods=['POST'])
def plugin_create_handler():
    data = flask.request.get_json(force=True)

    return str(PluginController().new_plugin(data['type'], data['arguments']))


@app.route('/plugin', methods=['GET'])
def plugin_list_handler():
    return json.dumps(PluginController().list_plugin())


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
