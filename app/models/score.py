from sqlalchemy import CheckConstraint
from app import db

class Score(db.Model):
    __tablename__ = "Score"
    score_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    points = db.Column(db.Integer, nullable=False)
    change_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    description = db.Column(db.String(255))