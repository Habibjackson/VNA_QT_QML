# import socket
# import time
# from PySide6.QtCore import Signal, QObject

# class RETController(QObject):
#     deviceCounted = Signal(int)         # Emits number of scanned devices
#     tiltChanged = Signal(str, int)     # Emits port and new tilt value
#     operationCompleted = Signal(str)   # Emits when an operation finishes
#     errorOccurred = Signal(str)        # Emits error messages

#     AVAILABLE_PORTS = {}

#     def __init__(self, host="localhost", port=5000, parent=None):
#         super().__init__(parent)
#         self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
#         self.host = host
#         self.port = port
#         try:
#             self.s.connect((self.host, self.port))
#             print(self.s.recv(1024).decode())
#             self.s.send(b'Init:"COM5"\n')
#             time.sleep(1)
#         except ConnectionRefusedError:
#             self.errorOccurred.emit("Error connecting to CCULib server")
#             self.s = None

#     def initialize(self):
#         if not self.s:
#             self.errorOccurred.emit("No socket connection")
#             return
#         self.pca_power_on()
#         self.scan_start()
#         self.get_scan_state()
#         self.get_scanned_device_count()
#         self.get_scanned_devices()
#         self.operationCompleted.emit("Initialization completed")
#         print("Operation completed")

#     def pca_power_on(self):
#         if self.s:
#             self.s.send(b'pca_PowerOn\n')
#             print(self.s.recv(1024).decode(), "Powered On")
#             time.sleep(1)

#     def scan_start(self):
#         if self.s:
#             self.s.send(b'ScanStart\n')
#             print(self.s.recv(1024).decode(), "Scanned")
#             state = self.get_scan_state()
#             print(state)
#             while self.get_scan_state() == "SCAN_STATE_RUNNING":
#                 time.sleep(0.5)
#             print("Scan completed")

#     def get_scan_state(self):
#         if self.s:
#             self.s.send(b'GetScanState\n')
#             scan_state = self.s.recv(1024).decode().strip().split(":")[-1]
#             print(scan_state, "scanstate")
#             return scan_state
#         return "ERROR"

#     def get_scanned_device_count(self):
#         if self.s:
#             self.s.send(b'GetScannedDeviceCount\n')
#             msg = self.s.recv(1024).decode().strip().split(":")
#             print(msg, "msg")
#             try:
#                 self.device_count = int(msg[-1])
#                 self.deviceCounted.emit(self.device_count)
#                 print(f"Device count: {self.device_count}")
#             except ValueError as e:
#                 print(e)
#                 self.errorOccurred.emit(f"Invalid device count response: {msg}")
#             time.sleep(1)

#     def get_scanned_devices(self):
#         if not self.s or not hasattr(self, 'device_count'):
#             self.errorOccurred.emit("Device count not set or no connection")
#             return
#         devices = []
#         for i in range(1, self.device_count):
#             self.s.send(bytes(f'GetScannedDevice:{i}\n', encoding="utf-8"))
#             response = self.s.recv(1024).decode()
#             devices.append((response, f"Scan dev {i}"))
#             self.aisg_connect()
#             time.sleep(2)
#         data = self.extract_data(devices)
#         print(data, "data")
#         RETController.AVAILABLE_PORTS = {value: key for key, value in data}
#         with open('text.txt', 'w') as file:
#             file.write(str(data))
#         print(f"Scanned devices: {data}")

#     def extract_data(self, data):
#         my_list = []
#         for item in data:
#             s = item[0].strip()
#             ok = s.find('OK:')
#             if ok != -1:
#                 num = s[ok + 3:].lstrip()
#                 number = num.split(',')[0].strip()
#             quote_start = s.find('"')
#             quote_end = s.find('"', quote_start + 1)
#             if quote_start != -1 and quote_end != -1:
#                 id = s[quote_start + 1:quote_end].replace('-', ',')
#                 newid1 = id.split(',')[0].strip()
#                 newid2 = id.split(',')[1].strip()
#                 my_list.append([number, newid2])
#         return my_list

#     def aisg_connect(self):
#         if self.s:
#             self.s.send(b'AisgConnect\n')
#             print(self.s.recv(1024).decode(), "Aisg connect")
#             time.sleep(7)

