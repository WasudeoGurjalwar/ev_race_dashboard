from flask import Flask
from flask_socketio import SocketIO
from networking.signal_handler import signal_handler

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route("/")
def index():
    return "EV Race Dashboard - Master Server (LOCAL)"

@socketio.on("update_leaderboard")
def handle_leaderboard(data):
    print("Received leaderboard update:", data)
    signal_handler.update_leaderboard.emit(data)

@socketio.on("update_station")
def handle_station(data):
    print("Received station update:", data)
    signal_handler.update_station.emit(data)

@socketio.on("new_message")
def handle_message(data):
    print("Received new message:", data)
    signal_handler.new_message.emit(data)

@socketio.on("update_battery")
def handle_battery(data):
    print("Received battery update:", data)
    signal_handler.update_battery.emit(data)

def run_server():
    socketio.run(app, host="127.0.0.1", port=5000)
    