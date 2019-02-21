from scripts.devices import RGBLED, Temperature
from flask_socketio import SocketIO, send

# Device Setup
rgbled = RGBLED(42, "nodemcu/rgbled", 'rgbled')
temperature = Temperature(43, "nodemcu/temp", 'temp')

# ledCheck: Change the color of the LED based on input
# @input
# ledRequestSubmit: takes in light input from browser
# @output
# error: for development checking purposes
def ledCheck(ledRequestSubmit):
    if ledRequestSubmit == "red":
        rgbled.update_state(255, 0, 0)
        error = 'RED'
    elif ledRequestSubmit == "green":
        rgbled.update_state(0, 255, 0)
        error = 'Green'
    elif ledRequestSubmit == "blue":
        rgbled.update_state(0, 0, 255)
        error = 'Blue'
    elif ledRequestSubmit == "off":
        rgbled.update_state(0, 0, 0)
        error = 'Off'
    else:
        error = "Invalid"
    return error


def new_element(type, id):
    pass    # Fill out function


def check_if_element_exists(id):
    if not temperature.id:
        print('temperature id does not exist')
    else:
        print('temperature id exists')

# Temperature reading, update if changed.
temp_temperature = temperature.temperature # Called once to initialize temp
def update_temp(id, newTemperature):
    global temp_temperature
    if temp_temperature != newTemperature.temperature:
        temp_temperature = newTemperature.temperature
        print('New Temperature reading: ', temp_temperature)
        send(temp_temperature)
        # return temp_temperature
    else:
        print('Temperature is still the same')
        # return temp_temperature