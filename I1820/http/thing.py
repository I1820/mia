'''
thing related apis which can be used for sending information to things
or reading its information.
'''
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


@dataclasses.dataclass
class ThingWriteRequest():
    '''
    configuration request for the thing settings.
    '''
    agent_id: str
    device_id: str | list[str]
    type: str
    settings: dict[str, typing.Any]


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
    @openapi.body({"application/json": ThingWriteRequest})
    @openapi.description('''
    write things information these information includes:
    - settings
    ''')
    @validate(json=ThingWriteRequest)
    async def thing_write_handler(
            _: sanic.Request,
            body: ThingWriteRequest,
    ) -> sanic.HTTPResponse:
        agent_id = body.agent_id
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

        for thing in things:
            for key, value in body.settings.items():
                setattr(thing, key, value)

        return json(body)

    def register(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("things", url_prefix='/things')
        bp.add_route(self.thing_read_handler, '/', methods=['POST'])
        bp.add_route(self.thing_write_handler, '/', methods=['PUT'])

        return bp
