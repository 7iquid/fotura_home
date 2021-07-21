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



class Barcode_Db(Resource):
	def get(self,query_key = None,query_value = None):
		if query_value:
			data = Barcode_table.query.filter_by(barcode_id=query_value).first()
			if data:
				if data.prod_pic:
					prod_pic =base64.b64encode(data.prod_pic)
					data.prod_pic = prod_pic.decode("UTF-8")
				data_dic =({
					'id': data.id,
		            'barcode_id': data.barcode_id, 
		            'item_name': data.item_name,
		            'brand_name' : data.brand_name,
		            'part_no': data.part_no,
		            'serila_no': data.serila_no,
		            'description': data.description,
		            'remarks': data.remarks,
		            'prod_pic': data.prod_pic,
		            'mimetype_db': data.mimetype_db,
		            'date_added': data.date_added,
		            'user_id': data.user_id
							})
				return jsonify(data_dic)
			flash('Item not exist', category='error')	
			return jsonify({"error":"query not found"})
		else:
			Barcode_table.query.all()
			for i in data:
				if i.prod_pic:
					prod_pic =base64.b64encode(i.prod_pic)
					prod_pic = prod_pic.decode("UTF-8")
				data_dic =({
							'id': i.id,
				            'barcode_id': i.barcode_id, 
				            'item_name': i.item_name,
				            'brand_name' : i.data.brand_name,
				            'part_no': i.part_no,
				            'serila_no': i.serila_no,
				            'description': i.description,
				            'remarks': i.remarks,
				            'prod_pic': i.prod_pic,
				            'mimetype_db': i.mimetype_db,
				            'date_added': i.date_added,
				            'user_id': i.user_id
								})
				user_list.append(data_dic)
			return jsonify(user_list)

api.add_resource(Barcode_Db, "/api_barcode/<string:query_key>/<string:query_value>")



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