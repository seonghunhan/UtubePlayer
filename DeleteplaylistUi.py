from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Deleteplaylist(object):

    def __init__(self) :
        self.Deleteplaylist = QtWidgets.QMainWindow()
        self.setupUi()
        # self.Deleteplaylist.show()


    def setupUi(self):
        self.Deleteplaylist.setObjectName("MainWindow")
        self.Deleteplaylist.resize(822, 209)

        self.centralwidget = QtWidgets.QWidget(self.Deleteplaylist)
        self.centralwidget.setObjectName("centralwidget")

        self.PlayListLabel = QtWidgets.QLabel(self.centralwidget)
        self.PlayListLabel.setGeometry(QtCore.QRect(20, 70, 180, 31))
        self.PlayListLabel.setObjectName("PlayListLabel")

        self.InputPlayList = QtWidgets.QLineEdit(self.centralwidget)
        self.InputPlayList.setGeometry(QtCore.QRect(210, 70, 600, 31))
        self.InputPlayList.setObjectName("InputPlayList")

        
        self.Completedelete = QtWidgets.QPushButton(self.centralwidget)
        self.Completedelete.setGeometry(QtCore.QRect(620, 170, 170 , 31))
        self.Completedelete.setObjectName("CompleteAdd")

        self.Deleteplaylist.setCentralWidget(self.centralwidget)
        self.retranslateUi(self.Deleteplaylist)
        QtCore.QMetaObject.connectSlotsByName(self.Deleteplaylist)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add PlatList"))
        self.PlayListLabel.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">PlayListName</span></p></body></html>"))
        self.Completedelete.setText(_translate("YouTubePlayer", "플레이목록 제거"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = Ui_Deleteplaylist()
    
    sys.exit(app.exec_())