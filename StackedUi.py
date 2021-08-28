from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
import sys
import vlc
import pafy





class Ui_YouTubePlayer(object):
    def __init__(self,asd) :
        self.StackedUi = QtWidgets.QMainWindow()
        self.Test = asd
        self.playlist_x = 1500
        self.playlist_y = 800
        self.setupUi()



        self.stackedWidget.setCurrentWidget(self.PlayListPage)
        
 

        self.StackedUi.show()

        self.playlistpage1Ui()

        self.playlistpage1ui = Ui_YouTubePlayer.playlistpage1Ui(self)

        self.widgetList = []

        


    def showPlayListPage(self) : 
        self.stackedWidget.setCurrentWidget(self.PlayListPage)

    def showPlayPage(self) : 
        self.stackedWidget.setCurrentWidget(self.PlayPage)

    def showSearchPage(self) : 
        self.stackedWidget.setCurrentWidget(self.SearchPage)
        

    def playlistpage1Ui(self) :
        self.List1 = QtWidgets.QLabel(self.PlayListPage)
        self.List1.setGeometry(QtCore.QRect(150,200, 200, 200))
        self.List1.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List1.setPixmap(self.pixmap) # 이미지 세팅
        self.List1.resize(self.pixmap.width(), self.pixmap.height())



        self.ListName1 = QtWidgets.QLabel("고고고고", self.PlayListPage)
        self.ListName1.setGeometry(QtCore.QRect(200,350, 101, 18))
        self.ListName1.setObjectName("ListName1")

        # self.List1.show()
        # self.ListName1.show()


    def setupUi(self):
        self.StackedUi.setObjectName("YouTubePlayer")
        self.StackedUi.resize(1740, 1308)

        self.centralwidget = QtWidgets.QWidget(self.StackedUi)
        self.centralwidget.setObjectName("centralwidget")
       
        self.MoveSearchPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MoveSearchPageBtn.setGeometry(QtCore.QRect(1420, 30, 121, 51))
        self.MoveSearchPageBtn.setObjectName("MoveSearchPageBtn")

        self.MovePlayPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MovePlayPageBtn.setGeometry(QtCore.QRect(1560, 30, 141, 51))
        self.MovePlayPageBtn.setObjectName("MovePlayPageBtn")

        self.MovePlayListPageBtn = QtWidgets.QPushButton(self.centralwidget)
        self.MovePlayListPageBtn.setGeometry(QtCore.QRect(1250, 30, 151, 51))
        self.MovePlayListPageBtn.setObjectName("MovePlayListBtn")
        self.StackedUi.setCentralWidget(self.centralwidget)

        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(10, 90, 1711, 1121))
        self.stackedWidget.setObjectName("stackedWidget")

        self.PlayListPage = QtWidgets.QWidget()
        self.PlayListPage.setObjectName("PlayListPage")

        self.PlayListPage_background = QtWidgets.QWidget(self.PlayListPage)
        self.PlayListPage_background.setGeometry(QtCore.QRect(60, 110, self.playlist_x, self.playlist_y))
        self.PlayListPage_background.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")
        self.scrollArea = QtWidgets.QScrollArea(self.PlayListPage_background)
        self.scrollArea.setGeometry(0, 0, self.playlist_x, self.playlist_y)

        self.verticalFrame = QtWidgets.QWidget(self.scrollArea)
        self.verticalFrame.setGeometry(0, 0, self.playlist_x -30, 10)
        self.scrollArea.setWidget(self.verticalFrame)
        self.verticalFrame.setStyleSheet("border : 1px solid red")




        # self.PlayListPage_YoutubeLogoBtn = QtWidgets.QPushButton(self.PlayListPage)
        # self.PlayListPage_YoutubeLogoBtn.setGeometry(QtCore.QRect(70, 1030, 112, 34))
        # self.PlayListPage_YoutubeLogoBtn.setObjectName("PlayListPage_YoutubeLogoBtn")
        
        self.PlayListPage_YoutubeLogoBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_YoutubeLogoBtn.setGeometry(QtCore.QRect(70, 1030, 120, 40))
        self.PlayListPage_YoutubeLogoBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayListPage_YoutubeLogoBtn.setIcon(icon)
        self.PlayListPage_YoutubeLogoBtn.setIconSize(QtCore.QSize(120, 40))
        self.PlayListPage_YoutubeLogoBtn.setObjectName("PlayListPage_YoutubeLogoBtn")

        

        self.PlayListPage_AddPlayVideoBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_AddPlayVideoBtn.setGeometry(QtCore.QRect(1520, 1040, 161, 41))
        self.PlayListPage_AddPlayVideoBtn.setObjectName("PlayListPage_AddPlayListBtn")
        self.stackedWidget.addWidget(self.PlayListPage)


        self.PlayListPage_AddPlayListBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_AddPlayListBtn.setGeometry(QtCore.QRect(1320, 1040, 161, 41))
        self.PlayListPage_AddPlayListBtn.setObjectName("PlayListPage_AddPlayListBtn")
        self.stackedWidget.addWidget(self.PlayListPage)

        self.PlayListPage_DeletePlayListBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_DeletePlayListBtn.setGeometry(QtCore.QRect(1120, 1040, 161, 41))
        self.PlayListPage_DeletePlayListBtn.setObjectName("PlayListPage_AddPlayListBtn")
        self.stackedWidget.addWidget(self.PlayListPage)


        self.PlayPage = QtWidgets.QWidget()
        self.PlayPage.setObjectName("PlayPage")

        self.PlayListPage_background1 = QtWidgets.QLineEdit(self.PlayPage)
        self.PlayListPage_background1.setGeometry(QtCore.QRect(1200, 80, 460, 1000))
        self.PlayListPage_background1.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")
        self.PlayListPage_background1.setObjectName("lineEdit")

        self.PlayListPage_background2 = QtWidgets.QLineEdit(self.PlayPage)
        self.PlayListPage_background2.setGeometry(QtCore.QRect(10, 200, 1060, 800))
        self.PlayListPage_background2.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")
        self.PlayListPage_background2.setObjectName("lineEdit")



        # self.PlayPage_TitleScrollArea = QtWidgets.QScrollArea(self.PlayPage)
        # self.PlayPage_TitleScrollArea.setGeometry(QtCore.QRect(10, 80, 500, 91))
        # self.PlayPage_TitleScrollArea.setWidgetResizable(True)
        # self.PlayPage_TitleScrollArea.setObjectName("PlayPage_TitleScrollArea")
        # self.PlayPage_TitleScrollArea.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        

        # self.PlayPage_ScrollAreaWidgetContents = QtWidgets.QWidget()
        # self.PlayPage_ScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 510, 100))
        # self.PlayPage_ScrollAreaWidgetContents.setObjectName("PlayPageScrollAreaWidgetContents")



        # self.PlayPage_TitleLabel = QtWidgets.QLabel(self.PlayPage_TitleScrollArea)
        # self.PlayPage_TitleLabel.setGeometry(QtCore.QRect(10, 10, 1200, 71))
        # self.PlayPage_TitleLabel.setObjectName("PlayPage_TitleLabel")

        # 해일씨 코드
        # self.scroll = QtWidgets.QScrollArea(self.PlayPage)
        # self.scroll.setGeometry(30 , 110, 500, 90)

        # self.PlayPage_TitleLable = QtWidgets.QLabel("ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ", self.scroll)
        # self.PlayPage_TitleLable.setGeometry(0, 0, 800, 90) 
        # self.scroll.setWidget(self.PlayPage_TitleLable)   


        self.scroll = QtWidgets.QScrollArea(self.PlayPage)
        self.scroll.setGeometry(10 , 100, 1050, 90)
        self.PlayPage_TitleLabel = QtWidgets.QLabel("ㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇdd",self.scroll)
        self.PlayPage_TitleLabel.setGeometry(10, 100, 2000, 70)
        self.scroll.setWidget(self.PlayPage_TitleLabel)



        self.PlayPage_PlayListNameLabel = QtWidgets.QLabel(self.PlayPage)
        self.PlayPage_PlayListNameLabel.setGeometry(QtCore.QRect(1250, 80, 460, 31))
        self.PlayPage_PlayListNameLabel.setObjectName("PlayPage_PlayListNameLabel")

        # self.PlayPage_PlayBeforeVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        # self.PlayPage_PlayBeforeVideoBtn.setGeometry(QtCore.QRect(1100, 80, 112, 34))
        # self.PlayPage_PlayBeforeVideoBtn.setObjectName("PlayPage_PlayBeforeVideoBtn")

        self.PlayPage_PlayBeforeVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_PlayBeforeVideoBtn.setGeometry(QtCore.QRect(1100, 80, 50, 50))
        self.PlayPage_PlayBeforeVideoBtn.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("Before.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_PlayBeforeVideoBtn.setIcon(icon)
        self.PlayPage_PlayBeforeVideoBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayPage_PlayBeforeVideoBtn.setObjectName("PlayPage_PlayBeforeVideoBtn")


        # self.PlayPage_PlayVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        # self.PlayPage_PlayVideoBtn.setGeometry(QtCore.QRect(1100, 140, 112, 34))
        # self.PlayPage_PlayVideoBtn.setObjectName("PlayPage_PlayVideoBtn")

        self.PlayPage_PlayVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_PlayVideoBtn.setGeometry(QtCore.QRect(1100, 140, 51, 51))
        self.PlayPage_PlayVideoBtn.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("Play.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_PlayVideoBtn.setIcon(icon1)
        self.PlayPage_PlayVideoBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayPage_PlayVideoBtn.setObjectName("PlayPage_PlayVideoBtn")


        # self.PlayPage_StopVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        # self.PlayPage_StopVideoBtn.setGeometry(QtCore.QRect(1100, 200, 112, 34))
        # self.PlayPage_StopVideoBtn.setObjectName("PlayPage_StopVideoBtn")

        self.PlayPage_StopVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_StopVideoBtn.setGeometry(QtCore.QRect(1100, 200, 51, 51))
        self.PlayPage_StopVideoBtn.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("Stop.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_StopVideoBtn.setIcon(icon2)
        self.PlayPage_StopVideoBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayPage_StopVideoBtn.setObjectName("PlayPage_StopVideoBtn")


        # self.PlayPage_PlayNextVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        # self.PlayPage_PlayNextVideoBtn.setGeometry(QtCore.QRect(1100, 250, 112, 34))
        # self.PlayPage_PlayNextVideoBtn.setObjectName("PlayPage_PlayNextVideoBtn")

        self.PlayPage_PlayNextVideoBtn = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_PlayNextVideoBtn.setGeometry(QtCore.QRect(1100, 260, 51, 51))
        self.PlayPage_PlayNextVideoBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Next.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_PlayNextVideoBtn.setIcon(icon3)
        self.PlayPage_PlayNextVideoBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayPage_PlayNextVideoBtn.setObjectName("PlayPage_PlayNextVideoBtn")

        # self.PlayPage_ShupplePlayListBtn = QtWidgets.QPushButton(self.PlayPage)
        # self.PlayPage_ShupplePlayListBtn.setGeometry(QtCore.QRect(1100, 300, 112, 34))
        # self.PlayPage_ShupplePlayListBtn.setObjectName("PlayPage_ShupplePlayListBtn")

        self.PlayPage_ShupplePlayListBtn = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_ShupplePlayListBtn.setGeometry(QtCore.QRect(1100, 320, 51, 51))
        self.PlayPage_ShupplePlayListBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("Shupple.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_ShupplePlayListBtn.setIcon(icon3)
        self.PlayPage_ShupplePlayListBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayPage_ShupplePlayListBtn.setObjectName("PlayPage_PlayNextVideoBtn")

        # self.PlayPage_OnePlayBtn = QtWidgets.QPushButton(self.PlayPage)
        # self.PlayPage_OnePlayBtn.setGeometry(QtCore.QRect(1100, 350, 112, 34))
        # self.PlayPage_OnePlayBtn.setObjectName("PlayPage_OnePlayBtn")

        self.PlayPage_OnePlayBtn = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_OnePlayBtn.setGeometry(QtCore.QRect(1100, 380, 51, 51))
        self.PlayPage_OnePlayBtn.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("OnePlay.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.PlayPage_OnePlayBtn.setIcon(icon3)
        self.PlayPage_OnePlayBtn.setIconSize(QtCore.QSize(55, 55))
        self.PlayPage_OnePlayBtn.setObjectName("PlayPage_OnePlayBtn")        

        self.PlayPage_MinimumButton = QtWidgets.QPushButton(self.PlayPage)
        self.PlayPage_MinimumButton.setGeometry(QtCore.QRect(1550, 20, 151, 41))
        self.PlayPage_MinimumButton.setObjectName("pushButton")        
        self.stackedWidget.addWidget(self.PlayPage)

        # self.mediaplayer = QtWidgets.QLabel(self.PlayPage)
        # self.mediaplayer.setGeometry(QtCore.QRect(400, 450, 101, 18))
        # self.mediaplayer.setObjectName("playvideo")
        # ----------------------------------------------------------------------------------
  
        # self.videoframe = QtWidgets.QFrame(self.PlayPage)
        # self.videoframe.setGeometry(QtCore.QRect(400,450,100,20))
        # self.videoframe.setObjectName("playvideo")

        # if sys.platform.startswith("linux"):  # for Linux using the X Server
        #     self.Test.mediaplayer.set_xwindow(self.videoframe.winId())
        # elif sys.platform == "win32":  # for Windows
        #     self.Test.mediaplayer.set_hwnd(self.videoframe.winId())
        # elif sys.platform == "darwin":  # for MacOS
        #     self.Test.mediaplayer.set_nsobject(self.videoframe.winId())

        # 여기질문하기!!! Test1페이지를 로직통해서 임포트했는데 미디어플레이어변수를 인식을 못함

        
        

        self.videoframe = QtWidgets.QFrame(self.PlayPage)
        self.videoframe.setGeometry(QtCore.QRect(40,220,1000,750))

        if sys.platform.startswith("linux"):  # for Linux using the X Server
            self.Test.medaiplayer.set_xwindow(self.videoframe.winId())
        elif sys.platform == "win32":  # for Windows
            self.Test.mediaplayer.set_hwnd(self.videoframe.winId())
        elif sys.platform == "darwin":  # for MacOS
            self.mediaplayer.set_nsobject(self.videoframe.winId())







        



        self.playurl = QtWidgets.QLineEdit(self.PlayPage)
        self.playurl.setGeometry(QtCore.QRect(30, 20, 1371, 31))
        self.playurl.setObjectName("playurl_Bar")


        self.urlgogobtn = QtWidgets.QPushButton(self.PlayPage)
        self.urlgogobtn.setGeometry(QtCore.QRect(200, 200, 50, 50))
        self.urlgogobtn.setText("urlㄱㄱ")











        self.SearchPage = QtWidgets.QWidget()
        self.SearchPage.setObjectName("SearchPage")

        self.SearchPage_background = QtWidgets.QLineEdit(self.SearchPage)
        self.SearchPage_background.setGeometry(QtCore.QRect(30, 130, 1371, 800))
        self.SearchPage_background.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")
        self.SearchPage_background.setObjectName("lineEdit")

        self.SearchPage_SearchBar = QtWidgets.QLineEdit(self.SearchPage)
        self.SearchPage_SearchBar.setGeometry(QtCore.QRect(30, 80, 1371, 31))
        self.SearchPage_SearchBar.setObjectName("SearchPage_SearchBar")

        self.SearchPage_SearchBtn = QtWidgets.QPushButton(self.SearchPage)
        self.SearchPage_SearchBtn.setGeometry(QtCore.QRect(1410, 80, 171, 34))
        self.SearchPage_SearchBtn.setObjectName("SearchPage_SearchBtn")        
        self.stackedWidget.addWidget(self.SearchPage)
        

        self.retranslateUi()
        self.stackedWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(self.StackedUi)

    def retranslateUi(self):
        _translate = QtCore.QCoreApplication.translate
        self.StackedUi.setWindowTitle(_translate("YouTubePlayer", "MainWindow"))
        self.MoveSearchPageBtn.setText(_translate("YouTubePlayer", "검색"))
        self.MovePlayPageBtn.setText(_translate("YouTubePlayer", "재생중인 영상"))
        # self.PlayListPage_background.setText(_translate("YouTubePlayer", ""))
        # self.List1.setText(_translate("YouTubePlayer", ""))
        # self.List2.setText(_translate("YouTubePlayer", ""))
        # self.List3.setText(_translate("YouTubePlayer", ""))
        # self.List4.setText(_translate("YouTubePlayer", ""))
        # self.List5.setText(_translate("YouTubePlayer", ""))
        # self.List6.setText(_translate("YouTubePlayer", ""))
        # self.List7.setText(_translate("YouTubePlayer", ""))
        # self.List8.setText(_translate("YouTubePlayer", ""))
        # self.List9.setText(_translate("YouTubePlayer", ""))
        # self.List10.setText(_translate("YouTubePlayer", ""))
        # self.ListName1.setText(_translate("YouTubePlayer", "ListName1"))
        # self.ListName2.setText(_translate("YouTubePlayer", "ListName2"))
        # self.ListName3.setText(_translate("YouTubePlayer", "ListName3"))
        # self.ListName4.setText(_translate("YouTubePlayer", "ListName4"))
        # self.ListName5.setText(_translate("YouTubePlayer", "ListName5"))
        # self.ListName6.setText(_translate("YouTubePlayer", "ListName6"))
        # self.ListName7.setText(_translate("YouTubePlayer", "ListName7"))
        # self.ListName8.setText(_translate("YouTubePlayer", "ListName8"))
        # self.ListName9.setText(_translate("YouTubePlayer", "ListName9"))
        # self.ListName10.setText(_translate("YouTubePlayer", "ListName10"))
        self.PlayListPage_YoutubeLogoBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayListPage_AddPlayVideoBtn.setText(_translate("YouTubePlayer", "재생영상 추가"))
        self.PlayListPage_AddPlayListBtn.setText(_translate("YouTubePlayer", "재생목록 추가"))
        self.PlayListPage_DeletePlayListBtn.setText(_translate("YouTubePlayer", "재생목록 제거"))
        #self.PlayPage_TitleLabel.setText(_translate("YouTubePlayer", "PlayPageTitleLabelㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇㅇ"))
        self.PlayPage_PlayListNameLabel.setText(_translate("YouTubePlayer", "PlayPagePlayListNameLabel"))
        self.PlayPage_PlayBeforeVideoBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayPage_PlayVideoBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayPage_StopVideoBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayPage_PlayNextVideoBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayPage_ShupplePlayListBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayPage_OnePlayBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayPage_MinimumButton.setText(_translate("YouTubePlayer", "최소화 기능"))
        # self.videoframe.setText(_translate("YouTubePlayer", "비디오재생"))
        self.SearchPage_SearchBtn.setText(_translate("YouTubePlayer", "검색"))
        self.SearchPage_background.setText(_translate("YouTubePlayer", ""))
        self.MovePlayListPageBtn.setText(_translate("YouTubePlayer", "PlayList"))



    


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
    
#     ui = Ui_YouTubePlayer()

#     sys.exit(app.exec_())