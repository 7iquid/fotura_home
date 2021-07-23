from flask import Flask, Blueprint, Response, request, jsonify,render_template, session, flash
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_login import login_required, current_user
from models.Baracode_user_DB import Barcode_table
from models.Baracode_user_DB import User
from models.Baracode_user_DB import db
import base64
import json
import time


api_ko = Blueprint('api_ko', __name__)

api= Api(api_ko)

class User_Db(Resource):
	def get(self):
		data_dic = {}
		user_list = []

		data = User.query.all()
		for i in data:
			data_dic =({
							"id":i.id,
							"name":i.first_name,
							"position" : i.position,
							"email" : i.email,
							"password": i.password
							})
			if i.user_id.Barcode_table:
				print(i.user_id.Barcode_table)
				# for j in i.user
				# data_dic=({ 
				# 		"barcode added:j"
				# 	})
			user_list.append(data_dic)
		return jsonify(user_list)
api.add_resource(User_Db, "/api")








# barcode_data = reqparse.RequestParser()
# barcode_data.add_argument("barcode_id", type=str,)
# barcode_data.add_argument("item_name", type=str,)
# barcode_data.add_argument("brand_name", type=str,)
# barcode_data.add_argument("part_no", type=str,)
# barcode_data.add_argument("serila_no", type=str,)
# barcode_data.add_argument("description", type=str,)
# barcode_data.add_argument("remarks", type=str,)
# barcode_data.add_argument("prod_pic", type=str,)

bar = {}
class Barcode_Db(Resource):
	def get(self,pri_key):
		barcode_id =request.get_json()
		return barcode_id

	def put(self,pri_key):
		args = request.get_json()	
		barcode = Barcode_table(barcode_id=args["barcode_id"],item_name=args["item_name"],brand_name=args["brand_name"],part_no=args["part_no"],serila_no=args["serila_no"],description=args["description"],remarks=args["remarks"],mimetype_db="1.png",user_id = current_user.id)
		# print(args["barcode_id"])
		db.session.add(barcode)
		db.session.commit()
		return args

# api.add_resource(Barcode_Db, "/api_barcode/<string:query_key>/<string:query_value>")
api.add_resource(Barcode_Db, "/api_barcode/<pri_key>")














class test1(Resource):
	def get(self):
		data_dic = {}
		user_list = []

		data = User.query.all()
		for i in data:
			data_dic =({
							"id":i.id,
							"name":i.first_name,
							"position" : i.position,
							"email" : i.email,
							"password": i.password
							})
			user_list.append(data_dic)
		return jsonify(user_list)

class test2(Resource):
	def get(self):
		time.sleep(3)
		data_dic = {}
		user_list = []

		data = User.query.all()
		for i in data:
			data_dic =({
							"id":i.id,
							"name":i.first_name,
							"position" : i.position,
							"email" : i.email,
							"password": i.password
							})
			user_list.append(data_dic)
		return jsonify(user_list)




api.add_resource(test1, "/mutithread_test1")
api.add_resource(test2, "/mutithread_test2")