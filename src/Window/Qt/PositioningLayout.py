import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QWidget, QPushButton, QHBoxLayout, QVBoxLayout
from PyQt5 import QtGui, QtCore, QtWidgets
from PyQt5.QtGui import QFont, QCursor, QIcon, QPixmap
import platform

if platform.system() == 'Linux':
    FONT_SIZE = 9
else:
    FONT_SIZE = 12

class PositioningLayout(QWidget):
    def __init__(self, application):
        super().__init__()
        self._application = application
        self.init_ui()

    def init_ui(self):
        self.move(300, 300)
        self.resize(550, 250)
        self.setWindowTitle('Window: positioning layout')

        # button OK
        btn_ok = QtWidgets.QPushButton("OK")

        font = QtGui.QFont()
        font.setPointSize(18)
        # font.setBold(True)
        font.setWeight(75)
        # btn_ok.setBackground(QtGui.QColor('#ffff99'))
        # r = btn_ok.renderer()
        # btn_ok.setColor(QtGui.QColor('grey'))
        btn_ok.setFont(font)

        # button Cancel
        btn_cancel = QPushButton("Cancel")

        font = QtGui.QFont()
        font.setPointSize(13)
        # font.setBold(True)
        font.setWeight(75)
        btn_cancel.setFont(font)

        # button Ignore
        btn_ignore = QPushButton("Ignore")
        btn_ignore.setGeometry(QtCore.QRect(150, 40, 111, 28))

        font = QtGui.QFont()
        font.setPointSize(11)
        # font.setBold(False)
        font.setWeight(35)
        btn_ignore.setFont(font)

        self._set_font()

        # button Default
        btn_default = QPushButton("Default")

        horizontal_box = QHBoxLayout()
        horizontal_box.addStretch(1)
        horizontal_box.addWidget(btn_ok)
        horizontal_box.addWidget(btn_cancel)
        horizontal_box.addWidget(btn_ignore)
        horizontal_box.addWidget(btn_default)

        vertical_box = QVBoxLayout()
        vertical_box.addStretch(1)
        vertical_box.addLayout(horizontal_box)

        self.setLayout(vertical_box)

        self.show()
        sys.exit(self.application.exec_())

    @property
    def application(self):
        return self._application

    def _set_font(self):
        """Sets the font of the table"""
        font = QFont()
        font.setPointSize(FONT_SIZE)
        self.setFont(font)
        print("Font", FONT_SIZE)

object_ = PositioningLayout(QApplication(sys.argv))
