from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
from sqlalchemy.orm import relationship, backref
import os
import json

RGB= '80:7D:3A:3C:54:5B'
TEMP= '80:7D:3A:3C:57:60'
WEATHER= '80:7D:3A:6E:96:78'
DOORLOCK= '80:7D:3A:6E:88:0D'
DOCKER_BROKER = '0.0.0.0'
security_pin = None
dateTime = datetime.now()


# Flask + Socket + MQTT Setup
app = Flask(__name__, template_folder="templates")
app.config.update(
    SECRET_KEY='iotSecret_key',
    SQLALCHEMY_DATABASE_URI=os.environ['POSTGRES_DB'],
    SQLALCHEMY_USERNAME=os.environ['POSTGRES_USER'],
    SQLALCHEMY_PASSWORD=os.environ['POSTGRES_PASSWORD']
    # MQTT_BROKER_URL=AWS_MOSQUITTO,
    # MQTT_BROKER_PORt=1883,
    # MQTT_KEEPALIVE=60
)
socketio = SocketIO(app)
# mqtt = Mqtt(app)
db = SQLAlchemy(app)
engine = create_engine(os.environ['POSTGRES_DB'], convert_unicode=True, echo=False)

Base = declarative_base()
Base.metadata.reflect(engine)


# These classes will allow you to query the database
# In Terminal you can query by following these steps:
# from main import db
# db.create_all()
# from main import -className-
# variable = className(parameters)
# db.session.add(variable)
# db.session.commit()
class TemperatureSensor(Base, db.Model):
    __tablename__ = Base.metadata.tables['temperature_sensor']
    id = db.Column('id', db.Integer, primary_key=True)
    value = db.Column('value', db.Float)
    timestamp = db.Column('timestamp', db.DateTime())

    def __repr__(self):
        return f"TemperatureSensor('{self.id}', '{self.value}', '{self.timestamp}')"


class RgbLED(Base, db.Model):
    __tablename__ = Base.metadata.tables['rgb_led']
    id = db.Column('id', db.Integer, primary_key=True)
    color = db.Column('color', db.Unicode)
    change = db.Column('change', db.Boolean)
    timestamp = db.Column('timestamp', db.DateTime())

    def __repr__(self):
        return f"RgbLED('{self.id}', '{self.color}', '{self.change}', '{self.timestamp}')"


class WeatherDisplay(Base, db.Model):
    __tablename__ = Base.metadata.tables['weather']
    id = db.Column('id', db.Integer, primary_key=True)
    location = db.Column('location', db.Unicode)
    change = db.Column('change', db.Boolean)
    timestamp = db.Column('timestamp', db.DateTime())

    def __repr__(self):
        return f"WeatherDisplay('{self.id}', '{self.location}', '{self.change}', '{self.timestamp}')"


class DoorLock(Base, db.Model):
    __tablename__ = Base.metadata.tables['doorlock']
    id = db.Column('id', db.Integer, primary_key=True)
    pin = db.Column('pin', db.Integer)
    timestamp = db.Column('timestamp', db.DateTime())

    def __repr__(self):
        return f"DoorLock('{self.id}', '{self.pin}', '{self.timestamp}')"


# MQTT Subscriptions (Temporary, try to remove at earliest possibility)
# mqtt.subscribe('nodemcu/temp')
# mqtt.subscribe('nodemcu/doorlock/pub')


# PIN Device variable (Temporary, try to remove at earliest possibility)
security_pin = 1232


@app.route('/', methods=['GET', 'POST'])
def default():

    if request.method =='POST':
        if "colorpicked" in request.form:
            f = request.form['ledSwitch']
            newRGB_led(f)
        if "pinSet" in request.form:
            f = request.form['pinCombo']
            newSet_pin(f)
        if "forecastSet" in request.form:
            f = request.form['forecast']
            newForecast(f)

    return render_template("index.html")


# RGBLED
# Receive rgb Hex value from client
@socketio.on('rgbled_hex')
def update_rgb_led(rgbled_hex):
    rgbled_hex = str(rgbled_hex).replace('#', '')

    rgbled = RgbLED(color=rgbled_hex, change=True)
    db.session.add(rgbled)
    db.session.commit()
    print("data: " + rgbled)


# Weather Display
# Receive location string from client
@socketio.on('weather_location')
def change_weather_display(weather_location):
    print("testing connection")
    json_string = scripts.api_handler.retrieve_weather(weather_location)
    parsed_string = scripts.api_handler.parse_weather_data(json_string)

    weatherlocation = WeatherDisplay(location=parsed_string, change=True)
    db.session.add(weatherlocation)
    db.session.commit()
    print("data: " + weatherlocation)


# Door Lock
# Set pin (Finish)
@socketio.on('door_pin')
def set_pet(door_pin):
    global security_pin
    security_pin = str(door_pin)

    doorlock = DoorLock.query.filter_by(id=DOORLOCK).first()
    doorlock.pin = security_pin
    db.session.commit()

    print(security_pin)


def newForecast(value):
    weather = WeatherDisplay.query.filter_by(id=WEATHER).first()
    weather.location = value
    db.session.commit()


def newRGB_led(value):
    rgbled = RgbLED.query.filter_by(id=RGB).first()
    rgbled.color = value
    db.session.commit()


def newSet_pin(value):
    global security_pin
    security_pin = str(value)

    doorlock = DoorLock.query.filter_by(id=DOORLOCK).first()
    doorlock.pin = security_pin
    db.session.commit()

# Temperature
# Send new temp received from MQTT to client
# Retrieving the data from Database
def update_temperature():
    myTemperature = TemperatureSensor.query.order_by(TemperatureSensor.id.desc()).first()
    socketio.emit('temperature', myTemperature.value)


# # <<<   Device Socket Methods  >>>
# # Temperature
# # Send new temp received from MQTT to client
# @mqtt.on_topic('nodemcu/temp')
# def update_temperature(client, userdata, message):
#     json_object = json.loads(message.payload.decode())
#     temp = json_object['temperature']
#     socketio.emit('temperature', str(round(temp, 1)))
#
#
# # RGBLED
# # Receive rgb Hex value from client
# @socketio.on('rgbled_hex')
# def update_rgb_led(rgbled_hex):
#     rgbled_hex = str(rgbled_hex).replace('#', '')
#     mqtt.publish('nodemcu/rgbled', rgbled_hex)
#
#
# # Weather Display
# # Receive location string from client
# @socketio.on('weather_location')
# def change_weather_display(weather_location):
#     json_string = scripts.api_handler.retrieve_weather(weather_location)
#     parsed_string = scripts.api_handler.parse_weather_data(json_string)
#     mqtt.publish('nodemcu/weather', parsed_string)
#
#
# # Door Lock
# # Set pin (Finish)
# @socketio.on('door_pin')
# def set_pet(door_pin):
#     global security_pin
#     security_pin = str(door_pin)
#     print(security_pin)
#
#
# # Check pin (Finish)
# @mqtt.on_topic('nodemcu/doorlock/pub')
# def check_pin(client, userdata, message):
#     print(message)
#     json_object = json.loads(message.payload.decode())
#     if security_pin == str(json_object["Passcode"]):
#         return_json = {"validation": 1}
#     else:
#         return_json = {"validation": 0}
#     print(return_json)
#     mqtt.publish('nodemcu/doorlock/sub', json.dumps(return_json))


if __name__ == "__main__":
    socketio.run(app, debug=True)
