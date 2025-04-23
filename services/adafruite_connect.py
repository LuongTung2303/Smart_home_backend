import sys
from Adafruit_IO import MQTTClient
import random
import time


AIO_USERNAME = "tungnluong04"
AIO_KEY = "aio_OytL29CGRe4aS5l62rZPLGTrMEkZ"
AIO_FEED_ID = "bbc_led"  # Example feed name

def connected(client):
    print("Ket noi thanh cong ...")
    client.subscribe(AIO_FEED_ID)

def subscribe(client , userdata , mid , granted_qos):
    print("Subscribe thanh cong ...")

def disconnected(client):
    print("Ngat ket noi ...")
    sys.exit (1)

def message(client , feed_id , payload):
    print("Nhan du lieu từ feed {AIO_FEED_ID}: " + payload)


client = MQTTClient(AIO_USERNAME , AIO_KEY)
client.on_connect = connected
client.on_disconnect = disconnected
client.on_message = message
client.on_subscribe = subscribe
client.connect()
client.loop_background()

while True:
    value = random.randint (0 , 2)
    print("Cap nhat :", value )
    client.publish (AIO_FEED_ID, value )
    time.sleep (5)