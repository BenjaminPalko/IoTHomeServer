from flask import Flask, render_template, flash, request, url_for
from scripts.devices import RGBLED

# Flask app constructor
app = Flask("__main__", template_folder="templates")
app.secret_key = 'iotSecretKey'

# Devices
rgbled = RGBLED(42, "nodemcu/rgbled", 'rgbled')


@app.route("/", methods=['GET', 'POST'])
def dev_test():
    error = 'error testing'
    try:
        if request.method == 'POST':
            submit_attempt = request.form['passwordName']
            # submit_color_red = request.form['red-led']
            # submit_color_blue = request.form['blue-led']
            # submit_color_green = request.form['green-led']
            # submit_color_off = request.form['off-led']
            # request.
            # if submit_color_blue
            if submit_attempt == "red":
                rgbled.update_state(255, 0, 0)
                return render_template("index.html", token="Flask+React Connect Success: Home", error="GOOD")
            if submit_attempt == "green":
                rgbled.update_state(0, 255, 0)
                return render_template("index.html", token="Flask+React Connect Success: Home", error="GOOD")
            if submit_attempt == "blue":
                rgbled.update_state(0, 0, 255)
                return render_template("index.html", token="Flask+React Connect Success: Home", error="GOOD")
            
            else:
                error = "Invalid"
        return render_template("index.html", token="Flask+React Connect Success: Home", error=error)
    except Exception as e:
        return render_template("index.html", token="Flask+React Connect Success: Home", error=e)
# ================================================


@app.route("/about")
def my_about():
    return render_template("index.html", token="Flask+React Connect Success: About")


@app.route("/devices")
def my_devices():
    return render_template("index.html", token="Flask+React Connect Success: Devices")


def new_element(type, id):
    pass    # Fill out function

def check_if_element_exists(id):
    pass    # Fill out function


def update_temp(id, temperature):
    pass    # Fill out function


# Start App
app.run(debug=True)
