import os
from paho.mqtt import client
import json
import d

broker = os.environ['AWS_BROKER']


def on_connect(client, userdata, rc):
    pass


def on_message(client, userdata, msg):
    if msg.topic == '/connect':
        json_object = json.loads(msg.payload.decode())

client = client.Client()
client.connect(broker)
client.subscribe('#')

