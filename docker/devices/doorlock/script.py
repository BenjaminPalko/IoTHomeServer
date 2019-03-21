from paho.mqtt import client
from sqlalchemy import create_engine, text
from datetime import datetime
import logging
import time
import json
import sys
import os

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
loop_delay = 3


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


def query_pin():
    query = text("SELECT pin FROM doorlock WHERE id = :mac")
    result = connection.execute(query, mac=device_mac)
    return result.fetchone()[0]


def validate_pin(pin1, pin2):
    if pin1 == pin2:
        logger.debug('Pin is valid')
        validation = 1
    else:
        logger.debug('Pin is invalid')
        validation = 0
    new_object = {
        "mac": device_mac,
        "data": {
            "validation": validation
        }
    }
    return json.dumps(new_object)


def on_message(client, userdata, msg):
    logger.debug('Message received on topic - ' + msg.topic)
    json_object = json.loads(msg.payload)
    if json_object["mac"] == device_mac and "passcode" in json_object['data']:
        logger.debug('Correct mac - Querying database')
        # result_pin = query_pin()
        try:
            query = text("SELECT pin FROM doorlock WHERE id = :mac")
            result = connection.execute(query, mac=device_mac)
            result_pin = result.fetchone()[0]
        except TypeError:
            logger.error('Query error on pin retrieval from database')

        logger.info('Pin queried as ' + result_pin)
        json_string = validate_pin(result_pin, json_object["data"]["passcode"])
        logger.debug('Sending message - ' + json_string)
        logger.info('Passcode good - Publishing reply')
        client.publish(topic, json_string)


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
    time.sleep(loop_delay)


if __name__ == '__main__':
    #   Broker connection
    client = client.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    while client.connect(broker, 1883):
        logger.warning('Broker failed to connect, attempting to reconnect in 4 seconds...')
        time.sleep(4)
    client.subscribe(topic)
    client.loop_start()
    #   Start main program
    main()

