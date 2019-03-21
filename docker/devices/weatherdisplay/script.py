from urllib import request
from sqlalchemy import create_engine, text
from paho.mqtt import client
from datetime import datetime
import logging
import time
import json
import os
import sys

#   Logging
logger = logging.getLogger()


'''
    Environment
'''
device_mac = os.environ['MAC_ADDRESS']
broker = os.environ['MQTT_BROKER']
topic = os.environ['MQTT_TOPIC']
db_url = os.environ['POSTGRES_URL']
db_logging = bool(os.environ['POSTGRES_LOGGING'])
loop_delay = 5


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


def on_connect(client, userdata, flags, rc):
    logger.info(connect_results[rc])


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


'''
    Execution Area
'''


def query_location():
    try:
        logger.debug('Querying database')
        query = text("select location, change from weather where id = :mac")
        result = connection.execute(query, mac=device_mac).fetchone()
        logger.debug('Location: ' + result[0] + ' Flag: ' + str(result[1]))
        if result[1]:
            logger.debug('Retrieving updated location')
            try:
                update_flag = text("update weather set change = FALSE where id = :mac")
                weather_object = {
                    "mac": device_mac,
                    "data": retrieve_weather(result[0])
                }
                connection.execute(update_flag, mac=device_mac)
                client.publish(topic, json.dumps(weather_object))
            except TypeError:
                logger.error('SQL error on flag update')
        logger.info('Sending location: ' + result[0])
    except TypeError:
        logger.error('SQL error on change/location select')


def main():
    #   Logging setup
    logging_level = logging.INFO
    logger.setLevel(logging_level)
    formatter = logging.Formatter('%(levelname)s %(asctime)s %(message)s')

    stream_handler = logging.StreamHandler(sys.stdout)
    stream_handler.setLevel(logging_level)
    stream_handler.setFormatter(formatter)

    file_handler = logging.FileHandler('./logs/{:%Y-%m-%d}.log'.format(datetime.now()))
    file_handler.setLevel(logging_level)
    file_handler.setFormatter(formatter)

    logger.addHandler(stream_handler)
    logger.addHandler(file_handler)

    logger.info('Program Started...')
    #   Start execution loop
    while True:
        query_location()
        time.sleep(loop_delay)


if __name__ == '__main__':
    #   Broker connection
    client = client.Client()
    client.on_connect = on_connect
    while client.connect(broker, 1883):
        logger.warning('Broker failed to connect, attempting to reconnect in 4 seconds...')
        time.sleep(4)
    client.subscribe(topic)
    client.loop_start()
    #   Start main program
    main()
