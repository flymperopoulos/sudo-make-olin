import requests
import simplejson as json
from flask import Flask, render_template

app = Flask(__name__)
app.debug = True

faces = []

@app.route("/")
def main():
    return 'Hello world!'
    #return send_from_directory('','index.html')
    #return app.send_static_file('index.html')
<<<<<<< HEAD

    return render_template('index.html')
=======
    #return render_template('index.html')
>>>>>>> dca4c285ba8c46303e4457c5677bb11ada95f29e

@app.route("/test")#,methods=["POST"])
def test():
<<<<<<< HEAD
    return "Testing!"


@app.route("/facerecognition")
def facerecognition():
	faces = [
		"http://www.greenteam.mersd.org/wp-content/uploads/2013/11/amazon-logo.jpeg",
		"http://static.infowars.com/bindnfocom/2013/11/Bank-of-America-logo1.jpg",
		"http://siliconrepublic.com/fs/img/news/201209/rs-426x288/new-ebay-logo.jpg",
		"http://www.computec.co.jp/clients/images/logo_citi.jpg",
		"http://d1xcqlxj49e9dd.cloudfront.net/wp-content/uploads/chase_3_after1.jpg",
		"http://www.myrtlebeachgolf.com/media/images/fedex_logo.jpg"
	]
	return render_template("facerecognition.html", faces=faces)

if __name__ == "__main__":
    app.run()
=======
    faces.append( request.form['img'] )
    #return "Testing!"
>>>>>>> dca4c285ba8c46303e4457c5677bb11ada95f29e
