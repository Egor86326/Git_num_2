# _*_coding:utf-8_*_
import sys, random
from PyQt5 import uic
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import *


class Window(QMainWindow):
    def __init__(self):
        super(Window, self).__init__()
        self.setWindowTitle('случайные окружности')
        self.setFixedSize(370, 250)

        self.pushButton = QPushButton(self)
        self.pushButton.setGeometry(270, 210, 90, 30)
        self.pushButton.setText('Создать')
        self.pushButton.clicked.connect(self.run)

    def run(self):
        self.update()

    def paintEvent(self, event):
        # Создаем объект QPainter для рисования
        qp = QPainter()
        # Начинаем процесс рисования
        qp.begin(self)
        self.draw(qp)
        # Завершаем рисование
        qp.end()

    def draw(self, qp):
        r = random.randrange(0, 255, 1)
        g = random.randrange(0, 255, 1)
        b = random.randrange(0, 255, 1)
        qp.setBrush(QColor(r, g, b))
        i = random.randrange(0, 120, 1)
        x = random.randrange(0, 200, 1)
        y = random.randrange(0, 200, 1)
        qp.drawEllipse(x, y, i, i)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    wnd = Window()
    wnd.show()
    sys.exit(app.exec())