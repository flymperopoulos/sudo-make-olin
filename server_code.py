import requests
import simplejson as json
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hello world!'

@app.route("/test")
def test():
    return "Testing!"