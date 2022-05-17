import typing

import sanic
from sanic.response import json

from ..domain.schemas.schema import log_request_schema, notif_request_schema
from ..things import Things


class ThingHandler():
    @staticmethod
    async def thing_read_handler(request: sanic.Request) -> sanic.HTTPResponse:
        data = request.json
        if data is None:
            return json(status=401, body='bad request')
        data = typing.cast(dict, data)

        agent_id = data['agent_id']
        device_id = data['device_id']
        things = []
        if isinstance(data['device_id'], str):
            device_id = data['device_id']
            things.append(
                Things.get(data['type']).get_thing(agent_id, device_id)
            )
        elif isinstance(data['device_id'], list):
            for device_id in data['device_id']:
                things.append(
                    Things.get(data['type']).get_thing(agent_id, device_id))
        result = {}

        # handles the requested states
        if 'states' in data.keys():
            for thing in things:
                if len(data['states']) == 0:
                    data['states'] = [state.name for state in thing.states]
                for key in data['states']:
                    result[key] = getattr(thing, key)

        # handles the requested settings.
        # these are not synced between mia nodes.
        # mia is not a distributed system!
        if 'settings' in data.keys():
            for thing in things:
                for key in data['settings']:
                    result[key] = getattr(thing, key)

        # handles the statistics.
        if 'statistics' in data.keys():
            for thing in things:
                for key in [statistic.name for statistic in thing.statistics]:
                    result[key] = getattr(thing, key)

        return json(result)

    @staticmethod
    async def thing_write_handler(request: sanic.Request) -> sanic.HTTPResponse:
        data = request.json
        if data is None:
            return json(status=401, body='bad request')
        data = typing.cast(dict, data)

        agent_id = data['agent_id']
        things = []
        if isinstance(data['device_id'], str):
            device_id = data['device_id']
            things.append(
                Things.get(data['type']).get_thing(agent_id, device_id)
            )
        elif isinstance(data['device_id'], list):
            for device_id in data['device_id']:
                things.append(
                    Things.get(data['type']).get_thing(agent_id, device_id))

        if 'settings' in data.keys():
            for thing in things:
                for key, value in data['settings'].items():
                    setattr(thing, key, value)

        return json(data)

    def register(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("things", url_prefix='/things')
        bp.add_route(self.thing_read_handler, '/', methods=['POST'])
        bp.add_route(self.thing_write_handler, '/', methods=['PUT'])

        return bp
