from PyQt5.QtWidgets import QGroupBox, QVBoxLayout, QListWidget, QListWidgetItem
from PyQt5.QtCore import QTimer, Qt
from datetime import datetime

class CommunicationPanel(QGroupBox):
    def __init__(self):
        super().__init__("Live Communication Feed")
        layout = QVBoxLayout()
        self.list_widget = QListWidget()
        layout.addWidget(self.list_widget)
        self.setLayout(layout)

    def append_message(self, message):
        timestamp = datetime.now().strftime("%H:%M:%S")
        item = QListWidgetItem(f"[{timestamp}] {message}")
        item.setBackground(Qt.white)
        self.list_widget.addItem(item)
        self.animate_item(item)

    def animate_item(self, item):
        item.setBackground(Qt.yellow)
        QTimer.singleShot(800, lambda: item.setBackground(Qt.white))
