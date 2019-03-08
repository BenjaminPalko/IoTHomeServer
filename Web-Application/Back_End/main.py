from flask import Flask, render_template, flash, request, url_for
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from flask_sqlalchemy import SQLAlchemy
# from helper import update_temp, ledCheck, doorLockCheck, geoLocationCheck, ledHexCheck
from werkzeug.security import generate_password_hash, \
    check_password_hash
import json
import scripts.api_handler

AWS_MOSQUITTO = '3.84.42.130'
AZURE_MOSQUITTO = '40.86.204.73'
security_pin = None

# Flask app constructor
app = Flask(__name__, template_folder="templates")
app.config.update(
    SECRET_KEY='iotSecret_key',
    SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://iotadmin:JerryBetaLocal13'
                            '@iot-database.postgres.database.azure.com/iot-server',
    MQTT_BROKER_URL='3.84.42.130',
    MQTT_BROKER_PORt=1883,
    MQTT_KEEPALIVE=60
)
socketio = SocketIO(app)
mqtt = Mqtt(app)
db = SQLAlchemy(app)


# <<<   Database Model Definitions  >>>
class User(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(128), nullable=False)
    pw_hash = db.Column(db.String(256), nullable=False)

    is_authenticated = False
    is_active = False
    is_anonymous = False

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)

    def check_password(self, password):
        is_authenticated = check_password_hash(self.pw_hash, password)

    @staticmethod
    def get_id():
        return id

    def __repr__(self):
        return '<User %r>' % self.username


# Create Test Users
admin = User(username='admin', password='Hello!')
db.session.add(admin)

# MQTT Subscriptions (Temporary, try to remove at earliest possibility)
mqtt.subscribe('nodemcu/temp')
mqtt.subscribe('nodemcu/doorlock/pub')

# PIN Device variable (Temporary, try to remove at earliest possibility)
security_pin = 1232


# Home Page
@app.route("/")
def my_home():
    return render_template("index.html")

'''
@app.route("/devices", methods=['GET', 'POST'])
@app.route("/", methods=['GET', 'POST'])
def dev_DevicesTest():
    #LED Testing
    output = 'Select led light to test'
    try:
        if request.method == 'POST':
            if 'ledSwitch' in request.form:
                ledRequestSubmit = request.form['ledSwitch']
                # ledCheck(ledRequestSubmit)
                ledHexCheck(ledRequestSubmit)
            elif 'pinCombo' in request.form:
                pinComboSubmit = request.form['pinCombo']
                doorLockCheck(pinComboSubmit)
            elif 'cityName' in request.form:
                cityNameSubmit = request.form['cityName']
                geoLocationCheck(cityNameSubmit)
        return render_template("index.html", token="Requires a Valid Input", error=output)
    except Exception as e:
        return render_template("index.html", token="Error", error=e)
'''


# About Page
@app.route("/about")
def my_about():
    return render_template("index.html", token="Flask+React Connect Success: About")


# Login Page
@app.route("/login/", methods=['GET', 'POST'])
def my_login():
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


# <<<   User/Security   >>>
# Create User (Finish)
@socketio.on('new_user')
def user_creation(new_user):
    #user = User(new_user['username'], new_user['password'])
    pass


# Validate User (Finish)
@socketio.on('validate_user')
def user_validation(validate_user):
    user = validate_user['username']
    # Get user from database
    #User.check_password(validate_user['password'])
    pass


# Start App
# app.run(debug=True) Socketio.run replaces this to allow real time comm.
if __name__ == "__main__":
    socketio.run(app, debug=True)
