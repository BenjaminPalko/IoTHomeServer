from flask import Flask, render_template, flash, request, url_for
from flask_socketio import SocketIO, send
from scripts.devices import RGBLED, Temperature

# Flask app constructor
app = Flask("__main__", template_folder="templates")
app.secret_key = 'iotSecretKey'
socketio = SocketIO(app)

# Device Setup
rgbled = RGBLED(42, "nodemcu/rgbled", 'rgbled')
temperature = "temperature" # Temperature(43, "nodemcu/temp", 'temp')

# Home Page
@app.route("/", methods=['GET', 'POST'])
def dev_LEDtest():
    error = 'Select led light to test'
    try:
        if request.method == 'POST':
            ledRequestSubmit = request.form['ledSwitch']

            if ledRequestSubmit == "red":
                rgbled.update_state(255, 0, 0)
                error = 'RED'
                return render_template("index.html", token="Red", error=error)
            if ledRequestSubmit == "green":
                rgbled.update_state(0, 255, 0)
                error = 'Green'
                return render_template("index.html", token="Green", error=error)
            if ledRequestSubmit == "blue":
                rgbled.update_state(0, 0, 255)
                error = 'Blue'
                return render_template("index.html", token="Blue", error=error)
            if ledRequestSubmit == "off":
                rgbled.update_state(0, 0, 0)
                error = 'Off'
                return render_template("index.html", token="Off", error=error)
            else:
                error = "Invalid"
        return render_template("index.html", token="Requires a Valid Input", error=error)
    except Exception as e:
        return render_template("index.html", token="Error", error=e)
# ================================================

# About Page
@app.route("/about")
def my_about():
    return render_template("index.html", token="Flask+React Connect Success: About")

# Devices Page
@app.route("/devices")
def my_devices():
    return render_template("index.html", token="Flask+React Connect Success: Devices")

# Temperature Testing
@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True) #broadcast sends to all other clients
    send(temperature)

def new_element(type, id):
    pass    # Fill out function


def check_if_element_exists(id):
    pass    # Fill out function


def update_temp(id, temperature):
    pass    # Fill out function


# Start App
# app.run(debug=True)
socketio.run(app)
