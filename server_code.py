import requests
import simplejson as json
from flask import Flask

app = Flask(__name__,static_url_path='')

@app.route("/")
def hello():
    #return send_from_directory('','index.html')
    #return app.send_static_file('index.html')
    return render_template('index.html',None)

@app.route("/test")
def test():
    return "Testing!"
