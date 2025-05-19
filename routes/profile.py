from flask import Blueprint, request
from models.user import get_user_infor, update_user_infor, delete_user
from utils.decorators import token_required

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/update', methods=['PUT'])
@token_required
def update():
    data = request.get_json()
    return update_user_infor(data)

@profile_bp.route('/delete', methods=['DELETE'])
@token_required
def delete():
    data = request.get_json()
    return delete_user(data)

@profile_bp.route('/get', methods=['GET'])
@token_required
def get():
    data = request.get_json()
    return get_user_infor(data)
