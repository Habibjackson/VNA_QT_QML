from PySide6.QtCore import QSettings, QObject, Property, Signal, QStringListModel, Slot
from PySide6.QtQml import QmlElement
from PySide6.QtSerialPort import QSerialPort, QSerialPortInfo

# Required for QML registration
QML_IMPORT_NAME = "MyApp"
QML_IMPORT_MAJOR_VERSION = 1

@QmlElement
class SettingsManager(QObject):
    # Define signals for property changes
    windowWidthChanged = Signal()
    windowHeightChanged = Signal()
    directoryChanged = Signal()
    serialPortChanged = Signal()
    serialPortsModelChanged = Signal()
    serialDataReceived = Signal(str)
    serialConnectedChanged = Signal()

    def __init__(self, parent=None):
        super().__init__(parent)
        # Initialize QSettings
        self._settings = QSettings("HCLTech", "VNA")
        # Load initial values with defaults
        self._window_width = self._settings.value("window/width", 800, type=int)
        self._window_height = self._settings.value("window/height", 600, type=int)
        self._directory = self._settings.value("storage/directory", "D://", type=str)
        self._serial_port_name = self._settings.value("serial/port", "COM3", type=str)

        # Initialize serial ports model
        self._serial_ports_model = QStringListModel(self)
        self._update_serial_ports()

        # Initialize QSerialPort
        self._serial_port = QSerialPort(self)
        self._serial_port.readyRead.connect(self._read_serial_data)
        self._is_serial_connected = False

    def _update_serial_ports(self):
        """Update the list of available serial ports using QSerialPortInfo."""
        ports = [port.portName() for port in QSerialPortInfo.availablePorts()]
        if not ports:  # Fallback if no ports are detected
            ports = ["COM1", "COM2", "/dev/ttyS0"]
        self._serial_ports_model.setStringList(ports)
        # Ensure the current serial port is valid
        if self._serial_port_name not in ports and ports:
            self._serial_port_name = ports[0]
            self._save_settings()

    @Property(int, notify=windowWidthChanged)
    def windowWidth(self):
        return self._window_width

    @windowWidth.setter
    def windowWidth(self, value):
        if self._window_width != value:
            self._window_width = value
            self._save_settings()
            self.windowWidthChanged.emit()

    @Property(int, notify=windowHeightChanged)
    def windowHeight(self):
        return self._window_height

    @windowHeight.setter
    def windowHeight(self, value):
        if self._window_height != value:
            self._window_height = value
            self._save_settings()
            self.windowHeightChanged.emit()

    @Property(str, notify=directoryChanged)
    def directory(self):
        return self._directory

    @directory.setter
    def directory(self, value):
        if self._directory != value:
            self._directory = value
            self._save_settings()
            self.directoryChanged.emit()

    @Property(str, notify=serialPortChanged)
    def serialPort(self):
        return self._serial_port_name

    @serialPort.setter
    def serialPort(self, value):
        if self._serial_port_name != value:
            self._serial_port_name = value
            self._save_settings()
            self.serialPortChanged.emit()

    @Property(QStringListModel, notify=serialPortsModelChanged)
    def serialPortsModel(self):
        return self._serial_ports_model

    @Property(bool, notify=serialConnectedChanged)
    def isSerialConnected(self):
        return self._is_serial_connected

    @Slot()
    def refreshSerialPorts(self):
        """Refresh the serial ports list."""
        self._update_serial_ports()
        self.serialPortsModelChanged.emit()

    @Slot()
    def toggleSerialConnection(self):
        """Open or close the serial port."""
        if self._is_serial_connected:
            self._serial_port.close()
            self._is_serial_connected = False
        else:
            self._serial_port.setPortName(self._serial_port_name)
            self._serial_port.setBaudRate(QSerialPort.Baud9600)  # Default baud rate
            if self._serial_port.open(QSerialPort.ReadWrite):
                self._is_serial_connected = True
            else:
                print(f"Failed to open {self._serial_port_name}: {self._serial_port.errorString()}")
        self.serialConnectedChanged.emit()

    @Slot()
    def _read_serial_data(self):
        """Read data from the serial port and emit it to QML."""
        data = self._serial_port.readAll().data().decode('utf-8', errors='ignore')
        if data:
            self.serialDataReceived.emit(data)

    def _save_settings(self):
        """Save current settings to QSettings."""
        self._settings.setValue("window/width", self._window_width)
        self._settings.setValue("window/height", self._window_height)
        self._settings.setValue("paths/directory", self._directory)
        self._settings.setValue("serial/port", self._serial_port_name)
        self._settings.sync()
