import sys
import traceback
import os
from PySide2 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):
        '''Folder Generator: creates a general folder structure for freelance projects'''

        super(MainWindow, self).__init__()
        #folder items
        self.nukeScripts = QtGui.QStandardItem()
        self.blenderScripts = QtGui.QStandardItem()
        self.scripts = QtGui.QStandardItem()
        self.nukePrecomp = QtGui.QStandardItem()
        self.nukeRender = QtGui.QStandardItem()
        self.premiereRender = QtGui.QStandardItem()
        self.blenderRenders = QtGui.QStandardItem()
        self.renders = QtGui.QStandardItem()
        self.footage = QtGui.QStandardItem()
        self.shotName = QtGui.QStandardItem()

        #layouts
        self.setWindowTitle('Folder Generator')
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.path_layout = QtWidgets.QFormLayout()
        self.folder_layout = QtWidgets.QGridLayout()
        self.generalLayout.addLayout(self.path_layout)

        #setting central widget
        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)

        #widgets
        self.root_path_le = QtWidgets.QLineEdit()
        self.model = QtGui.QStandardItemModel()
        self.tree = QtWidgets.QTreeView()
        self.tree.setHeaderHidden(True)
        self.rootNode = self.model.invisibleRootItem()
        self.tree.setModel(self.model)
        self.tree.setObjectName('tree')

        #setting main layout
        self.generalLayout.addWidget(self.tree)

        #button to create folders in root path
        self.createButton = QtWidgets.QPushButton('Create Folders')
        self.generalLayout.addWidget(self.createButton)
        self.createButton.pressed.connect(self.createFolders)

        #creating widgets
        self.createFolderWidgets()
        self.createRootPathWidget()

    def createRootPathWidget(self):
        # creating line edit for user to input the root folder path
        self.root_path_le.setFixedHeight(20)
        self.root_path_le.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout.addRow('Folder Path: ', self.root_path_le)

    def createFolderWidgets(self):
        # creating folder widgets
        self.shotName.setText('Shot_Name')
        self.rootNode.appendRow(self.shotName)
        index = self.model.indexFromItem(self.shotName)
        self.tree.setExpanded(index, True)

        self.footage.setText('Footage')
        self.footage.setEditable(False)
        self.shotName.appendRow(self.footage)

        self.renders.setText('Renders')
        self.renders.setEditable(False)
        self.shotName.appendRow(self.renders)
        index = self.model.indexFromItem(self.renders)
        self.tree.setExpanded(index, True)

        self.blenderRenders.setText('Blender')
        self.blenderRenders.setEditable(False)
        self.renders.appendRow(self.blenderRenders)

        self.premiereRender.setText('Premier_Pro')
        self.premiereRender.setEditable(False)
        self.renders.appendRow(self.premiereRender)

        self.nukeRender.setText('Nuke')
        self.nukeRender.setEditable(False)
        self.renders.appendRow(self.nukeRender)
        index = self.model.indexFromItem(self.nukeRender)
        self.tree.setExpanded(index, True)

        self.nukePrecomp.setText('Precomp')
        self.nukePrecomp.setEditable(False)
        self.nukeRender.appendRow(self.nukePrecomp)

        self.scripts.setText('Scripts')
        self.scripts.setEditable(False)
        self.shotName.appendRow(self.scripts)
        index = self.model.indexFromItem(self.scripts)
        self.tree.setExpanded(index, True)

        self.blenderScripts.setText('Blender')
        self.blenderScripts.setEditable(False)
        self.scripts.appendRow(self.blenderScripts)

        self.nukeScripts.setText('Nuke')
        self.nukeScripts.setEditable(False)
        self.scripts.appendRow(self.nukeScripts)

    def getPaths(self):
        # creating paths that match folder widgets
        shotName = str(self.shotName.text())
        rootpath = str(self.root_path_le.text())

        if not rootpath:
            print('Folder path is empty')
            return list()

        rootPath = os.path.join(rootpath, shotName)
        folders = {'Footage': list(),
                   'Renders': ['Nuke/Precomp', 'Blender', 'Premiere Pro'],
                   'Scripts': ['Nuke', 'Blender']
                   }

        folderPaths = list()

        for folder, subFolders in folders.items():
            newPath = os.path.join(rootPath, folder).replace('\\', '/')
            folderPaths.append(newPath)
            for subFolder in subFolders:
                subPath = os.path.join(newPath, subFolder).replace('\\', '/')
                folderPaths.append(subPath)

        return folderPaths

    def createFolders(self):
        # creating folders
        folderPaths = self.getPaths()
        for path in folderPaths:
            if not os.path.exists(path):
                print(path)
                print('Creating path:', path)
                try:
                    os.makedirs(path)
                except (IOError, PermissionError):
                    print('Attempt to create directory failed:', path)
                    traceback.print_exc()


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
