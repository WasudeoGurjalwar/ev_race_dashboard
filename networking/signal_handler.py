from PyQt5.QtCore import QObject, pyqtSignal

class SignalHandler(QObject):
    update_leaderboard = pyqtSignal(dict)
    update_station = pyqtSignal(dict)
    new_message = pyqtSignal(str)
    update_battery = pyqtSignal(dict)  # NEW SIGNAL

signal_handler = SignalHandler()
