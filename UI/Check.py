from PyQt5.QtCore import Qt, QSize
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QWidget, QLabel, QHBoxLayout


class Check(QWidget):
    def __init__(self, parent=None):
        self.__img_true = 'UI/img/check1.png'
        self.__img_false = 'UI/img/check.png'
        self.__size = QSize(22, 22)
        self.state = False

        QWidget.__init__(self, parent)
        self.lbl = QLabel(self)
        self.lbl.setAlignment(Qt.AlignCenter)

        self.hbox = QHBoxLayout(self)
        self.lbl.resize(self.__size)
        self.hbox.addWidget(self.lbl)
        self.setLayout(self.hbox)
        self.draw()

    def draw(self):
        if self.state:
            pixmap = QPixmap(self.__img_true).scaled(self.__size, aspectRatioMode=Qt.KeepAspectRatio)
        else:
            pixmap = QPixmap(self.__img_false).scaled(self.__size, aspectRatioMode=Qt.KeepAspectRatio)
        self.lbl.setPixmap(pixmap)
        self.show()

    def set_state(self, value: bool):
        self.state = value
        self.draw()