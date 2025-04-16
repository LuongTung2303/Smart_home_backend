from flask import Blueprint, request, jsonify
from utils.decorators import token_required
from services.adafruit_service import send_data, get_data

feeds_bp = Blueprint('feeds', __name__)

@feeds_bp.route('/send', methods=['POST'])
@token_required
def send():
    data = request.get_json()
    return send_data(data)

@feeds_bp.route('/get', methods=['GET'])
@token_required
def get():
    return get_data()
