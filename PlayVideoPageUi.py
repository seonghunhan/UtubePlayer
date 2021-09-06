from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
import sys
import vlc
import pafy


class PlayVideoPageUi(object) :

    def __init__(self) :
        self.Window_x = 1700
        self.Window_y = 1300
        # self.Stacked = Stacked

        self.setupUi()







    def setupUi(self) :

        # self.MainWindow = QtWidgets.QMainWindow()
        # self.MainWindow.resize(self.Window_x, self.Window_y)
        # self.MainWindow.setWindowTitle("YouTube Player")

        # self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        # self.centralwidget.setGeometry(0, 0, self.Window_x, self.Window_y)

        # self.stacked = QtWidgets.QStackedWidget(self.centralwidget)
        # self.stacked.setGeometry(0, 0, self.Window_x, self.Window_y)


        self.PlayVideoPage = QtWidgets.QWidget()
        self.PlayVideoPage_background1 = QtWidgets.QWidget(self.PlayVideoPage)
        self.PlayVideoPage_background1.setGeometry(QtCore.QRect(1200, 80, 460, 1000))
        self.PlayVideoPage_background1.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                    "border-radius: 10px ;\n"
                                                    "border-style: solid;\n"
                                                    "border-width: 1px;\n"
                                                    "border-color: rgb(7, 7, 7)\n"
                                                    "")

        self.PlayVideoPage_background2 = QtWidgets.QWidget(self.PlayVideoPage)
        self.PlayVideoPage_background2.setGeometry(QtCore.QRect(10, 200, 1060, 800))
        self.PlayVideoPage_background2.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                    "border-radius: 10px ;\n"
                                                    "border-style: solid;\n"
                                                    "border-width: 1px;\n"
                                                    "border-color: rgb(7, 7, 7)\n"
                                                    "")

        self.scroll = QtWidgets.QScrollArea(self.PlayVideoPage)
        self.scroll.setGeometry(10 , 100, 1050, 90)
        self.PlayVideoPage_TitleLabel = QtWidgets.QLabel("ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇdd",self.scroll)
        self.PlayVideoPage_TitleLabel.setGeometry(10, 100, 2000, 70)
        self.scroll.setWidget(self.PlayVideoPage_TitleLabel)

        self.PlayPage_PlayListNameLabel = QtWidgets.QLabel(self.PlayVideoPage)
        self.PlayPage_PlayListNameLabel.setGeometry(QtCore.QRect(1250, 80, 460, 30))

        self.PlayPage_MinimumButton = QtWidgets.QPushButton(self.PlayVideoPage)
        self.PlayPage_MinimumButton.setGeometry(QtCore.QRect(1550, 20, 150, 40))
        self.PlayPage_MinimumButton.setText("최소화 모드")      

        self.PlayPage_ShupplePlayListBtn = QtWidgets.QPushButton(self.PlayVideoPage)
        self.PlayPage_ShupplePlayListBtn.setGeometry(QtCore.QRect(1130, 80, 50, 50))
        self.PlayPage_ShupplePlayListBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Shupple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_ShupplePlayListBtn.setIcon(icon3)
        self.PlayPage_ShupplePlayListBtn.setIconSize(QtCore.QSize(55, 55))

        self.PlayPage_OnePlayBtn = QtWidgets.QPushButton(self.PlayVideoPage)
        self.PlayPage_OnePlayBtn.setGeometry(QtCore.QRect(1130, 140, 50, 50))
        self.PlayPage_OnePlayBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("OnePlay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_OnePlayBtn.setIcon(icon3)
        self.PlayPage_OnePlayBtn.setIconSize(QtCore.QSize(55, 55))

        self.videoframe = QtWidgets.QFrame(self.PlayVideoPage)
        self.videoframe.setGeometry(QtCore.QRect(40,220,1000,750))

        # if sys.platform.startswith("linux"):  # for Linux using the X Server
        #     self.Test.medaiplayer.set_xwindow(self.videoframe.winId())
        # elif sys.platform == "win32":  # for Windows
        #     self.Test.mediaplayer.set_hwnd(self.videoframe.winId())
        # elif sys.platform == "darwin":  # for MacOS
        #     self.mediaplayer.set_nsobject(self.videoframe.winId())

        # self.playurl = QtWidgets.QLineEdit(self.PlayVideoPage)
        # self.playurl.setGeometry(QtCore.QRect(30, 20, 1371, 31))

        # self.urlgogobtn = QtWidgets.QPushButton(self.PlayVideoPage)
        # self.urlgogobtn.setGeometry(QtCore.QRect(200, 200, 50, 50))













if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = PlayVideoPageUi()
    
    sys.exit(app.exec_())

