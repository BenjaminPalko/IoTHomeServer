import paho.mqtt.client as mqttclient
import time


# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    print(msg.payload)


def start_loop(topic):
    client.connect("3.84.42.130", 1883, 60)
    client.subscribe(topic)
    client.loop()

    print('Script is running, Ctrl-C to quit...')
    while True:
        time.sleep(0.2)


client = mqttclient.Client()
client.on_connect = on_connect
client.on_message = on_message
start_loop("nodemcu/temp")
