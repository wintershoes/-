# user_controller.py
from flask import Blueprint, request, jsonify
from app.services.user_service import *
from flask_jwt_extended import jwt_required, get_jwt_identity

bp = Blueprint('user', __name__, url_prefix='/api/users')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    result,status = register_user(data['username'], data['password'], data['email'], data['role'])
    return jsonify(result),status

@bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    result,status = login_user(data['username'], data['password'])
    return jsonify(result),status

@bp.route('/<int:user_id>', methods=['GET'])
@jwt_required()
def get_user(user_id):
    print(user_id)
    current_user_id = get_jwt_identity()
    # 确保用户只能访问自己的信息，除非他们有更高权限（例如管理员）
    if current_user_id != user_id:
        return jsonify({'error': 'Access denied'}), 400

    user_info = get_user_by_id(user_id)
    if not user_info:
        return jsonify({'error': 'User not found'}), 404
    return jsonify(user_info), 200

@bp.route('/<int:user_id>', methods=['PUT'])
@jwt_required()
def update_user(user_id):
    current_user_id = get_jwt_identity()
    if current_user_id != user_id:
        return jsonify({'error': 'Access denied'}), 400

    data = request.get_json()
    result, status = update_user_info(user_id, data.get('email'))
    return jsonify(result), status