#     def set_tilt(self, port, tilt, phase=1):
#         if not self.s:
#             self.errorOccurred.emit("No socket connection")
#             return
#         cmd = bytes(f"SetTilt:{RETController.AVAILABLE_PORTS[port]},{phase},{tilt}\n", encoding="utf-8")
#         self.s.send(cmd)
#         task_id = self.s.recv(1024).decode().split(":")[1].strip()
#         status = self.get_command_results(task_id)
#         while status == 'EXEC_RESULT_PENDING':
#             time.sleep(1)
#             status = self.get_command_results(task_id)
#         self.tiltChanged.emit(port, tilt)
#         print(f"Set tilt for port {port} to {tilt}")

#     def get_tilt(self, phase):
#         if not self.s:
#             self.errorOccurred.emit("No socket connection")
#             return None
#         cmd = bytes(f'GetTilt:{phase},1\n', encoding="utf-8")
#         self.s.send(cmd)
#         msg = self.s.recv(1024).decode().split(":")[-1].strip()
#         response = self.get_command_results(msg)
#         while response == "EXEC_RESULT_PENDING":
#             time.sleep(1)
#             response = self.get_command_results(msg)
#         tilt_value = response.split(",")[-1]
#         return int(tilt_value) if tilt_value.isdigit() else None

#     def calibrate(self, port, phase):
#         if not self.s:
#             self.errorOccurred.emit("No socket connection")
#             return
#         cmd = bytes(f"Calibrate:{port},{phase}\n", encoding="utf-8")
#         self.s.send(cmd)
#         task_id = self.s.recv(1024).decode().split(":")[1].strip()
#         status = self.get_command_results(task_id)
#         while status == 'EXEC_RESULT_PENDING':
#             time.sleep(1)
#             status = self.get_command_results(task_id)
#         self.operationCompleted.emit(f"Calibration completed for port {port}")

#     def get_command_results(self, task_id):
#         if self.s:
#             self.s.send(bytes(f'GetCommandResult:{task_id}\n', encoding="utf-8"))
#             return self.s.recv(1024).decode().split(":")[1].strip()
#         return "ERROR"

#     def close_server(self):
#         if self.s:
#             self.s.close()
#             print("Server connection closed")

# if __name__ == "__main__":
#     ret = RETController()
#     ret.initialize()

import socket
import time
from http.client import responses

from PySide6.QtCore import Signal, QObject


