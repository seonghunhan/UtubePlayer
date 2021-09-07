from PyQt5 import QtCore, QtWidgets
class Widget(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super(Widget, self).__init__(parent)
        self.label_content = QtWidgets.QLabel(
            wordWrap=True,
            alignment=QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop
        )
        self.button_view = QtWidgets.QPushButton("View Database")
        self.input_label = QtWidgets.QLabel("Input:") 
        self.lineedit = QtWidgets.QLineEdit()
        self.ask_button = QtWidgets.QPushButton("Ask Question")
        grid_layout = QtWidgets.QGridLayout(self)
        grid_layout.addWidget(self.label_content)
        grid_layout.addWidget(self.button_view, 0, 1, alignment=QtCore.Qt.AlignTop)
        grid_layout.addWidget(self.input_label, 1, 0, 1, 2)
        grid_layout.addWidget(self.lineedit, 2, 0)
        grid_layout.addWidget(self.ask_button, 2, 1)
        grid_layout.setRowStretch(0, 1)
        self.label_content.setText("Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nulla sollicitudin aliquet mauris quis fringilla. Vivamus scelerisque mauris turpis, a imperdiet purus varius eget. Suspendisse pretium est id augue accumsan, vel luctus purus luctus. In hendrerit, turpis ac ultricies volutpat, urna enim hendrerit nisl, a sagittis arcu justo sit amet elit. Aenean bibendum, lacus nec commodo consequat, tortor lectus pulvinar velit, eu ultrices sem felis eget velit. Curabitur id ipsum sit amet tellus euismod mollis. Vivamus et imperdiet ligula. Donec malesuada fermentum felis, at egestas justo ultrices ac. In quis risus ut odio mattis commodo vel sit amet mauris. Vestibulum rutrum ligula tellus, quis faucibus urna imperdiet at. Praesent fermentum condimentum leo. Phasellus quis lacus sapien. Duis viverra sodales aliquet. Sed volutpat non nibh tincidunt blandit. Sed elementum sem at ligula pharetra hendrerit. Donec vel scelerisque mauris. ")
if __name__ == '__main__':
    import sys
    app = QtWidgets.QApplication.instance()
    if app is None:
        app = QtWidgets.QApplication(sys.argv)
    w = Widget()
    w.resize(640, 480)
    w.show()
    sys.exit(app.exec_())