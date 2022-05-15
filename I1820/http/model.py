import sanic

from ..things.model import ModelService


class ModelHanlder():
    def __init__(self, model_service: ModelService):
        self.model_service = model_service

    def list(self, request: sanic.Request) -> sanic.HTTPResponse:
        self.model_service
