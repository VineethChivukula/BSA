from flask import Blueprint, request, jsonify
from app.services.user_service import UserService

user_bp = Blueprint('user_bp', __name__)


@user_bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    try:
        UserService.register(data)
        return jsonify({'message': 'User registered successfully'}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@user_bp.route('/login', methods=['POST'])
def login():
    data = request.get_json()
    try:
        user = UserService.login(data)
        return jsonify(user), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
