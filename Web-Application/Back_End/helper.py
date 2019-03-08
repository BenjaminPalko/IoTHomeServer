from flask_socketio import SocketIO, send


# LED Device Method
# ledCheck: Change the color of the LED based on input
# @input
# ledRequestSubmit: takes in light input from browser
# @output
# error: for development checking purposes
def ledCheck(ledRequestSubmit):
    output = None
    if ledRequestSubmit == "red":
        rgbled.update_state(255, 0, 0)
        output = 'RED'
    elif ledRequestSubmit == "green":
        rgbled.update_state(0, 255, 0)
        output = 'Green'
    elif ledRequestSubmit == "blue":
        rgbled.update_state(0, 0, 255)
        output = 'Blue'
    elif ledRequestSubmit == "off":
        rgbled.update_state(0, 0, 0)
        output = 'Off'
    else:
        output = "Invalid"
    print('===========================')
    print('The LED is set to: ' + output)
    print('===========================\n')
    return output


def ledHexCheck(ledRequestSubmit):
    print('===========================')
    print('The LED is set to: ' + ledRequestSubmit)
    print('===========================\n')


# Temperature Device Methods
# update_temp: Checks if the browser needs to update and display the new temperature. Temperature reading, update if changed.
# @input
# id: device unique id
# newTemperature: device temperature input to be checked
# @output
# no outputs, only socket call to send data to browser.
temp_temperature = temperature.temperature # Called once to initialize temp
def update_temp(id, newTemperature):
    global temp_temperature
    if temp_temperature != newTemperature.temperature:
        temp_temperature = newTemperature.temperature
        print('===========================')
        print('New Temperature reading: ', temp_temperature)
        print('===========================\n')
        send(temp_temperature)
        # return temp_temperature
    else:
        print('===========================')
        print('Temperature is still the same')
        print('===========================\n')
        # return temp_temperature


# Doorlock Device Method
def doorLockCheck(doorComboRequestSubmit):
    if doorComboRequestSubmit == '1231':
        print('===========================')
        print('User Submitted Pin Combo: ' + doorComboRequestSubmit)
        print('CORRECT - do something')
        print('===========================\n')
    else:
        print('===========================')
        print('User Submitted Pin Combo: ' + doorComboRequestSubmit)
        print('**Door Combo Incorrect**')
        print('===========================\n')
        #Possibly put a counter for how many tries till it locks out
    pass # return something for device


# Weather Forecase Device Method
def geoLocationCheck(geoLocationRequestSubmit):
    print('===========================')
    print('City Name Submitted: ' + geoLocationRequestSubmit)
    print('**Checking Weather Forecast**')
    print('===========================\n')
    pass # return something for device