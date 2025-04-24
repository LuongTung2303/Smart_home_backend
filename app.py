from flask import Flask
from flask_socketio import SocketIO
from routes.auth import auth_bp
from routes.feeds import feeds_bp
from services.mqtt_listener import start_mqtt
import threading
import eventlet
from eventlet import wsgi

app = Flask(__name__)
socketio = SocketIO(app)

#Tạo socket gửi dữ liệu tới client realtime
def handle_mqtt_message(feed_id, payload):
    socketio.emit('mqtt_message', {
        'feed': feed_id,
        'data': payload
    })

# Bắt đầu MQTT trong thread riêng
def start_background_mqtt():
    start_mqtt(socketio, handle_mqtt_message)
# Tạo một luồng riêng cho socket chạy vì không thể xử lý socket chạy chung với Flask
threading.Thread(target=start_background_mqtt).start()

app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(feeds_bp, url_prefix="/feeds")

if __name__ == '__main__':
    eventlet.wsgi.server(eventlet.listen(('0.0.0.0', 5000)), app)
