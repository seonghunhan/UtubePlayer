from PyQt5 import QtCore, QtWidgets

class mainUI(QtWidgets.QMainWindow):
    def __init__(self):
        super(mainUI, self).__init__()
        self.initUI()
    
    def initUI(self):
        self.setWindowTitle("BlogWindow11")
        self.setGeometry(250, 250, 250, 250)
        # Actions
        _exit = QtWidgets.QAction("나가기", self)
        _exit.setShortcut("Ctrl+E")

        # Menu Bar Settings
        menu = self.menuBar()
        _file = menu.addMenu("파일")
        _file.addAction(_exit)
        
        # Connect Actions
        _exit.triggered.connect(self.exitAction)
        
        self.show()
    
    def exitAction(self):
        self.close()
        print("Exited")

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = mainUI()
    sys.exit(app.exec_())
5