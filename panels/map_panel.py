from PyQt5.QtWidgets import QGroupBox, QGridLayout, QLabel
from PyQt5.QtCore import QVariantAnimation, Qt
from PyQt5.QtGui import QColor
from PyQt5.QtGui import QFont

class AnimatedSlot(QLabel):
    def __init__(self, slot_id, status):
        super().__init__()
        self.slot_id = slot_id
        self.status = status
        self.setAlignment(Qt.AlignCenter)
        self.setFixedSize(160, 30)
        self.setStyleSheet("border-radius: 6px; border: 1px solid black;")
        self.update_text()
        self.animate_status(status)

    def update_text(self):
        self.setText(f"🔌 Slot {self.slot_id}: {self.status}")

    def animate_status(self, status):
        self.status = status
        self.update_text()
        color_map = {
            "Available": QColor(0, 200, 0),
            "Occupied": QColor(200, 0, 0),
            "Not Working": QColor(128, 128, 128),
            "Not Available": QColor(128, 128, 128)
        }
        color = color_map.get(status, QColor(128, 128, 128))
        self.animation = QVariantAnimation(startValue=QColor("white"), endValue=color, duration=500)
        self.animation.valueChanged.connect(self._apply_color)
        self.animation.start()

    def _apply_color(self, color):
        self.setStyleSheet(f"background-color: {color.name()}; border-radius: 6px; border: 1px solid black;")

class MapPanel(QGroupBox):
    def __init__(self, stations):
        super().__init__("Charging Station Map")
        self.stations = stations
        self.layout = QGridLayout()
        self.setLayout(self.layout)
        self.slot_labels = {}
        self.update_ui()

    def update_ui(self):
        # Clear the layout first
        while self.layout.count():
            item = self.layout.takeAt(0)
            widget = item.widget()
            if widget is not None:
                widget.deleteLater()
        self.layout.setSpacing(8)
        self.slot_labels = {}

        # Place station names horizontally at the top
        for col, station in enumerate(self.stations):
            name_label = QLabel(f"📍 {station.name}")
            font = QFont()
            font.setPointSize(12)  # Increase font size as needed
            font.setBold(True)
            name_label.setFont(font)
            name_label.setAlignment(Qt.AlignCenter)
            self.layout.addWidget(name_label, 0, col)

            # Place slots vertically below each station name
            for row, slot in enumerate(station.slots):
                widget = AnimatedSlot(row + 1, slot)
                self.slot_labels[(station.name, row)] = widget
                self.layout.addWidget(widget, row + 1, col)


    def update_station_status(self, data):
        name, slots = data['station'], data['slots']
        for idx, status in enumerate(slots):
            key = (name, idx)
            if key in self.slot_labels:
                self.slot_labels[key].animate_status(status)
