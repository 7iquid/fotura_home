from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from controllers.UserController import *
from flask_login import login_required, current_user
from models.User_DB import Barcode_table
from models.User_DB import User
from models.User_DB import db

user_bp = Blueprint('user_bp', __name__)

# user_bp.route('/', methods=['GET'])(index)
# user_bp.route('/create', methods=['POST'])(store)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)


user_bp.route('/login', methods=['GET', 'POST'])(login)
user_bp.route('/logout')(logout)
user_bp.route('/sign-up', methods=['GET', 'POST'])(sign_up)


@user_bp.route('/sign-up')
def call_s():
	return render_template("home.html", user=current_user)
