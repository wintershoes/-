# user_controller.py
from flask import Blueprint, request, jsonify
from app.services.user_service import register_user

bp = Blueprint('user', __name__, url_prefix='/api/users')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result = register_user(data['username'], data['password'], data['email'], data['role'])
    return jsonify(result)
