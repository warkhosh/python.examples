import sys
from PyQt5.QtWidgets import QApplication, QWidget


def simple_window():
    application = QApplication(sys.argv)
    widget = QWidget()
    widget.resize(350, 250)
    widget.move(300, 300)
    widget.setWindowTitle('Simple window 350x250')

    """
    Метод show() отображает виджет на экране. 
    Виджет сначала создаётся в памяти, и только потом (с помощью метода show) показывается на экране.
    """
    widget.show()

    """
    Основной цикл заканчивается, если мы вызываем метод exit() или главный виджет уничтожен. 
    Метод sys.exit() гарантирует чистый выход.
    """
    sys.exit(application.exec_())


# Процедурный тип
simple_window()
