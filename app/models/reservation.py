from sqlalchemy import CheckConstraint
from app import db

class Reservation(db.Model):
    __tablename__ = 'Reservation'
    reservation_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('Book.book_id'))
    reservation_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    status = db.Column(db.String(50), nullable=False)
    book_location = db.Column(db.String(50), nullable=False)
    reservation_location = db.Column(db.String(50), nullable=False)
    __table_args__ = (
        CheckConstraint("status IN ('confirmed', 'cancelled', 'completed', 'failed')"),
    )