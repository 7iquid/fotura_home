from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from controllers.UserController import index, store, show, update, destroy
from models.User import Barcode_table
from models.User import db

user_bp = Blueprint('user_bp', __name__)

user_bp.route('/', methods=['GET'])(index)
user_bp.route('/create', methods=['POST'])(store)
user_bp.route('/<int:user_id>', methods=['GET'])(show)
user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)


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