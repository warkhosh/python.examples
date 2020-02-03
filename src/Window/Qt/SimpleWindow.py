import sys
from PyQt5.QtWidgets import QApplication, QMainWindow


class SimpleWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(350, 250)
        self.setWindowTitle('Window: simple window 350x250')
        # Fixing the window size
        self.setFixedSize(350, 250)


if __name__ == "__main__":
    # Qt Application
    app = QApplication(sys.argv)

    window = SimpleWindow()
    window.show()

    # Execute application
    sys.exit(app.exec_())
