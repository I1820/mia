# In The Name Of God
# ========================================
# [] File Name : main.py
#
# [] Creation Date : 26-08-2016
#
# [] Created By : Parham Alvani (parham.alvani@gmail.com)
# =======================================
from .route import app
from gevent.wsgi import WSGIServer

import logging

logger = logging.getLogger('I1820.wsgi')


def main():
    ip = '0.0.0.0'
    port = 8080
    http_server = WSGIServer((ip, port), application=app, log=logger)
    print(' * HTTP at %s:%d' % (ip, port))
    http_server.serve_forever()
