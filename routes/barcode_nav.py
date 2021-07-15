from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from controllers.UserController import *
from flask_login import login_required, current_user
from models.User_DB import Barcode_table
from models.User_DB import User
from models.User_DB import db
import jyserver.Flask as jsf



barcode_nav = Blueprint('barcode_nav', __name__)


@barcode_nav.route('/ok')
def login():
    print(session["barcode"])
   


@user_bp.route('/add_code', methods=['GET',"POST"])
def upload_pic():
    if request.method == "POST":
        file = request.files['pic']
        filename = (file.filename)
        mimetype = (file.mimetype)
        img = Barcode_table(img_ko = file.read(), mimetype_db=mimetype, name_db=filename)
        db.session.add(img)
        db.session.commit()

        return render_template("upload_ko.html")
    else:
        return render_template("upload_ko.html")