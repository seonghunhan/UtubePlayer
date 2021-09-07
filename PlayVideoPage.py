from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import PlayVideoPageUi
import MinimumModeUi
import DB

class PlayVideoPage(object) : # 영상재생페이지

    def __init__(self, MainWindow, clikedlistidx) :

        self.PlayVideoPageUi = PlayVideoPageUi.PlayVideoPageUi()
        self.widgetList2 = self.PlayVideoPageUi.widgetList2
        self.verticalFrame = self.PlayVideoPageUi.verticalFrame
        self.MinimumModeUi = MinimumModeUi.Ui_MinimumMode()
        self.MainWindow = MainWindow
        self.beclicked_listidx = clikedlistidx
        self.PlayVideoPageUi.PlayPage_MinimumButton.mousePressEvent = lambda event : self.MinimumModeUi_ShowEvent(event)
        self.MinimumModeUi.MaxiumBtn.mousePressEvent = lambda event : self.MaximumModeUi_showEvent(event)

        # print(clikedlistidx[1])

    def set_frame(self, event) : # 아직 덜완성
        db = DB.DataBase


    def MinimumModeUi_ShowEvent(self, event) : # 최소화모드 Show이벤트

        if event.buttons() & QtCore.Qt.LeftButton:
            self.MinimumModeUi.MinimumUi.show()
            self.MainWindow.close() # 최소화모드 실행시 MainUi의 메인윈도우 close
            
    def MaximumModeUi_showEvent(self, event) : # 최소화모드에서 최대화모드 Show이벤트

        if event.buttons() & QtCore.Qt.LeftButton:
            self.MainWindow.show()
            self.PlayVideoPageUi.PlayVideoPage.show()
            self.MinimumModeUi.MinimumUi.close()




        