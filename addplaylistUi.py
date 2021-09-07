from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   

class Ui_AddplayUi(object): # 리스트추가 UI

    def __init__(self) :

        self.setup()
        

    def setup(self) :
        self.AddplaylistUi = QtWidgets.QMainWindow()
        self.AddplaylistUi.resize(520, 150)
        self.AddplaylistUi.setWindowTitle("플레이리스트 이름변경")

        self.centralwidget = QtWidgets.QWidget(self.AddplaylistUi)
        self.centralwidget.setGeometry(0, 0, 520, 150)

        self.ReNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReNameLabel.setGeometry(QtCore.QRect(30, 50, 80, 30))
        self.ReNameLabel.setText("변경 이름 : ")


        self.ReNameText = QtWidgets.QLineEdit(self.centralwidget)
        self.ReNameText.setGeometry(QtCore.QRect(150, 50, 300, 30))

        self.confirmBtn = QtWidgets.QPushButton(self.centralwidget)
        self.confirmBtn.setGeometry(QtCore.QRect(350,100,100,30))
        self.confirmBtn.setText("확인")


    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = Ui_AddplayUi()
    
#     sys.exit(app.exec_())

