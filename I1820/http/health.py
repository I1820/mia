import sanic
from sanic.response import empty


class HealthHanlder():
    @staticmethod
    async def health(request: sanic.Request) -> sanic.HTTPResponse:
        return empty()

    def register(self) -> sanic.Blueprint:
        bp = sanic.Blueprint("healthz", url_prefix='/healthz')
        bp.add_route(self.health, '/', methods=['GET'])

        return bp
