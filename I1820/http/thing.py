import dataclasses
import typing

import sanic
from sanic.response import json
from sanic_ext import openapi, validate

from ..things import Things


@dataclasses.dataclass
class ThingReadRequest():
    '''
    request for the thing information including states,
    settings and statistics.
    '''
    agent_id: str
    device_id: str | list[str]
    type: str
    states: list[str] = dataclasses.field(default_factory=list)
    settings: list[str] | None = None
    statistics: bool = False


class ThingWriteRequest():
    pass


class ThingHandler():
    @staticmethod
    @openapi.body({"application/json": ThingReadRequest})
    @openapi.description('''
    read things information these information includes:
    - states
    - statistics
    - settings

    please note that *settings* must be set before they can be read.
    ''')
    @validate(json=ThingReadRequest)
    async def thing_read_handler(
            _: sanic.Request,
            body: ThingReadRequest,
    ) -> sanic.HTTPResponse:
        '''
        read lastest things' state, settings etc.
        '''
        agent_id = body.agent_id
        device_id = body.device_id
        things = []

        if isinstance(body.device_id, str):
            device_id = body.device_id
            things.append(
                Things.get(body.type).get_thing(agent_id, device_id)
            )
        elif isinstance(body.device_id, list):
            for device_id in body.device_id:
                things.append(
                    Things.get(body.type).get_thing(agent_id, device_id))
        result = {}

        # handles the requested states
        for thing in things:
            if len(body.states) == 0:
                body.states = [state.name for state in thing.states]
            for key in body.states:
                result[key] = getattr(thing, key)

        # handles the requested settings.
        # these are not synced between mia nodes.
        # mia is not a distributed system!
        if body.settings is not None:
            for thing in things:
                for key in body.settings:
                    result[key] = getattr(thing, key)

        # handles the statistics.
        if body.statistics is True:
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
