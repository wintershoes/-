# user_service.py
from app import db
from app.models.model import User
from sqlalchemy.exc import IntegrityError

def register_user(username, password, email, role):
    try:
        new_user = User(username=username, password=password, email=email, role=role)
        db.session.add(new_user)
        db.session.commit()
        return {'message': 'User registered successfully', 'userId': new_user.user_id}
    except IntegrityError:
        db.session.rollback()
        return {'error': 'Username already exists'}
