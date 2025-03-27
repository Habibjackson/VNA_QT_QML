from PySide6.QtCore import QObject, Signal, Slot, QTimer
from Switch.Switch import SwitchController
from VNA.VNA import VNA
from RET.RETController import RETController
import time

class Worker(QObject):
    switchPositionChanged = Signal(int, int)
    vnaOperationCompleted = Signal(str)
    retDeviceCounted = Signal(int)
    retTiltChanged = Signal(str, int)
    busyChanged = Signal(bool)
    errorOccurred = Signal(str)
    statuSignal = Signal(dict)

    def __init__(self):
        super().__init__()
        self._is_busy = False

        # Connect signals
        # self.retController.tiltChanged.connect(self.retTiltChanged)
        # self.retController.operationCompleted.connect(self.vnaOperationCompleted)
        # self.retController.errorOccurred.connect(self.errorOccurred)
    def initialize(self):
        self.switch_controller = SwitchController()
        self.vna = VNA("TCPIP0::192.168.0.1::inst0::INSTR")
        self.retController = RETController()
        self.retController.initialize()
        self.switch_controller.positionChanged.connect(self.switchPositionChanged)
        self.retController.deviceCounted.connect(self.retDeviceCounted)

    def _start_operation(self):
        if self._is_busy:
            self.errorOccurred.emit("Operation blocked: Worker is busy")
            return False
        self._is_busy = True
        self.busyChanged.emit(self._is_busy)
        return True

    def _end_operation(self):
        self._is_busy = False
        self.busyChanged.emit(self._is_busy)

    @Slot(int)
    def set_switch_r1_position(self, value):
        if not self._start_operation():
            return
        try:
            self.switch_controller.set_r1_position(value)
        finally:
            self._end_operation()

    @Slot(int, int)
    def set_switch_r1_r2_pos(self, r1pos, r2pos):
        if not self._start_operation():
            return
        try:
            self.switch_controller.set_r1_r2_pos(r1pos, r2pos)
        finally:
            self._end_operation()

    @Slot(str, str, list)
    def run_singlePort(self, name, description, ports):
        """
        [{port: "Y1", tR: {"min": 2, "max": 12}, fR: {min: "999", "max": 2244}}]s
        """
        if not self._start_operation():
            return

        try:
            self.statuSignal.emit({"status": "Initializing the test", "deter":  1 , "progress": 1})
            self.switch_controller.set_r1_r2_pos(0, 0) # set the switch position to 0
            self.vna.Remote("ON")
            self.vna.create_folder_two_port(name)
            # self.vna.load_zvx("617-894-AMAL1")

            s_param = ["S11", "S22", "S21"]
            s_format = ["SWR", "SWR", "MAGN"]

            pDiv = (0.1, 0.1, 5)
            rlev = (1.5, 1.5, -25)

            a = 'OFF'

            for port in ports:
                startFreq = port.get("fR").get("min")
                stopFreq = port.get("fR").get("max")
                minTilt = float(port.get("tR").get("min"))
                maxTilt = float(port.get("tR").get("max"))
                mid = None
                portName = port.get("port")
                switchPos = port.get("index")
                self.switch_controller.set_r1_r2_pos(switchPos, switchPos)
                if maxTilt > 10:
                    mid = 7
                else:
                    mid = 5

                self.vna.load_zvx(f"{startFreq}-{stopFreq}")
                # self.vna.load_zvx(f"617-894-AMAL-3")
                
                self.statuSignal.emit({"status": f"Setting tilt {portName} to {minTilt}", "deter": 1, "progress": 1})
                self.retController.settilt(portName, minTilt * 10)

                self.vna.Frequency(port.get("fR").get("min"), port.get("fR").get("max"), "MHz")
                for i in range(1, 4):
                    self.vna.Trace_window(i, 1)
                    self.vna.vna_win_display(i, "ON")
                    self.vna.vna_window(i, s_param[i - 1], i , s_format[i - 1])
                    self.vna.vna_3marker("ON", stopFreq, startFreq)
                    self.vna.vna_smooth(a)
                    # time.sleep(2)
                    self.vna.vna_win_display(i, "OFF")

                for i in range(1, 3):
                    self.vna.vna_scale_div(i, pDiv[i - 1], rlev[i - 1], 50, 'ON', i)
                self.vna.vna_set_sweep_points(1601, 10)

                tilt = [minTilt, mid, maxTilt]
                for degree in tilt:
                    pRange=('min','mid','max')
                    ran = pRange[tilt.index(degree)]
                    self.statuSignal.emit({"status": f"Measuring {pRange[tilt.index(degree)]} value", "progress": 40, "deter": 1})
                    degName = int(degree * 10)
                    self.retController.settilt(portName,degName)
                    time.sleep(1)
                    self.statuSignal.emit({"status": f"Saving measured values for port {portName} {ran}", "deter": 1, "progress": 20})
                    self.vna.twoport_VNA_savescreen(f"{portName}_{pRange[tilt.index(degree)]}", "two")
                    self.vna.save_S2P(f"{portName}_{pRange[tilt.index(degree)]}", "two")
                    self.vna.Marker_Text(f"{portName}_{pRange[tilt.index(degree)]}", "two")
                    # time.sleep(1)
                    print("passed")
                    self.retController.settilt(portName, minTilt * 10)

                a = "MAX"

                self.vna.load_zvx(f"{startFreq}-{stopFreq}")
                # self.vna.load_zvx(f"617-894-AMAL-3")
                self.vna.Frequency(startFreq, stopFreq, "MHz")

                self.statuSignal.emit({"status": "Enabling smooth shift hold", "progress":  4, "deter": 1})
                for i in range(1, 4):
                    self.vna.Trace_window(i, 1)
                    self.vna.vna_win_display(i, "ON")
                    self.vna.vna_window(i, s_param[i - 1], i , s_format[i - 1])
                    self.vna.vna_3marker("ON", stopFreq, startFreq)
                    self.vna.vna_smooth(a)
                    self.vna.vna_win_display(i, "OFF")

                for i in range(1, 3):
                    self.vna.vna_scale_div(i, pDiv[i - 1], rlev[i - 1], 50, 'ON', i)
                self.vna.vna_set_sweep_points(1601, 10)

                self.statuSignal.emit({"status": f"Setting tilt to max for {portName}", "deter": 1, "progress": 2})
                self.retController.settilt(portName, maxTilt * 10)

                self.statuSignal.emit({"status": f"Saving worstcase values for port {portName}", "deter": 1, "progress": 20})
                self.vna.twoport_VNA_savescreen(f"{portName}_{pRange[tilt.index(degree)]}_worstcase", "two")
                self.vna.save_S2P(f"{portName}_{pRange[tilt.index(degree)]}_worstcase", "two")
                self.vna.Marker_Text(f"{portName}_{pRange[tilt.index(degree)]}_worstcase", "two")
            
            self.statuSignal.emit({"status": "Completed Single Port test", 'progress':  100, "deter": 0})

        except Exception as e:
            self.errorOccurred.emit(f"VNA two_port failed: {e}")
            self.statuSignal.emit({"status": "Completed Single Port test", 'progress':  100, "deter": 0})
            print(e, "Error occured")
        finally:
            self._end_operation()

    @Slot()
    def initialize_ret(self):
        if not self._start_operation():
            return
        try:
            self.retController.initialize()
        finally:
            self._end_operation()

    @Slot(str, int)
    def set_ret_tilt(self, port: str, tilt: float):
        if not self._start_operation():
            return
        try:
            self.retController.settilt(port, tilt)
        finally:
            self._end_operation()

    @Slot(str, int)
    def calibrate_ret(self, port, phase):
        if not self._start_operation():
            return
        try:
            self.retController.calibrate(port, phase)
        finally:
            self._end_operation()

    def get_ret_tilt(self, phase):
        return self.retController.gettilt(phase)

    def is_busy(self):
        return self._is_busy
