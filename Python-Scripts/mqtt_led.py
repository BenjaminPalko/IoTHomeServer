import time
import RPi.GPIO as GPIO
import paho.mqtt.client as mqtt

def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    client.subscribe("/leds/pi")

def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))

    if msg.topic == "/leds/pi":
        if msg.payload == "TOGGLE":
            client.publish('/leds/esp8266', 'TOGGLE')

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect('localhost', 1883, 60)

client.loop_start()

print('Script is running, Ctrl-C to quit...')
while True:
    time.sleep(0.2)
    x = raw_input('You may input a command\n')
    if x == "TOGGLE":
        client.publish('/leds/esp8266', 'TOGGLE')
