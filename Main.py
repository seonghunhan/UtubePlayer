
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PlayVideoPage
import Playlistpage
import MainUi

class Main() :

    def __init__(self) :


 
        self.MainUi = MainUi.MainUi()
        self.Stacked = self.MainUi.stacked

        self.PlayVideoPage = PlayVideoPage.PlayVideoPage(self.Stacked)
        self.PlaylistPage = Playlistpage.PlayListPage()

    




















if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    

    
    start = Main()

    sys.exit(app.exec_())