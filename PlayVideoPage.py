from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import PlayVideoPageUi


class PlayVideoPage(object) :

    def __init__(self,Stacked) :
        self.asd = Stacked
        self.PlayVideoPageUi = PlayVideoPageUi.PlayVideoPageUi(self.asd)
        



        