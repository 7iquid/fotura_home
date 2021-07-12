from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.sql import func

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'    

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120))
    age = db.Column(db.String(120))
    address = db.Column(db.String(120))    

    @property
    def serialize(self):
        return {
            'id': self.id,
            'name': self.name,
            'city': self.city,
            'state': self.state,
            'address': self.address
            }

class Barcode_table(db.Model):
    __tablename__ = 'Barcode_table' 

    id = db.Column(db.Integer, primary_key=True)
    part_no = db.Column(db.String(100))
    by = db.Column(db.String(100))
    name_db = db.Column(db.String(100))
    date_entry = db.Column(db.DateTime(timezone=True), default=func.now())
    date_exit = db.Column(db.DateTime(timezone=True), default=func.now())
    img_ko = db.Column(db.LargeBinary)
    mimetype_db = db.Column(db.Text, nullable=False)

    @property
    def serialize(self):
        return {
            'id': self.id,
            'part_no': self.part_no,
            'by': self.by,
            'name_db': self.name_db,
            'date_entry': self.date_entry,
            'date_exit': self.date_exit,
            'img_ko': self.img_ko,
            'mimetype_db': self.mimetype_db
            }