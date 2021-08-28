from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
import sys
import vlc
import pafy


class PlayListUi(object) :

    def __init__(self) :
        self.Window_x = 1700
        self.Window_y = 1300
        self.playlist_x = 1500   # 플레이목록 프레임사이즈
        self.playlist_y = 800

        self.widgetList = []

        self.setupUi()


    def setupUi(self) :

        self.MainWindow = QtWidgets.QMainWindow()
        self.MainWindow.resize(self.Window_x, self.Window_y)
        self.MainWindow.setWindowTitle("YouTube Player")

        self.centralwidget = QtWidgets.QWidget(self.MainWindow)
        self.centralwidget.setGeometry(0, 0, self.Window_x, self.Window_y)

        self.stacked = QtWidgets.QStackedWidget(self.centralwidget)
        self.stacked.setGeometry(0, 0, self.Window_x, self.Window_y)

        self.PlayListPage = QtWidgets.QWidget()

        self.PlayListPage_background = QtWidgets.QWidget(self.PlayListPage)
        self.PlayListPage_background.setGeometry(QtCore.QRect(50, 100, self.playlist_x, self.playlist_y))
        self.PlayListPage_background.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")

        self.scrollArea = QtWidgets.QScrollArea(self.PlayListPage_background)
        self.scrollArea.setGeometry(0, 0, self.playlist_x, self.playlist_y)

        self.verticalFrame = QtWidgets.QWidget(self.scrollArea)
        self.verticalFrame.setGeometry(0, 0, self.playlist_x -30, 10)
        self.scrollArea.setWidget(self.verticalFrame)
        self.verticalFrame.setStyleSheet("border : 1px solid red")

        self.PlayListPage_YoutubeLogoBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_YoutubeLogoBtn.setGeometry(QtCore.QRect(50, 1000, 120, 40))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayListPage_YoutubeLogoBtn.setIcon(icon)
        self.PlayListPage_YoutubeLogoBtn.setIconSize(QtCore.QSize(120, 40))

        self.PlayListPage_AddPlayVideoBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_AddPlayVideoBtn.setGeometry(QtCore.QRect(1520, 1040, 161, 41))
        self.PlayListPage_AddPlayVideoBtn.setText("재생영상 추가")

        self.PlayListPage_AddPlayListBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_AddPlayListBtn.setGeometry(QtCore.QRect(1320, 1040, 161, 41))
        self.PlayListPage_AddPlayListBtn.setText("재생목록 추가")

        self.PlayListPage_DeletePlayListBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_DeletePlayListBtn.setGeometry(QtCore.QRect(1120, 1040, 161, 41))
        self.PlayListPage_DeletePlayListBtn.setText("재생목록 제거")

        self.stacked.addWidget(self.PlayListPage)

        self.stacked.setCurrentIndex(0)




# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = PlayListUi()
    
#     sys.exit(app.exec_())












