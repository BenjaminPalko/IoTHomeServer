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


def on_connect(client, userdata, flags, rc):
    print(connect_results[rc])


def on_message(client, userdata, msg):
    json_object = json.loads(msg.payload.decode())
    if json_object["mac"] == device_mac:
        print(msg.payload.decode())
        query = text("INSERT INTO temperature_sensor VALUES (:id, :temperature, CURRENT_TIMESTAMP)")
        result = connection.execute(query, id=str(device_mac), temperature=float(json_object['data']['temperature']))
        result.close()


client = client.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(broker, 1883)
client.subscribe(topic)
client.loop_start()

print('Loop started CTRL-C to quit...')
while True:
    time.sleep(2)
