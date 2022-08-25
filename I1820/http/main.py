import sanic

from ..discovery import DiscoveryService
from .agent import AgentHanlder
from .health import HealthHanlder
from .model import ModelHanlder
from .thing import ThingHandler


def app(ds: DiscoveryService) -> sanic.Sanic:
    app = sanic.Sanic("mia")
    app.ctx.discovery_service = ds

    app.blueprint(ModelHanlder().register())
    app.blueprint(HealthHanlder().register())
    app.blueprint(AgentHanlder().register())
    app.blueprint(ThingHandler().register())

    return app
