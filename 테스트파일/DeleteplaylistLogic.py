from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QPixmap

import DeleteplaylistUi
import DB

class DeleteplaylistLogic(object) :
    
    def __init__(self) :
        
        self.deleteplaylistUi = DeleteplaylistUi.Ui_Deleteplaylist()
        

        self.deleteplaylistUi.Completedelete.clicked.connect(self.DB_Delete_Event)

    def DB_Delete_Event(self) :
        listname = self.deleteplaylistUi.InputPlayList.text()

        db = DB.DataBase()

        db.DeleteList(listname)


    