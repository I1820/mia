import logging

import sanic

from .model import ModelHanlder


def app() -> sanic.Sanic:
    app = sanic.Sanic('mia')
    app.ctx.logger = logging.getLogger('mia.http')

    mh = ModelHanlder()
    app.blueprint(mh.register())

    return app
