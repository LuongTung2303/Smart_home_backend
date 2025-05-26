from flask import Blueprint, request
from models.user import get_user_infor, update_user_infor, delete_user
from utils.decorators import token_required

profile_bp = Blueprint('profile', __name__)

@profile_bp.route('/update/<int:user_id>', methods=['PUT'])
@token_required
def update(user_id):
    data = request.get_json()
    return update_user_infor(user_id, data)

@profile_bp.route('/delete/<int:user_id>', methods=['DELETE'])
@token_required
def delete(user_id):
    return delete_user(user_id)

@profile_bp.route('/get/<int:user_id>', methods=['GET'])
@token_required
def get(user_id):
    return get_user_infor(user_id)
