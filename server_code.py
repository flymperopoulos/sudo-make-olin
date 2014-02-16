import requests
import simplejson as json
from flask import Flask, jsonify, request
from pprint import pprint

app = Flask(__name__)
app.debug = True
faces = []

@app.route("/")
def main():
    return str(faces)
    #return send_from_directory('','index.html')
    #return app.send_static_file('index.html')
    #return render_template('index.html')

@app.route("/upload",methods=["POST"])
def test():
    pprint(vars(request))
    print request.form['img']
    #faces.append( request.form['img'] )
    #return "Testing!"
    return jsonify(dict(ok=True))

if __name__ == '__main__':
    app.run()
