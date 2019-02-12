import paho.mqtt.client as mqttclient
import docker
import json as json
import time


# RBGLED Control
def rgbled_control(red, green, blue):
    json_object = {"Red": red, "Green": green, "Blue": blue}
    msg = json.dumps(json_object)
    client.publish("nodemcu/rgbled", msg)
    return json_object


# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload, "utf-8"))
    if msg.topic == "nodemcu/rgbled":
        command = msg.payload.decode()
        print(command)
        if command == "red":
            rgbled_control(255, 0, 0)
        elif command == "green":
            rgbled_control(0, 255, 0)
        elif command == "blue":
            rgbled_control(0, 0, 255)
        elif command == "off":
            rgbled_control(0, 0, 0)
        else:
            print("Invalid command on rgbled topic")
    elif msg.topic == "nodemcu/temp":
        json_object = json.loads(msg.payload.decode())
        print("The temperature is " + str(json_object["temperature"]))
    elif msg.topic == "nodemcu/doorlock/sub":
        json_object = json.loads(msg.payload.decode())


# Start client loop
def start_client_loop():
    client.connect("3.84.42.130", 1883, 60)
    client.subscribe("#", 0)
    client.loop_start()

    print('Script is running, Ctrl-C to quit...')
    while True:
        time.sleep(0.2)


client = mqttclient.Client()
client.on_connect = on_connect
client.on_message = on_message
start_client_loop()
