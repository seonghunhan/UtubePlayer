
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import PlayVideoPage
import Playlistpage
import MainUi


class Main() :

    def __init__(self) :

        self.MainUi = MainUi.MainUi()
        self.PlaylistPage = Playlistpage.PlayListPage()
        self.beclicked_listidx = self.PlaylistPage.beclickedlistidx
        self.MainWindow = self.MainUi.MainWindow

         # 셋커런트를 저거로해줘도 우선 addWIdget을 해줘야한다
        self.MainUi.stacked.addWidget(self.PlaylistPage.PlaylistUi.PlayListPage)
        self.MainUi.stacked.setCurrentWidget(self.PlaylistPage.PlaylistUi.PlayListPage)

        self.MainUi.MovePlayPageBtn.mousePressEvent = lambda event : self.PlayVideoPageMoveEvent(event)
        self.MainUi.MovePlayListPageBtn.mousePressEvent = lambda event : self.PlaylistPageMoveEvent(event)

        ani = QtCore.QPropertyAnimation(self.MainUi.MovePlayPageBtn, b"geometry")
        self.MainUi.MovePlayPageBtn.enterEvent = lambda event, animation = ani , : self.MovePlayPagebuttonEnterEvent(event, animation)
        self.MainUi.MovePlayPageBtn.leaveEvent = lambda event, animation = ani , : self.MovePlayPagebuttonleaveEvent(event, animation)

        ani1 = QtCore.QPropertyAnimation(self.MainUi.MovePlayListPageBtn, b"geometry")
        self.MainUi.MovePlayListPageBtn.enterEvent = lambda event, animation = ani1 , : self.MovePlayListPagebuttonEnterEvent(event, animation)
        self.MainUi.MovePlayListPageBtn.leaveEvent = lambda event, animation = ani1 , : self.MovePlayListPagebuttonleaveEvent(event, animation)
    
        self.PlaylistPage.Addplaylistlogic.initList() #프로그램 재시작할경우 리스트리셋

        # self.PlaylistPage.widgetList[self.beclicked_listidx[0]][0].mousePressEvent = lambda event : self.PlayVideoPageMoveEvent(event)
        # self.PlaylistPage.widgetList[1][0].mousePressEvent = lambda event : self.PlayVideoPageMoveEvent(event)


    def PlayVideoPageMoveEvent(self, event) : # PlayVideoPage로 이동

        if event.buttons() & QtCore.Qt.LeftButton:
            self.PlayVideoPage = PlayVideoPage.PlayVideoPage(self.MainWindow,self.beclicked_listidx) #여기서 객체선언해야 처음부터 실행되지않음(메모리효율관련)
            self.MainUi.stacked.addWidget(self.PlayVideoPage.PlayVideoPageUi.PlayVideoPage)
            self.MainUi.stacked.setCurrentWidget(self.PlayVideoPage.PlayVideoPageUi.PlayVideoPage)
            self.MainUi.stacked.removeWidget(self.PlaylistPage.PlaylistUi.PlayListPage)
            print(self.MainUi.stacked.count()) # 실제로 위젯이 1개만 실행되는지 확인


    def PlaylistPageMoveEvent(self, event) : # PlaylistPage로 이동

        if event.buttons() & QtCore.Qt.LeftButton : # and self.MainUi.stacked.count() == 2 : # &은 비트연산자비교 ex) 0001 = 0001인지 비교
            self.MainUi.stacked.addWidget(self.PlaylistPage.PlaylistUi.PlayListPage)
            self.MainUi.stacked.setCurrentWidget(self.PlaylistPage.PlaylistUi.PlayListPage)
            self.MainUi.stacked.removeWidget(self.PlayVideoPage.PlayVideoPageUi.PlayVideoPage)
            print(self.MainUi.stacked.count())

    def MovePlayPagebuttonEnterEvent(self, event, animation) : #버튼들 확대/축소 이벤트
        animation.setStartValue(QtCore.QRect(1560, 30, 141, 51)) #원래값
        animation.setEndValue(QtCore.QRect(1555, 25, 151, 61)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def MovePlayPagebuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1560, 30, 141, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1560, 30, 141, 51)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def MovePlayListPagebuttonEnterEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1390, 30, 151, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1385, 25, 161, 61)) # 바뀔값
        animation.setDuration(30)
        animation.start()

    def MovePlayListPagebuttonleaveEvent(self, event, animation) :
        animation.setStartValue(QtCore.QRect(1390, 30, 151, 51 )) #원래값
        animation.setEndValue(QtCore.QRect(1390, 30, 151, 51)) # 바뀔값
        animation.setDuration(30)
        animation.start()






if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    

    
    start = Main()

    sys.exit(app.exec_())