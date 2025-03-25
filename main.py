# # from PySide6.QtWidgets import QApplication
# # from PySide6.QtQml import QQmlApplicationEngine
# # from Backend import Backend
# # import sys, os

# # app = QApplication(sys.argv)
# # engine = QQmlApplicationEngine()
# # backend = Backend()
# # engine.rootContext().setContextProperty("backend", backend)
# # engine.load("ui/main.qml")

# # if not engine.rootObjects():
# #     sys.exit(-1)

# # sys.exit(app.exec())

# from PySide6.QtCore import QFileSystemWatcher, QUrl
# from PySide6.QtQml import QQmlApplicationEngine
# from PySide6.QtWidgets import QApplication
# import sys

# class QMLLiveReloader:
#     def __init__(self, engine, qml_file):
#         self.engine = engine
#         self.qml_file = qml_file
#         self.watcher = QFileSystemWatcher([qml_file])
#         self.watcher.fileChanged.connect(self.reload_qml)

#     def reload_qml(self):
#         self.engine.clearComponentCache()
#         self.engine.load(QUrl.fromLocalFile(self.qml_file))

# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     engine = QQmlApplicationEngine()
#     qml_file = "ui/main.qml"
#     reloader = QMLLiveReloader(engine, qml_file)
#     engine.load(QUrl.fromLocalFile(qml_file))

#     if not engine.rootObjects():
#         sys.exit(-1)
#     sys.exit(app.exec())

import sys
import os
from PySide6.QtCore import QFileSystemWatcher, QUrl, QObject
from PySide6.QtQml import QQmlApplicationEngine
from PySide6.QtWidgets import QApplication
from Models.AntennaListModel import AntennaListModel
from settingsManager import SettingsManager
from Antenna.AntennaManager import AntennaManager
from tests import Tests

class ProjectReloader(QObject):
    def __init__(self, engine, project_folder):
        super().__init__()
        self.engine = engine
        self.project_folder = project_folder
        self.watcher = QFileSystemWatcher()

        # Scan all QML files initially
        self.scan_qml_files()

        # Connect file change event
        self.watcher.fileChanged.connect(self.reload_component)
        self.watcher.directoryChanged.connect(self.scan_qml_files)

    def scan_qml_files(self):
        """ Scans the project folder for all QML files and watches them. """
        qml_files = []
        for root, _, files in os.walk(self.project_folder):
            for file in files:
                if file.endswith(".qml"):
                    qml_files.append(os.path.join(root, file))

        # Update watcher with new QML files
        self.watcher.addPaths(qml_files)
        print("Watching files:", qml_files)

    def reload_component(self, changed_file):
        """ Reloads the changed QML component dynamically. """
        print(f"Reloading {changed_file}...")

        # Clear QML cache
        self.engine.clearComponentCache()

        # Find all loaders in the UI
        root_object = self.engine.rootObjects()[0]
        loaders = root_object.findChildren(QObject, "dynamicLoader")

        for loader in loaders:
            if loader.property("source") == changed_file:
                loader.setProperty("source", "")  # Clear first
                loader.setProperty("source", changed_file)  # Reload the changed file

if __name__ == "__main__":
    app = QApplication(sys.argv)
    engine = QQmlApplicationEngine()
    antennaModel = AntennaListModel()
    settings = SettingsManager()
    antennaModel.loadFiles()

    test = Tests()

    antennaManger = AntennaManager(antennaModel)

    engine.rootContext().setContextProperty("settingsManager", settings)
    engine.rootContext().setContextProperty("antennaManager", antennaManger)
    engine.rootContext().setContextProperty("antennaModel", antennaModel )
    engine.rootContext().setContextProperty("test", test )
    engine.load(QUrl.fromLocalFile("ui/main.qml"))

    if not engine.rootObjects():
        sys.exit(-1)

    # Watch the entire project folder
    project_folder = os.path.join(os.getcwd(), "ui")  # Change this to your QML project folder
    reloader = ProjectReloader(engine, project_folder)

    sys.exit(app.exec())
