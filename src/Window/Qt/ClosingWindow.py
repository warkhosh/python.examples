import sys
from PyQt5.QtWidgets import QWidget, QMainWindow, QMessageBox, QPushButton, QApplication


class ClosingWindow(QMainWindow):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('Window: close event')

        btn = QPushButton('Quit', self)
        btn.clicked.connect(self.close)
        btn.resize(btn.sizeHint())
        btn.move(50, 50)

        # если нужно закрыть окно минуя события
        # btn = QPushButton('Quit', self)
        # btn.clicked.connect(QCoreApplication.instance().quit)
        # btn.resize(btn.sizeHint())
        # btn.move(50, 50)

        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application

    """
    Переопределяем обработчик события closeEvent
    """
    def closeEvent(self, event):
        reply = QMessageBox.question(
            self,
            'Message',
            "Are you sure to quit?",
            QMessageBox.Yes | QMessageBox.No,
            QMessageBox.No
        )

        if reply == QMessageBox.Yes:
            event.accept()
        else:
            event.ignore()


object_ = ClosingWindow(QApplication(sys.argv))
