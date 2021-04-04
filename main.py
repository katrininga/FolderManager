import sys

from PySide6 import QtWidgets, QtCore, QtGui
from PySide6.QtWidgets import QApplication


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        #set central widget and layout
        self.setWindowTitle("Katrins Amazing Folder Generator")
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)
        self.lineEdit = QtWidgets.QLineEdit()


        self.file_path()
        self.new_folder()
        self.new_folder()
        self.new_folder()
        self.create_files()


    def new_folder(self):
        """Create the display."""
        self.display = QtWidgets.QLineEdit()
        self.display.setFixedHeight(20)
        self.display.setAlignment(QtCore.Qt.AlignRight)
        self.generalLayout.addWidget(self.display)

    def file_path(self):
        self.lineEdit = QtWidgets.QLineEdit()
        self.lineEdit.setFixedHeight(20)
        self.lineEdit.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout = QtWidgets.QFormLayout()
        self.path_layout.addRow("Folder Path: ", self.lineEdit)
        self.generalLayout.addLayout(self.path_layout)


    def create_files(self):
        self.button = QtWidgets.QPushButton("Create Folders")
        #self.button.pressed.connect(self.execute_button)
        self.generalLayout.addWidget(self.button)







"""
    def new_folder(self):
        self.lineEdit.returnPressed.connect(self.user_input())
        self.generalLayout.addWidget(self.lineEdit)

    def user_input(self):
        self.folder_input = self.lineEdit.text()

"""






def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
