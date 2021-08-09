import os
from flask_sqlalchemy import SQLAlchemy

SECRET_KEY = os.urandom(32)

# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
SQLALCHEMY_DATABASE_URI = 'sqlite:///barcodeDb.sqlite3'
MONGO_URI = "mongodb+srv://7iquid:2222222@cluster0.jvx0i.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
MONGO_URI_GUMAGAMIT = "mongodb+srv://7iquid:2222222@cluster0.jvx0i.mongodb.net/Gumagamit?retryWrites=true&w=majority"
# MONGO_URI = "mongodb+srv://7iquid:2222222@cluster0.jvx0i.mongodb.net/sample_analytics?retryWrites=true&w=majority"						

# Turn off the Flask-SQLAlchemy event system and warning
SQLALCHEMY_TRACK_MODIFICATIONS = False