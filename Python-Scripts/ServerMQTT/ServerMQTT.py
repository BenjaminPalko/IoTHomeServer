# Benjamin Palko 100964652
import time
import paho.mqtt.client as mqtt

topics = []


# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    if msg.topics in topics:
        print(msg.topic + " " + str(msg.payload))


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect('192.168.1.215', 1883, 60)

client.loop_start()

print('Script is running, Ctrl-C to quit...')
while True:
    time.sleep(0.2)
