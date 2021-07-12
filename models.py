from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func


class Note(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    notes = db.relationship('Note')

class Img(db.Model)
    id = db.Column(db.Integer, primary_key=True)
    img = db.Column(db.Text, unique=True, nullable=False)
    name = db.Column(db.Text, nullable=False)
    mimetype = db.Column(db.Text, nullable=False)

class FileContents(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    part_no = db.Column(db.String(100))
    by = db.Column(db.String(100))
    date_entry = db.Column(db.String(100))
    date_exit = db.Column(db.String(100))
    img_ko = db.Column(db.LargeBinary)
    mimetype_db = db.Column(db.Text, nullable=False)
