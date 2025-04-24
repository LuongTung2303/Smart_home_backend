import requests
from flask import jsonify
from dotenv import load_dotenv
from config import Config
import os

load_dotenv()
AIO_USERNAME = Config.AIO_USERNAME
AIO_KEY = os.getenv('AIO_KEY')

BASE_URL = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds"

def send_data(data,feed_name):
    headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/{feed_name}/data", headers=headers, json={"value": data['value']})
    print(response.status_code)
    print(response.text)
    return response.json(), response.status_code

data = {
    "value": 0,
    "message": "You're very nice!"
}
feed_name = "button2";
res = send_data(data,feed_name);