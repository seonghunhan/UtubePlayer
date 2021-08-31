from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMenu, QAction
import sys


class Main(object) :
        def __init__(self) :
            self.setupUi()



            self.MainWindow.show()

        def setupUi(self) :

            self.MainWindow = QtWidgets.QMainWindow()
            self.MainWindow.resize(1700, 1300)
            self.MainWindow.setWindowTitle("YouTube Player")

            self.centralwidget = QtWidgets.QWidget(self.MainWindow)
            self.centralwidget.setGeometry(0, 0, 1700, 1300)

            self.MovePlayPageBtn = QtWidgets.QPushButton(self.centralwidget)
            self.MovePlayPageBtn.setGeometry(QtCore.QRect(500, 500, 141, 51))
            self.MovePlayPageBtn.setText("Test")

            self.MovePlayPageBtn.contextMenuEvent = lambda event : self.test(event)            

        def test(self, event):
            print(event.pos())
            print(self.mapToGlobal(event.pos()))
            menu = QtWidgets.QMenu(self)
            copy_action = menu.addAction("복사하기")
            quit_action = menu.addAction("Quit")
            action = menu.exec_(self.mapToGlobal(event.pos()))
            if action == quit_action:
                qApp.quit()
            elif action == copy_action:
                print("copy...")


if __name__ == "__main__":
    
    app = QtWidgets.QApplication(sys.argv)
    

    
    start = Main()

    sys.exit(app.exec_())








# class Window(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.title = "PyQt5 Context Menu"
#         self.top = 200
#         self.left = 500
#         self.width = 400
#         self.height = 300
#         self.InitWindow()


#     def InitWindow(self):
#         self.setWindowIcon(QtGui.QIcon("icon.png"))
#         self.setWindowTitle(self.title)
#         self.setGeometry(self.left, self.top, self.width, self.height)
#         self.show()

#     def contextMenuEvent(self, event):
#         contextMenu = QMenu(self)
#         newAct = contextMenu.addAction("New")
#         openAct = contextMenu.addAction("Open")
#         quitAct = contextMenu.addAction("Quit")
#         action = contextMenu.exec_(self.mapToGlobal(event.pos()))
#         if action == quitAct:
#             self.close()


# App = QApplication(sys.argv)
# window = Window(