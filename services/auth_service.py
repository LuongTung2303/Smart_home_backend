import jwt
import datetime
from flask import jsonify
from config import Config
from models.user import find_user_by_username
from werkzeug.security import generate_password_hash, check_password_hash

def login_user(data):
    user = find_user_by_username(data['username'])
    if user and check_password_hash(user['password'], data['password']):
        token = jwt.encode({
            'user_id': user['id'],
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)
        }, Config.SECRET_KEY, algorithm='HS256')
        return jsonify({'token': token})
    return jsonify({'message': 'Invalid credentials'}), 401

def register_user(data):
    # Placeholder: Bạn sẽ thêm truy vấn insert thủ công sau
    return jsonify({'message': 'Register endpoint placeholder'})
