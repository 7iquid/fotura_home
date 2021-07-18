from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from controllers.UserController import *
from flask_login import login_required, current_user
from models.Baracode_user_DB import Barcode_table
from models.Baracode_user_DB import User
from models.Baracode_user_DB import db
import jyserver.Flask as jsf



barcode_nav = Blueprint('barcode_nav', __name__)


@barcode_nav.route('/Barcode_sys/user_db_nav')
def user_DB_list():
    data = User.query.all()
    return render_template("Barcode_sys/Front_end/user_db_nav.html",data = data, user = current_user)  
   


@barcode_nav.route('/Barcode_sys/barcode_upload', methods=['GET',"POST"])
def upload_pic():
    if request.method == "POST":
        file = request.files['pic']
        filename = (file.filename)
        mimetype = (file.mimetype)
        img = Barcode_table(img_ko = file.read(), mimetype_db=mimetype, name_db=filename)
        db.session.add(img)
        db.session.commit()

        return render_template("Barcode_sys/Front_end/barcode_upload.html",user = current_user)
    else:
        return render_template("Barcode_sys/Front_end/barcode_upload.html", user = current_user)