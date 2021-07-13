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
        self.setWindowTitle("Katrins Amazing Folder Generator")
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.path_layout = QtWidgets.QFormLayout()
        self.folder_layout = QtWidgets.QGridLayout()
        self.generalLayout.addLayout(self.path_layout)

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)

        self.Data = []

        self.root_path_le = QtWidgets.QLineEdit()

        self.model = QtGui.QStandardItemModel()


        self.tree = QtWidgets.QTreeView()
        self.tree.setHeaderHidden(True)
        self.rootNode = self.model.invisibleRootItem()
        self.tree.setModel(self.model)
        self.tree.setObjectName("tree")
        self.tree.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tree.customContextMenuRequested.connect(self.on_context_menu)


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
            Item = QtGui.QStandardItem()
            if self.tree.selectedIndexes():
                index = self.tree.selectedIndexes()[0]
                crawler = index.model().itemFromIndex(index)
                Item.setText("NewFolder")
                crawler.appendRow(Item)
                self.tree.setExpanded(index, True)
                self.tree.clearSelection()
                self.Data.append(Item)


            else:
                Item.setText("NewFolder")
                self.rootNode.appendRow(Item)
                self.Data.append(Item)
                self.tree.clearSelection()


        if action == actionremove:
            index = self.tree.selectedIndexes()[0]
            crawler = index.model().itemFromIndex(index)
            if crawler.parent():
                crawler.parent().removeRow(crawler.row())
                self.Data.remove(crawler.parent())
            else:
                self.model.removeRow(crawler.row())
                self.Data.remove(crawler)

            self.tree.clearSelection()





    def folder_path(self):
        self.root_path_le.setFixedHeight(20)
        self.root_path_le.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout.addRow("Folder Path: ", self.root_path_le)


    def create_files(self):
        for x in self.Data:
            index = self.model.indexFromItem(x)
            child = self.model.index(x.row(),x.column(),parent=index)
            rowcount = self.model.rowCount(parent=index)
            number = 0
            if self.model.hasChildren(parent=index):
                print(index.model().itemFromIndex(child))




        """        for k, v in self.folder_dict.items():
            new_path_list = []
            if v == []:
                new_path = os.path.join(root_path, str(k.text())).replace('\\', '/')
                new_path_list.append(new_path)

            else:
                for x in v:
                    new_path = os.path.join(root_path, str(k.text()), str(x.text())).replace('\\', '/')
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
"""




def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()