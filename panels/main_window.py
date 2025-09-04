from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QHBoxLayout
from models.ev_client import EV
from models.charging_station import ChargingStation
from panels.map_panel import MapPanel
from panels.leaderboard_panel import LeaderboardPanel
from panels.communication_panel import CommunicationPanel
from panels.battery_panel import BatteryPanel
from networking.signal_handler import signal_handler


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("VIrtual EV Challenge Dashboard")
        self.setMinimumSize(1400, 800)
        self.evs = [EV(c) for c in ["OffVOlt", "CEG_Motor_Sports" , "EPD_12" , "Herakles_Racing", "MTR" ]]
        self.stations = [ChargingStation(city) for city in ["Bangalore", "Tumakuru", "Chitradurga", "Kolhapur", "Pune"]]
        self.init_ui()

        # Connect signals
        signal_handler.update_leaderboard.connect(self.leaderboard.update_leaderboard)
        signal_handler.update_battery.connect(self.battery_panel.update_battery)
        signal_handler.update_station.connect(self.map_panel.update_station_status)
        signal_handler.new_message.connect(self.comm_panel.append_message)

    def init_ui(self):
        central_widget = QWidget()
        main_layout = QVBoxLayout()  # Main vertical layout

        # 1. Charging station map at the top (full width)
        self.map_panel = MapPanel(self.stations)
        self.map_panel.setFixedHeight(160)
        main_layout.addWidget(self.map_panel)

        # 2. Middle and bottom area split horizontally
        middle_bottom_layout = QHBoxLayout()

        # Left side (vertical split: battery panel on top, leaderboard at bottom)
        left_layout = QVBoxLayout()
        self.battery_panel = BatteryPanel(self.evs)
        self.battery_panel.setFixedHeight(300)
        self.battery_panel.setFixedWidth(500)
        left_layout.addWidget(self.battery_panel)

        self.leaderboard = LeaderboardPanel(self.evs)
        self.leaderboard.setFixedWidth(500)
        left_layout.addWidget(self.leaderboard)

        # Right side: Communication panel (takes most of the right side)
        self.comm_panel = CommunicationPanel()
        # Optionally set minimum size or stretch
        # self.comm_panel.setMinimumHeight(400)

        middle_bottom_layout.addLayout(left_layout, 1)
        middle_bottom_layout.addWidget(self.comm_panel, 2)

        main_layout.addLayout(middle_bottom_layout)

        central_widget.setLayout(main_layout)
        self.setCentralWidget(central_widget)