import paho.mqtt.client as mqttclient
import json as json
import time
import sqlite3 as sqlite
from sqlite3 import Error


def create_database_connection():
    try:
        conn = sqlite.connect('devices.db')
        return conn
    except Error as e:
        print(e)
        return None


# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    device_db = create_database_connection()
    c = device_db.cursor()
    c.execute("CREATE TABLE IF NOT EXISTS devices (id Integer, type Text, topic Text)")
    print("Connected with result code: " + str(rc))
    device_db.close()


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    # print(msg.topic + " " + str(msg.payload) + "\n")
    if msg.topic == "connection/request":
        print("Request Connection Received")
        json_object = json.loads(msg.payload)
        print("Type: " + json_object["type"])
        if json_object["type"] == "LED":
            # new_topic = "device/rgbled/1"
            # new_topic = "test/led"
            new_topic = create_device(json_object["id"], json_object["type"])
            new_json = {
                "id": json_object["id"],
                "ack": True,
                "topic": new_topic
            }
        new_msg = json.dumps(new_json)
        print("Sending response: " + new_msg)
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


def create_device(deviceid, type):
    device_db = create_database_connection()
    c = device_db.cursor()
    c.execute('SELECT topic FROM devices WHERE id = ?', (deviceid,))
    topic = c.fetchone()
    if topic is not None:
        return topic
    c.execute("SELECT COUNT(*) FROM devices WHERE type = ?", (type,))

    # Create new topic based on number of other devices that share the type
    rowcount = c.fetchone()[0]
    print("Rowcount: " + str(rowcount))
    if rowcount == -1:
        new_device_num = 1
    else:
        new_device_num = rowcount + 1
    new_topic = "devices/" + str(type) + "/" + str(new_device_num)
    c.execute('INSERT INTO devices (id, type, topic) VALUES (?, ?, ?)', (int(deviceid), str(type), str(new_topic)))
    print(new_topic)
    device_db.close()
    return new_topic


# Publishes to device topic
def publish_device(deviceid, msg):
    device_db = create_database_connection()
    c = device_db.cursor()
    topic = c.execute("SELECT topic FROM devices WHERE id = ?", deviceid).fetchone()
    device_db.close()
    client.publish(topic, msg)
