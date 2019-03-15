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


def on_message(client, userdata, msg):
    logger.debug('Message received - ' + msg.payload)
    json_object = json.loads(msg.payload.decode())
    if json_object["mac"] == device_mac:
        logger.debug('MAC recognized')
        try:
            temp_string = float(json_object['data']['temperature'])
            query = text("INSERT INTO temperature_sensor VALUES (:id, :temperature, CURRENT_TIMESTAMP)")
            connection.execute(query, id=str(device_mac), temperature=float(temp_string))
            logger.info('Temperature {' + temp_string)
        except TypeError:
            logger.error('SQL error on insert')


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
        pass
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
