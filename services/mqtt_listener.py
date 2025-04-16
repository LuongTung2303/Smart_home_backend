import paho.mqtt.client as mqtt
from config import Config

def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    # Subscribe to topic khi kết nối thành công
    client.subscribe(Config.MQTT_TOPIC)

def on_message(client, userdata, msg):
    print(f"Received message '{msg.payload.decode()}' on topic '{msg.topic}'")

def start_mqtt_listener():
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message

    client.connect(Config.MQTT_BROKER, Config.MQTT_PORT, 60)
    client.loop_forever()  # Để lắng nghe liên tục
