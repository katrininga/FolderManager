import sys
import traceback
import os
from PySide2 import QtWidgets, QtCore, QtGui


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

        self.Data = []

        self.root_path_le = QtWidgets.QLineEdit()

        self.model = QtGui.QStandardItemModel()

        self.tree = QtWidgets.QTreeView()
        self.tree.setHeaderHidden(True)
        self.rootNode = self.model.invisibleRootItem()
        self.tree.setModel(self.model)
        self.tree.setObjectName("tree")


        self.generalLayout.addWidget(self.tree)

        self.createButton = QtWidgets.QPushButton("Create Folders")
        self.generalLayout.addWidget(self.createButton)
        self.createButton.pressed.connect(self.create_folders)

        self.folders_widgets()



        self.folder_path()



    def folder_path(self):
        self.root_path_le.setFixedHeight(20)
        self.root_path_le.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout.addRow("Folder Path: ", self.root_path_le)


    def folders_widgets(self):
        #creating folder widgets
        self.shotName = QtGui.QStandardItem()
        self.shotName.setText("Shot_Name")
        self.rootNode.appendRow(self.shotName)
        index = self.model.indexFromItem(self.shotName)
        self.tree.setExpanded(index, True)


        self.footage = QtGui.QStandardItem()
        self.footage.setText("Footage")
        self.footage.setEditable(False)
        self.shotName.appendRow(self.footage)

        self.renders = QtGui.QStandardItem()
        self.renders.setText("Renders")
        self.renders.setEditable(False)
        self.shotName.appendRow(self.renders)
        index = self.model.indexFromItem(self.renders)
        self.tree.setExpanded(index, True)

        self.blenderRenders = QtGui.QStandardItem()
        self.blenderRenders.setText("Blender")
        self.blenderRenders.setEditable(False)
        self.renders.appendRow(self.blenderRenders)

        self.premiereRender = QtGui.QStandardItem()
        self.premiereRender.setText("Premier_Pro")
        self.premiereRender.setEditable(False)
        self.renders.appendRow(self.premiereRender)

        self.nukeRender = QtGui.QStandardItem()
        self.nukeRender.setText("Nuke")
        self.nukeRender.setEditable(False)
        self.renders.appendRow(self.nukeRender)
        index = self.model.indexFromItem(self.nukeRender)
        self.tree.setExpanded(index, True)

        self.nukePrecomp = QtGui.QStandardItem()
        self.nukePrecomp.setText("Precomp")
        self.nukePrecomp.setEditable(False)
        self.nukeRender.appendRow(self.nukePrecomp)

        self.scripts = QtGui.QStandardItem()
        self.scripts.setText("Scripts")
        self.scripts.setEditable(False)
        self.shotName.appendRow(self.scripts)
        index = self.model.indexFromItem(self.scripts)
        self.tree.setExpanded(index, True)

        self.blenderScripts = QtGui.QStandardItem()
        self.blenderScripts.setText("Blender")
        self.blenderScripts.setEditable(False)
        self.scripts.appendRow(self.blenderScripts)

        self.nukeScripts = QtGui.QStandardItem()
        self.nukeScripts.setText("Nuke")
        self.nukeScripts.setEditable(False)
        self.scripts.appendRow(self.nukeScripts)


    def create_paths(self):
        #creating paths that match folder widgets
        shotName = str(self.shotName.text())
        rootpath = str(self.root_path_le.text())
        if not rootpath:
            print('Folder path is empty')

        else:
            rootpath = os.path.join(rootpath, shotName)

            folderlist = ['Footage', 'Renders', 'Scripts']
            subfolders = ['Nuke', 'Blender']
            folderpaths = []

            for x in folderlist:
                newpath = os.path.join(rootpath,x).replace('\\','/')
                folderpaths.append(newpath)
                if x == "Renders":
                    for y in subfolders:
                        renderpath = os.path.join(newpath, y).replace('\\','/')
                        folderpaths.append(renderpath)
                        if y == 'Nuke':
                            precomppath = os.path.join(renderpath,'Precomp').replace('\\','/')
                            folderpaths.append(precomppath)

                if x == "Scripts":
                    for y in subfolders:
                        scriptpath = os.path.join(newpath, y).replace('\\','/')
                        folderpaths.append(scriptpath)


            return folderpaths

    def create_folders(self):
        #creating folders
        folderpaths = self.create_paths()

        if folderpaths:
            for path in folderpaths:
                if not os.path.exists(path):
                    print(path)
                    print('Creating path:', path)
                    try:
                        os.makedirs(path)
                    except (IOError, PermissionError):
                        print('Attempt to create directory failed:', path)
                        traceback.print_exc()
                        # The below is helpful to see exactly what the error encountered was
                        # traceback.print_exc()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()