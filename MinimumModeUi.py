from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MinimumMode(object):

    def __init__(self) :
        self.MinimumUi = QtWidgets.QMainWindow()
        self.setupUi()

        
    # def MinimumModeUi_show(self) :
    #     self.MinimumUi.show()

    def setupUi(self):
        self.MinimumUi.setObjectName("MainWindow")
        self.MinimumUi.resize(993, 204)

        self.centralwidget = QtWidgets.QWidget(self.MinimumUi)
        self.centralwidget.setObjectName("centralwidget")

        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setGeometry(QtCore.QRect(0, 0, 991, 71))
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")

        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 989, 69))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")

        self.Min_Title = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        self.Min_Title.setGeometry(QtCore.QRect(10, 30, 971, 31))
        self.Min_Title.setObjectName("Min_Title")
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        
        self.BeforePlayBtn = QtWidgets.QPushButton(self.centralwidget)
        self.BeforePlayBtn.setGeometry(QtCore.QRect(30, 110, 51, 51))
        self.BeforePlayBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Before.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.BeforePlayBtn.setIcon(icon)
        self.BeforePlayBtn.setIconSize(QtCore.QSize(55, 55))
        self.BeforePlayBtn.setObjectName("BeforePlayBtn")

        self.PlayBtn = QtWidgets.QPushButton(self.centralwidget)
        self.PlayBtn.setGeometry(QtCore.QRect(110, 110, 51, 51))
        self.PlayBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayBtn.setIcon(icon1)
        self.PlayBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayBtn.setObjectName("PlayBtn")

        self.StopBtn = QtWidgets.QPushButton(self.centralwidget)
        self.StopBtn.setGeometry(QtCore.QRect(190, 110, 51, 51))
        self.StopBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.StopBtn.setIcon(icon2)
        self.StopBtn.setIconSize(QtCore.QSize(55, 55))
        self.StopBtn.setObjectName("StopBtn")

        self.NextBtn = QtWidgets.QPushButton(self.centralwidget)
        self.NextBtn.setGeometry(QtCore.QRect(270, 110, 51, 51))
        self.NextBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.NextBtn.setIcon(icon3)
        self.NextBtn.setIconSize(QtCore.QSize(55, 55))
        self.NextBtn.setObjectName("NextBtn")

        self.MaxiumBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MaxiumBtn.setGeometry(QtCore.QRect(810, 150, 171, 41))
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(12)
        self.MaxiumBtn.setFont(font)
        self.MaxiumBtn.setObjectName("MaxiumBtn")
        self.MinimumUi.setCentralWidget(self.centralwidget)

        self.retranslateUi(self.MinimumUi)
        QtCore.QMetaObject.connectSlotsByName(self.MinimumUi)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MinimumModeUi"))
        self.Min_Title.setText(_translate("MainWindow", "노래제목"))
        self.MaxiumBtn.setText(_translate("MainWindow", "최대화"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())

