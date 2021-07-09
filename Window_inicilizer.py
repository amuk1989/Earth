import sys

from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from UI import window
from Controllers.ConnectController import Connect_controller


class Window_initilizer(QtWidgets.QMainWindow, QWidget):
    def __init__(self, win):
        super().__init__()
        win.setupUi(self)


class Initilizer():

    def __init__(self):
        self.connect_controller = Connect_controller()

    def render(self):
        app = QtWidgets.QApplication(sys.argv)
        self.main_window = window.Ui_MainWindow()
        self.window = Window_initilizer(self.main_window)
        self.window.show()
        self.main_window.openConnect.clicked.connect(self.connect_clicked)
        self.main_window.startButton.clicked.connect(self.start_clicked)

        app.exec_()

    def connect_clicked(self):
        result = self.connect_controller.connect(self.main_window.port.currentText(),
                                                 int(self.main_window.speedConnection.currentText()))
        print(result)
        self.main_window.connectIndicator.set_state(result)

    def start_clicked(self):
        self.connect_controller.send(self.main_window.time.value(), self.main_window.mode.currentIndex())
