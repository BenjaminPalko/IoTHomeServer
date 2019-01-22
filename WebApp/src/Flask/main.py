from flask import Flask, request, render_template
from rgbledcontroller import *

app = Flask(__name__)

@app.route("/index")
def redon():
    # red_on()
    return render_template("index.html")

# @app.route("/red_on", methods=['POST'])
# def redon():
#     red_on()
#     return render_template("index.html")

@app.route('/<led_setting>')
def testing(led_setting):
    if led_setting == "red":
        red_on()
    if led_setting == "blue":
        blue_on()
    if led_setting == "green":
        green_on()
    if led_setting == "off":
        led_off()
    return render_template("index.html", setting=led_setting)

if __name__== "__main__":
    app.run(debug=True)

# @app.route("/profile/<name>")
# def profile(name):
#     return render_template("profile.html", name=name)

# @app.route("/") # for null input
# @app.route("/<user>")
# def index(user="nothing"):
#     return render_template("user.html", user=user)

# @app.route("/objects") 
# def objectPassing():
#     objects = ["object1", "object2", "object3"]
#     return render_template("objectList.html", objects = objects)

# # @This is a decorator - wrap a function and modify its behavior
# @app.route("/prototype") #Mapped a URL to return vaule ex/prototype
# def prototype():
#     return 'This is to test Flask'

# # Passing username into parameter
# @app.route("/profile/<username>")
# def profile(username):
#     return "Hey there %s" % username

# # Checking method type of your browsing, usually GET when youre just running the URL
# @app.route("/methodType", methods=['GET', 'POST'])
# def methodType():
#     if request.method == 'POST':
#         return "You are using POST"
#     else:
#         return "You are using GET"