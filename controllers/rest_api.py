from flask import Flask, Blueprint, Response, request, jsonify,render_template, session, flash
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models.Baracode_user_DB import Barcode_table
from models.Baracode_user_DB import User
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
			user_list.append(data_dic)
		return jsonify(user_list)
api.add_resource(User_Db, "/api")








barcode_data = reqparse.RequestParser()
barcode_data.add_argument("name", type=str,)
# barcode_data.add_argument("views", type=int, help="Views of the video", required=True)
# barcode_data.add_argument("likes", type=int, help="Likes on the video", required=True)

bar = {}
class Barcode_Db(Resource):
	def get(self,pri_key):
		return {"name":pri_key}


	def put(self,pri_key):
		print("put is working")
		print(pri_key)
		tinapay =request.headers
		# args = barcode_data.parse_args()
		# return bar[args],201
		return tinapay
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