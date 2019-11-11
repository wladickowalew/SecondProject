import sys
import random
from PyQt5 import uic
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QPushButton
from PyQt5.QtGui import QPainter, QColor


class Example(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui2.ui',self)
        self.addBtn.clicked.connect(self.paintOval)

    def paintOval(self, event):
        qp = QPainter()
        qp.begin(self)
        r = random.rand(5,55)
        x, y = random.rand(40, 200), random.rand(40, 200)
        qp.setBrush(QColor(255,255,0))
        qp.drawEllipse(x, y, r, r)
        qp.end()
        


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    ex.show()
    sys.exit(app.exec_())
