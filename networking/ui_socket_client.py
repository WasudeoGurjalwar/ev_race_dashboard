import socketio
from PyQt5.QtCore import QTimer

class UISocketClient:
    def __init__(self, main_window):
        self.sio = socketio.Client()
        self.main_window = main_window

        @self.sio.on("update_battery")
        def on_battery(data):
            print("UI received update_battery:", data)
            def call_update():
                print("Calling update_battery on:", self.main_window.battery_panel)
                self.main_window.battery_panel.update_battery(data)
            print("Scheduling call_update with QTimer")
            QTimer.singleShot(0, call_update)
            
    def connect(self):
        self.sio.connect("http://127.0.0.1:5000")