class RETController(QObject):
    deviceCounted = Signal(int)
    AVAILABLE_PORTS = {}

    def __init__(self):
        super(RETController, self).__init__()
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # get local machine name
        host = socket.gethostname()
        print(host)
        port = 5000
        try:
            # connection to hostname on the port.
            self.s.connect((host, port))
        except ConnectionRefusedError:
            print("Error Connecting to the CCULib server")

        print(self.s.recv(1024))
        self.s.send(b'Init:"COM5"\n')
        print(self.s.recv(1024), "Initialized")
        time.sleep(1)

    def initialize(self):
        self.pca_power_on()
        self.Scanstart()
        self.GetScanedDeviceCount()
        self.GetScanedDevice()
        # self.AignConnect()

    def pca_power_on(self):
        self.s.send(b'pca_PowerOn\n')
        print(self.s.recv(1024), "Powered On")
        time.sleep(1)

    def Scanstart(self):
        self.s.send(b'ScanStart\n')
        print(self.s.recv(1024), "Scanned")
        scanState = self.GetScanState()
        print(scanState, "Scanstaet342")
        while scanState == "SCAN_STATE_RUNNING":
            if self.GetScanState() == "SCAN_STATE_FINISHED":
                break

    def GetScanState(self):
        self.s.send(b'GetScanState\n')
        scanState = self.s.recv(1024).decode().split(":")[1]
        return scanState.strip()

    def GetScanedDeviceCount(self):
        self.s.send(b'GetScannedDeviceCount\n')
        msg = self.s.recv(1024)
        self.devicecount = int(msg.decode().strip()[-1])
        print(self.devicecount,'1')
        print(str(msg), "Device count")
        self.deviceCounted.emit(self.devicecount)
        time.sleep(1)

    def GetScanedDevice(self):
        a1=self.devicecount
        # for _ in range(1, self.devicecount):
        empty_list=[]

        for _ in range(1,a1):
            self.s.send(bytes('GetScannedDevice:{}\n'.format(_),encoding="utf-8"))
            a = self.s.recv(1024), f"Scan dev {_}"
            self.AignConnect()
            empty_list.append(a)
            self.new_list=empty_list
            print(f"print from cclin new list for loop {self.new_list}")
            time.sleep(2)

        data=self.extract_data(self.new_list)
        RETController.AVAILABLE_PORTS = {value: key for key, value in data}
        with open('text.txt','w') as file:
            file.write(str(data))


    def extract_data(self,data):
        my_list=[]
        for item in data:

            s = item[0].decode('utf-8').strip()
            ok = s.find('OK:')
            if ok != -1:
                num = s[ok + 3:].lstrip()
                number=num.split(',')[0].strip()
            quote_start = s.find('"')
            quote_end = s.find('"', quote_start + 1)
            if quote_start != -1 and quote_end != -1:
                id = s[quote_start + 1:quote_end].replace('-', ',')
                newid1 = id.split(',')[0].strip()
                newid2 = id.split(',')[1].strip()
                my_list.append([number,newid2])

        return my_list




    def AignConnect(self):

        self.s.send(b'AisgConnect\n')
        print(self.s.recv(1024), "Aisg connect")
        time.sleep(7)

    def updated_AignConnect(self):

        self.s.send(b'AisgConnect\n')
        response = self.s.recv(1024)
        print(response.decode(), "Aisg connect")
        time.sleep(7)
    #
    # def GetScanedDevice2(self):
    #     self.s.send(b'GetScannedDevice:2\n')
    #     print(self.s.recv(1024), "Scan dev 2")
    #     time.sleep(1)

    def settilt(self, port,tilt,phase=1):  # phase r = 1, y = 2, b = 3 & tilt 1° = 10, 14°=140
        """
        Port is inverted from ALDC R1 = 2, R2 = 1
        :return:
        """
        print(port, tilt,'in cculib')

        # print(type(tilt))
        cmd = bytes("SetTilt:{},{},{}\n".format(RETController.AVAILABLE_PORTS[port], phase, tilt), encoding="utf-8")
        # print(cmd)
        # cmd = b'SetTilt:1,1,20\n'
        self.s.send(cmd)
        task_id = self.s.recv(1024).decode().split(":")[1].strip()
        print("Setting tilt", port, phase, tilt)
        status = self.getcommandresults(task_id)
        while status == 'EXEC_RESULT_PENDING':
            if self.getcommandresults(task_id) != "EXEC_RESULT_PENDING":
                break

        # print(msg)
        # msgdec = msg.decode().split(":").strip()
        # print(msgdec, "Tilt")
        # print(msgdec[3:])
        return

    # def fixtilt(self,tilt):
    #
    #     for degree in tilt:
    #         degname = int(degree*10)
    #         self.settilt(2,degname)
    #         print(f"Setting tilt to {degname}")
    #         while True:
    #             res= self.getcommandresults()
    #             if res == 'OK:EXEC_RESULT_PENDING\n':
    #                 continue
    #             elif res.startswith('OK:EXEC_RESULT_FINISHED'):
    #                 print("success")
    #                 break
    #             else:
    #                 print(f"Invalid error")
    #                 break
    #
    #         # while self.getcommandresults() == 'OK:EXEC_RESULT_PENDING\n':
    #         #     if self.getcommandresults().startswith('OK:EXEC_RESULT_FINISHED'):
    #         #         print("success")
    #         #         break


    def gettilt(self,phase):# phase r = 1, y = 2, b = 3 & tilt 1° = 10, 14°=140
        #self.s.send(b'GetTilt:2,1\n')
        # cmd = bytes("Calibrate:{},{}\n".format(port, phase), encoding="utf-8")
        # print(cmd)
        # self.s.send(cmd)
        try:
            command = bytes(f'GetTilt:{phase},1\n', encoding="utf-8")
            self.s.send(command)
            msg = self.s.recv(1024)
            print(msg, "response")
            msg_decoded = msg.decode().split(":")[-1].strip()
            response = self.getcommandresults(msg_decoded)
            while response == "EXEC_RESULT_PENDING":
                response  = self.getcommandresults(msg_decoded)

            tiltValue = response.split(",")[-1]
            print("Parsed Response:",tiltValue)
            return tiltValue
        except socket.timeout:
            print("timeout occurred")
            return None
        except Exception as e:
            print(f"An error: {e}")
            return None

    def Updated_gettilt(self):
        self.s.send(b'GetTilt:1,1\n')
        time.sleep(5)
        msg = self.s.recv(1024)
        time.sleep(5)
        msgdec = msg.decode()
        print(msgdec, "GetTilt")
        time.sleep(1)


    def calibrate(self,port, phase):
        # self.s.send(b'Calibrate:2,1\n')
        cmd = bytes("Calibrate:{},{}\n".format(port, phase), encoding="utf-8")
        self.s.send(cmd)
        taskId = self.s.recv(1024).decode().split(":")[1].strip()
        status = self.getcommandresults(taskId)
        print(1, status,2, 4, taskId, 3, "calibaration")
        while status == 'EXEC_RESULT_PENDING':
            if self.getcommandresults(taskId) != "EXEC_RESULT_PENDING":
                break
        return

    def getcommandresults(self, taskId):
        self.s.send(bytes(f'GetCommandResult:{taskId}\n', encoding="utf-8"))
        msg = self.s.recv(1024)
        msgdec = msg.decode().split(":")[1]
        return msgdec.strip()

    def getcommandresults2(self):
        try:
            self.s.sendall(b'GetCommandResult:65536\n')
            msg = self.s.recv(1024)
            msg_decoded = msg.decode('utf-8')
            print(msg_decoded)
            time.sleep(1)
            return msg_decoded
        except Exception as e:
            print(f"An error occurred: {e}")
            return None

    def updated_fetch_command_results(self):

        while self.getcommandresults() == 'OK:EXEC_RESULT_PENDING\n':
            if self.getcommandresults().startswith('OK:EXEC_RESULT_FINISHED'):
                print("success")
                break
            #self.s.recv(1024)

    def upd_fetch_command_res2(self):
        for _ in iter(int, 1):
            result = self.getcommandresults()
            if result == 'OK:EXEC_RESULT_PENDING\n':
                continue
            if result.startswith('OK: EXEC_RESULT_FINISHED'):
                print("Success")
                break
            print("Unexpected Result:",result)
            break

    # def fix_ufr(self):
    #     while True:
    #         res = self.getcommandresults()
    #         if res == 'OK:EXEC_RESULT_PENDING\n':
    #             continue
    #         elif res.startswith('OK:EXEC_RESULT_FINISHED'):
    #             print("Success")
    #             break


    def fetch_command_results(self):
        """
        Continuously fetch command results until a desired condition is met.
        """
        while True:
            # Get the command results
            result = self.getcommandresults()
            # Print the results
            print("Result:", result)

            # Check for a specific condition (e.g., "Success" or a numeric value)
            if "Success" in result or result.strip() == "0":
                print("Command execution completed successfully.")
                break

            # Optional: Add a delay to prevent overwhelming the device
            time.sleep(1)
        msg = self.s.recv(1024)
        print(msg.decode('ascii'))
    def closeServer(self):
        self.s.close()


