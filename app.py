from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from flask_migrate import Migrate
from models.Baracode_user_DB import db
from models.Baracode_user_DB import db_mongo

#blueprint
from templates.Barcode_sys.back_end import barcode_nav
from routes.user_bp import user_bp
from controllers.rest_api import api_ko

from models.Baracode_user_DB import User
from flask_login import LoginManager, current_user
from templates.Barcode_sys.back_end.barcode_nav import *



app = Flask(__name__)
app.config.from_object('config')


#flask login manager ====>
login_manager = LoginManager()
login_manager.login_view = 'user_bp.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))
#=====<


#data base model=====>
db.init_app(app)
db_mongo.init_app(app)
migrate = Migrate(app, db)
#====<

#route blue print====>
app.register_blueprint(user_bp)
app.register_blueprint(barcode_nav)
app.register_blueprint(api_ko)
#====<



#home
@app.route('/')
def index(user=None):
	return render_template('index.html',user=current_user)
	
if __name__ == '__main__':
	# app.debug = True
	# app.run(host="192.168.43.227",debug=True)
	app.run(host="127.0.0.1",debug=True)