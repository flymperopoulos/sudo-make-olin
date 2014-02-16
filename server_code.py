import requests
import simplejson as json
from flask import Flask, jsonify, request, render_template
from pprint import pprint

app = Flask(__name__)
app.debug = True
faces = []
faces = [
	"http://www.greenteam.mersd.org/wp-content/uploads/2013/11/amazon-logo.jpeg",
	"http://static.infowars.com/bindnfocom/2013/11/Bank-of-America-logo1.jpg",
	"http://siliconrepublic.com/fs/img/news/201209/rs-426x288/new-ebay-logo.jpg",
	"http://www.computec.co.jp/clients/images/logo_citi.jpg",
	"http://d1xcqlxj49e9dd.cloudfront.net/wp-content/uploads/chase_3_after1.jpg",
	"http://www.myrtlebeachgolf.com/media/images/fedex_logo.jpg"
	]

@app.route("/")
def main():
    #return send_from_directory('','index.html')
    #return app.send_static_file('index.html')
    return render_template('index.html')

@app.route("/facerecognition")
def facerecognition():
    global faces
    return render_template("facerecognition.html", faces=faces)

@app.route("/upload",methods=["POST"])
def test():
    pprint(vars(request))
    print request.form['img']
    #faces.append( request.form['img'] )
    #return "Testing!"
    return jsonify(dict(ok=True))

if __name__ == '__main__':
    app.run()

