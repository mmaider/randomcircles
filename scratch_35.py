import random

from PyQt5 import uic
import sys

from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

class SetupWin(object):
    def setupUi(self, Form):
        self.width, self.height = 300, 300
        Form.setGeometry(100, 100, self.width, self.height)

        self.btn = QPushButton('НАЖМИ НА МЕНЯ!', self)
        self.btn.move(100, 100)
        self.btn.resize(200, 50)


class Example(QWidget, SetupWin):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.pushButton.clicked.connect(self.drawc)
        self.show()

    def drawc(self):
        self.x = random.randint(0, 300)
        self.y = random.randint(0, 300)
        self.radius = random.randint(1, 100)
        self.flag = True
        self.repaint()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
            painter.drawEllipse(self.x, self.y, self.radius, self.radius)
            painter.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
