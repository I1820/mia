import logging

from gevent.wsgi import WSGIServer

from .route import app

logger = logging.getLogger('I1820.wsgi')

IP = '0.0.0.0'
PORT = 8080
http_server = WSGIServer((IP, PORT), application=app, log=logger)


def main():
    print(' * HTTP at %s:%d' % (IP, PORT))
    http_server.serve_forever()


def die():
    print(' > HTTP Die')
    http_server.stop()
