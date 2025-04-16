from config import Config
import requests
from flask import jsonify

BASE_URL = f"https://io.adafruit.com/api/v2/{Config.ADA_IO_USERNAME}/feeds"

def send_data(data):
    headers = {"X-AIO-Key": Config.ADA_IO_KEY, "Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/{data['feed']}/data", headers=headers, json={"value": data['value']})
    return jsonify(response.json()), response.status_code

def get_data():
    # Placeholder: bạn có thể thêm lấy dữ liệu từ feed cụ thể
    return jsonify({'message': 'Get data placeholder'})
