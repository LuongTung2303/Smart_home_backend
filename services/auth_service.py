import jwt
import datetime
from flask import jsonify
from config import SECRET_KEY
from database.db import get_connection


def login_user(data):
    username = data.get('username');
    password = data.get('password');
    conn = get_connection();
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM user WHERE username = %s"
    cursor.execute(query, (username))
    user = cursor.fetchone()
    if user is None:
        return jsonify({'message': 'Username not found'}), 404
    elif user['password'] == password:
        token = create_token(user['id']);
        return jsonify({'token': token}), 200
    else: 
        return jsonify({'message': 'Invalid password'}), 401

def register_user(data):
    username = data.get('username');
    password = data.get('password');
    conn = get_connection();
    cursor = conn.cursor(dictionary=True)
    query = "SELECT * FROM user WHERE username = %s"
    cursor.execute(query, (username))
    user = cursor.fetchone()
    if user is None:
        return jsonify({'message': 'Username not found'}), 404
    elif user['password'] == password:
        token = create_token(user['id']);
        return jsonify({'token': token}), 200
    else: 
        return jsonify({'message': 'Invalid password'}), 401
    return jsonify({'message': 'Register endpoint placeholder'})

def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    return token