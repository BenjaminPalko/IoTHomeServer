from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
import json
import scripts.api_handler

AWS_MOSQUITTO = '3.84.42.130'
AZURE_MOSQUITTO = '40.86.204.73'
security_pin = None


# Flask + Socket + MQTT Setup
app = Flask(__name__, template_folder="templates")
app.config.update(
    SECRET_KEY='iotSecret_key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/postgres',
    SQLALCHEMY_USERNAME='postgres',
    SQLALCHEMY_PASSWORD='root',
    MQTT_BROKER_URL='3.84.42.130',
    MQTT_BROKER_PORt=1883,
    MQTT_KEEPALIVE=60
)
socketio = SocketIO(app)
mqtt = Mqtt(app)


# MQTT Subscriptions (Temporary, try to remove at earliest possibility)
mqtt.subscribe('nodemcu/temp')
mqtt.subscribe('nodemcu/doorlock/pub')


# PIN Device variable (Temporary, try to remove at earliest possibility)
security_pin = 1232


@app.route('/')
def default():
    return render_template("index.html")


# <<<   Device Socket Methods  >>>
# Temperature
# Send new temp received from MQTT to client
@mqtt.on_topic('nodemcu/temp')
def update_temperature(client, userdata, message):
    json_object = json.loads(message.payload.decode())
    temp = json_object['temperature']
    socketio.emit('temperature', str(round(temp, 1)))


# RGBLED
# Receive rgb Hex value from client
@socketio.on('rgbled_hex')
def update_rgb_led(rgbled_hex):
    rgbled_hex = str(rgbled_hex).replace('#', '')
    mqtt.publish('nodemcu/rgbled', rgbled_hex)


# Weather Display
# Receive location string from client
@socketio.on('weather_location')
def change_weather_display(weather_location):
    json_string = scripts.api_handler.retrieve_weather(weather_location)
    parsed_string = scripts.api_handler.parse_weather_data(json_string)
    mqtt.publish('nodemcu/weather', parsed_string)


# Door Lock
# Set pin (Finish)
@socketio.on('door_pin')
def set_pet(door_pin):
    global security_pin
    security_pin = str(door_pin)
    print(security_pin)


# Check pin (Finish)
@mqtt.on_topic('nodemcu/doorlock/pub')
def check_pin(client, userdata, message):
    print(message)
    json_object = json.loads(message.payload.decode())
    if security_pin == str(json_object["Passcode"]):
        return_json = {"validation": 1}
    else:
        return_json = {"validation": 0}
    print(return_json)
    mqtt.publish('nodemcu/doorlock/sub', json.dumps(return_json))


if __name__ == "__main__":
    socketio.run(app, debug=True)
