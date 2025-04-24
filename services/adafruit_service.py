import requests
from flask import jsonify
from config import Config

AIO_USERNAME = Config.AIO_USERNAME
AIO_KEY = Config.AIO_KEY

BASE_URL = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds"

def send_data(data,feed_name):
    headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/{feed_name}/data", headers=headers, json={"value": data['value']})
    print(response.status_code)
    print(response.text)
    return jsonify(response.json()), response.status_code

