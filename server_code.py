import cv2 as cv
import numpy as np
import requests
import simplejson as json
from flask import Flask, jsonify, request, render_template, send_from_directory
from pprint import pprint
from ast import literal_eval

app = Flask(__name__)
app.debug = True
faces = []

@app.route("/")
def main():
    #return send_from_directory('','index.html')
    #return app.send_static_file('index.html')
    return render_template('index.html')

@app.route("/faces/<path:filename>")
def returnFace(filename):
    print filename
    return send_from_directory('./faces/',filename)

@app.route("/facerecognition")
def facerecognition():
    global faces
    paths = []
    i = 0
    for face in faces:
        face = np.array(face)
        #face = cv.imdecode(face,1)
        filename = "./faces/" + str(i)+".jpg"
        cv.imwrite(filename,face)
        paths.append(filename)
        i += 1
    return render_template("facerecognition.html", faces=paths)

@app.route("/upload",methods=["POST"])
def test():
    #pprint(vars(request))
    #print json.loads(request.form['img'])
    faces.append(json.loads(request.form['img']))
    #faces.append( request.form['img'] )
    #return "Testing!"
    try:
        return jsonify(dict(ok=True))
    except:
        pass


if __name__ == '__main__':
    app.run()

