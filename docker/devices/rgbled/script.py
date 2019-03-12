from paho.mqtt import client
from sqlalchemy import create_engine, text
import json
import time
import os

#   Device Id
device_mac = os.environ['MAC_ADDRESS']
broker = os.environ['MQTT_BROKER']
topic = os.environ['MQTT_TOPIC']
db_url = os.environ['POSTGRES_URL']
db_password = os.environ['POSTGRES_PASSWORD']


'''
    POSTGRES Database
'''
engine = create_engine(db_url, echo=True)
connection = engine.connect()


'''
    MQTT Client
'''
connect_results = {
    0: "Connection Successful",
    1: "Connection refused - incorrect protocol version",
    2: "Connection refused - invalid client identifier",
    3: "Connection refused - bad username or password",
    4: "Connection refused - not authorised"
}
client = client.Client()


def on_connect(client, userdata, flags, rc):
    print(connect_results[rc])


client.connect(broker, 1883)
client.subscribe(topic)
client.loop_start()


def check_update():
    try:
        query = text("select * from rgb_led where id = :mac")
        result = connection.execute(query, mac=device_mac).fetchone()
        if result is not None and result[3]:
            query2 = text("update rgb_led set change = FALSE where id = :mac")
            connection.execute(query2, mac=device_mac)
            json_object = {"mac": device_mac, "data": {"color": result[1]}}
            client.publish(topic, json.dumps(json_object))
            print('Message sent')
    except TypeError:
        pass


while True:
    check_update()
    time.sleep(5)
