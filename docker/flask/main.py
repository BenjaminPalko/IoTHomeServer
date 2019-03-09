from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
import json

app = Flask(__name__, template_folder="templates")
socketio = SocketIO(app)
app.config.update(
    SECRET_KEY='iotSecret_key',
    SQLALCHEMY_DATABASE_URI='postgresql://postgres@localhost:5432/postgres',
    SQLALCHEMY_USERNAME='postgres',
    SQLALCHEMY_PASSWORD='root'
)

@app.route('/')
def default():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app, host="0.0.0.0", debug=True)
