import sys
import traceback
import os
from PySide2 import QtWidgets, QtCore, QtGui


class MainWindow(QtWidgets.QMainWindow):
    def __init__(self):

        super(MainWindow, self).__init__()
        # set central widget and layout
        # all attributes to self should be defined in the init method.
        # Since the attribute is set to self it can be called from anywhere within the class.
        # Right now if this method isn't called then teh attribute won't ever exist and if
        # anything was to call it before this it would cause an error
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
        # Nothing wrong here for a personal project however I would recommend a more direct name
        # like Folder Generator
        self.setWindowTitle("Folder Generator")
        self.generalLayout = QtWidgets.QVBoxLayout()
        self.path_layout = QtWidgets.QFormLayout()
        self.folder_layout = QtWidgets.QGridLayout()
        self.generalLayout.addLayout(self.path_layout)

        self.centralWidget = QtWidgets.QWidget()
        self.setCentralWidget(self.centralWidget)
        self.centralWidget.setLayout(self.generalLayout)

        # small but I would change this to be a literal of just list() and lowercase name
        self.data = list()

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
        self.createButton.pressed.connect(self.createFolders)

        self.createFolderWidgets()
        self.createRootPathWidget()

    def createRootPathWidget(
            self):  # Overall add docstrings to the methods, you may want to re-name this as well since I presumed this was a property of some sort that would be the folder path to something
        self.root_path_le.setFixedHeight(20)
        self.root_path_le.setAlignment(QtCore.Qt.AlignRight)
        self.path_layout.addRow("Folder Path: ", self.root_path_le)

    def createFolderWidgets(self):  # same note about the name here
        # creating folder widgets
        self.shotName.setText(
            "Shot_Name")  # setting the attribute here is fine as long as it was defined first in the init.  Even it if is just set to None
        self.rootNode.appendRow(self.shotName)
        index = self.model.indexFromItem(self.shotName)
        self.tree.setExpanded(index, True)

        self.footage.setText("Footage")
        self.footage.setEditable(False)
        self.shotName.appendRow(self.footage)

        self.renders.setText("Renders")
        self.renders.setEditable(False)
        self.shotName.appendRow(self.renders)
        index = self.model.indexFromItem(self.renders)
        self.tree.setExpanded(index, True)

        self.blenderRenders.setText("Blender")
        self.blenderRenders.setEditable(False)
        self.renders.appendRow(self.blenderRenders)

        self.premiereRender.setText("Premier_Pro")
        self.premiereRender.setEditable(False)
        self.renders.appendRow(self.premiereRender)

        self.nukeRender.setText("Nuke")
        self.nukeRender.setEditable(False)
        self.renders.appendRow(self.nukeRender)
        index = self.model.indexFromItem(self.nukeRender)
        self.tree.setExpanded(index, True)

        self.nukePrecomp.setText("Precomp")
        self.nukePrecomp.setEditable(False)
        self.nukeRender.appendRow(self.nukePrecomp)

        self.scripts.setText("Scripts")
        self.scripts.setEditable(False)
        self.shotName.appendRow(self.scripts)
        index = self.model.indexFromItem(self.scripts)
        self.tree.setExpanded(index, True)

        self.blenderScripts.setText("Blender")
        self.blenderScripts.setEditable(False)
        self.scripts.appendRow(self.blenderScripts)

        self.nukeScripts.setText("Nuke")
        self.nukeScripts.setEditable(False)
        self.scripts.appendRow(self.nukeScripts)

    def getPaths(self):  # renamed to be more descriptive of what this method does
        # creating paths that match folder widgets
        shotName = str(self.shotName.text())
        rootpath = str(self.root_path_le.text())
        if not rootpath:
            # you may want to put a return None here for when there isn't a root path
            print('Folder path is empty')
            return list()

        # I tweaked the logic here to make it a bit shorter, but I presume this will be changed down the line to reference the tree view instead
        rootPath = os.path.join(rootpath, shotName)
        folders = {'Footage': list(),
                   'Renders': ['Nuke/Precomp', 'Blender'],
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
                    # The below is helpful to see exactly what the error encountered was
                    # traceback.print_exc()


"""
General overall notes
1. Add Docstrings to all methods
2. Use a common naming scheme either camelCasing or standard_naming.  try not to mix the two with the exception being built in names for modules such as Qt, os, etc
3. When using names like folderpath I would maintain camel casing by using folderPath so that you know the start of each new word
"""


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
