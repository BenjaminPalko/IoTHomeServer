from sqlalchemy import create_engine, text
from paho.mqtt import client
import time
import json
import os

device_mac = os.environ['MAC_ADDRESS']
broker = os.environ['MQTT_BROKER']
topic = os.environ['MQTT_TOPIC']
db_url = os.environ['POSTGRES_URL']
db_password = os.environ['POSTGRES_PASSWORD']

#   <<< SQLALCHEMY  >>>
engine = create_engine(db_url, echo=True)
connection = engine.connect()

#   <<< MQTT Client >>>
connect_results = {
    0: "Connection Successful",
    1: "Connection refused - incorrect protocol version",
    2: "Connection refused - invalid client identifier",
    3: "Connection refused - bad username or password",
    4: "Connection refused - not authorised"
}
client = client.Client()


def on_connect(client, userdata, flags, rc):
    """

    :param client: client subscribed to the topic being received on
    :param userdata: not currently used
    :param flags: not currently used
    :param rc: connection results
    :return:
    """
    print(connect_results[rc])


def query_pin():
    query = text("SELECT pin FROM doorlock WHERE id = :mac")
    result = connection.execute(query, mac=device_mac)
    return result.fetchone()[0]


def get_validation(pin1, pin2):
    if pin1 == pin2:
        validation = 1
    else:
        validation = 0
    new_object = {
        "mac": device_mac,
        "data": {
            "validation": validation
        }
    }
    return json.dumps(new_object)


def on_message(client, userdata, msg):
    """
    Handles
    :param client: client subscribed to the topic being received on
    :param userdata: not currently used
    :param msg: message received, uses .topic and .payload commands
    :return: N/A
    """
    print(msg.payload.decode())
    json_object = json.loads(msg.payload)
    if json_object["mac"] == device_mac and "passcode" in json_object['data']:
        result_pin = query_pin()
        json_string = get_validation(result_pin, json_object["data"]["passcode"])
        client.publish(topic, json_string)


client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic)
client.loop_start()

print('Loop started CTRL-C to quit...')
while True:
    time.sleep(2)
