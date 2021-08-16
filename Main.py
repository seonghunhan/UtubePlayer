
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import StackedLogic


class Main() :

    def __init__(self) :
        self.Stacked = StackedLogic.StackedLogic()

    











if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    
    start = Main()

    sys.exit(app.exec_())