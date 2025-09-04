from PyQt5.QtWidgets import QGroupBox, QHBoxLayout, QPushButton

class RaceControlPanel(QGroupBox):
    def __init__(self):
        super().__init__("Race Control")
        layout = QHBoxLayout()
        self.start_btn = QPushButton("🚦 Start")
        self.pause_btn = QPushButton("⏸ Pause")
        self.reset_btn = QPushButton("🔄 Reset")
        for btn in [self.start_btn, self.pause_btn, self.reset_btn]:
            btn.setStyleSheet("""
                QPushButton {
                    background-color: #007BFF;
                    color: white;
                    font-weight: bold;
                    padding: 8px;
                    border-radius: 6px;
                }
                QPushButton:hover {
                    background-color: #0056b3;
                }
            """)
            layout.addWidget(btn)
        self.setLayout(layout)
