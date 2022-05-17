import typing

import sanic
from sanic.response import json

from ..discovery import DiscoveryService


class AgentHanlder():
    @staticmethod
    async def list(request: sanic.Request) -> sanic.HTTPResponse:
        ds = typing.cast(DiscoveryService, request.app.ctx.discovery_service)

        return json(ds.agents)

    @staticmethod
    async def delete(request: sanic.Request, agent: str) -> sanic.HTTPResponse:
        ds = typing.cast(DiscoveryService, request.app.ctx.discovery_service)

        return json(ds.pong(agent))

    def register(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("agents", url_prefix='/agents')
        bp.add_route(self.list, '/', methods=['GET'])
        bp.add_route(self.delete, '/<agent:str>', methods=['DELETE'])

        return bp
