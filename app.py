from flask import Flask
from flask_socketio import SocketIO
from flask_cors import CORS
from routes.auth import auth_bp
from routes.feeds import feeds_bp
from routes.profile import profile_bp
from services.mqtt_listener import start_mqtt
import threading

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app, cors_allowed_origins="*")  # Cho phép React kết nối

# Gửi dữ liệu MQTT qua socket
def handle_mqtt_message(feed_id, payload):
    socketio.emit('mqtt_message', {
        'feed': feed_id,
        'data': payload
    })

# Chạy MQTT ở thread riêng
def start_background_mqtt():
    print("Starting MQTT client in background...")
    start_mqtt(socketio, handle_mqtt_message)

# Start MQTT thread
threading.Thread(target=start_background_mqtt).start()

# Đăng ký blueprint
app.register_blueprint(auth_bp, url_prefix="/auth")
app.register_blueprint(feeds_bp, url_prefix="/feeds")
app.register_blueprint(profile_bp, url_prefix="/profile")

if __name__ == '__main__':
    socketio.run(app, host='0.0.0.0', port=5000)  # ✅ dùng socketio.run thay vì eventlet.wsgi
