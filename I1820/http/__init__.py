from flask import Flask
from flask_cors import CORS
import socketio

sio = socketio.Server(async_mode='eventlet')

app = Flask("I1820")
app.config['LOGGER_NAME'] = 'I1820.http'
app.wsgi_app = socketio.Middleware(sio, app.wsgi_app)

CORS(app)
