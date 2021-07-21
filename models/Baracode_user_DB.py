from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func
from flask_login import UserMixin

db = SQLAlchemy()

class User_activity(db.Model):
    __tablename__ = 'User_activity'  

    id = db.Column(db.Integer, primary_key=True)
    user_action = db.Column(db.String(150), unique=True)
    user_time_log =db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'user_action': self.user_action,
            'user_time_log': self.user_time_log,
            'user_id': self.user_id
            }



class User(db.Model, UserMixin):
    __tablename__ = 'User'   

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    first_name = db.Column(db.String(150))
    position =db.Column(db.String(150))
    User_activity_parent = db.relationship('User_activity')
    User_barcode_parent = db.relationship('Barcode_table')

    @property
    def serialize(self):
        return {
            'id': self.id,
            'email': self.email,
            'first_name': self.first_name,
            'position': self.position,
            'password': self.password,
            'User_activity_parent': self.User_activity_parent,
            'User_barcode_parent': self.User_barcode_parent
            }

class Barcode_table(db.Model):
    __tablename__ = 'Barcode_table' 

    id = db.Column(db.Integer, primary_key=True)
    barcode_id = db.Column(db.String(100))
    item_name = db.Column(db.String(100))
    brand_name = db.Column(db.String(100))
    part_no = db.Column(db.String(100))
    serila_no = db.Column(db.String(100))
    description = db.Column(db.String(100))
    remarks = db.Column(db.String(400))
    prod_pic = db.Column(db.LargeBinary)
    mimetype_db = db.Column(db.Text, nullable=False)
    date_added = db.Column(db.DateTime(timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'))

    @property
    def serialize(self):
        return {
            'id': self.id,
            'barcode_id': self.barcode_id, 
            'item_name': self.item_name,
            'brand_name': self.brand_name,
            'part_no': self.part_no,
            'serila_no': self.serila_no,
            'description': self.description,
            'remarks': self.remarks,
            'prod_pic': self.prod_pic,
            'mimetype_db': self.mimetype_db,
            'date_added': self.date_added,
            'user_id': self.user_id

            }

