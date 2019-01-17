import paho.mqtt.client as mqtt
import time


def on_message(client, userdata, msg):
    print(msg.topic)


def on_connect(client, userdata, flags, rc):
    print("Connection return: " + str(rc))


def blue_on():
    client.publish("nodemcu/rgbled", "{\"Red\":0,\"Green\":0,\"Blue\":255}")


def green_on():
    client.publish("nodemcu/rgbled", "{\"Red\":0,\"Green\":255,\"Blue\":0}")


def red_on():
    client.publish("nodemcu/rgbled", "{\"Red\":255,\"Green\":0,\"Blue\":0}")


def led_off():
    client.publish("nodemcu/rgbled", "{\"Red\":0,\"Green\":0,\"Blue\":0}")


client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.3", 1883, 60)

delay = 0.5
while True:
    blue_on()
    print("Blue")
    time.sleep(delay)
    print("Green")
    green_on()
    time.sleep(delay)
    print("Red")
    red_on()
    time.sleep(delay)
    print("Off")
    led_off()
    time.sleep(delay)
