from sqlalchemy import CheckConstraint
from app import db




class Activity(db.Model):
    __tablename__ = "Activity"
    activity_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    start_time = db.Column(db.TIMESTAMP, nullable=False)
    end_time = db.Column(db.TIMESTAMP, nullable=False)
    location = db.Column(db.String(100), nullable=False)
    link = db.Column(db.String(255))


