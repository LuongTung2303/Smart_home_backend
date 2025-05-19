from Adafruit_IO import MQTTClient
from dotenv import load_dotenv
from database.db import get_connection
import os
import sys

load_dotenv()
AIO_USERNAME = os.getenv('AIO_USERNAME')
AIO_KEY = os.getenv('AIO_KEY')
FEEDS = ['button1', 'button2', 'button3', 'button4', 'button5', 'sensor1', 'sensor2', 'sensor3', 'sensor4', 'lock']

# Callback sẽ được định nghĩa từ file app.py
on_message_callback = None
socketio = None
subscribe_mid_map = {}
def connected(client):
    print("Ket noi Adafruit thanh cong")
    for feed in FEEDS:
        client.subscribe(feed)

def subscribe(client, userdata, mid, granted_qos):
    print("Subscribed thanh cong vao feed")

def disconnected(client):
    print("Mat ket noi MQTT")
    sys.exit(1)

def message(client, feed_id, payload):
    match feed_id:
        case 'button1': name = 'air_condition'
        case 'button2': name = 'led1'
        case 'button3': name = 'led2'
        case 'button4': name = 'led3'
        case 'button5': name = 'led4'
        case 'sensor1': name = 'temp'
        case 'sensor2': name = 'humd'
        case 'sensor3': name = 'slot'
        case 'sensor4': name = 'rfid'
        case 'lock': name = 'door'
    print(f"Nhan gia tri tu {name}: {payload}")
    if on_message_callback:
        on_message_callback(feed_id, payload)

# Tạo một hàm để khởi động MQTT
def start_mqtt(socketio_instance, message_callback):
    global on_message_callback, socketio

    on_message_callback = message_callback
    socketio = socketio_instance

    client = MQTTClient(AIO_USERNAME, AIO_KEY)
    client.on_connect = connected
    client.on_disconnect = disconnected
    client.on_message = message
    client.on_subscribe = subscribe

    client.connect()
    client.loop_background()
