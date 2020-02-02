import sys
from PyQt5.QtWidgets import QApplication, QWidget


def simple_window():
    _window = QApplication(sys.argv)
    w = QWidget(None)
    w.resize(350, 250)
    w.move(300, 300)
    w.setWindowTitle('Simple window 350x250')

    """
    Метод show() отображает виджет на экране. 
    Виджет сначала создаётся в памяти, и только потом (с помощью метода show) показывается на экране.
    """
    w.show()

    """
    Основной цикл заканчивается, если мы вызываем метод exit() или главный виджет уничтожен. 
    Метод sys.exit() гарантирует чистый выход.
    """
    sys.exit(_window.exec_())


simple_window()
