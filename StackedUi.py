from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap, QImage   
import sys





class Ui_YouTubePlayer(object):
    def __init__(self,Test) :
        self.StackedUi = QtWidgets.QMainWindow()
        self.Test = Test
        self.setupUi()

        self.stackedWidget.setCurrentWidget(self.PlayListPage)
        
 

        self.StackedUi.show()


    def showPlayListPage(self) : 
        self.stackedWidget.setCurrentWidget(self.PlayListPage)

    def showPlayPage(self) : 
        self.stackedWidget.setCurrentWidget(self.PlayPage)

    def showSearchPage(self) : 
        self.stackedWidget.setCurrentWidget(self.SearchPage)
        

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

        self.PlayListPage_background = QtWidgets.QLineEdit(self.PlayListPage)
        self.PlayListPage_background.setGeometry(QtCore.QRect(60, 110, 1500, 800))
        self.PlayListPage_background.setStyleSheet("background-color:rgb(188, 188, 188);\n"
                                                "border-radius: 10px ;\n"
                                                "border-style: solid;\n"
                                                "border-width: 1px;\n"
                                                "border-color: rgb(7, 7, 7)\n"
                                                "")
        self.PlayListPage_background.setObjectName("lineEdit")


        self.List1 = QtWidgets.QLabel(self.PlayListPage)
        self.List1.setGeometry(QtCore.QRect(150,200, 200, 200))
        self.List1.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List1.setPixmap(self.pixmap) # 이미지 세팅
        self.List1.resize(self.pixmap.width(), self.pixmap.height())



        self.List2 = QtWidgets.QLabel(self.PlayListPage)
        self.List2.setGeometry(QtCore.QRect(420,200, 200, 200))
        self.List2.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List2.setPixmap(self.pixmap) # 이미지 세팅
        self.List2.resize(self.pixmap.width(), self.pixmap.height())

        self.List3 = QtWidgets.QLabel(self.PlayListPage)
        self.List3.setGeometry(QtCore.QRect(690,200, 200, 200))
        self.List3.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List3.setPixmap(self.pixmap) # 이미지 세팅
        self.List3.resize(self.pixmap.width(), self.pixmap.height())

        self.List4 = QtWidgets.QLabel(self.PlayListPage)
        self.List4.setGeometry(QtCore.QRect(960,200, 200, 200))
        self.List4.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List4.setPixmap(self.pixmap) # 이미지 세팅
        self.List4.resize(self.pixmap.width(), self.pixmap.height())

        self.List5 = QtWidgets.QLabel(self.PlayListPage)
        self.List5.setGeometry(QtCore.QRect(1230,200, 200, 200))
        self.List5.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List5.setPixmap(self.pixmap) # 이미지 세팅
        self.List5.resize(self.pixmap.width(), self.pixmap.height())

        self.List6 = QtWidgets.QLabel(self.PlayListPage)
        self.List6.setGeometry(QtCore.QRect(150,500, 200, 200))
        self.List6.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List6.setPixmap(self.pixmap) # 이미지 세팅
        self.List6.resize(self.pixmap.width(), self.pixmap.height())

        self.List7 = QtWidgets.QLabel(self.PlayListPage)
        self.List7.setGeometry(QtCore.QRect(420,500, 200, 200))
        self.List7.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List7.setPixmap(self.pixmap) # 이미지 세팅
        self.List7.resize(self.pixmap.width(), self.pixmap.height())

        self.List8 = QtWidgets.QLabel(self.PlayListPage)
        self.List8.setGeometry(QtCore.QRect(690,500, 200, 200))
        self.List8.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List8.setPixmap(self.pixmap) # 이미지 세팅
        self.List8.resize(self.pixmap.width(), self.pixmap.height())

        self.List9 = QtWidgets.QLabel(self.PlayListPage)
        self.List9.setGeometry(QtCore.QRect(960,500, 200, 200))
        self.List9.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List9.setPixmap(self.pixmap) # 이미지 세팅
        self.List9.resize(self.pixmap.width(), self.pixmap.height())

        self.List10 = QtWidgets.QLabel(self.PlayListPage)
        self.List10.setGeometry(QtCore.QRect(1230,500, 200, 200))
        self.List10.setObjectName("List1")
        self.pixmap = QPixmap('File1.PNG')
        self.List10.setPixmap(self.pixmap) # 이미지 세팅
        self.List10.resize(self.pixmap.width(), self.pixmap.height())

        self.ListName1 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName1.setGeometry(QtCore.QRect(200,350, 101, 18))
        self.ListName1.setObjectName("ListName1")

        self.ListName2 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName2.setGeometry(QtCore.QRect(470, 350, 101, 18))
        self.ListName2.setObjectName("ListName2")

        self.ListName3 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName3.setGeometry(QtCore.QRect(740, 350, 101, 18))
        self.ListName3.setObjectName("ListName3")

        self.ListName4 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName4.setGeometry(QtCore.QRect(1010, 350, 101, 18))
        self.ListName4.setObjectName("ListName4")

        self.ListName5 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName5.setGeometry(QtCore.QRect(1280, 350, 101, 18))
        self.ListName5.setObjectName("ListName5")

        self.ListName6 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName6.setGeometry(QtCore.QRect(200, 650, 101, 18))
        self.ListName6.setObjectName("ListName6")

        self.ListName7 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName7.setGeometry(QtCore.QRect(470, 650, 101, 18))
        self.ListName7.setObjectName("ListName7")

        self.ListName8 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName8.setGeometry(QtCore.QRect(740, 650, 101, 18))
        self.ListName8.setObjectName("ListName8")

        self.ListName9 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName9.setGeometry(QtCore.QRect(1010, 650, 101, 18))
        self.ListName9.setObjectName("ListName9")

        self.ListName10 = QtWidgets.QLabel(self.PlayListPage)
        self.ListName10.setGeometry(QtCore.QRect(1280, 650, 101, 18))
        self.ListName10.setObjectName("ListName10")

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

        

        self.PlayListPage_AddPlayListBtn = QtWidgets.QPushButton(self.PlayListPage)
        self.PlayListPage_AddPlayListBtn.setGeometry(QtCore.QRect(1520, 1040, 161, 41))
        self.PlayListPage_AddPlayListBtn.setObjectName("PlayListPage_AddPlayListBtn")
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

        self.PlayPage_TitleScrollArea = QtWidgets.QScrollArea(self.PlayPage)
        self.PlayPage_TitleScrollArea.setGeometry(QtCore.QRect(10, 80, 1060, 91))
        self.PlayPage_TitleScrollArea.setWidgetResizable(True)
        self.PlayPage_TitleScrollArea.setObjectName("PlayPage_TitleScrollArea")

        self.PlayPage_ScrollAreaWidgetContents = QtWidgets.QWidget()
        self.PlayPage_ScrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 1059, 89))
        self.PlayPage_ScrollAreaWidgetContents.setObjectName("PlayPageScrollAreaWidgetContents")

        self.PlayPage_TitleLabel = QtWidgets.QLabel(self.PlayPage_ScrollAreaWidgetContents)
        self.PlayPage_TitleLabel.setGeometry(QtCore.QRect(10, 10, 1031, 71))
        self.PlayPage_TitleLabel.setObjectName("PlayPage_TitleLabel")

        self.PlayPage_TitleScrollArea.setWidget(self.PlayPage_ScrollAreaWidgetContents)
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

  
        self.videoframe = QtWidgets.QFrame(self.PlayPage)
        self.videoframe.setGeometry(QtCore.QRect(400,450,100,20))
        self.videoframe.setObjectName("playvideo")

        # if sys.platform.startswith("linux"):  # for Linux using the X Server
        #     self.Test.mediaplayer.set_xwindow(self.videoframe.winId())
        # elif sys.platform == "win32":  # for Windows
        #     self.Test.mediaplayer.set_hwnd(self.videoframe.winId())
        # elif sys.platform == "darwin":  # for MacOS
        #     self.Test.mediaplayer.set_nsobject(self.videoframe.winId())

        # 여기질문하기!!! Test1페이지를 로직통해서 임포트했는데 미디어플레이어변수를 인식을 못함




        



        self.playurl = QtWidgets.QLineEdit(self.PlayPage)
        self.playurl.setGeometry(QtCore.QRect(30, 80, 1371, 31))
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
        self.PlayListPage_background.setText(_translate("YouTubePlayer", ""))
        self.List1.setText(_translate("YouTubePlayer", ""))
        self.List2.setText(_translate("YouTubePlayer", ""))
        self.List3.setText(_translate("YouTubePlayer", ""))
        self.List4.setText(_translate("YouTubePlayer", ""))
        self.List5.setText(_translate("YouTubePlayer", ""))
        self.List6.setText(_translate("YouTubePlayer", ""))
        self.List7.setText(_translate("YouTubePlayer", ""))
        self.List8.setText(_translate("YouTubePlayer", ""))
        self.List9.setText(_translate("YouTubePlayer", ""))
        self.List10.setText(_translate("YouTubePlayer", ""))
        self.ListName1.setText(_translate("YouTubePlayer", "ListName1"))
        self.ListName2.setText(_translate("YouTubePlayer", "ListName2"))
        self.ListName3.setText(_translate("YouTubePlayer", "ListName3"))
        self.ListName4.setText(_translate("YouTubePlayer", "ListName4"))
        self.ListName5.setText(_translate("YouTubePlayer", "ListName5"))
        self.ListName6.setText(_translate("YouTubePlayer", "ListName6"))
        self.ListName7.setText(_translate("YouTubePlayer", "ListName7"))
        self.ListName8.setText(_translate("YouTubePlayer", "ListName8"))
        self.ListName9.setText(_translate("YouTubePlayer", "ListName9"))
        self.ListName10.setText(_translate("YouTubePlayer", "ListName10"))
        self.PlayListPage_YoutubeLogoBtn.setText(_translate("YouTubePlayer", ""))
        self.PlayListPage_AddPlayListBtn.setText(_translate("YouTubePlayer", "재생목록 추가"))
        self.PlayPage_TitleLabel.setText(_translate("YouTubePlayer", "PlayPageTitleLabel"))
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