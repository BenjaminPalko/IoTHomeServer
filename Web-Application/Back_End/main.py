from flask import Flask, render_template, flash, request, url_for
from flask_socketio import SocketIO, send
from scripts.devices import RGBLED, Temperature
from helper import update_temp, ledCheck, doorLockCheck, geoLocationCheck

# Flask app constructor
app = Flask("__main__", template_folder="templates")
app.secret_key = 'iotSecretKey'
socketio = SocketIO(app)

# Device Setup - Might not need this here anymore 
# since theyre assigned in helper.py
# need to test it out
# rgbled = RGBLED(42, "nodemcu/rgbled", 'rgbled')
temperature = Temperature(43, "nodemcu/temp", 'temp')

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
                ledCheck(ledRequestSubmit)
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

# # Devices Page
# @app.route("/devices")
# def my_devices():
#     return render_template("index.html", token="Flask+React Connect Success: Devices")

# Login Page
@app.route("/login/", methods=['GET', 'POST'])
def my_login():
    return render_template("index.html")

# Socket Connections Below

# Temperature Testing
@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    # send(msg, broadcast=True) #broadcast sends to all other clients
    update_temp(0, temperature)

# Start App
# app.run(debug=True) Socketio.run replaces this to allow real time comm.
socketio.run(app, debug=True)
