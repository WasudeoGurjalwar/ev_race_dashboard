from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QProgressBar, QLabel

class BatteryPanel(QGroupBox):
    def __init__(self, evs):
        super().__init__("Battery Levels")
        self.layout = QVBoxLayout()
        self.bars = {}
        self.setLayout(self.layout)

        for ev in evs:
            label = QLabel(ev.name)
            bar = QProgressBar()
            bar.setValue(100)
            bar.setStyleSheet("""
                QProgressBar {
                    border: 1px solid #bbb;
                    border-radius: 5px;
                    text-align: center;
                }
                QProgressBar::chunk {
                    background-color: #4CAF50;
                    width: 20px;
                }
            """)
            self.bars[ev.name] = bar
            self.layout.addWidget(label)
            self.layout.addWidget(bar)

    def update_battery(self, data):
        print("Received battery pannel data:", data)
        print("BatteryPanel bars:", list(self.bars.keys()))
        name = data["name"]
        battery = data.get("battery", 100)
        if name in self.bars:
            self.bars[name].setValue(battery)
