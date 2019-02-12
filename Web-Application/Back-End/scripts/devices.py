import paho.mqtt.client as mqtt
import json

hello = "hello"


def on_message(client, userdata, msg):
    print("Received on topic: " + msg.topic + "\nWith message: " + str(msg.payload, "utf-8"))


def on_connect(client, userdata, flags, rc):
    print("Returned with return: " + rc)


class Device:
    def __init__(self, topic):
        self.client = mqtt.Client()
        self.topic = topic
        self.client.subscribe(topic)
        self.client.on_message = on_message
        self.client.on_connect = on_connect
        self.client.loop_start()

    def publish(self, msg):
        self.client.publish(self.topic, msg)


class RGBLED(Device):
    def __init__(self, topic):
        super().__init__(topic)

    def update_state(self, red, green, blue):
        json_object = {"red": red, "green": green, "blue": blue}
        json_string = json.dumps(json_object)
        super().publish(json_string)


class Temperature(Device):
    def __init__(self, topic):
        super().__init__(topic)
