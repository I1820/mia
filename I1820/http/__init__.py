from flask import Flask
from flask_cors import CORS

app = Flask("I1820")
app.config['LOGGER_NAME'] = 'I1820.http'
CORS(app)
