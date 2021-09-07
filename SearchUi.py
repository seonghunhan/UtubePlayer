from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   

class Ui_SearchUi(object): # 검색창 UI

    def __init__(self) :

        self.setup()


    def setup(self) :
        self.SearchUi = QtWidgets.QMainWindow()
        self.SearchUi.resize(520, 300)
        self.SearchUi.setWindowTitle("비디오 검색")

        self.centralwidget = QtWidgets.QWidget(self.SearchUi)
        self.centralwidget.setGeometry(0, 0, 520, 300)

        self.PlaylistLabel = QtWidgets.QLabel(self.centralwidget)
        self.PlaylistLabel.setGeometry(QtCore.QRect(20, 50, 130, 50))
        self.PlaylistLabel.setText("플레이리스트 : ")

        self.SearchLabel = QtWidgets.QLabel(self.centralwidget)
        self.SearchLabel.setGeometry(QtCore.QRect(20, 140, 80, 30))
        self.SearchLabel.setText("검색명  : ")

        self.PlaylistText = QtWidgets.QLineEdit(self.centralwidget)
        self.PlaylistText.setGeometry(QtCore.QRect(150, 60, 330, 30))

        self.SearchText = QtWidgets.QLineEdit(self.centralwidget)
        self.SearchText.setGeometry(QtCore.QRect(150, 140, 330, 30))

        self.AddBtn = QtWidgets.QPushButton(self.centralwidget)
        self.AddBtn.setGeometry(QtCore.QRect(380,220,100,30))
        self.AddBtn.setText("추가")


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = Ui_SearchUi()
    
#     sys.exit(app.exec_())

