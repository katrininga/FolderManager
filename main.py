import sys
import traceback
import os
import yaml

from PySide2 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        # set central widget and layout
        self.setWindowTitle("Katrins Amazing Folder Generator")
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.path_layout = QtWidgets.QFormLayout()
        self.folder_layout = QtWidgets.QGridLayout()

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)

        # It is best to always name variables with a descriptive name, this helps down the line when you have very large
        # modules to both keep the code clean and referencing when you need to call different
        self.root_path_le = QtWidgets.QLineEdit()
        self.root_sub_folder_le = QtWidgets.QLineEdit()

        # We need to create a list to store the line edits so each one remains its own object
        self.path_line_edits = list()
        self.folder_line_edits = list()
        self.folder_dict = dict()

        self.folder_path()

        self.newLeButton = QtWidgets.QPushButton("New Folder")
        self.generalLayout.addWidget(self.newLeButton)
        self.newLeButton.pressed.connect(self.new_folder)

        self.subLeButton = QtWidgets.QPushButton("New Sub Folder")
        self.generalLayout.addWidget(self.subLeButton)
        self.subLeButton.pressed.connect(self.new_sub_folder)


        self.createButton = QtWidgets.QPushButton("Create Folders")
        self.generalLayout.addWidget(self.createButton)
        self.createButton.pressed.connect(self.create_files)

        self.createButton = QtWidgets.QPushButton("printTest")
        self.generalLayout.addWidget(self.createButton)
        self.createButton.pressed.connect(self.testtest)

        self.generalLayout.addLayout(self.path_layout)
        self.generalLayout.addLayout(self.folder_layout)

        self.new_folder()


    def folder_path(self):
        self.root_path_le = QtWidgets.QLineEdit()
        self.root_path_le.setFixedHeight(20)
        self.root_path_le.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout.addRow("Folder Path: ", self.root_path_le)

    def new_folder(self):
        # Here since the addition of the lines is dynamic we don't want to define them to self as this will overwrite
        # the previously defined item.  In addition any variable/attribute that is getting defined as self.*** should
        # be done in the init method.  So once we have defined the line we need to add it to the list we created in the
        # init so it isn't destroyed once this method is complete
        path_le = QtWidgets.QLineEdit()
        path_le.setFixedHeight(20)
        path_le.setAlignment(QtCore.Qt.AlignRight)
        foldername = "  Folder: "
        empty_value = ""

        self.path_layout.addRow(foldername, path_le)
        self.folder_dict[path_le] = empty_value

    def new_sub_folder(self):
        sub_path_le = QtWidgets.QLineEdit()
        sub_path_le.setFixedHeight(20)
        sub_path_le.setAlignment(QtCore.Qt.AlignRight)
        subfoldername = "       SubFolder: "

        self.path_layout.addRow(subfoldername, sub_path_le)
        parent_folder = list(self.folder_dict)[-1]
        self.folder_dict[parent_folder] = sub_path_le


    def testtest(self):
        # Generally I convert anything from a line into str just to be safe as QT will sometimes return a QString which
        # can be useful but in %99 of cases that I have experienced cause more issues than it solves
        root_path = str(self.root_path_le.text())
        # Here we can now iterate over the list of widgets we created as previously it was only referencing a single
        # line edit



        for k, v in self.folder_dict.items():
            if v == "":
                new_path = os.path.join(root_path, str(k.text())).replace('\\', '/')

            else:
                new_path = os.path.join(root_path, str(k.text()), str(v.text())).replace('\\', '/')

            if not os.path.exists(new_path):
                print('Creating path:', new_path)
                try:
                    os.makedirs(new_path)
                except (IOError, PermissionError):
                    print('Attempt to create directory failed:', new_path)
                    traceback.print_exc()
                    # The below is helpful to see exactly what the error encountered was
                    # traceback.print_exc()




            else:
                # For debug prints like this it is good to add the data regarding what it tried so that in the event
                # this is not expected behaviour you will know exactly what it was referring to
                print("folder already exists:", new_path)


    def refreshAll(self):
        #TODO: refreshing window. Removes all existing folder lineEdits and starts from scratch.
        pass

#TODO: this will only create one subfolder(value) per folder(key), need to replace dictionary with something else that can hold multiple subfolders per folder
    def create_files(self):
        # Generally I convert anything from a line into str just to be safe as QT will sometimes return a QString which
        # can be useful but in %99 of cases that I have experienced cause more issues than it solves
        root_path = str(self.root_path_le.text())
        # Here we can now iterate over the list of widgets we created as previously it was only referencing a single
        # line edit
        for key in self.folder_dict:
            # I changed this to the os.path.join since it is IMO the best way to consolidate items into a path
            new_path = os.path.join(root_path, str(key.text())).replace('\\', '/')

            if not os.path.exists(new_path):
                print('Creating path:', new_path)
                try:
                    os.makedirs(new_path)
                except (IOError, PermissionError):
                    print('Attempt to create directory failed:', new_path)
                    traceback.print_exc()
                    # The below is helpful to see exactly what the error encountered was
                    # traceback.print_exc()




            else:
                # For debug prints like this it is good to add the data regarding what it tried so that in the event
                # this is not expected behaviour you will know exactly what it was referring to
                print("folder already exists:", new_path)










def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
