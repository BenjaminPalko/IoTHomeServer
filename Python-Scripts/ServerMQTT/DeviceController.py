import paho.mqtt.client as mqttclient
import json as json
import time
import sqlite3 as sqlite
device_db = sqlite.connect('devices.db')


# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))
    device_db.execute("CREATE TABLE IF NOT EXISTS devices (id Integer, type Text, topic Text)")


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload) + "\n")
    if msg.topic == "connection/request":
        print("Request Connection Received")
        c = device_db.cursor()
        json_object = json.loads(msg.payload)
        print("Type: " + json_object["type"])
        if json_object["type"] == "ledrgb":
            new_topic = "device/led/rgb/1"
            c.execute('INSERT INTO devices VALUES (?, ?, ?)', json_object["id"], json_object["type"], new_topic)
            new_json = {
                "id": json_object["id"],
                "ack": True,
                "topic": new_topic
            }
        new_msg = json.dumps(new_json)
        client.publish("connection/response", new_msg)


# Start client loop
def start_client_loop():
    client.connect("192.168.1.3", 1883, 60)
    client.subscribe("#", 0)
    client.loop_start()

    print('Script is running, Ctrl-C to quit...')
    while True:
        time.sleep(0.2)


client = mqttclient.Client()
client.on_connect = on_connect
client.on_message = on_message


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
