from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_addplayVideo(object):

    def __init__(self) :
        self.addplaylist = QtWidgets.QMainWindow()
        self.setupUi()
        # self.addplaylist.show()


    def setupUi(self):
        self.addplaylist.setObjectName("MainWindow")
        self.addplaylist.resize(822, 209)

        self.centralwidget = QtWidgets.QWidget(self.addplaylist)
        self.centralwidget.setObjectName("centralwidget")

        self.UrlLabel = QtWidgets.QLabel(self.centralwidget)
        self.UrlLabel.setGeometry(QtCore.QRect(50, 40, 91, 31))
        self.UrlLabel.setObjectName("UrlLabel")

        self.PlayListLabel = QtWidgets.QLabel(self.centralwidget)
        self.PlayListLabel.setGeometry(QtCore.QRect(20, 120, 141, 31))
        self.PlayListLabel.setObjectName("PlayListLabel")

        self.InputUrl = QtWidgets.QLineEdit(self.centralwidget)
        self.InputUrl.setGeometry(QtCore.QRect(150, 40, 621, 31))
        self.InputUrl.setObjectName("InputUrl")

        self.InputPlayList = QtWidgets.QLineEdit(self.centralwidget)
        self.InputPlayList.setGeometry(QtCore.QRect(150, 118, 621, 31))
        self.InputPlayList.setObjectName("InputPlayList")

        
        self.CompleteAdd = QtWidgets.QPushButton(self.centralwidget)
        self.CompleteAdd.setGeometry(QtCore.QRect(620, 170, 170 , 31))
        self.CompleteAdd.setObjectName("CompleteAdd")

        self.addplaylist.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.addplaylist)
        QtCore.QMetaObject.connectSlotsByName(self.addplaylist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add PlatVideo"))
        self.UrlLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Url</span></p></body></html>"))
        self.PlayListLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">PlayList</span></p></body></html>"))
        self.CompleteAdd.setText(_translate("YouTubePlayer", "플레이영상 추가"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = Ui_addplaylist()
    
#     sys.exit(app.exec_())

