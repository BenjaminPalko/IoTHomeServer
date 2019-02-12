import flask
# from rgbledcontroller import *

app = flask.Flask("__main__")

@app.route("/")
def my_index():
    return flask.render_template("index.html", token="Flask+React Connect Success: Home")

@app.route("/about")
def my_about():
    return flask.render_template("index.html", token="Flask+React Connect Success: About")

@app.route("/devices")
def my_devices():
    return flask.render_template("index.html", token="Flask+React Connect Success: Devices")

app.run(debug=True)