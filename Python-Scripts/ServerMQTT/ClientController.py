# Benjamin Palko 100964652
import time
import paho.mqtt.client as mqtt

idleclients = {}
activeclients = {}

# Passed to client as default 'on_connect' function
def on_connect(client, userdata, flags, rc):
    print("Connected with result code: " + str(rc))


# Passed to client as default 'on_message' function
def on_message(client, userdata, msg):
    if msg.topics in topics:
        print(msg.topic + " " + str(msg.payload))

def create_client(name, topics, address='192.168.1.215'):
    """ Create client given
    INPUTS:
    name    -- Client name
    address -- Address of MQTT Broker
    topics  -- String of topics to be subscribed to
    
    Return 0 on success
    """
    client = mqtt.Client()
    client.on_connect = on_connect
    client.on_message = on_message
    
    for topic in topics:
        client.subscribe(topic)

    try:
        client.connect(address, 1883, 60)
        idleclients[name] = client
        return 0
    except:
        return -1

def get_client(name):
    """ Retrieve client by name
    INPUT:
    name    -- Client name
    """
    try:
        if name in idleclients:
            return idleclients[name]
        else:
            return activeclients[name]
    except:
        return -1



# Start up selected client
def start_client(name):
    """ Start client loop
    INPUT:
    name    -- Client name
    """
    try:
        client = idleclients[name]
        client.loop_start()
        del idleclients[name]
        activeclients[name] = client
        return True
    except:
        return False # Client is either already running or doesn't exist

def stop_client(name):
    """ Stop client loop
    INPUT:
    name    -- Client name
    """
    try:
        client = activeclients[name]
        client.loop_stop()
        del activeclients[name]
        idleclients[name] = client
        return True
    except:
        return False # Client is either already stopped or doesn't exist

def subscribe_client(name, topic):
    """ Subscribe Client to topic
    INPUT:
    name    -- Client name
    topic   -- Topic to subscribe to
    """
    client = get_client(name)
    if client != -1:
        client.subscribe(topic)
        return True
    return False

def publish_client(name, topic, msg):
    """ Publish to topic through given client

    """
    client = get_client(name)
    if client != -1:
        client.publish(topic, msg)
        return True
    return False


def get_clients():
    """ Return 2D array of clients
    """
    return [idleclients, activeclients]