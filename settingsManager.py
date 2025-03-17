from PySide6.QtCore import QObject, Slot, QSettings

class SettingsManager(QObject):
    def __init__(self):
        super().__init__()
        self.settings = QSettings("MyCompany", "MyApp")

    @Slot(str, result=str)
    def getSetting(self, key):
        """Retrieve a setting, default to empty string if not found."""
        return self.settings.value(key, "")

    @Slot(str, str)
    def setSetting(self, key, value):
        """Save a setting."""
        self.settings.setValue(key, value)

    @Slot(int, int)
    def saveWindowSize(self, width, height):
        """Save window size settings."""
        self.settings.setValue("window/width", width)
        self.settings.setValue("window/height", height)

    @Slot(result=int)
    def getWindowWidth(self):
        """Get stored window width, default to 400."""
        return int(self.settings.value("window/width", 400))

    @Slot(result=int)
    def getWindowHeight(self):
        """Get stored window height, default to 300."""
        return int(self.settings.value("window/height", 300))
