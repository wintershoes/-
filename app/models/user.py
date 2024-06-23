from sqlalchemy import CheckConstraint
from app import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    points = db.Column(db.Integer, default=0)
    registration_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    role = db.Column(db.String(20), nullable=False)
    __table_args__ = (
        CheckConstraint("role IN ('student', 'teacher', 'admin')"),
    )

    reservations = db.relationship('Reservation', backref='users', lazy=True)
    reviews = db.relationship('Review', backref='users', lazy=True)
    scores = db.relationship('Score', backref='users', lazy=True)