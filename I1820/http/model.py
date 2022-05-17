import logging
import typing

import sanic
from sanic.response import json

from ..things import Things


class ModelHanlder():
    @staticmethod
    async def get(request: sanic.Request, name: str) -> sanic.HTTPResponse:
        logger = typing.cast(logging.Logger, request.app.ctx.logger)
        logger.info('request for thing %s', name)
        return json(Things.get(name).to_dict())

    def register(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("models", url_prefix='/models')
        bp.add_route(self.get, '/<name:str>', methods=['GET'])

        return bp
