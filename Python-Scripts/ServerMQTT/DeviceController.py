import requests
import paho.mqtt.client as mqttclient
import json as json
import paho.mqtt.publish as mqttpublish
import paho.mqtt.subscribe as mqttsubscribe
import paho.mqtt.matcher as mqttmatcher


# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


client = mqttclient.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect("192.168.1.3", 1883, 60)
client.subscribe("#", 0)


# Handles device types
def device_handler(device, input, data):
    """

    :param device: device name
    :param input: boolean
    :param data: data to transfer
    :return:
    """
    if input is True:
        # Send to device method
        update_field(device, data)
    else:
        publish_device(device, data)


# Create new field
def create_field(field, type):
    """

    :param field:
    :param type:
    :return:
    """
    return field


# Publishes to device topic
def publish_device(topic, msg):
    pub = client.publish(topic, msg)
    if pub.rc != "MQTT_ERR_SUCCESS":
        return


def update_field(field, data):
    return True
