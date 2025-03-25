from PySide6.QtCore import QObject, QThread, Property, Signal, Slot
from worker import Worker

class Tests(QObject):
    switchPositionChanged = Signal()
    busyChanged = Signal()
    vnaOperationCompleted = Signal(str)
    errorOccurred = Signal(str)

    def __init__(self, parent=None):
        super().__init__(parent)
        self._worker = Worker()
        self._thread = QThread()
        self._worker.moveToThread(self._thread)

        # Connect signals
        self._worker.switchPositionChanged.connect(self._update_switch_positions)
        self._worker.busyChanged.connect(self._update_busy)
        self._worker.vnaOperationCompleted.connect(self.vnaOperationCompleted)
        self._worker.errorOccurred.connect(self.errorOccurred)

        self._thread.start()

        self._is_busy = self._worker.is_busy()

    @Property(int, notify=switchPositionChanged)
    def r1_position(self):
        return self._r1_position

    @Property(int, notify=switchPositionChanged)
    def r2_position(self):
        return self._r2_position

    @Property(bool, notify=busyChanged)
    def isBusy(self):
        return self._is_busy

    @Slot(int, int)
    def _update_switch_positions(self, r1, r2):
        self._r1_position = r1
        self._r2_position = r2
        self.switchPositionChanged.emit()

    @Slot(bool)
    def _update_busy(self, busy):
        self._is_busy = busy
        self.busyChanged.emit()

    @Slot(int)
    def setR1Position(self, value):
        self._worker.set_switch_r1_position(value)

    @Slot(int, int)
    def setR1R2Pos(self, r1pos, r2pos):
        self._worker.set_switch_r1_r2_pos(r1pos, r2pos)

    @Slot(str, str, list)
    def runSinglePort(self, name, description, ports):
        print(name, description, ports)
        self._worker.run_singlePort(name, description, ports)

    def cleanup(self):
        self._worker.switch_controller.close_connection()
        self._thread.quit()
        self._thread.wait()