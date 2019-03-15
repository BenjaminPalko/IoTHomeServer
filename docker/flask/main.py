from flask import Flask, render_template, request
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime
import os


RGB= '80:7D:3A:3C:54:5B'
TEMP= '80:7D:3A:3C:57:60'
WEATHER= '80:7D:3A:6E:96:78'
DOORLOCK= '80:7D:3A:6E:88:0D'
DOCKER_BROKER = '0.0.0.0'
security_pin = None


# Flask + Socket + Thread Setup
app = Flask(__name__, template_folder="templates")
app.config.update(
    SECRET_KEY='iotSecret_key',
    SQLALCHEMY_DATABASE_URI=os.environ['POSTGRES_DB'],
    SQLALCHEMY_USERNAME=os.environ['POSTGRES_USER'],
    SQLALCHEMY_PASSWORD=os.environ['POSTGRES_PASSWORD']
)
socketio = SocketIO(app)
db = SQLAlchemy(app)
engine = create_engine(os.environ['POSTGRES_DB'], convert_unicode=True, echo=False)

Base = declarative_base()
Base.metadata.reflect(engine)

DEFAULT_COLOR = '#FFFFFF'
DEFAULT_PIN = 1111
DEFAULT_TEMPERATURE = 0.00
DEFAULT_LOCATION = 'Ottawa, Ontario'


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


@app.route('/')
def default():
    return render_template("index.html")


# Weather Display
# Receive location string from client
@socketio.on('weather_location')
def newForecast(value):

    if WeatherDisplay.query.filter_by(id=WEATHER).first() is not None:
        print("Sent Location")
        weather = WeatherDisplay.query.filter_by(id=WEATHER).first()
        weather.location = value
        weather.timestamp = datetime.now()
        weather.change = True
        db.session.commit()
    else:
        weather = WeatherDisplay()
        weather.id = WEATHER
        weather.location = value
        weather.change = True
        weather.timestamp = datetime.now()
        db.session.add(weather)
        db.session.commit()


# RGBLED
# Receive rgb Hex value from client
@socketio.on('rgbled_hex')
def newRGB_led(value):

    if RgbLED.query.filter_by(id=RGB).first() is not None:
        print("Sent LED")
        rgbled = RgbLED.query.filter_by(id=RGB).first()
        rgbled.color = value
        rgbled.timestamp = datetime.now()
        rgbled.change = True
        db.session.commit()
    else:
        rgbled = RgbLED()
        rgbled.id = RGB
        rgbled.color = value
        rgbled.change = True
        rgbled.timestamp = datetime.now()
        db.session.add(rgbled)
        db.session.commit()


# Doorlock
# Set doorlock for device
@socketio.on('door_pin')
def newSet_pin(value):

    if DoorLock.query.filter_by(id=DOORLOCK).first() is not None:
        print("Sent Pin")
        doorlock = DoorLock.query.filter_by(id=DOORLOCK).first()
        doorlock.pin = value
        doorlock.timestamp = datetime.now()
        db.session.commit()
    else:
        doorlock = DoorLock()
        doorlock.id = DOORLOCK
        doorlock.pin = value
        doorlock.timestamp = datetime.now()
        db.session.add(doorlock)
        db.session.commit()


# Temperature
# Send new temp received from MQTT to client
# Retrieving the data from Database
@socketio.on('temperatureLoop')
def temperatureLoop(value):

    if TemperatureSensor.query.filter_by(id=TEMP).first() is not None:
        #print("Checking Temperature")
        myTemperature = TemperatureSensor.query.order_by(TemperatureSensor.timestamp.desc()).first()
        #myTemperature = TemperatureSensor.query.filter_by(id=TEMP).first()
        socketio.emit('temperature', myTemperature.value)
    else:
        myTemperature = TemperatureSensor()
        myTemperature.id = TEMP
        myTemperature.value = DEFAULT_TEMPERATURE
        myTemperature.timestamp = datetime.now()
        db.session.add(myTemperature)
        db.session.commit()


if __name__ == "__main__":
    socketio.run(app, debug=True)