if __name__ == "__main__":

    ccuLib = CCULib()
    ccuLib.intialize()

    # ccuLib.fixtilt([3,5,9])

    # current_tilt = ccuLib.settilt(2,100)
    # ccuLib.getcommandresults()
    # ccuLib.updated_fetch_command_results()
    # print("Current Tilt:", current_tilt)


    ccuLib.Updated_gettilt()
    # ccuLib.getcommandresults()
    # ccuLib.updated_fetch_command_results()
    # print("Current Tilt:", current_tilt)

    # calibration_response = ccuLib.calibrate(3,1)
    # ccuLib.getcommandresults()
    # ccuLib.updated_fetch_command_results()
    # print("Calibration Response:", calibration_response)

    # ccuLib.closeServer()


# while(1):
#     deg = int(input("Enter the tilt degree: "))
#     settilt(1, 1, deg)
#     time.sleep(15)
#     print(f"set tilt started at {time.time()}")
#
    # while (getcommandresults() == 'OK:EXEC_RESULT_PENDING\n'):
    #     s.send(b'GetCommandResult:65536\n')
    #     msg = s.recv(1024)
    #     msgdec = msg.decode()
    #     print(msgdec, f"Messaged recieved at {time.time()}")
    #     time.sleep(1)
#
#     gettilt(1, 1)
#     s.send(b'GetCommandAnswerBytes:65536\n')
#     msg_tilt = s.recv(1024)
#     msg_tilt_dec = msg_tilt.decode()
#     print(msg_tilt_dec, "degree")

