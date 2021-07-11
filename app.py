from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from datetime import timedelta
from flask_sqlalchemy import SQLAlchemy
import time
from router.route_ko import simple_page
# import os

app = Flask(__name__)
app.secret_key="hello"
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///barcodeDb.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.permanent_session_lifetime = timedelta(minutes=5)
# back end  location
db = SQLAlchemy(app)
app.register_blueprint(simple_page)


class FileContents(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	part_no = db.Column(db.String(100))
	by = db.Column(db.String(100))
	date_entry = db.Column(db.String(100))
	date_exit = db.Column(db.String(100))
	img_ko = db.Column(db.LargeBinary)


@app.route("/" ,methods = ["GET","POST"])
# @app.route("/index")
def index(barcode=None):
	if request.method == "POST":
		barcode = request.form.get("barcode")
		session["barcode"] = barcode
		print(barcode)
		return render_template("home.html", id_ko = barcode)
	else:
		return render_template("home.html",id_ko = barcode)


@app.route('/upload_pic' ,methods = ["GET","POST"])
def upload_pic():
    if request.method == "POST":
        file = request.files['pic']
        img = FileContents(img_ko = file.read())
        db.session.add(img)
        db.session.commit()

        return render_template("upload_ko.html")
    else:
        return render_template("upload_ko.html")

@app.route('/view_picture' ,methods = ["GET","POST"])
def view_picture():
		if request.method == "POST":
			img = Img.query.filter_by(id=id).first()
			if not img
				return "no image found with this id", 404     
        	return render_template("upload_ko.html", picture_ko = img)
        else:
        	return render_template("upload_ko.html")





if __name__ == '__main__':
	db.create_all()
	# app.run(debug=True, host="192.168.1.44",port = 5000, threaded=True)
	app.run(debug=True, host="localhost",port = 5000, threaded=True) 