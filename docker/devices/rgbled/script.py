from paho.mqtt import client
from sqlalchemy import create_engine, text
from datetime import datetime
import logging
import json
import time
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


def check_value():
    try:
        logger.debug('Checking for new value')
        device_query = text("select * from rgb_led where id = :mac")
        result = connection.execute(device_query, mac=device_mac).fetchone()
        if result is not None and result[3]:
            try:
                logger.debug('Query Data for RGB hex value')
                hex_query = text("update rgb_led set change = FALSE where id = :mac")
                connection.execute(hex_query, mac=device_mac)
                json_string = json.dumps({"mac": device_mac, "data": {"color": result[1]}})
                logger.info('Sending value: ' + result[1])
                client.publish(topic, json.dumps(json_string))
            except TypeError:
                logger.error('SQL query error on value retrieval')
    except TypeError:
        logger.error('SQL query error on check for new value')


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
        check_value()
        time.sleep(2)

    client.loop_stop()
    logger.debug('Program exiting...')
    time.sleep(3)


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
