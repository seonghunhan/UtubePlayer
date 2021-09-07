from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage  
import urllib.request


class Popup_Window(object):

    def __init__(self):
        
        self.setup()
        self.Popup_Window.show()


    def setup(self):

        self.Popup_Window = QtWidgets.QMainWindow()
        self.Popup_Window.resize(1000, 500)
        self.Popup_Window.setWindowTitle("경고창")


        self.centralwidget = QtWidgets.QWidget(self.Popup_Window)
        self.centralwidget.setGeometry(0, 0, 1000, 500)

        self.background = QtWidgets.QWidget(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(100, 100, 450, 200))
        self.background.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")




        self.ReNameLabel = QtWidgets.QLabel()
        # self.ReNameLabel = QtWidgets.QLabel(self.background)
        self.ReNameLabel.setGeometry(QtCore.QRect(0, 0, 250, 200))

        url = "https://i.ytimg.com/vi/LCwuahHcQdU/default.jpg"
        image = urllib.request.urlopen(url).read()
        pixmap = QPixmap()
        pixmap.loadFromData(image)
        self.ReNameLabel.setPixmap(pixmap.scaled(QtCore.QSize(self.ReNameLabel.width(),self.ReNameLabel.height()),aspectRatioMode=QtCore.Qt.KeepAspectRatio))

        # self.TitleLabel = QtWidgets.QLabel(wordWrap=True,alignment=QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        # self.TitleLabel = QtWidgets.QLabel(self.background)
        self.TitleText = QtWidgets.QTextBrowser()
        self.TitleText.setGeometry(QtCore.QRect(250,0,200,200))
        self.TitleText.setFont(QtGui.QFont("monospace",15))
        self.TitleText.setText("dddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddddd")

        self.listlayout = QtWidgets.QGridLayout(self.background)
        self.listlayout.addWidget(self.ReNameLabel,0,0)
        self.listlayout.addWidget(self.TitleText,0,1)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    start = Popup_Window()
    
    sys.exit(app.exec_())
