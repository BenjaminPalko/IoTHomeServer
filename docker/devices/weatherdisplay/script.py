from paho.mqtt import client
from urllib import request
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
engine = create_engine(db_url)
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


'''
    Weather API
'''
opencage_key = os.environ['OPENCAGE_KEY']
opencage_api = 'https://api.opencagedata.com/geocode/v1/json?key=' + opencage_key

weather_key = os.environ['DARKSKY_KEY']
weather_api = 'https://api.darksky.net/forecast/' + weather_key + '/'


def retrieve_geocode(location):
    encode = location.replace(' ', '+')
    encode = encode.replace(',', '%2C')
    args = '&q=' + encode
    response = request.urlopen(opencage_api + args)
    data = response.read().decode('utf-8')
    json_object = json.loads(data)
    return json_object['results'][0]['bounds']['northeast']


def retrieve_weather(location):
    geocode = retrieve_geocode(location)
    args = str(geocode['lat']) + ',' + str(geocode['lng']) + '?units=si'
    response = request.urlopen(weather_api + args)
    data = response.read().decode('utf-8')
    json_object = json.loads(data)
    cut_json_object = json_object['currently']
    return cut_json_object


def update():
    try:
        query = text("select location from weather where id = :mac")
        result = connection.execute(query, mac=device_mac)
        weather_object = {
            "mac": device_mac,
            "data": retrieve_weather(result.fetchone()[0])
        }
        print('Publishing')
        client.publish(os.environ['MQTT_TOPIC'], json.dumps(weather_object))
        print('Success')
        result.close()
    except TypeError:
        pass


'''
    Execution Area
'''
while True:
    update()
    time.sleep(15)
