from PyQt5.QtWidgets import QGroupBox, QTableWidget, QVBoxLayout, QTableWidgetItem, QHeaderView
from PyQt5.QtGui import QColor
from PyQt5.QtCore import QTimer

class LeaderboardPanel(QGroupBox):
    def __init__(self, evs):
        super().__init__("Leaderboard")
        self.evs = evs
        self.table = QTableWidget(5, 4)  # Now 4 columns
        self.table.setHorizontalHeaderLabels(["Team", "Distance", "Rank", "ETA"])
        self.table.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)  # Fit columns to board size
        self.table.horizontalHeader().setSectionResizeMode(0, QHeaderView.Interactive)  # Team column resizable
        self.table.setColumnWidth(0, 180)  # Increase the width of the Team column
        self.table.verticalHeader().setVisible(False)
        self.table.setShowGrid(True)
        layout = QVBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)
        self.update_table()

    def update_table(self):
        self.evs.sort(key=lambda ev: -ev.distance)
        for i, ev in enumerate(self.evs):
            ev.rank = i + 1
            self.table.setItem(i, 0, QTableWidgetItem(ev.name))
            self.table.setItem(i, 1, QTableWidgetItem(str(ev.distance)))
            self.table.setItem(i, 2, QTableWidgetItem(str(ev.rank)))
            self.table.setItem(i, 3, QTableWidgetItem(ev.eta))

    def update_leaderboard(self, data):
        for ev in self.evs:
            if ev.name == data["name"]:
                ev.distance = data["distance"]
                ev.eta = data["eta"]
        self.update_table()
        #self.flash_row(data["name"])

    def flash_row(self, name):
        for row in range(self.table.rowCount()):
            if self.table.item(row, 0) and self.table.item(row, 0).text() == name:
                for col in range(self.table.columnCount()):
                    item = self.table.item(row, col)
                    if item:
                        item.setBackground(QColor("yellow"))
                QTimer.singleShot(800, lambda: self.clear_row_color(row))
                break

    def clear_row_color(self, row):
        for col in range(self.table.columnCount()):
            item = self.table.item(row, col)
            if item:
                item.setBackground(QColor("white"))