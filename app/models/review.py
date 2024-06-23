from sqlalchemy import CheckConstraint
from app import db






class Review(db.Model):
    __tablename__ = "Review"
    review_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'))
    book_id = db.Column(db.Integer, db.ForeignKey('Book.book_id'))
    content = db.Column(db.Text, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    review_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp())
    __table_args__ = (
        CheckConstraint("rating BETWEEN 1 AND 5"),
    )