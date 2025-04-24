from flask import Blueprint, request, jsonify
from utils.decorators import token_required
from services.adafruit_service import send_data

feeds_bp = Blueprint('feeds', __name__)

@feeds_bp.route('/led1', methods=['POST'])
@token_required
def send_led1():
    data = request.get_json()
    return send_data(data,"button2")

@feeds_bp.route('/led2', methods=['POST'])
@token_required
def send_led2():
    data = request.get_json()
    return send_data(data,"button3")

@feeds_bp.route('/led3', methods=['POST'])
@token_required
def send_led3():
    data = request.get_json()
    return send_data(data,"button4")

@feeds_bp.route('/led4', methods=['POST'])
@token_required
def send_led4():
    data = request.get_json()
    return send_data(data,"button5")

@feeds_bp.route('/air_cond', methods=['POST'])
@token_required
def send_air_cond():
    data = request.get_json()
    return send_data(data,"button1")



