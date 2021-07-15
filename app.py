from flask import Flask, Blueprint, Response, request, jsonify,render_template, session
from flask_migrate import Migrate
from models.Baracode_user_DB import db
from templates.Barcode_sys.back_end import barcode_nav

from routes.user_bp import user_bp
from models.Baracode_user_DB import User
from flask_login import LoginManager, current_user
from templates.Barcode_sys.back_end.barcode_nav import *


app = Flask(__name__)
app.config.from_object('config')

login_manager = LoginManager()
login_manager.login_view = 'user_bp.login'
login_manager.init_app(app)

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))



db.init_app(app)
migrate = Migrate(app, db)



# app.register_blueprint(user_bp, url_prefix='/users')
app.register_blueprint(user_bp)
app.register_blueprint(barcode_nav)



@app.route('/')
def index(user=None):
	return render_template('index.html',user=current_user)
	
if __name__ == '__main__':
	app.debug = True
	app.run()