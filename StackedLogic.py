from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import StackedUi
import MinimumModeUi
import addplayvideoUi
import Test1
import AddplaylistUi
import DB
import DeleteplaylistLogic


class StackedLogic(object) :
    
    def __init__(self) :
        
        self.MinimumModeUi = MinimumModeUi.Ui_MinimumMode()
        self.AddPlayVideoUi = addplayvideoUi.Ui_addplayVideo()
        self.AddPlayListUi = AddplaylistUi.Ui_Addplaylist()
        self.Test = Test1.Test()
        self.StackedUi = StackedUi.Ui_YouTubePlayer(self.Test) # 여기서는 이렇게 해야함 -> 여기파일에서 작동시키니깐
                                                                # DB는 서로 껐다켰다 수정하니깐 각자 import해도 상관무
        
        self.Deleteplaylist = DeleteplaylistLogic.DeleteplaylistLogic()

        
        


        self.StackedUi.PlayPage_MinimumButton.clicked.connect(self.MinimumModeUi_showEvent)
        self.StackedUi.PlayPage_MinimumButton.clicked.connect(self.StackedUi_closeEvent)

        self.MinimumModeUi.MaxiumBtn.clicked.connect(self.StackedUi_showEvent)
        self.MinimumModeUi.MaxiumBtn.clicked.connect(self.MinimumModeUi_closeEvent)

        self.StackedUi.PlayListPage_AddPlayVideoBtn.clicked.connect(self.addplayVideoUi_showEvent)
        self.StackedUi.PlayListPage_AddPlayListBtn.clicked.connect(self.addplaylistUi_showEvent)
        self.StackedUi.PlayListPage_DeletePlayListBtn.clicked.connect(self.deleteplatlistUi_showEvent)



        self.StackedUi.urlgogobtn.clicked.connect(self.urlEvent)

        self.AddPlayListUi.CompleteAdd.clicked.connect(self.AddListEvent)


        
        

        self.StackedUi.MovePlayListPageBtn.clicked.connect(self.StackedUi.showPlayListPage)
        self.StackedUi.MovePlayPageBtn.clicked.connect(self.StackedUi.showPlayPage)
        self.StackedUi.MoveSearchPageBtn.clicked.connect(self.StackedUi.showSearchPage)

        ani = QtCore.QPropertyAnimation(self.StackedUi.MovePlayPageBtn, b"geometry")
        self.StackedUi.MovePlayPageBtn.enterEvent = lambda event, animation = ani , : self.MovePlayPagebuttonEnterEvent(event, animation)
        self.StackedUi.MovePlayPageBtn.leaveEvent = lambda event, animation = ani , : self.MovePlayPagebuttonleaveEvent(event, animation)

        ani1 = QtCore.QPropertyAnimation(self.StackedUi.MoveSearchPageBtn, b"geometry")
        self.StackedUi.MoveSearchPageBtn.enterEvent = lambda event, animation = ani1 , : self.MoveSearchPagebuttonEnterEvent(event, animation)
        self.StackedUi.MoveSearchPageBtn.leaveEvent = lambda event, animation = ani1 , : self.MoveSearchPagebuttonleaveEvent(event, animation)

        ani2 = QtCore.QPropertyAnimation(self.StackedUi.MovePlayListPageBtn, b"geometry")
        self.StackedUi.MovePlayListPageBtn.enterEvent = lambda event, animation = ani2 , : self.MovePlayListPagebuttonEnterEvent(event, animation)
        self.StackedUi.MovePlayListPageBtn.leaveEvent = lambda event, animation = ani2 , : self.MovePlayListPagebuttonleaveEvent(event, animation)

        ani3 = QtCore.QPropertyAnimation(self.StackedUi.PlayListPage_YoutubeLogoBtn, b"geometry")
        self.StackedUi.PlayListPage_YoutubeLogoBtn.enterEvent = lambda event, animation = ani3 , : self.PlayListPage_YoutubeLogobuttonEnterEvent(event, animation)
        self.StackedUi.PlayListPage_YoutubeLogoBtn.leaveEvent = lambda event, animation = ani3 , : self.PlayListPage_YoutubeLogobuttonleaveEvent(event, animation)

        ani4 = QtCore.QPropertyAnimation(self.StackedUi.PlayPage_PlayBeforeVideoBtn, b"geometry")
        self.StackedUi.PlayPage_PlayBeforeVideoBtn.enterEvent = lambda event, animation = ani4 , : self.PlayPage_PlayBeforeVideobuttonEnterEvent(event, animation)
        self.StackedUi.PlayPage_PlayBeforeVideoBtn.leaveEvent = lambda event, animation = ani4 , : self.PlayPage_PlayBeforeVideobuttonleaveEvent(event, animation)

        ani5 = QtCore.QPropertyAnimation(self.StackedUi.PlayPage_PlayVideoBtn, b"geometry")
        self.StackedUi.PlayPage_PlayVideoBtn.enterEvent = lambda event, animation = ani5 , : self.PlayPage_PlayVideobuttonEnterEvent(event, animation)
        self.StackedUi.PlayPage_PlayVideoBtn.leaveEvent = lambda event, animation = ani5 , : self.PlayPage_PlayVideobuttonleaveEvent(event, animation)

        ani6 = QtCore.QPropertyAnimation(self.StackedUi.PlayPage_StopVideoBtn, b"geometry")
        self.StackedUi.PlayPage_StopVideoBtn.enterEvent = lambda event, animation = ani6 , : self.PlayPage_StopVideobuttonEnterEvent(event, animation)
        self.StackedUi.PlayPage_StopVideoBtn.leaveEvent = lambda event, animation = ani6 , : self.PlayPage_StopVideobuttonleaveEvent(event, animation)

        ani7 = QtCore.QPropertyAnimation(self.StackedUi.PlayPage_PlayNextVideoBtn, b"geometry")
        self.StackedUi.PlayPage_PlayNextVideoBtn.enterEvent = lambda event, animation = ani7 , : self.PlayPage_PlayNextVideobuttonEnterEvent(event, animation)
        self.StackedUi.PlayPage_PlayNextVideoBtn.leaveEvent = lambda event, animation = ani7 , : self.PlayPage_PlayNextVideobuttonleaveEvent(event, animation)

        ani8 = QtCore.QPropertyAnimation(self.StackedUi.PlayPage_ShupplePlayListBtn, b"geometry")
        self.StackedUi.PlayPage_ShupplePlayListBtn.enterEvent = lambda event, animation = ani8 , : self.PlayPage_ShupplePlayListbuttonEnterEvent(event, animation)
        self.StackedUi.PlayPage_ShupplePlayListBtn.leaveEvent = lambda event, animation = ani8 , : self.PlayPage_ShupplePlayListbuttonleaveEvent(event, animation)
        
        ani9 = QtCore.QPropertyAnimation(self.StackedUi.PlayPage_OnePlayBtn, b"geometry")
        self.StackedUi.PlayPage_OnePlayBtn.enterEvent = lambda event, animation = ani9 , : self.PlayPage_OnePlaybuttonEnterEvent(event, animation)
        self.StackedUi.PlayPage_OnePlayBtn.leaveEvent = lambda event, animation = ani9 , : self.PlayPage_OnePlaybuttonleaveEvent(event, animation)

    def PlayPage_OnePlaybuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_OnePlayBtn.x(), self.StackedUi.PlayPage_OnePlayBtn.y(), self.StackedUi.PlayPage_OnePlayBtn.width(), self.StackedUi.PlayPage_OnePlayBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_OnePlayBtn.x()-5, self.StackedUi.PlayPage_OnePlayBtn.y()-5, self.StackedUi.PlayPage_OnePlayBtn.width()+10, self.StackedUi.PlayPage_OnePlayBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayPage_OnePlaybuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_OnePlayBtn.x(), self.StackedUi.PlayPage_OnePlayBtn.y(), self.StackedUi.PlayPage_OnePlayBtn.width(), self.StackedUi.PlayPage_OnePlayBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_OnePlayBtn.x()+5, self.StackedUi.PlayPage_OnePlayBtn.y()+5, self.StackedUi.PlayPage_OnePlayBtn.width()-10, self.StackedUi.PlayPage_OnePlayBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def PlayPage_ShupplePlayListbuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_ShupplePlayListBtn.x(), self.StackedUi.PlayPage_ShupplePlayListBtn.y(), self.StackedUi.PlayPage_ShupplePlayListBtn.width(), self.StackedUi.PlayPage_ShupplePlayListBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_ShupplePlayListBtn.x()-5, self.StackedUi.PlayPage_ShupplePlayListBtn.y()-5, self.StackedUi.PlayPage_ShupplePlayListBtn.width()+10, self.StackedUi.PlayPage_ShupplePlayListBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayPage_ShupplePlayListbuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_ShupplePlayListBtn.x(), self.StackedUi.PlayPage_ShupplePlayListBtn.y(), self.StackedUi.PlayPage_ShupplePlayListBtn.width(), self.StackedUi.PlayPage_ShupplePlayListBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_ShupplePlayListBtn.x()+5, self.StackedUi.PlayPage_ShupplePlayListBtn.y()+5, self.StackedUi.PlayPage_ShupplePlayListBtn.width()-10, self.StackedUi.PlayPage_ShupplePlayListBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def PlayPage_PlayNextVideobuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_PlayNextVideoBtn.x(), self.StackedUi.PlayPage_PlayNextVideoBtn.y(), self.StackedUi.PlayPage_PlayNextVideoBtn.width(), self.StackedUi.PlayPage_PlayNextVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_PlayNextVideoBtn.x()-5, self.StackedUi.PlayPage_PlayNextVideoBtn.y()-5, self.StackedUi.PlayPage_PlayNextVideoBtn.width()+10, self.StackedUi.PlayPage_PlayNextVideoBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayPage_PlayNextVideobuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_PlayNextVideoBtn.x(), self.StackedUi.PlayPage_PlayNextVideoBtn.y(), self.StackedUi.PlayPage_PlayNextVideoBtn.width(), self.StackedUi.PlayPage_PlayNextVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_PlayNextVideoBtn.x()+5, self.StackedUi.PlayPage_PlayNextVideoBtn.y()+5, self.StackedUi.PlayPage_PlayNextVideoBtn.width()-10, self.StackedUi.PlayPage_PlayNextVideoBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def PlayPage_StopVideobuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_StopVideoBtn.x(), self.StackedUi.PlayPage_StopVideoBtn.y(), self.StackedUi.PlayPage_StopVideoBtn.width(), self.StackedUi.PlayPage_StopVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_StopVideoBtn.x()-5, self.StackedUi.PlayPage_StopVideoBtn.y()-5, self.StackedUi.PlayPage_StopVideoBtn.width()+10, self.StackedUi.PlayPage_StopVideoBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayPage_StopVideobuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_StopVideoBtn.x(), self.StackedUi.PlayPage_StopVideoBtn.y(), self.StackedUi.PlayPage_StopVideoBtn.width(), self.StackedUi.PlayPage_StopVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_StopVideoBtn.x()+5, self.StackedUi.PlayPage_StopVideoBtn.y()+5, self.StackedUi.PlayPage_StopVideoBtn.width()-10, self.StackedUi.PlayPage_StopVideoBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def PlayListPage_YoutubeLogobuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayListPage_YoutubeLogoBtn.x(), self.StackedUi.PlayListPage_YoutubeLogoBtn.y(), self.StackedUi.PlayListPage_YoutubeLogoBtn.width(), self.StackedUi.PlayListPage_YoutubeLogoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayListPage_YoutubeLogoBtn.x()-5, self.StackedUi.PlayListPage_YoutubeLogoBtn.y()-5, self.StackedUi.PlayListPage_YoutubeLogoBtn.width()+10, self.StackedUi.PlayListPage_YoutubeLogoBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayListPage_YoutubeLogobuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayListPage_YoutubeLogoBtn.x(), self.StackedUi.PlayListPage_YoutubeLogoBtn.y(), self.StackedUi.PlayListPage_YoutubeLogoBtn.width(), self.StackedUi.PlayListPage_YoutubeLogoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayListPage_YoutubeLogoBtn.x()+5, self.StackedUi.PlayListPage_YoutubeLogoBtn.y()+5, self.StackedUi.PlayListPage_YoutubeLogoBtn.width()-10, self.StackedUi.PlayListPage_YoutubeLogoBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def PlayPage_PlayVideobuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_PlayVideoBtn.x(), self.StackedUi.PlayPage_PlayVideoBtn.y(), self.StackedUi.PlayPage_PlayVideoBtn.width(), self.StackedUi.PlayPage_PlayVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_PlayVideoBtn.x()-5, self.StackedUi.PlayPage_PlayVideoBtn.y()-5, self.StackedUi.PlayPage_PlayVideoBtn.width()+10, self.StackedUi.PlayPage_PlayVideoBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayPage_PlayVideobuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_PlayVideoBtn.x(), self.StackedUi.PlayPage_PlayVideoBtn.y(), self.StackedUi.PlayPage_PlayVideoBtn.width(), self.StackedUi.PlayPage_PlayVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_PlayVideoBtn.x()+5, self.StackedUi.PlayPage_PlayVideoBtn.y()+5, self.StackedUi.PlayPage_PlayVideoBtn.width()-10, self.StackedUi.PlayPage_PlayVideoBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def PlayPage_PlayBeforeVideobuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_PlayBeforeVideoBtn.x(), self.StackedUi.PlayPage_PlayBeforeVideoBtn.y(), self.StackedUi.PlayPage_PlayBeforeVideoBtn.width(), self.StackedUi.PlayPage_PlayBeforeVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_PlayBeforeVideoBtn.x()-5, self.StackedUi.PlayPage_PlayBeforeVideoBtn.y()-5, self.StackedUi.PlayPage_PlayBeforeVideoBtn.width()+10, self.StackedUi.PlayPage_PlayBeforeVideoBtn.height()+10)) # 바뀔값
        animation.setDuration(30)
        animation.start()
    def PlayPage_PlayBeforeVideobuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(self.StackedUi.PlayPage_PlayBeforeVideoBtn.x(), self.StackedUi.PlayPage_PlayBeforeVideoBtn.y(), self.StackedUi.PlayPage_PlayBeforeVideoBtn.width(), self.StackedUi.PlayPage_PlayBeforeVideoBtn.height() )) #원래값
        animation.setEndValue(QtCore.QRect(self.StackedUi.PlayPage_PlayBeforeVideoBtn.x()+5, self.StackedUi.PlayPage_PlayBeforeVideoBtn.y()+5, self.StackedUi.PlayPage_PlayBeforeVideoBtn.width()-10, self.StackedUi.PlayPage_PlayBeforeVideoBtn.height()-10)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def MovePlayPagebuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1560, 30, 141, 51)) #원래값
        animation.setEndValue(QtCore.QRect(1555, 25, 151, 61)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def MovePlayPagebuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1560, 30, 141, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1560, 30, 141, 51)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    # def MovePlayPagebuttonEnterEvent(self, event, animation) :
    #     animation.setStartValue(QtCore.QRect(self.StackedUi.MovePlayPageBtn.x(), self.StackedUi.MovePlayPageBtn.y(), self.StackedUi.MovePlayPageBtn.width(), self.StackedUi.MovePlayPageBtn.height() )) #원래값
    #     animation.setEndValue(QtCore.QRect(self.StackedUi.MovePlayPageBtn.x()-5, self.StackedUi.MovePlayPageBtn.y()-5, self.StackedUi.MovePlayPageBtn.width()+10, self.StackedUi.MovePlayPageBtn.height()+10)) # 바뀔값
    #     animation.setDuration(30)
    #     animation.start()

    # def MovePlayPagebuttonleaveEvent(self, event, animation) :
    #     animation.setStartValue(QtCore.QRect(self.StackedUi.MovePlayPageBtn.x(), self.StackedUi.MovePlayPageBtn.y(), self.StackedUi.MovePlayPageBtn.width(), self.StackedUi.MovePlayPageBtn.height() )) #원래값
    #     animation.setEndValue(QtCore.QRect(self.StackedUi.MovePlayPageBtn.x()+5, self.StackedUi.MovePlayPageBtn.y()+5, self.StackedUi.MovePlayPageBtn.width()-10, self.StackedUi.MovePlayPageBtn.height()-10)) # 바뀔값
    #     animation.setDuration(30)
    #     animation.start()

    def MoveSearchPagebuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1420, 30, 121, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1415, 25, 131, 61)) # 바뀔값
        animation.setDuration(30)

        animation.start()

    def MoveSearchPagebuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1420, 30, 121, 51)) #원래값
        animation.setEndValue(QtCore.QRect(1420, 30, 121, 51)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    # def MoveSearchPagebuttonEnterEvent(self, event, animation) :
    #     animation.setStartValue(QtCore.QRect(self.StackedUi.MoveSearchPageBtn.x(), self.StackedUi.MoveSearchPageBtn.y(), self.StackedUi.MoveSearchPageBtn.width(), self.StackedUi.MoveSearchPageBtn.height() )) #원래값
    #     animation.setEndValue(QtCore.QRect(self.StackedUi.MoveSearchPageBtn.x()-5, self.StackedUi.MoveSearchPageBtn.y()-5, self.StackedUi.MoveSearchPageBtn.width()+10, self.StackedUi.MoveSearchPageBtn.height()+10)) # 바뀔값
    #     animation.setDuration(30)
    #     animation.start()

    # def MoveSearchPagebuttonleaveEvent(self, event, animation) :
    #     animation.setStartValue(QtCore.QRect(self.StackedUi.MoveSearchPageBtn.x(), self.StackedUi.MoveSearchPageBtn.y(), self.StackedUi.MoveSearchPageBtn.width(), self.StackedUi.MoveSearchPageBtn.height() )) #원래값
    #     animation.setEndValue(QtCore.QRect(self.StackedUi.MoveSearchPageBtn.x()+5, self.StackedUi.MoveSearchPageBtn.y()+5, self.StackedUi.MoveSearchPageBtn.width()-10, self.StackedUi.MoveSearchPageBtn.height()-10)) # 바뀔값
    #     animation.setDuration(30)
    #     animation.start()

    def MovePlayListPagebuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1250, 30, 151, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1245, 25, 161, 61)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def MovePlayListPagebuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1250, 30, 151, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1250, 30, 151, 51)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    # def MovePlayListPagebuttonEnterEvent(self, event, animation) :
    #     animation.setStartValue(QtCore.QRect(self.StackedUi.MovePlayListPageBtn.x(), self.StackedUi.MovePlayListPageBtn.y(), self.StackedUi.MovePlayListPageBtn.width(), self.StackedUi.MovePlayListPageBtn.height() )) #원래값
    #     animation.setEndValue(QtCore.QRect(self.StackedUi.MovePlayListPageBtn.x()-5, self.StackedUi.MovePlayListPageBtn.y()-5, self.StackedUi.MovePlayListPageBtn.width()+10, self.StackedUi.MovePlayListPageBtn.height()+10)) # 바뀔값
    #     animation.setDuration(30)
    #     animation.start()

    # def MovePlayListPagebuttonleaveEvent(self, event, animation) :
    #     animation.setStartValue(QtCore.QRect(self.StackedUi.MovePlayListPageBtn.x(), self.StackedUi.MovePlayListPageBtn.y(), self.StackedUi.MovePlayListPageBtn.width(), self.StackedUi.MovePlayListPageBtn.height() )) #원래값
    #     animation.setEndValue(QtCore.QRect(self.StackedUi.MovePlayListPageBtn.x()+5, self.StackedUi.MovePlayListPageBtn.y()+5, self.StackedUi.MovePlayListPageBtn.width()-10, self.StackedUi.MovePlayListPageBtn.height()-10)) # 바뀔값
    #     animation.setDuration(30)
    #     animation.start()

    def MinimumModeUi_showEvent(self) :
        self.MinimumModeUi.MinimumUi.show()

    def MinimumModeUi_closeEvent(self) :
        self.MinimumModeUi.MinimumUi.close()

    def StackedUi_showEvent(self) :
        self.StackedUi.StackedUi.show()

    def StackedUi_closeEvent(self) :
        self.StackedUi.StackedUi.close()

    def addplayVideoUi_showEvent(self) :
        self.AddPlayVideoUi.addplaylist.show()

    def addplaylistUi_showEvent(self) :
        self.AddPlayListUi.addplaylist.show()

    def deleteplatlistUi_showEvent(self) :
        self.Deleteplaylist.deleteplaylistUi.Deleteplaylist.show()

        

    def urlEvent(self) :
        url = self.StackedUi.playurl.text()
        
        self.Test.videoplay(url)

    def AddListEvent(self) :
        listname = self.AddPlayListUi.InputPlayList.text()

        db = DB.DataBase()

        db.InputList(listname)