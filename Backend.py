# This Python file uses the following encoding: utf-8
from PySide6 import QtCore


class Backend(QtCore.QObject):
    messageChanged = QtCore.Signal()
    statusChanged = QtCore.Signal()

    def __init__(self):
        super().__init__()
        self._message = ""
        self._statusMessage = "status message"

    def getMessage(self):
        return self._message

    @QtCore.Slot(str)
    def setMessage(self, value):
        if self._message != value:
                    self._message = value
                    self.messageChanged.emit()

    def getStatusMessage(self):
        return self._statusMessage

    def setStatusMessage(self, value):
        if self._statusMessage != value:
            self._statusMessage = value
            self.statusChanged.emit()

    statusMessage = QtCore.Property(str, getStatusMessage, setStatusMessage, notify=statusChanged)


    message = QtCore.Property(str, getMessage, setMessage, notify=messageChanged)
