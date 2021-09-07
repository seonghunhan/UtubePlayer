from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
import sys
import vlc
import pafy


class MainUi(object) :

    def __init__(self) :
        
        self.setupUi()
        self.MainUi = QtWidgets.QMainWindow()
        self.MainWindow.show()


    def setupUi(self) :

        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.resize(1700, 1300)
        self.MainWindow.setWindowTitle("YouTube Player")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setGeometry(0, 0, 1700, 1300)

        self.stacked = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked.setGeometry(0, 100, 1700, 1100)

        self.MovePlayPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MovePlayPageBtn.setGeometry(QtCore.QRect(1560, 30, 141, 51))
        self.MovePlayPageBtn.setText("재생중인 영상")

        self.MovePlayListPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MovePlayListPageBtn.setGeometry(QtCore.QRect(1390, 30, 151, 51))
        self.MovePlayListPageBtn.setText("PlayList")

        self.stacked.setCurrentIndex(0)

