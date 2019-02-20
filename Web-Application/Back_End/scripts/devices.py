import paho.mqtt.client as mqtt
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import json
import time
import _thread as thread
import scripts.api_handler as api_handler

Base = declarative_base()


class Device(Base):
    __tablename__ = 'devices'

    server_ip = "3.84.42.130"
    server_port = 1883
    keep_alive = 60

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    type = Column(String)

    def __init__(self, id, topic, type):
        self.client = mqtt.Client()
        self.client.connect(self.server_ip, self.server_port, self.keep_alive)
        self.topic = topic

        def on_message(client, userdata, msg):
            print("Received on topic: " + msg.topic + "\nWith message: " + str(msg.payload, "utf-8"))
            pass

        def on_connect(client, userdata, flags, rc):

            print("Returned with return: " + rc)

        self.client.on_message = on_message
        self.client.on_connect = on_connect
        self.client.subscribe(self.topic)
        self.client.loop_start()

    def publish(self, msg):
        self.client.publish(self.topic, msg)


class RGBLED(Device):

    def update_state(self, red, green, blue):
        json_object = {"red": red, "green": green, "blue": blue}
        json_string = json.dumps(json_object)
        super().publish(json_string)


class Temperature(Device):

    temperature = None

    def __init__(self, id, topic, type):
        def on_message(client, userdata, msg):
            json_object = json.loads(str(msg.payload, 'utf-8'))
            self.temperature = json_object['temperature']
        super().__init__(id, topic, type)
        self.client.on_message = on_message


class LCDDisplay(Device):

    loop = True

    def start_loop(self, location, delay):
        def update_loop(location, delay):
            while self.loop:
                data = api_handler.retrieve_weather(location)
                self.publish(data)
                time.sleep(delay)
        thread.start_new_thread(update_loop, (location, delay))
