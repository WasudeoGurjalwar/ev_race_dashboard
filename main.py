import sys
from PyQt5.QtWidgets import QApplication
from panels.main_window import MainWindow
from server import run_server
import threading

if __name__ == "__main__":
    server_thread = threading.Thread(target=run_server, daemon=True)
    server_thread.start()

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())