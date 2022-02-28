import sys
import traceback
import os
from PySide2 import QtWidgets, QtCore, QtGui


ROOT_PATH = r"C:\Users\katrin\PycharmProjects\FolderManager_00\Testing".replace("\\","/")

#data = [("Folder1",[("Subfolder1",[]),("Subfolder1",[("SubSubFolder1",[])])]),("Folder2",[("Subfolder2",[])])]




class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        # set central widget and layout
        self.setWindowTitle("Oh Wow Amazing Folder Generator")
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.path_layout = QtWidgets.QFormLayout()
        self.folder_layout = QtWidgets.QGridLayout()
        self.generalLayout.addLayout(self.path_layout)

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)

        self.model = QtGui.QStandardItemModel()
        self.tree = QtWidgets.QTreeView()
        self.tree.setHeaderHidden(True)
        self.rootNode = self.model.invisibleRootItem()
        self.tree.setModel(self.model)
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.on_context_menu)
        self.tree.setObjectName("tree")

        self.Item = QtGui.QStandardItem()
        self.Item1 = QtGui.QStandardItem()
        self.Item2 = QtGui.QStandardItem()

        self.model.insertRow(0)
        self.Item.setText("NewFolder0")
        self.Item1.setText("NewFolder1")
        self.Item2.setText("NewFolder2")
        self.model.setItem(0,0, self.Item)
        self.model.setItem(0,1, self.Item1)
        self.model.setItem(1,0, self.Item2)

        #self.row1 = [self.Item, self.Item1,self.Item1,self.Item1]
        #self.row2 = [self.Item2]

        self.rows = []
        self.generalLayout.addWidget(self.tree)

        self.createButton = QtWidgets.QPushButton("Create Folders")
        self.generalLayout.addWidget(self.createButton)
        self.createButton.pressed.connect(self.create_files)

        self.folder_path()

    def on_context_menu(self, point):
        # show context menu
        menu = QtWidgets.QMenu()
        actionfolder = menu.addAction(self.tr("Add Folder"))
        actionremove = menu.addAction(self.tr("RemoveFolder"))
        action = menu.exec_(self.tree.mapToGlobal(point))

        if action == actionfolder:
            print('action')

        if action == actionremove:
            print('removed')

        self.tree.clearSelection()


    def remove_folder(self):
        pass

    def create_folder(self):
        pass

    def folder_path(self):
        self.root_path_le = QtWidgets.QLineEdit()
        self.root_path_le.setFixedHeight(20)
        self.root_path_le.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout.addRow("Folder Path: ", self.root_path_le)

    def new_row(self):
        pass

    def new_column(self):
        pass

    def create_files(self):

        # TODO: this will only create one subfolder(value) per folder(key), need to replace dictionary with something else that can hold multiple subfolders per folder
        # Generally I convert anything from a line into str just to be safe as QT will sometimes return a QString which
        # can be useful but in %99 of cases that I have experienced cause more issues than it solves
        root_path = str(self.root_path_le.text())
        # Here we can now iterate over the list of widgets we created as previously it was only referencing a single
        # line edit

        for row in self.rows:

            text_convert = [i.text() for i in row]

            #s = "c:/,home,foo,bar,some.txt".split(",")
            new_path = os.path.join(*text_convert)
            print(new_path)
        '''    
            new_path = os.path.join(root_path,combined_folders.replace('\\', '/'))
            new_path_list.append(new_path)

        for new_path in new_path_list:
            if not os.path.exists(new_path):
                print(new_path)
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
        '''




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()