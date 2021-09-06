from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import PlaylistUi
import Addplaylistlogic
import SearchPage

class PlayListPage(object) :

    def __init__(self) :

        self.PlaylistUi = PlaylistUi.PlayListUi()
        self.widgetList = self.PlaylistUi.widgetList
        self.verticalFrame = self.PlaylistUi.verticalFrame
        self.AddplaylistBtn = self.PlaylistUi.PlayListPage_AddPlayListBtn
        self.Addplaylistlogic = Addplaylistlogic.Addplaylistlogic(self.widgetList,self.verticalFrame,self.AddplaylistBtn)
        self.SearchBtn = self.PlaylistUi.PlayListPage_SearchBtn
        self.SearchPage = SearchPage.SearchPage(self.SearchBtn)

