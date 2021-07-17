from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from models.Baracode_user_DB import Barcode_table
from models.Baracode_user_DB import User
import json


api_ko = Blueprint('api_ko', __name__)

api= Api(api_ko)

class Video(Resource):
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
		return(user_list)

api.add_resource(Video, "/api")