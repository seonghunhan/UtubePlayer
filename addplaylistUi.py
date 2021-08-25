from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   

class Ui_AddplayUi(object):

    def __init__(self,StackedUi) :
        self.addplaylist = QtWidgets.QMainWindow()
        self.StackedUi = StackedUi
        self.playlistpage1Ui()
        
        # self.addplaylist.show()


    def playlistpage1Ui(self) :
        self.List1 = QtWidgets.QLabel(self.StackedUi.PlayListPage)
        self.List1.setGeometry(QtCore.QRect(150,200, 200, 200))
        self.List1.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List1.setPixmap(self.pixmap) # 이미지 세팅
        self.List1.resize(self.pixmap.width(), self.pixmap.height())



        self.ListName1 = QtWidgets.QLabel("고고고고", self.StackedUi.PlayListPage)
        self.ListName1.setGeometry(QtCore.QRect(200,350, 101, 18))
        self.ListName1.setObjectName("ListName1")

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = Ui_Addplaylist()
    
#     sys.exit(app.exec_())

