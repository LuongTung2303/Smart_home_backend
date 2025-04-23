import paho.mqtt.client as mqtt
import json
import time

ACCESS_TOKEN = "es12alt4fa25ryy4yej4"
BROKER = "app.coreiot.io"  # hoặc server của bạn
PORT = 1883

client = mqtt.Client()
client.username_pw_set(ACCESS_TOKEN)

# Callback khi nhận tin nhắn từ broker
def on_message(client, userdata, msg):
    print(f"Received message from topic {msg.topic}: {msg.payload.decode()}")

client.on_message = on_message

client.connect(BROKER, PORT, 60)

# Đăng ký lắng nghe topic phản hồi RPC
client.subscribe("v1/devices/me/rpc/request/+")

client.loop_start()

# Giả lập RFID check-in / check-out
def send_rfid_event(room):
    payload = {
        "method": "CHECK_IN_OUT",
        "params": {
            "REQUEST": "CHECK_IN",
            "ROOM": room
        }
    }
    client.publish("v1/devices/me/telemetry", json.dumps(payload), qos=1)
    print("Sent:", payload)

# === GIẢ LẬP THẺ QUÉT ===
time.sleep(1)
send_rfid_event(1)

time.sleep(5)
send_rfid_event(2)

time.sleep(2)

# Dừng vòng lặp MQTT và ngắt kết nối khi xong
client.loop_stop()
client.disconnect()
