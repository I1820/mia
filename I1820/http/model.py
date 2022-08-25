import logging
import typing

import sanic
from sanic.response import json

from I1820.things import Things
from I1820.logger import logger


class ModelHanlder:
    @staticmethod
    async def get(_: sanic.Request, name: str) -> sanic.HTTPResponse:
        logger.info("request for thing %s", name)
        return json(Things.get(name).to_dict())

    def register(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("models", url_prefix="/models")
        bp.add_route(self.get, "/<name:str>", methods=["GET"])

        return bp
