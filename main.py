import sys
import os

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
        self.le1 = QtWidgets.QLineEdit()

        self.file_path()

        self.button1 = QtWidgets.QPushButton("New Folder")
        self.generalLayout.addWidget(self.button1)
        self.button1.pressed.connect(self.new_folder)

        self.button2 = QtWidgets.QPushButton("Create Folders")
        self.generalLayout.addWidget(self.button2)
        self.button2.pressed.connect(self.create_files)

        self.new_folder()
        self.new_folder()
        self.new_folder()
        self.test()


    def file_path(self):
        self.le1 = QtWidgets.QLineEdit()
        self.le1.setFixedHeight(20)
        self.le1.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout = QtWidgets.QFormLayout()
        self.path_layout.addRow("Folder Path: ", self.le1)
        self.generalLayout.addLayout(self.path_layout)


    def new_folder(self):
        self.le2 = QtWidgets.QLineEdit()
        self.le2.setFixedHeight(20)
        self.le2.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout = QtWidgets.QFormLayout()
        filename = "File: "
        self.path_layout.addRow(filename, self.le2)
        self.generalLayout.addLayout(self.path_layout)


    def create_files(self):
        path = self.le1.text() + "\\"
        filename = self.le2.text()
        newpath = path + filename
        if not os.path.exists(newpath):
            os.makedirs(newpath)

        else:
            print("folder already exists")


    def test(self):
        for i in range(self.generalLayout.count()):
            item = self.generalLayout.itemAt(i)
            print(item)


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
