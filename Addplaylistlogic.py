from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import AddplaylistUi
import DB

class Addplaylistlogic(object) :
    
    def __init__(self,StackedUi) :
        
        self.AddplaylistUi = AddplaylistUi.Ui_AddplayUi(StackedUi)

        self.StackedUi = StackedUi

        # self.StackedUi.PlayListPage_AddPlayVideoBtn.clicked.connect(self.playlistshowEvent)

        # self.StackedUi.PlayListPage_AddPlayListBtn.mousePressEvent = lambda event : self.addplaylistEvent(event)
        self.StackedUi.PlayListPage_AddPlayListBtn.clicked.connect(self.addplaylistEvent)





    def addplaylistEvent(self) :
        db = DB.DataBase()
        
        db.InputList()

    def addlist(self) :
        
        listWidget = QtWidgets.QWidget()
        listWidget.setStyleSheet("background-color:blue;")
        

        IconLabel = QtWidgets.QLabel(listWidget)
        IconLabel.setGeometry(QtCore.QRect(11, 10, 360, 270))
        IconLabel.setGeometry(11, 10, 360, 270)
        IconLabel.setAlignment(QtCore.Qt.AlignCenter)
        self.pixmap = QPixmap('File1.PNG')
        IconLabel.setPixmap(self.pixmap) # 이미지 세팅
        IconLabel.resize(self.pixmap.width(), self.pixmap.height())

        self.playlistGUI.widgetList.append([listWidget, thumbnailLabel, listNameLabel]) # [[1,2,3], [1,2,3], [1,2,3]]
        listWidget.setParent(self.playlistGUI.verticalFrame)
        


        

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




