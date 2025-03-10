# This Python file uses the following encoding: utf-8
import os
from PySide6.QtCore import Qt, QFileSystemWatcher, QModelIndex, QAbstractListModel
from AntennaManager import AntennaManager

class AntennaListModel(QAbstractListModel):
    FilenameRole = Qt.UserRole + 1  # Define custom role for filenames

    def __init__(self):
        super().__init__()
        self.files = []  # List to hold filenames
        self.directory = os.path.join("database", "antennas")  # Folder where encrypted JSON files are stored
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.watcher = QFileSystemWatcher()
        self.watcher.addPath(self.directory)
        self.watcher.directoryChanged.connect(self.loadFiles)  # Detect folder changes

        self.loadFiles()  # Initial load

    def rowCount(self, parent=QModelIndex()):
        return len(self.files)

    def data(self, index, role=Qt.DisplayRole):
        if not index.isValid() or index.row() >= len(self.files):
            return None
        if role == self.FilenameRole:
            return self.files[index.row()]
        return None

    def roleNames(self):
        return {self.FilenameRole: b"filename"}  # Expose role to QML

    def loadFiles(self):
        """Load all encrypted JSON files into the model and refresh."""
        self.beginResetModel()
        self.files = [f for f in os.listdir(self.directory) if f.endswith(".ant")]
        print("The loaded files are", self.files)
        self.endResetModel()
