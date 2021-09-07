from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage  


class Popup_Window(object): # 팝업창UI

    def __init__(self):
        self.setup()


    def setup(self):

        self.Popup_Window = QtWidgets.QMainWindow()
        self.Popup_Window.resize(330, 150)
        self.Popup_Window.setWindowTitle("경고창")

        self.centralwidget = QtWidgets.QWidget(self.Popup_Window)
        self.centralwidget.setGeometry(0, 0, 330, 150)

        self.ReNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.ReNameLabel.setGeometry(QtCore.QRect(30, 50, 520, 50))
        self.ReNameLabel.setText("해당영상을 띄울수없습니다.")





# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     start = Popup_Window()
    
#     sys.exit(app.exec_())