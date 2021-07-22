from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from controllers.UserController import *
from flask_login import login_required, current_user
from models.Baracode_user_DB import Barcode_table
from models.Baracode_user_DB import User
from models.Baracode_user_DB import db
import jyserver.Flask as jsf

user_bp = Blueprint('user_bp', __name__)

# user_bp.route('/', methods=['GET'])(index)
# user_bp.route('/create', methods=['POST'])(store)
# user_bp.route('/<int:user_id>', methods=['GET'])(show)
# user_bp.route('/<int:user_id>/edit', methods=['POST'])(update)
# user_bp.route('/<int:user_id>', methods=['DELETE'])(destroy)


user_bp.route('/login', methods=['GET', 'POST'])(login)
user_bp.route('/logout')(logout)
user_bp.route('/sign-up', methods=['GET', 'POST'])(sign_up)
user_bp.route('/add_barcode', methods=['GET', 'POST'])(upload_data)
user_bp.route('/test1', methods=['GET', 'POST'])(test_ko)

# @user_bp.route('/sign-up', methods=['GET', 'POST'])
# def call_s():
# 	return render_template("index.html", user=current_user)

@user_bp.route('/test', methods=['GET', 'POST'])
def test_web():    
	return render_template("Barcode_sys/Front_end/test.html",user=current_user)


@jsf.use(user_bp)
class App:
	def __init__(self):
		self.count = 0
	def increment(self):
		my_list_data = my_list_data
		self.js.document.getElementById('count').innerHTML = self.my_list_data["email"]

