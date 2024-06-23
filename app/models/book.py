from sqlalchemy import CheckConstraint
from app import db


class Book(db.Model):
    __tablename__ = 'Book'
    book_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    book_image = db.Column(db.LargeBinary)
    author = db.Column(db.String(100), nullable=False)
    publisher = db.Column(db.String(100), nullable=False)
    publish_date = db.Column(db.Date, nullable=False)
    isbn = db.Column(db.String(20), nullable=False)
    location = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)
    reservation_count = db.Column(db.Integer, default=0)
    borrower_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    __table_args__ = (
        CheckConstraint("status IN ('available', 'reserved', 'borrowed', 'damaged')"),
    )

    reservations = db.relationship('Reservation', backref='Book', lazy=True)
    reviews = db.relationship('Review', backref='Book', lazy=True)

