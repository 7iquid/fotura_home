from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
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

class Barcode_Db(Resource):
	def get(self):
		data_dic = {}
		user_list = []

		data = Barcode_table.query.all()

		for i in data:
			img_ko =base64.b64encode(i.img_o)
			img_ko = img_ko.decode("UTF-8")
			data_dic =({
							"id":i.id,
							"part_no":i.part_no,
							"by" : i.by,
							"date_entry" : i.date_entry,
							"img_ko": img_ko,
							"mimetype_db": i.mimetype_db
							})
			user_list.append(data_dic)
		return jsonify(user_list)

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


api.add_resource(User_Db, "/api")
api.add_resource(Barcode_Db, "/api_barcode")
api.add_resource(test1, "/mutithread_test1")
api.add_resource(test2, "/mutithread_test2")