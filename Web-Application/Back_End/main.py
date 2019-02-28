from flask import Flask, render_template, flash, request, url_for
from flask_socketio import SocketIO
from flask_mqtt import Mqtt
from scripts.devices import RGBLED, Temperature
from helper import update_temp, ledCheck, doorLockCheck, geoLocationCheck, ledHexCheck
import json


# Flask app constructor
app = Flask(__name__, template_folder="templates")
app.config.update(
    SECRET_KEY='iotSecret_key',
    MQTT_BROKER_URL='3.84.42.130',
    MQTT_BROKER_PORt=1883,
    MQTT_KEEPALIVE=60
)
socketio = SocketIO(app)
mqtt = Mqtt(app)
mqtt.subscribe('nodemcu/temp')

# Home Page
@app.route("/")
def my_home():
    return render_template("index.html")

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

# About Page
@app.route("/about")
def my_about():
    return render_template("index.html", token="Flask+React Connect Success: About")

# Login Page
@app.route("/login/", methods=['GET', 'POST'])
def my_login():
    return render_template("index.html")

# Socket Connections Below

# New Temperature Connection
@mqtt.on_topic('nodemcu/temp')
def update_temperature(client, userdata, message):
    temp = json.loads(message.payload.decode())['temperature']
    socketio.emit('Temperature', str(round(temp, 1)))

# Start App
# app.run(debug=True) Socketio.run replaces this to allow real time comm.
if __name__ == "__main__":
    socketio.run(app, debug=True)
