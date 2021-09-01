from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu

import AddplaylistUi
import DB

class Addplaylistlogic(object) :
    
    def __init__(self,widgetList,verticalframe,AddplaylistBtn) :
        
        # self.AddplaylistUi = AddplaylistUi.Ui_AddplayUi(StackedUi)

        # self.StackedUi = StackedUi

        # self.StackedUi.PlayListPage_AddPlayVideoBtn.clicked.connect(self.playlistshowEvent)

        # self.StackedUi.PlayListPage_AddPlayListBtn.mousePressEvent = lambda event : self.addplaylistEvent(event)

        self.WidgetList = widgetList
        self.VerticalFrame = verticalframe
        self.AddplaylistBtn = AddplaylistBtn
        self.playlist_x = 1600   # 플레이목록 프레임사이즈
        self.playlist_y = 800
        self.oneplaylist_x = 400
        self.oneplaylist_y = 400
        db = DB.DataBase()
        self.lists = db.calllist()

        self.AddplaylistBtn.mousePressEvent = lambda event : self.newListEvent(event)

        self.menu = QtWidgets.QMenu()
        self.newListNameAction = QtWidgets.QAction("재생목록 이름 변경", self.menu)
        self.deleteAction = QtWidgets.QAction("재생목록 삭제", self.menu)
        self.menu.addAction(self.newListNameAction)
        self.menu.addAction(self.deleteAction)
        self.menu.addSeparator()



    def newListEvent(self, event):
        db = DB.DataBase()

        index = 0
        listName = "재생목록 " + str(index + 1)

        while not db.listNameCheck(listName):  # not False는 True니깐 True가 될때까지 반복하는것(매번 db체크하면서)
            index += 1
            listName = "재생목록 " + str(index + 1)  # db에서 False가 반환되면 listname을 계속 1씩 늘려주는것

        db.InputList(listName)

        self.lists.clear()
        self.lists = db.calllist()
        
        idx = len(self.lists) - 1
        if idx % 4 == 0:
            self.VerticalFrame.resize(self.playlist_x, self.oneplaylist_y * (idx // 4 + 1))

        self.addlist(idx)

    def addlist(self, idx) :
        
        listWidget = QtWidgets.QWidget()
        listWidget.setStyleSheet("background-color:blue;")
        

        IconLabel = QtWidgets.QLabel(listWidget)
        IconLabel.setGeometry(QtCore.QRect(11, 10, 360, 270))
        IconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QPixmap('File1.PNG')
        size = QtCore.QSize(IconLabel.width(), IconLabel.height())
        IconLabel.setPixmap(self.pixmap.scaled(size, aspectRatioMode=QtCore.Qt.KeepAspectRatio)) # 최종적으로 label에 pixmap을 넣고 
        
  

        listNameLabel = QtWidgets.QLabel(listWidget)
        listNameLabel.setText(self.lists[idx][2]) # 재생목록 이름 설정
        listNameLabel.setGeometry(10, 280, 360, 60)

        self.WidgetList.append([listWidget, IconLabel, listNameLabel]) # [[1,2,3], [1,2,3], [1,2,3]]
        listWidget.setParent(self.VerticalFrame)

        self.location(idx)

        listWidget.show()

        if idx % 4 == 0 :
            self.VerticalFrame.resize(self.playlist_x - 30, self.playlist_y * (idx // 4 + 1) )

    def location(self, listIdx) :
# idx = len(self.lists) - 1
        for idx in range(listIdx, len(self.WidgetList)) :
            row = idx // 4
            column = idx % 4

            self.WidgetList[idx][0].enterEvent = lambda event, index = idx : self.enterWidgetEvent(event, index)
            self.WidgetList[idx][0].leaveEvent = lambda event, index = idx : self.leaveWidgetEvent(event, index)

            for num in range(0, 3):
                self.WidgetList[idx][num].mousePressEvent = lambda event, listIdx = idx, listName = self.lists[idx][2] : self.listClickEvent(event, listIdx, listName)        

            self.WidgetList[idx][0].setGeometry(column * self.oneplaylist_x, row * self.oneplaylist_y, 
                                                self.oneplaylist_x, self.oneplaylist_y)
        

    def listClickEvent(self, event, listIdx, listName) :

        if event.buttons() & QtCore.Qt.RightButton :
            self.deleteAction.triggered.connect(lambda hsh, listIdx = listIdx , listName = listIdx, : self.listdeleteEvent(listIdx, listName))

            self.menu.exec_(event.globalPos())

    def listdeleteEvent(self, listIdx, listName) :
        db = DB.DataBase()
        db.DeleteList(listName)



        


    def enterWidgetEvent(self, event, index):
        self.WidgetList[index][0].setStyleSheet("background-color:red;")

    def leaveWidgetEvent(self, event, index):
        self.WidgetList[index][0].setStyleSheet("background-color:blue;")


    def initList(self): #리스트 초기화시키는것
        for widget in self.WidgetList:
            widget[0].setParent(None)

        self.WidgetList.clear()

        if len(self.lists) % 4 > 0:
            row = len(self.lists) // 4 + 1
        else:
            row = len(self.lists) // 4

        self.VerticalFrame.resize(self.playlist_x, self.oneplaylist_y * row)

        for index in range(0, len(self.lists)):
            self.addlist(index)
            
    # def listDeleteEvent(self) :
    #     self.deleteAction.tr


    

        

        # self.AddplaylistUi.CompleteAdd.clicked.connect(self.AddListEvent)

        # self.StackedUi.List1.show()
        # self.StackedUi.ListName1.show()

        # self.list1 = self.StackedUi.List1
        # self.list1name = self.StackedUi.ListName1

        # self.showlist1 = Addplaylistlogic.playlist1showEvent(self)





    # def AddListEvent(self) :
    #     listname = self.AddplaylistUi.InputPlayList.text()

    #     db = DB.DataBase()

    #     db.InputList(listname)

    # def playlistshowEvent(self) :
    #     self.AddplaylistUi.List1.show()
    #     self.AddplaylistUi.ListName1.show()
    # def playlist1showEvent(self) :

    #     db = DB.DataBase()

    #     db.cur.execute("SELECT * FROM playerdata")
    #     data = db.cur.fetchall()

    #     # recvlist = data[1][2]

    #     if data[1][2] == None :
      
    #         return False
    #     else :
    #         self.StackedUi.ListName1.setText(data[1][2])
    #         self.show()

    # def show(self) :
    #     self.list1.show()
    #     self.list1name.show()




