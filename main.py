import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtCore import QPointF
import random


class Interface(QWidget):
    def __init__(self):
        super().__init__()
        self.layout = QVBoxLayout(self)
        self.btn = QPushButton("Добавить круг")
        self.layout.addWidget(self.btn)


class MyWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.widget = Interface()

        self.widget.btn.clicked.connect(self.paint)
        self.setCentralWidget(self.widget)
        self.do_paint = False
        self.setGeometry(300, 300, 500, 500)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        diameter = random.uniform(20, 100)
        x = random.uniform(0, self.width() - diameter // 2)
        y = random.uniform(0, self.height() - diameter // 2)

        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        qp.drawEllipse(QPointF(x, y), diameter / 2, diameter / 2)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
