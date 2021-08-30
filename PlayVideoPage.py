from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import PlayVideoPageUi
import MinimumModeUi


class PlayVideoPage(object) :

    def __init__(self, MainWindow) :

        self.PlayVideoPageUi = PlayVideoPageUi.PlayVideoPageUi()
        self.MinimumModeUi = MinimumModeUi.Ui_MinimumMode()
        self.MainWindow = MainWindow

        self.PlayVideoPageUi.PlayPage_MinimumButton.mousePressEvent = lambda event : self.MinimumModeUi_ShowEvent(event)
        self.MinimumModeUi.MaxiumBtn.mousePressEvent = lambda event : self.MaximumModeUi_showEvent(event)




    def MinimumModeUi_ShowEvent(self, event) :

        if event.buttons() & QtCore.Qt.LeftButton:
            self.MinimumModeUi.MinimumUi.show()
            self.MainWindow.close()
            
    def MaximumModeUi_showEvent(self, event) :

        if event.buttons() & QtCore.Qt.LeftButton:
            self.MainWindow.show()
            self.PlayVideoPageUi.PlayVideoPage.show()
            self.MinimumModeUi.MinimumUi.close()


        