from flask import Flask
from flask_socketio import SocketIO


app = Flask("I1820")
socketio = SocketIO(app)
