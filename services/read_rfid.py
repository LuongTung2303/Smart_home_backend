import requests
import random
import time

AIO_USERNAME = "lena5415"
AIO_KEY = "aio_RnGn51Rgxgf0IaTnCCDXRPmYKYxQ"

BASE_URL = f"https://io.adafruit.com/api/v2/{AIO_USERNAME}/feeds"

def send_data(data,feed_name):
    headers = {"X-AIO-Key": AIO_KEY, "Content-Type": "application/json"}
    response = requests.post(f"{BASE_URL}/{feed_name}/data", headers=headers, json={"value": data['value']})
    print(response.status_code)
    print(response.text)
    return response.json(), response.status_code

while True:
    value = random.randint(0,1);
    data = {
        "value": value,
        "message": "Hello my friend"
    }
    send_data(data, "button2")
    time.sleep(2)