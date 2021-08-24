# importing libraries
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import * 
from PyQt5.QtCore import * 
import sys
  
  
class Window(QMainWindow):
  
    def __init__(self):
        super().__init__()
  
        # setting title
        self.setWindowTitle("Python ")
  
        # setting geometry
        self.setGeometry(100, 100, 500, 400)
  
        # calling method
        self.UiComponents()
  
        # showing all the widgets
        self.show()
  
  
  
    # method for components
    def UiComponents(self):
  
        # creating a QListWidget
        list_widget = QListWidget(self)
  
        # setting geometry to it
        list_widget.setGeometry(50, 70, 150, 100)
  
        # list widget items
        item1 = QListWidgetItem("A")
        item2 = QListWidgetItem("B")
        item3 = QListWidgetItem("C")
        item4 = QListWidgetItem("D")
  
        # adding items to the list widget
        list_widget.addItem(item1)
        list_widget.addItem(item2)
        list_widget.addItem(item3)
        list_widget.addItem(item4)
  
        # scroll bar
        scroll_bar = QScrollBar(self)
  
        # setting style sheet to the scroll bar
        scroll_bar.setStyleSheet("background : lightgreen;")
  
        # setting vertical scroll bar to it
        list_widget.setVerticalScrollBar(scroll_bar)
  
        # creating a label
        label = QLabel("GeesforGeeks", self)
  
        # setting geometry to the label
        label.setGeometry(230, 80, 280, 80)
  
        # making label multi line
        label.setWordWrap(True)
  
  
  
  
# create pyqt5 app
App = QApplication(sys.argv)
  
# create the instance of our Window
window = Window()
  
# start the app
sys.exit(App.exec())