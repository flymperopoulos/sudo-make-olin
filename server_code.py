import requests
import simplejson as json
from flask import Flask

app = Flask(__name__,static_url_path='')

faces = []

@app.route("/")
def main():
    return 'Hello world!'
    #return send_from_directory('','index.html')
    #return app.send_static_file('index.html')
    #return render_template('index.html')

@app.route("/test")#,methods=["POST"])
def test():
    faces.append( request.form['img'] )
    #return "Testing!"
