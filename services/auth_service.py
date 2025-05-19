import jwt
import datetime
from flask import jsonify
from config import Config
from database.db import get_connection


def create_token(user_id):
    payload = {
        'user_id': user_id,
        'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }
    token = jwt.encode(payload, Config.SECRET_KEY, algorithm='HS256')
    return token

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
        return jsonify({'token': token, 'data' : user, 'message' : 'Success'}), 200
    else: 
        return jsonify({'message': 'Invalid password'}), 401

def register_user(data):
    username = data.get('username');
    password = data.get('password');
    conn = get_connection();
    cursor = conn.cursor(dictionary=True)
    query = "INSERT INTO user (username, password) VALUES (%s, %s)";
    try:
        cursor.execute(query, (username, password));
        conn.commit();
        new_id = cursor.lastrowid;
        token = create_token(new_id);
        res_data = {'username' : username};
        return jsonify({'token' : token, 'message' : 'Insert success', 'data' : res_data}), 201
    except Exception as e:
        conn.rollback()
        return jsonify({'error' : str(e)}), 500

