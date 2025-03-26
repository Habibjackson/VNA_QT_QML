# from PyQt5.QtCore import QObject, pyqtSignal, QTime
# import multiprocessing
# from VNA import DSOX3054T
# from cculib import CCULib
# import time
# import datetime
# import os,ast
# import excel
# from datetime import datetime
# from switch import SwitchController

# class Controller(QObject):
#     statusSignal = pyqtSignal(str)
#     signalGetTilt = pyqtSignal(int)
#     acknowledgePortChanage = pyqtSignal(str)

#     def __init__(self):
#         super(Controller, self).__init__()
#         # self.vna = DSOX3054T('USB0::0x0AAD::0x0199::101436::INSTR')
#         self.vna = DSOX3054T('TCPIP0::192.168.0.1::inst0::INSTR')
#         self.ccuLib = CCULib()
#         self.threadObj = self.thread()
#         self.changePortStatus = 0
#         pass

#     def initalizeCCUlib(self):
#         self.statusSignal.emit("Initializing VNA and PCA")
#         self.ccuLib.intialize()
#         self.statusSignal.emit("Ready")
#         pass

#     def setStart_stop_freq(self, startfreq, stopfreq, unit):
#         print(startfreq, stopfreq, unit)
#         self.vna.Frequency(startfreq, stopfreq, unit)

#     def Trace_window(self, channel_no, channel_sts):
#         self.vna.Trace_window(channel_no, channel_sts)
#         pass
    
#     def assign_traces(self, win_param):
#         """
#             "enabled": self.enableWindowCheck.isChecked(),
#             "format": self.format.currentText(),
#             "enableTimeDomain": self.time_domain_state.currentText(),
#             "timeDomain": self.time_domain.currentText(),
#             "smoothShift": self.smooth_shift.currentText(),
#             "memtrace": self.memtrace.currentText(),
#             "traceEnabled": self.memtrace.currentText(),
#             "traceNum": self.window_no,
#             "gateState": self.gatestate.currentText(),
#             "startTime": self.startTime.text(),
#             "stopTime": self.stopTime.text(),
#             "rangeLinesEnable": self.showRange.currentText(),
#             "band": self.bandnotch.currentText(),
#             """

#         self.vna.Assign_tracewindow(win_param["window_no"], win_param["enabled"],
#                                     win_param["enableTimeDomain"],
#                                     win_param["timeDomain"], win_param["gateState"],
#                                     win_param["startTime"], win_param["stopTime"],
#                                     win_param["sParam"], win_param["format"],
#                                     win_param["smoothShift"], win_param["memtrace"],
#                                     win_param["rangeLinesEnable"],win_param["band"])
            
#     def assign_layout(self):
#         self.vna.Assign_layout()
#         pass

#     def markerSettings(self):
#         pass
    
#     def applyScaleDiv(self, scaleDiv_param):
#         for widnow, param in scaleDiv_param.items():
#             self.vna.scale_div(widnow, param[0], param[1], param[2])
#         pass
            
#     def enableChannel(self, chnl_no, marker_no, state):
#         self.vna.setchannelEnable(chnl_no, marker_no, state)
#         print(chnl_no, marker_no, state)

#     def changeChannelFreq(self, chnl_no, marker_no, freq, unit):
#         self.vna.setChannelFrequency(chnl_no, marker_no, freq, unit)
#         print(chnl_no, marker_no, freq, unit, "change in channel freq")

#     def setChannelMaxHold(self, chnl_no, marker_no, state):
#         self.vna.setChannelMaxHold(chnl_no, marker_no, state)
#         print(chnl_no, marker_no, state)

#     def setChannelTracking(self, chnl_no, marker_no, state):
#         self.vna.setChannelTracking(chnl_no, marker_no, state)
#         print(chnl_no, marker_no, state)

#     def enCoupledMarker(self, state):
#         self.vna.marker_coupled(state)
#         pass

#     def getTilt(self,port):
#         self.statusSignal.emit(f"Getting tilt port {port}")
#         value = int(self.ccuLib.gettilt(port))
#         value /= 10
#         self.signalGetTilt.emit(value)
#         self.statusSignal.emit("Get tilt finished")

#     def calibrate(self, phase):
#         self.statusSignal.emit("Calibrating antenna")
#         self.ccuLib.calibrate(phase=phase, port=1)
#         self.statusSignal.emit("Calibration completed")

#     def setMarkerRange(self,chnl_no, params):
#         print(params, "params")
#         marker_no, startFreq, stopFreq, startunit, stopunit, showRange = params
#         print(chnl_no, marker_no, startFreq, stopFreq, startunit, showRange, marker_no)
#         self.vna.setRange(chnl_no, marker_no, startFreq, stopFreq, startunit, marker_no)

#     def saveSnp(self, params, filename, filetype, frmt):
#         self.vna.set_sweep_points(params)
#         if filetype == "s1p":
#             self.vna.save_S1P(filename)
#             pass
#         elif filetype == 's2p':
#             self.vna.save_S2P_new(filename, frmt)
#             pass

#     def startSinglPortTesting(self, param):
#         # self.vna.singl
#         pass
#     # def start_recording(self, filename, phase, start_degree, stop_degree):
#     #     print(start_degree, stop_degree)
#     #     for degree in range(start_degree, stop_degree+1):
#     #         degName = degree * 10
#     #         self.ccuLib.settilt(phase, degName)
#     #         print("before time sleep")
#     #         time.sleep(2)
#     #         self.ccuLib.getcommandresults()
#     #         print(degree)
#     #         time.sleep(7)
#     #         self.vna.VNA_savescreen(f"{filename}_{degree}")
#     #         time.sleep(7)
#     #         print("passed")

#     def start_recording(self, filename, phase, tilt):
#         print(tilt)
#         self.statusSignal.emit("Starting recording")
#         for degree in tilt:
#             self.statusSignal.emit("")
#             degName = degree * 10
#             self.ccuLib.settilt(phase, degName)
#             print("before time sleep")
#             # time.sleep(2)
#             print(degree)
#             # time.sleep(10)
#             self.statusSignal.emit(f"Saving screen for degree {degree} ")
#             self.vna.VNA_savescreen(f"{filename}_{degree}")
#         self.ccuLib.settilt(phase, int(tilt[0]) * 10)
#         print(phase, int(tilt[0])*10)

#     def saveZnxml(self,filename):
#         self.vna.save_znxnml(filename)
#         pass

#     def setTilt(self,phase, degree):
#         self.statusSignal.emit(f"setting tilt to {degree} degree")
#         degName = degree * 10
#         self.ccuLib.settilt(phase,degName)
#         self.statusSignal.emit("SetTilt completed")

#     def two_port(self,freq_range,b,tilt,filename,znxmlname):
#         # freq_range = ['2500','2690']#, "698,824", "1695,2360", "1427,2690", "1695,2690", "3300,5500"]
#         # print(freq_range)
#         timer = QTime()
#         timer.start()
#         self.statusSignal.emit("Starting test")
#         self.vna.create_folder_two_port(filename)
#         freq_range1 = ['1427','2690']
#         window_num = [1, 2, 3]
#         format = ["SWR", "SWR", "MAGN"]
#         smooth_shift_hold = ["OFF", "MAX"]
#         pDiv = [0.1, 0.1, 5]
#         rlev = [1.5, 1.5, -25]
#         # tilt = [2.5,5,10]#,[2,7,12],[3,7,12]]
#         # b = [['R1','R2']]#,['Y1','Y4'],['Y2','Y3']]
#         # freq = ["'698','960'"]#, "'1695','2690'", "'1427','2690'"]

#         # filename = input("enter filename:")

#         with open("text.txt",'r') as file:
#             x=file.read()
#             i = eval(x)
#             c = []
#             for ports in b:
#                 for po in ports:
#                     for _ in i:
#                         if po in _:
#                             c.append(i[i.index(_)][0])
#             # print(c)

#         port1 = c
#         print(port1)
#         start_fr = freq_range[0]
#         print(start_fr)
#         stop_fr = freq_range[-1]
#         print(stop_fr)

#         # for fr in freq:
#         #     start_fr, stop_fr = fr.split(",")
#         #     print(start_fr, stop_fr)
#         #     print(fr)
#         #     print(freq_range1)

#         for index in range(len(port1)):
#             print(index, "index")
#             print(self.changePortStatus, "Changeportstatus")
#             while self.changePortStatus == 1:
#                 if self.changePortStatus == 0:
#                     break
#             if index % 2 == 0:
#                 port = port1[index]
#                 s_param = ["S11", "S22", "S21"]
#                 p = b[0][0]
#                 # znxmlname = znxmlname1
#             else:
#                 port = port1[index]
#                 s_param = ["S33", "S44", "S43"]
#                 p = b[0][1]
#                 #znxmlname = znxmlname2
#             print(port, s_param, p, "[rkfal")
#             if freq_range != freq_range1:

#                 for a in smooth_shift_hold:

#                     if a == 'OFF':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency( start_fr, stop_fr, "MHz")
#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i], 1)
#                             self.vna.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i],"ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)

#                         self.vna.Assign_layout()
#                         for i in range(3):
#                             self.vna.scale_div(window_num[i],pDiv[i],rlev[i],50)
#                         self.vna.updated_set_sweep_points()

#                         for degree in tilt:
#                             a=['min','mid','max']
#                             degName = int(degree * 10)
#                             self.ccuLib.settilt(port,degName)
#                             print("before time sleep")
#                             time.sleep(1)
#                             print(degree)
#                             self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{a[tilt.index(degree)]}","two")
#                             self.vna.save_S2P(f"{filename}_{p}_{a[tilt.index(degree)]}", "two")
#                             self.vna.Marker_Text(f"{filename}_{p}_{a[tilt.index(degree)]}", "two")
#                             time.sleep(1)
#                             print("passed")

#                         new_tilt = int(tilt[0] * 10)
#                         print(new_tilt)
#                         self.ccuLib.settilt(port, new_tilt)
#                         print(port,new_tilt)
#                         print(new_tilt)

#                     if a == 'MAX':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency(start_fr, stop_fr, "MHz")

#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i], 1)
#                             self.vna.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i],"ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)
#                         self.vna.Assign_layout()

#                         for i in range(3):
#                             self.vna.scale_div(window_num[i],pDiv[i],rlev[i],50)
#                         self.vna.updated_set_sweep_points()


#                         newtilt = int(tilt[-1] * 10)
#                         print(newtilt)
#                         self.ccuLib.settilt(port,newtilt)
#                         time.sleep(1)
#                         self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase","two")
#                         # self.vna.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase", "two")
#                         self.vna.save_S2P(f"{filename}_{p}_{tilt[-1]}_wrostcase", "two")
#                         self.vna.Marker_Text(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
#                         time.sleep(1)
#                         print("passed")

#                         newtilt = int(tilt[0] * 10)
#                         print(newtilt)
#                         self.ccuLib.settilt(port, newtilt)
#                         print(p,"ports is completed. ")
#                         self.acknowledgePortChanage.emit(f"Change the VNA port to corresponding antenna port")
#                         self.changePortStatus = 1
#                         print(self.changePortStatus, "Changeportstatus")

#             else:

#                 for a in smooth_shift_hold:

#                     if a == 'OFF':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency( start_fr,stop_fr,"MHz")
#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i],1)
#                             self.vna.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
#                         self.vna.Assign_layout()
#                         for i in range(3):
#                             self.vna.scale_div(window_num[i], pDiv[i], rlev[i], 50)
#                         self.vna.updated_set_sweep_points()

#                         for degree in tilt:
#                             degName = int(degree * 10)
#                             self.ccuLib.settilt(port, degName)
#                             print("before time sleep")
#                             time.sleep(1)
#                             self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{degree}", "two")
#                             self.vna.save_S2P(f"{filename}_{p}_{degree}", "COMP")
#                             self.vna.Marker_Text(f"{filename}_{p}_{degree}", "two")
#                             time.sleep(1)
#                             print("passed")

#                         new_tilt = int(tilt[0] * 10)
#                         print(new_tilt)
#                         self.ccuLib.settilt(port, new_tilt)
#                         self.acknowledgePortChanage.emit(f"Change the VNA port to corresponding antenna port")
#                         self.changePortStatus = 1

#                     if a == 'MAX':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency(start_fr,stop_fr,"MHz")
#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i],1)
#                             self.vna.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
#                         self.vna.Assign_layout()
#                         for i in range(3):
#                             self.vna.scale_div(window_num[i],pDiv[i],rlev[i],50)
#                         self.vna.updated_set_sweep_points()

#                         newtilt = int(tilt[-1] * 10)
#                         print(newtilt)
#                         self.ccuLib.settilt(port, newtilt)
#                         time.sleep(1)
#                         # self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase")
#                         self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase", "two")
#                         self.vna.save_S2P(f"{filename}_{p}_{newtilt}_worstcase", "two")
#                         self.vna.Marker_Text(f"{filename}_{p}_{tilt[-1]}_worstcase")
#                         time.sleep(1)
#                         print("passed")

#                         new_tilt = int(tilt[0] * 10)
#                         print(new_tilt)
#                         self.ccuLib.settilt(port, new_tilt)
#                         print(p, "ports is completed. ")
#                         self.acknowledgePortChanage.emit(f"Change the VNA port to corresponding antenna port")
#                         self.changePortStatus = 1
#             self.changePortStatus = 0
#             self.statusSignal.emit("Completed in " + str(timer.elapsed()))

#     def two_port_mux(self,freq_range,b,tilt,filename,znxmlname):
#         # freq_range = ['2500','2690']#, "698,824", "1695,2360", "1427,2690", "1695,2690", "3300,5500"]
#         # print(freq_range)
#         self.vna.create_folder_two_port(filename)
#         self.statusSignal.emit("Creating directories")
#         freq_range1 = ['1427','2690']
#         window_num = [1, 2, 3]
#         format = ["SWR", "SWR", "MAGN"]
#         smooth_shift_hold = ["OFF", "MAX"]
#         pDiv = [0.1, 0.1, 5]
#         rlev = [1.5, 1.5, -25]
#         # tilt = [2.5,5,10]#,[2,7,12],[3,7,12]]
#         # b = [['R1','R2']]#,['Y1','Y4'],['Y2','Y3']]
#         # freq = ["'698','960'"]#, "'1695','2690'", "'1427','2690'"]

#         # filename = input("enter filename:")
#         with open("text.txt",'r') as file:
#             x=file.read()
#             i = eval(x)
#             c = []
#             for ports in b:
#                 for po in ports:
#                     for _ in i:
#                         if po in _:
#                             c.append(i[i.index(_)][0])
#             # print(c)

#         port1 = c
#         print(port1)
#         start_fr = freq_range[0]
#         print(start_fr)
#         stop_fr = freq_range[-1]
#         print(stop_fr)

#         # for fr in freq:
#         #     start_fr, stop_fr = fr.split(",")
#         #     print(start_fr, stop_fr)
#         #     print(fr)
#         #     print(freq_range1)

#         for index in range(len(port1)):
#             self.statusSignal.emit(f"Swtiching ports S1{index+1} S2{index+1}")
#             self.statusSignal.emit("Running test")
#             print(index, "index")
#             print(self.changePortStatus, "Changeportstatus")
#             while self.changePortStatus == 1:
#                 if self.changePortStatus == 0:
#                     break
#             if index % 2 == 0:
#                 port = port1[index]
#                 s_param = ["S11", "S22", "S21"]
#                 p = b[0][0]
#                 # znxmlname = znxmlname1
#             else:
#                 port = port1[index]
#                 s_param = ["S33", "S44", "S43"]
#                 p = b[0][1]
#                 #znxmlname = znxmlname2
#             # print(port, s_param, p, "[rkfal")
#             if freq_range != freq_range1:

#                 for a in smooth_shift_hold:

#                     if a == 'OFF':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency( start_fr, stop_fr, "MHz")
#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i], 1)
#                             self.vna.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i],"ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)

#                         self.vna.Assign_layout()
#                         for i in range(3):
#                             self.vna.scale_div(window_num[i],pDiv[i],rlev[i],50)
#                         self.vna.updated_set_sweep_points()

#                         for degree in tilt:
#                             a=['min','mid','max']
#                             degName = int(degree * 10)
#                             self.ccuLib.settilt(port,degName)
#                             print("before time sleep")
#                             # time.sleep(2)
#                             print(degree)
#                             self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{a[tilt.index(degree)]}","two")
#                             self.vna.save_S2P(f"{filename}_{p}_{a[tilt.index(degree)]}", "two")
#                             self.vna.Marker_Text(f"{filename}_{p}_{a[tilt.index(degree)]}", "two")
#                             time.sleep(1)
#                             print("passed")

#                         new_tilt = int(tilt[0] * 10)
#                         print(new_tilt)
#                         self.ccuLib.settilt(port, new_tilt)
#                         print(port,new_tilt)
#                         print(new_tilt)

#                     if a == 'MAX':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency(start_fr, stop_fr, "MHz")

#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i], 1)
#                             self.vna.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i],"ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)
#                         self.vna.Assign_layout()

#                         for i in range(3):
#                             self.vna.scale_div(window_num[i],pDiv[i],rlev[i],50)
#                         self.vna.updated_set_sweep_points()


#                         newtilt = int(tilt[-1] * 10)
#                         print(newtilt)
#                         self.ccuLib.settilt(port,newtilt)
#                         self.vna.Marker_Text(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
#                         self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase","two")
#                         # self.vna.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase", "two")
#                         self.vna.save_S2P(f"{filename}_{p}_{tilt[-1]}_wrostcase", "two")
#                         print("passed")

#                         newtilt = int(tilt[0] * 10)
#                         print(newtilt)
#                         self.ccuLib.settilt(port, newtilt)
#                         print(p,"ports is completed. ")
#                         self.changePortStatus = 1
#                         print(self.changePortStatus, "Changeportstatus")

#             else:

#                 for a in smooth_shift_hold:

#                     if a == 'OFF':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency( start_fr,stop_fr,"MHz")
#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i],1)
#                             self.vna.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
#                         self.vna.Assign_layout()
#                         for i in range(3):
#                             self.vna.scale_div(window_num[i], pDiv[i], rlev[i], 50)
#                         self.vna.updated_set_sweep_points()

#                         for degree in tilt:
#                             degName = int(degree * 10)
#                             self.ccuLib.settilt(port, degName)
#                             print("before time sleep")
#                             self.vna.Marker_Text(f"{filename}_{p}_{degree}", "two")
#                             self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{degree}", "two")
#                             self.vna.save_S2P(f"{filename}_{p}_{degree}", "COMP")

#                             print("passed")

#                         new_tilt = int(tilt[0] * 10)
#                         print(new_tilt)
#                         self.ccuLib.settilt(port, new_tilt)
#                         self.changePortStatus = 1

#                     if a == 'MAX':
#                         # self.vna.RST()
#                         self.vna.load_znxnml(znxmlname)
#                         self.vna.Frequency(start_fr,stop_fr,"MHz")
#                         for i in range(3):
#                             self.vna.Trace_window(window_num[i],1)
#                             self.vna.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
#                         self.vna.Assign_layout()
#                         for i in range(3):
#                             self.vna.scale_div(window_num[i],pDiv[i],rlev[i],50)
#                         self.vna.updated_set_sweep_points()

#                         newtilt = int(tilt[-1] * 10)
#                         print(newtilt)
#                         self.ccuLib.settilt(port, newtilt)
#                         self.vna.Marker_Text(f"{filename}_{p}_{tilt[-1]}_worstcase")
#                         # self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase")
#                         self.vna.twoport_VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase", "two")
#                         self.vna.save_S2P(f"{filename}_{p}_{newtilt}_worstcase", "two")

#                         print("passed")

#                         new_tilt = int(tilt[0] * 10)
#                         print(new_tilt)
#                         self.ccuLib.settilt(port, new_tilt)
#                         print(p, "ports is completed. ")
#                         self.changePortStatus = 1
#             self.acknowledgePortChanage.emit(f"Change the VNA port to corresponding antenna port")
#             print("Completed test")
#             self.changePortStatus = 0
#             self.statusSignal.emit("Completed in " + str(timer.elapsed()))



#     def interband_req_if(self, start_fr, stop_fr,s_param,tilt_angle,znxmlname,port1,fixed,variable):
#         window_num = [1, 2, 3, 4]
#         smooth_shift_hold = ["OFF", "MAX"]
#         for a in smooth_shift_hold:

#             if a == 'OFF':
#                 self.vna.smooth_off(a)

#                 # self.RST()
#                 self.vna.load_znxnml(znxmlname)
#                 self.vna.Frequency(start_fr, stop_fr, "MHz")

#                 for port in port1:
#                     tilt = tilt_angle[port1.index(port)][0]
#                     newtilt = int(tilt * 10)
#                     print(newtilt)
#                     self.ccuLib.settilt(port, newtilt)
#                     # time.sleep(2)
#                     # self.ccuLib.getcommandresults()
#                     # print(newtilt)
#                     # time.sleep(18)


#             if a == 'MAX':

#                 # self.RST()
#                 self.vna.load_znxnml(znxmlname)
#                 self.vna.Frequency(start_fr, stop_fr, "MHz")

#                 for i in range(4):
#                     self.vna.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], "MAGN", "ON", "ON", "ON",
#                                                     "OFF", start_fr, stop_fr, "MAX", "ON", a, range1=None,
#                                                     range_start_freq1=None, range_stop_freq1=None,
#                                                     show_range1=None, range2=None, range_start_freq2=None,
#                                                     range_stop_freq2=None, show_range2=None)
#                 self.vna.Assign_layout_four_win()

#                 for i in range(4):
#                     self.vna.scale_div(window_num[i], 5, '-25', 50)
#                 self.vna.updated_set_sweep_points()

#                 for port in port1:
#                     tilt = tilt_angle[port1.index(port)][-1]
#                     newtilt = int(tilt * 10)
#                     print(newtilt)
#                     self.ccuLib.settilt(port, newtilt)
#                     # print("before time sleep")
#                     # time.sleep(2)
#                     # self.ccuLib.getcommandresults()
#                     # print(newtilt)
#                     # time.sleep(18)

#                 for port in port1:
#                     tilt = tilt_angle[port1.index(port)][0]
#                     newtilt = int(tilt * 10)
#                     print(newtilt)
#                     self.ccuLib.settilt(port, newtilt)
#                     # time.sleep(2)
#                     # self.ccuLib.getcommandresults()
#                     # print(newtilt)
#                     # time.sleep(18)
#                 self.vna.twoport_VNA_savescreen(f"{fixed}_Constant_{variable}",f"inter")
#                 self.vna.Marker_Text(f"{fixed}_Constant_{variable}", f"inter")
#                 print("ports is completed. ")


#     def interband_req_else(self, start_fr, stop_fr,s_param,tilt_angle,znxmlname,port1,fixed,variable):
#         window_num = [1, 2, 3, 4]
#         smooth_shift_hold = ["OFF", "MAX"]
#         for a in smooth_shift_hold:

#             if a == 'OFF':
#                 self.vna.smooth_off(self, a)

#                 # self.RST()
#                 self.vna.load_znxnml(znxmlname)
#                 self.vna.Frequency(start_fr, stop_fr, "MHz")

#                 for port in port1:
#                     tilt = tilt_angle[port1.index(port)][0]
#                     newtilt = int(tilt * 10)
#                     print(newtilt)
#                     self.ccuLib.settilt(port, newtilt)
#                     # time.sleep(2)
#                     # self.ccuLib.getcommandresults()
#                     # print(newtilt)
#                     # time.sleep(18)

#             if a == 'MAX':

#                 # self.RST()
#                 self.vna.load_znxnml(znxmlname)
#                 self.vna.Frequency(start_fr, stop_fr, "MHz")

#                 for i in range(4):
#                     self.vna.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
#                 self.vna.Assign_layout_four_win()

#                 for i in range(4):
#                     self.vna.scale_div(window_num[i], 5, '-25', 50)
#                     self.vna.updated_set_sweep_points()

#                 for port in port1:
#                     tilt = tilt_angle[port1.index(port)][-1]
#                     newtilt = int(tilt * 10)
#                     print(newtilt)
#                     self.ccuLib.settilt(port, newtilt)
#                     print("before time sleep")
#                     # time.sleep(2)
#                     # self.ccuLib.getcommandresults()
#                     # print(newtilt)
#                     # time.sleep(18)

#                 for port in port1:
#                     tilt = tilt_angle[port1.index(port)][0]
#                     newtilt = int(tilt * 10)
#                     print(newtilt)
#                     self.ccuLib.settilt(port, newtilt)
#                     # time.sleep(2)
#                     # self.ccuLib.getcommandresults()
#                     # print(newtilt)
#                     # time.sleep(18)
#                 # vna should be outside of for loop
#                 self.vna.twoport_VNA_savescreen(f"{fixed}_Constant_{variable}",f"inter")
#                 self.vna.Marker_Text(f"{fixed}_Constant_{variable}", f"inter")
#                 print("ports is completed. ")

#     def updated_four_win_interband(self,freq_range,b,tilt,filename,znxmlname):
#         freq_range1 = ['1427', '2690']
#         self.vna.create_folder_interBand_port(filename)
#         window_num = [1, 2, 3, 4]
#         smooth_shift_hold = ["OFF", "MAX"]
#         # s_param = ["S12","S14","S32","S34"]
#         with open("text.txt", 'r') as file:
#             x = file.read()
#             i = eval(x)
#             c = []
#             for ports in b:
#                 for po in ports:
#                     for _ in i:
#                         if po in _:
#                             c.append(i[i.index(_)][0])
#             # print(c)

#         port1 = c
#         print(port1)
#         start_fr = freq_range[0]
#         print(start_fr)
#         stop_fr = freq_range[-1]
#         print(stop_fr)
#         rev = port1[::-1]
#         cde = []
#         cde.append(port1)
#         cde.append(rev)
#         print(cde)
#         for index in range(2):

#             if freq_range != freq_range1:

#                 if index == 0:
#                     port1 = cde[0]
#                     print(port1)
#                     s_param = ["S13", "S14", "S23","S24"]
#                     fixed = b[0][0]
#                     variable = b[0][1]
#                     # print(p)
#                     self.interband_req_if(start_fr,stop_fr,s_param,tilt,znxmlname,port1,fixed,variable)
#                     # self.VNA_savescreen(f"{fixed}_Constant_{variable}", f"inter")
#                     # self.Marker_Text(f"{fixed}_Constant_{variable}", f"inter")

#                     # znxmlname = znxmlname1
#                 elif index == 1:
#                     port1 = cde[1]
#                     s_param = ["S31", "S32", "S41","S42"]
#                     variable = b[0][0]
#                     fixed = b[0][1]
#                     self.interband_req_if(start_fr,stop_fr, s_param, tilt, znxmlname, port1,fixed,variable)
#                     # self.VNA_savescreen(f"{fixed}_Constant_{variable}", f"inter")
#                     # self.Marker_Text(f"{fixed}_Constant_{variable}", f"inter")

#             else:

#                 if index == 0:
#                     port1 = cde[0]
#                     s_param = ["S13", "S14", "S23", "S24"]
#                     fixed = b[0][0]
#                     variable = b[0][1]
#                     # print(p)
#                     self.interband_req_else(start_fr, stop_fr, s_param, tilt,znxmlname, port1,fixed,variable)
#                     # self.VNA_savescreen(f"{fixed}_Constant_{variable}", f"inter")
#                     # self.Marker_Text(f"{fixed}_Constant_{variable}", f"inter")
#                     # znxmlname = znxmlname1

#                 elif index == 1:
#                     port1 = cde[1]
#                     s_param = ["S31", "S32", "S41", "S42"]
#                     variable = b[0][0]
#                     fixed = b[0][1]
#                     self.interband_req_else(start_fr, stop_fr, s_param, tilt,znxmlname,port1,fixed,variable)

#     def win_interband(self,input_freq_range,b,tilt_angle,filename,znxmlname):
#         print(input_freq_range, tilt_angle)
#         freq_range1 = ['1427', '2690']
#         self.vna.create_folder_interBand_port(filename)
#         # window_num = [1, 2, 3, 4]
#         # smooth_shift_hold = ["OFF", "MAX"]
#         # s_param = ["S12","S14","S32","S34"]
#         with open("text.txt", 'r') as file:
#             x = file.read()
#             i = eval(x)
#             c = []
#             for ports in b:
#                 for po in ports:
#                     for _ in i:
#                         if po in _:
#                             c.append(i[i.index(_)][0])
#             # print(c)

#         port1 = c
#         print(port1)
#         rev = port1[::-1]
#         cde = []
#         cde.append(port1)
#         cde.append(rev)
#         print(cde)
#         for index in range(2):

#             if index == 0:

#                 freq_range = input_freq_range[0]
#                 # tilt = tilt_angle[0]
#                 start_fr = freq_range[0]
#                 print(start_fr)
#                 stop_fr = freq_range[-1]
#                 print(stop_fr)

#                 if freq_range != freq_range1:
#                     port1 = cde[0]
#                     print(port1)
#                     s_param = ["S13", "S14", "S23","S24"]
#                     fixed = b[0][0]
#                     variable = b[0][1]
#                     self.interband_req_if(start_fr,stop_fr,s_param,tilt_angle,znxmlname,port1,fixed,variable)
#                 else:
#                     port1 = cde[0]
#                     s_param = ["S13", "S14", "S23", "S24"]
#                     fixed = b[0][0]
#                     variable = b[0][1]
#                     self.interband_req_else(start_fr, stop_fr, s_param, tilt_angle, znxmlname, port1, fixed, variable)

#             elif index == 1:

#                 freq_range = input_freq_range[1]
#                 tilt = tilt_angle[1]
#                 start_fr = freq_range[0]
#                 print(start_fr)
#                 stop_fr = freq_range[-1]
#                 print(stop_fr)

#                 if freq_range != freq_range1:
#                     port1 = cde[1]
#                     s_param = ["S31", "S32", "S41","S42"]
#                     variable = b[0][0]
#                     fixed = b[0][1]
#                     self.interband_req_if(start_fr,stop_fr, s_param,tilt_angle, znxmlname, port1,fixed,variable)

#                 else:

#                     port1 = cde[1]
#                     s_param = ["S31", "S32", "S41", "S42"]
#                     variable = b[0][0]
#                     fixed = b[0][1]
#                     self.interband_req_else(start_fr, stop_fr, s_param, tilt_angle,znxmlname,port1,fixed,variable)
#         print("Change the next combination of INTER BAND Ports")

#     def multi_trace(self,freq_range,b,tilt,filename,znxmlname,s_param):

#         freq_range1 = ['1427','2690']
#         # smooth_shift_hold = ['OFF','MA  X']
#         start_fr = freq_range[0]
#         print(start_fr)
#         stop_fr = freq_range[-1]
#         print(stop_fr)
#         # l = len(tilt)-1

#         with open("text.txt",'r') as file:
#             x=file.read()
#             i = eval(x)
#             c = []
#             for ports in b:
#                 for po in ports:
#                     for _ in i:
#                         if po in _:
#                             c.append(i[i.index(_)][0])
#             # print(c)

#         port1 = c

#         z = len(tilt)
#         print(z)
#         mem = []
#         for i in range(z):
#             mem.append(i + 2)
#         print(mem)

#         zipped = zip(tilt, mem)

#         for index in range(len(port1)):

#             if index % 2 == 0:
#                 port = port1[index]
#                 s_param = "S11"
#                 p = b[0][0]

#             else:
#                 port = port1[index]
#                 s_param = "S11"
#                 p = b[0][1]
#             if freq_range != freq_range1:

#                 self.vna.RST()
#                 self.vna.load_znxnml(znxmlname)
#                 self.vna.Frequency(start_fr, stop_fr, "MHz")
#                 self.vna.trace_window_multi_trace(s_param)
#                 self.vna.smooth_multi_trace('OFF')
#                 self.vna.format_multi_trace("SWR")
#                 self.vna.mark_multitrace("ON","ON","ON","OFF",start_fr,stop_fr,"MAX","ON",range1=None,range_start_freq1=None,range_stop_freq1=None, show_range1=None, range2=None,range_start_freq2=None, range_stop_freq2=None, show_range2=None)
#                 self.vna.scale_division_multi_trace(0.1,1.5,50)
#                 self.vna.updated_set_sweep_points()

#                 for degree,memnum in zipped:
#                     degName = int(degree * 10)
#                     self.ccuLib.settilt(port, degName)
#                     time.sleep(2)
#                     self.ccuLib.getcommandresults()
#                     time.sleep(18)
#                     self.vna.mem_multi_trace(memnum)

#                 new_tilt = int(tilt[0] * 10)
#                 print(new_tilt)
#                 self.ccuLib.settilt(port, new_tilt)
#                 print(port, new_tilt)
#                 time.sleep(2)
#                 self.ccuLib.getcommandresults()
#                 print(new_tilt)
#                 time.sleep(18)

#                 self.vna.smooth_multi_trace("MAX")

#                 new_tilt = int(tilt[-1] * 10)
#                 print(new_tilt)
#                 self.ccuLib.settilt(port, new_tilt)
#                 time.sleep(2)
#                 self.ccuLib.getcommandresults()
#                 print(new_tilt)
#                 time.sleep(18)
#                 print("passed")

#                 new_tilt = int(tilt[0] * 10)
#                 print(new_tilt)
#                 self.ccuLib.settilt(port, new_tilt)
#                 time.sleep(2)
#                 self.ccuLib.getcommandresults()
#                 print(new_tilt)
#                 time.sleep(18)
#                 print(p, "ports is completed. ")
#                 self.vna.VNA_savescreen(f"{filename}_{p}_Multitrace", "inter")
#                 self.vna.save_S2P(f"{filename}_{p}_Multitrace", "two")


#             else:

#                 self.vna.RST()
#                 self.vna.load_znxnml(znxmlname)
#                 self.vna.Frequency(start_fr, stop_fr, "MHz")
#                 self.vna.trace_window_multi_trace(s_param)
#                 self.vna.smooth_multi_trace('OFF')
#                 self.vna.format_multi_trace("SWR")
#                 self.vna.mark_multitrace("ON", "ON", "ON", "ON", start_fr, stop_fr, "MAX", "ON", 1,1427,1518,1,2,1695,2690,1)
#                 self.vna.scale_division_multi_trace(0.1, 1.5, 50)
#                 self.vna.updated_set_sweep_points()

#                 for degree,memnum in zipped:
#                     degName = int(degree * 10)
#                     self.ccuLib.settilt(port, degName)
#                     time.sleep(2)
#                     self.ccuLib.getcommandresults()
#                     time.sleep(18)
#                     self.vna.mem_multi_trace(memnum)

#                 new_tilt = int(tilt[0] * 10)
#                 print(new_tilt)
#                 self.ccuLib.settilt(port, new_tilt)
#                 print(port, new_tilt)
#                 self.ccuLib.getcommandresults()
#                 self.ccuLib.updated_fetch_command_results()
#                 print("Current Tilt:", new_tilt)

#                 self.vna.smooth_multi_trace("MAx")

#                 new_tilt = int(tilt[-1] * 10)
#                 print(new_tilt)
#                 self.ccuLib.settilt(port, new_tilt)
#                 time.sleep(2)
#                 self.ccuLib.getcommandresults()
#                 print(new_tilt)
#                 time.sleep(18)
#                 print("passed")

#                 new_tilt = int(tilt[0] * 10)
#                 print(new_tilt)
#                 self.ccuLib.settilt(port, new_tilt)
#                 time.sleep(2)
#                 self.ccuLib.getcommandresults()
#                 print(new_tilt)
#                 time.sleep(18)
#                 print(p, "ports is completed. ")
#                 self.vna.VNA_savescreen(f"{filename}_{p}_Multitrace")
#                 self.vna.save_S2P(f"{filename}_{p}_Multitrace")


#     def saveScr(self, filename):
#         print(filename)
#         self.vna.VNA_savescreen(f"{filename}")

# if __name__ == "__main__":
#     DSO_OBJ = Controller()
#     DSO_OBJ.two_port_mux(['617','894'],[['R1']],[2,7,15],'sa3','amal')

import pyvisa  #ZNA
from PySide6.QtCore import QObject
import time
import os, ast
from Excel import excel
from newinterband import NewInterband
import datetime
import os,ast
from datetime import datetime

rm = pyvisa.ResourceManager()

class VNA():
    states = {0: "OFF", 1: "ON", 2: "MAX"}
    maxHoldState = {0: "MIN", 2: "MAX"}

    def __init__(self, address):
        # super(DSOX3054T, self).__init__()
        try:
            self.address = address
            self.inst = rm.open_resource(self.address)#open the resource
            self.inst.read_termination = '\n'         #assign the resource configuration
            self.inst.write_termination = '\n'
            self.inst.timeout = 20000
        except:
            print(f"Instrument not found {self.address}")

    def cls(self):
        '''
        Clear all event registers and Status Byte register

        :parameter  : None
        :returns    : None
        '''
        cmd = "*CLS"
        self.inst.write(cmd)

    def Remote(self, state):
        cmd = 'SYSTem:DISPlay:UPDate '+ str(state)
        self.inst.write(cmd)

    def Frequency(self, start, stop, unit):
        cmd1 = f":FREQuency:STARt {start}{unit}"
        cmd2 = f":FREQuency:STOP {stop}{unit}"
        self.inst.write(cmd1)
        self.inst.write(cmd2)

    def RST(self):
        '''
        Clear all event registers and Status Byte register

        :parameter  : None
        :returns    : None
        '''
        cmd = "*RST"
        self.inst.write(cmd)

    def load_znxnml(self,znxmlname):
        cmd1 = f"MMEM:LOAD:STAT 1,'C:\\Users\\Public\\Documents\\Rohde-Schwarz\\ZNA\\RecallSets\\amal\\{znxmlname}.znxml'"
        self.inst.write(cmd1)

    def load_zvx(self,znxmlname):
        cmd1 = f"MMEM:LOAD:STAT 1,'C:\\Rohde&Schwarz\\Nwa\\RecallSets\\{znxmlname}.zvx'"
        print("CMD", cmd1)
        self.inst.write(cmd1)

    def Trace_window(self, window_number, state):
        cmd = f':DISPLAY:WINDOW{window_number}:STATE '+ str(self.states[state])
        print(cmd)
        self.inst.write(cmd)

    def Assign_tracewindow(self, window: int, state, td_state, td_filter,
                           tg_state, tg_start, tg_stop, S_parameter, format,
                           smooth_shift, memdelete, tg_rangeLineState, bandNotch):

        cmd1 = f':DISPLAY:WINDOW{window}:STATE {self.states[state]}'

        cmd2 = f':CALCULATE1:PARAMETER:SDEFINE "Trc{window}","{S_parameter}"'
        cmd3 = ":DISPLAY:WINDOW{window}:TRACE1:FEED 'Trc{window}'"

        cmd4 = f"CALC1:FORM {format}"

        cmd5 = f":CALC1:TRAN:TIME:STAT {td_state}"
        # # # LPAS / BPAS / LPAS_STEP
        if td_filter == "STEP":
            cmd6="CALC1:TRAN:TIME:STIM STEP"
        else:
            cmd6 = f"CALC1:TRAN:TIME {td_filter}"

        cmd7 = f"CALC1:PHOLD {smooth_shift}"

        if memdelete == "ON":
            cmd8 = f":TRACE:COPY 'Mem{window}x[Trc{window}]',CH1DATA"
            cmd9 = f":DISPLAY:WINDOW{window}:TRACE{window}:FEED 'Mem{window}x[Trc{window}]'"
        else:
            cmd10 = "CALC1:PAR:DEL:MEM"

        cmd11 = f":CALC1:FILT:TIME:STAT {tg_state}"
        cmd12 = f"CALC1:FILT:GATE:TIME:START {tg_start}"
        cmd13 = f"CALC1:FILT:GATE:TIME:STOP {tg_stop}"
        cmd14 = f"CALC1:FILT:TIME:SHOW {tg_rangeLineState}"
        cmd15 = f"CALC1:FILT:TIME {bandNotch}"




        # cmd15="DISP:WIND1:STAT ON"
        # cmd16 = "DISP:WIND1:TRAC1:FEED 'CH1TR1'"
        # cmd17="DISP:WIND1:TRAC1:Y:PDIV 0.1"
        # cmd18 = "DISP:WIND1:TRAC1:Y:RLEV 1.5"
        # cmd19 = "DISP:WIND1:TRAC1:Y:RPOS 50"

        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        self.inst.write(cmd6)
        self.inst.write(cmd7)
        
        if memdelete == "ON":
            self.inst.write(cmd8)
            self.inst.write(cmd9)
        else:
            self.inst.write(cmd10)
        self.inst.write(cmd11)
        self.inst.write(cmd12)
        self.inst.write(cmd13)
        self.inst.write(cmd14)
        self.inst.write(cmd15)
        # self.inst.write(cmd16)
        # self.inst.write(cmd17)
        # self.inst.write(cmd18)
        # self.inst.write(cmd19)

    def updated_set_sweep_points(self):

        cmd1 = "SENSe1:SWEEp:TYPE LINear"
        cmd2 = "SENSe1:SWEEp:POINts 1601"

        cmd5 = "SOURce1:POWer -10DBM"
        self.inst.write(cmd1)
        self.inst.write(cmd2)

        self.inst.write(cmd5)

    def win_display(self, window_num, state):
        cmd = f":DISPLAY:WINDOW{window_num}:MAXimize {state}"
        self.inst.write(cmd)

    def vna_win_display(self,window_num, state):

        cmd1 = f':DISPLAY:WINDOW{window_num}:MAXimize {state}'
        print(cmd1)

        self.inst.write(cmd1)

    def vna_window(self,trace_num,s_peram,window_num,format):

        cmd2 = f':CALC1:PARAMETER:SDEFINE "Trc{trace_num}","{s_peram}"'
        cmd3 = f":DISPLAY:WINDOW{window_num}:TRACE{trace_num}:FEED 'Trc{trace_num}'"
        cmd4 = f":CALC1:FORM {format}"

        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)

    def vna_smooth(self, state):

        cmd = f"CALC1:PHOLD {state}"
        self.inst.write(cmd)

    def vna_scale_div(self, window: int, pDiv: int, rLev: int, rPos: int, state, trace_num):

        cmd4 = f"DISP:WIND{window}:STAT {state}"
        cmd10 = f"DISP:WIND{window}:TRAC{trace_num}:Y:PDIV {pDiv}"
        cmd13 = f"DISP:WIND{window}:TRAC{trace_num}:Y:RLEV {rLev}"
        cmd16 = f"DISP:WIND{window}:TRAC{trace_num}:Y:RPOS {rPos}"

        self.inst.write(cmd4)
        self.inst.write(cmd10)
        self.inst.write(cmd13)
        self.inst.write(cmd16)

    def vna_set_sweep_points(self,sweep_points,power):
        cmd1 = f"SENSe1:SWEEp:TYPE LINear"
        cmd2 = f"SENSe1:SWEEp:POINts {sweep_points}"
        cmd5 = f"SOURce1:POWer -{power}DBM"
        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd5)

    def vna_3marker(self,state,start_fr,stop_fr):

        cmd1 = f":CALC1:MARK1 {state}"
        cmd2 = f":CALC1:MARK1:X {start_fr}MHz"

        cmd3 = f":CALC1:MARK2 {state}"
        cmd4 = f":CALC1:MARK2:X {stop_fr}MHz"

        cmd5 = f":CALC1:MARK3 {state}"
        cmd6 = f"CALC1:MARK3:FUNC:DOM:USER {0}"
        cmd7 = f"CALC1:MARK3:FUNC:DOM:USER:STARt {start_fr}MHz"
        cmd8 = f"CALC1:MARK3:FUNC:DOM:USER:STOP {stop_fr}MHz"
        cmd9 = f":CALC1:MARK3:FUNC:EXEC MAXimum"
        cmd10 = f":CALC1:MARK3:SEAR:TRAC ON"
        cmd11 = f"CALC1:MARK5:FUNC:DOM:USER:SHOW {1}"
        cmd12 = f" CALC1:STAT:DOM:USER {1}"



        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        self.inst.write(cmd6)
        self.inst.write(cmd7)
        self.inst.write(cmd8)
        self.inst.write(cmd9)
        self.inst.write(cmd10)
        self.inst.write(cmd11)
        self.inst.write(cmd12)

    def vna_4marker(self,state,start_fr,stop_fr):

        cmd1 = f":CALC1:MARK1 {state}"
        cmd2 = f":CALC1:MARK1:X {start_fr}GHz"

        cmd3 = f":CALC1:MARK2 {state}"
        cmd4 = f":CALC1:MARK2:X {stop_fr}GHz"

        cmd5 = f":CALC1:MARK3 {state}"
        cmd6 = f"CALC1:MARK3:FUNC:DOM:USER {1}"
        cmd7 = f"CALC1:MARK3:FUNC:DOM:USER:STARt {1427}MHz"
        cmd8 = f"CALC1:MARK3:FUNC:DOM:USER:STOP {1518}MHz"
        cmd9 = f":CALC1:MARK3:FUNC:EXEC MAXimum"
        cmd10 = f":CALC1:MARK3:SEAR:TRAC ON"
        cmd11 = f"CALC1:MARK5:FUNC:DOM:USER:SHOW {1}"
        cmd12 = f" CALC1:STAT:DOM:USER {1}"

        cmd13 = f":CALC1:MARK3 {state}"
        cmd14 = f"CALC1:MARK3:FUNC:DOM:USER {2}"
        cmd15 = f"CALC1:MARK3:FUNC:DOM:USER:STARt {1695}MHz"
        cmd16 = f"CALC1:MARK3:FUNC:DOM:USER:STOP {2690}MHz"
        cmd17 = f":CALC1:MARK3:FUNC:EXEC MAXimum"
        cmd18 = f":CALC1:MARK3:SEAR:TRAC ON"
        cmd19 = f"CALC1:MARK5:FUNC:DOM:USER:SHOW {1}"
        cmd20 = f" CALC1:STAT:DOM:USER {1}"

        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        self.inst.write(cmd6)
        self.inst.write(cmd7)
        self.inst.write(cmd8)
        self.inst.write(cmd9)
        self.inst.write(cmd10)
        self.inst.write(cmd11)
        self.inst.write(cmd12)
        self.inst.write(cmd13)
        self.inst.write(cmd14)
        self.inst.write(cmd15)
        self.inst.write(cmd16)
        self.inst.write(cmd17)
        self.inst.write(cmd18)
        self.inst.write(cmd19)
        self.inst.write(cmd20)

    def updated_Assign_tracewindow(self, window: int, state,S_parameter,format,m1state,m2state,m3state,m4state,start_freq,stop_freq,trackmax,trackstate,smooth_shift,range1,range_start_freq1,range_stop_freq1,show_range1,range2,range_start_freq2,range_stop_freq2,show_range2,td_state=None, td_filter=None,
                                   tg_state=None, tg_start=None, tg_stop=None, memdelete=None, tg_rangeLineState=None, bandNotch=None):
        # print(window,state,S_parameter,format,smooth_shift)
        cmd1 = f':DISPLAY:WINDOW{window}:STATE {state}'

        cmd2 = f':CALCULATE1:PARAMETER:SDEFINE "Trc{window}","{S_parameter}"'
        cmd3 = f":DISPLAY:WINDOW{window}:TRACE1:FEED 'Trc{window}'"

        cmd4 = f"CALC1:FORM {format}"

        cmd5 = f":CALC1:TRAN:TIME:STAT {td_state}"
        # # # LPAS / BPAS / LPAS_STEP
        if td_filter == "STEP":
            cmd6 = "CALC1:TRAN:TIME:STIM STEP"
        else:
            cmd6 = f"CALC1:TRAN:TIME {td_filter}"

        cmd7 = f"CALC1:PHOLD {smooth_shift}"

        if memdelete == "ON":
            cmd8 = f":TRACE:COPY 'Mem{window}x[Trc{window}]',CH1DATA"
            cmd9 = f":DISPLAY:WINDOW{window}:TRACE{window}:FEED 'Mem{window}x[Trc{window}]'"
        else:
            cmd10 = "CALC1:PAR:DEL:MEM"

        cmd11 = f":CALC1:FILT:TIME:STAT {tg_state}"
        cmd12 = f"CALC1:FILT:GATE:TIME:START {tg_start}"
        cmd13 = f"CALC1:FILT:GATE:TIME:STOP {tg_stop}"
        cmd14 = f"CALC1:FILT:TIME:SHOW {tg_rangeLineState}"
        cmd15 = f"CALC1:FILT:TIME {bandNotch}"

        cmd16 = f":CALC1:MARK1 {m1state}"
        cmd17 = f":CALC1:MARK2 {m2state}"
        cmd18 = f":CALC1:MARK3 {m3state}"
        cmd19 = f":CALC1:MARK4 {m4state}"
        cmd20 = f":CALC1:MARK1:X {start_freq}MHz"
        cmd21 = f":CALC1:MARK2:X {stop_freq}MHz"

        cmd22 = f"CALC1:MARK3:FUNC:DOM:USER {range1}"
        cmd23 = f"CALC1:MARK3:FUNC:DOM:USER:STARt {range_start_freq1}MHz"
        cmd24 = f"CALC1:MARK3:FUNC:DOM:USER:STOP {range_stop_freq1}MHz"
        cmd25 = f":CALC1:MARK3:FUNC:EXEC {trackmax}"
        cmd26 = f":CALC1:MARK3:SEAR:TRAC {trackstate}"
        cmd27 = f"CALC1:MARK5:FUNC:DOM:USER:SHOW {show_range1}"
        cmd28 = f" CALC1:STAT:DOM:USER {show_range1}"

        cmd29 = f"CALC1:MARK4:FUNC:DOM:USER {range2}"
        cmd30 = f"CALC1:MARK4:FUNC:DOM:USER:STARt {range_start_freq2}MHz"
        cmd31 = f"CALC1:MARK4:FUNC:DOM:USER:STOP {range_stop_freq2}MHz"
        cmd32 = f":CALC1:MARK4:FUNC:EXEC {trackmax}"
        cmd33 = f":CALC1:MARK4:SEAR:TRAC {trackstate}"
        cmd34 = f"CALC1:MARK4:FUNC:DOM:USER:SHOW {show_range2}"
        cmd35 = f" CALC1:STAT:DOM:USER {show_range2}"

        # cmd40 = f"DISP:WIND{window}:STAT ON"
        # cmd23 = f"DISP:WIND1:TRAC1:Y:{pDiv}"
        # cmd24 = f"DISP:WIND2:TRAC2:Y:RLEV {rLev}"
        # cmd25 = f"DISP:WIND3:TRAC3:Y:RPOS {rPos}"

        # cmd2 = "CALC1:MARK5:FUNC:DOM:USER 1"
        # cmd3 = "CALC1:MARK5:FUNC:DOM:USER:STARt 1.5GHz"
        # cmd4 = "CALC1:MARK5:FUNC:DOM:USER:STOP 2.5GHz"
        # cmd5 = ":CALC1:MARK5:FUNC:EXEC MAXimum"
        # cmd6 = ":CALC1:MARK5:SEAR:TRAC ON"
        # cmd7 = "CALC1:MARK5:FUNC:DOM:USER:SHOW 1"
        # cmd8 = " CALC1:STAT:DOM:USER 1"

        # cmd1 = f":CALC{channel_no}:MARK{marker_no} ON"
        # cmd2 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER {user_no}"
        # cmd3 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER:STARt {start_freq}{unit}"
        # cmd4 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER:STOP {stop_freq}{unit}"
        # cmd7 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER:SHOW {user_no}"
        # cmd8 = f" CALC{channel_no}:STAT:DOM:USER {user_no}"
        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd7)
        # self.inst.write(cmd8)
        # cmd15="DISP:WIND1:STAT ON"
        # cmd16 = "DISP:WIND1:TRAC1:FEED 'CH1TR1'"
        # cmd17="DISP:WIND1:TRAC1:Y:PDIV 0.1"
        # cmd18 = "DISP:WIND1:TRAC1:Y:RLEV 1.5"
        # cmd19 = "DISP:WIND1:TRAC1:Y:RPOS 50"

        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        self.inst.write(cmd6)
        self.inst.write(cmd7)

        if memdelete == "ON":
            self.inst.write(cmd8)
            self.inst.write(cmd9)
        else:
            self.inst.write(cmd10)
        self.inst.write(cmd11)
        self.inst.write(cmd12)
        self.inst.write(cmd13)
        self.inst.write(cmd14)
        self.inst.write(cmd15)
        self.inst.write(cmd16)
        self.inst.write(cmd17)
        self.inst.write(cmd18)
        self.inst.write(cmd19)
        self.inst.write(cmd20)
        self.inst.write(cmd21)
        self.inst.write(cmd22)
        self.inst.write(cmd23)
        self.inst.write(cmd24)
        self.inst.write(cmd25)
        self.inst.write(cmd26)
        self.inst.write(cmd27)
        self.inst.write(cmd28)
        self.inst.write(cmd29)
        self.inst.write(cmd30)
        self.inst.write(cmd31)
        self.inst.write(cmd32)
        self.inst.write(cmd33)
        self.inst.write(cmd34)
        self.inst.write(cmd35)

    def Assign_tracewindow2(self):

        cmd1 = f':DISPLAY:WINDOW2:STATE ON'

        cmd2 = f':CALCULATE1:PARAMETER:SDEFINE "Trc2","S22"'
        cmd3 = f":DISPLAY:WINDOW2:TRACE2:FEED 'Trc2'"

        cmd4 =f"CALC1:FORM SWR"
        # cmd11 = "CALC1:FORM OFF"

        # cmd5=":CALC1:TRAN:TIME:STAT OFF"
        # # LPAS / BPAS
        # cmd6="CALC1:TRAN:TIME LPAS"

        cmd7 = "CALC1:PHOLD OFF"

        # cmd8 = ":TRACE:COPY 'Mem2x[Trc2]',CH1DATA"
        # cmd9 = ":DISPLAY:WINDOW2:TRACE2:FEED 'Mem2x[Trc2]'"
        # cmd10 = "CALC1:PAR:DEL:MEM"

        # cmd101 = ":CALC1:FILT:TIME:STAT ON"
        # cmd11 = "CALC1:FILT:GATE:TIME:START 0.31ns"
        # cmd12 = "CALC1:FILT:GATE:TIME:STOP 0.371ns"
        # cmd13 = "CALC1:FILT:TIME:SHOW OFF"
        # cmd14 = "CALC1:FILT:TIME NOTCH"

        # cmd15 = "DISP:WIND2:STAT ON"
        # cmd16 = "DISP:WIND2:TRAC2:FEED 'CH1TR2'"
        # cmd17 = "DISP:WIND2:TRAC2:Y:PDIV 0.1"
        # cmd18 = "DISP:WIND2:TRAC2:Y:RLEV 1.5"
        # cmd19 = "DISP:WIND2:TRAC2:Y:RPOS 50"

        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        # self.inst.write(cmd5)
        # self.inst.write(cmd6)
        self.inst.write(cmd7)
        # self.inst.write(cmd8)
        # self.inst.write(cmd9)
        # self.inst.write(cmd10)
        # self.inst.write(cmd101)
        # self.inst.write(cmd11)
        # self.inst.write(cmd12)
        # self.inst.write(cmd13)
        # self.inst.write(cmd14)
        # self.inst.write(cmd15)
        # self.inst.write(cmd16)
        # self.inst.write(cmd17)
        # self.inst.write(cmd18)
        # self.inst.write(cmd19)


    def Assign_tracewindow3(self):
        cmd1 = f':DISPLAY:WINDOW3:STATE ON'

        cmd2 = f':CALCULATE1:PARAMETER:SDEFINE "Trc3","S11"'
        cmd3 = f":DISPLAY:WINDOW3:TRACE3:FEED 'Trc3'"

        cmd4 = f"CALC1:FORM MAGN"

        # cmd5=":CALC1:TRAN:TIME:STAT OFF"
        # # LPAS / BPAS
        # cmd6="CALC1:TRAN:TIME:STIM STEP"

        cmd7 = "CALC1:PHOLD OFF"

        # cmd8 = ":TRACE:COPY 'Mem3x[Trc3]',CH1DATA"
        # cmd9 = ":DISPLAY:WINDOW3:TRACE3:FEED 'Mem3x[Trc3]'"
        # cmd10 = "CALC1:PAR:DEL:MEM"

        # cmd101 = ":CALC1:FILT:TIME:STAT ON"
        # cmd11 = "CALC1:FILT:GATE:TIME:START 0.31ns"
        # cmd12 = "CALC1:FILT:GATE:TIME:STOP 0.371ns"
        # cmd13 = "CALC1:FILT:TIME:SHOW ON"
        # cmd14 = "CALC1:FILT:TIME BANDPASS"

        # cmd15 = "DISP:WIND3:STAT ON"
        # cmd16 = "DISP:WIND3:TRAC3:FEED 'CH1TR3'"
        # cmd17 = "DISP:WIND3:TRAC3:Y:PDIV 5"
        # cmd18 = "DISP:WIND3:TRAC3:Y:RLEV -25"
        # cmd19 = "DISP:WIND3:TRAC3:Y:RPOS 50"

        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        # self.inst.write(cmd5)
        # self.inst.write(cmd6)
        self.inst.write(cmd7)
        # self.inst.write(cmd8)
        # self.inst.write(cmd9)
        # self.inst.write(cmd10)
        # self.inst.write(cmd101)
        # self.inst.write(cmd11)
        # self.inst.write(cmd12)
        # self.inst.write(cmd13)
        # self.inst.write(cmd14)
        # self.inst.write(cmd15)
        # self.inst.write(cmd16)
        # self.inst.write(cmd17)
        # self.inst.write(cmd18)
        # self.inst.write(cmd19)

    # def Assign_tracewindow1(self, window: int, state, time_state, td_filter, S_parameter, format, smooth_shift,
    #                         memdelete):
    #     cmd1 = f':DISPLAY:WINDOW{window}:STATE {state}'

    #     cmd2 = f':CALC1:PARAMETER:SDEFINE "Trc1","{S_parameter}"'
    #     cmd3 = ":DISPLAY:WINDOW{window}:TRACE1:FEED 'Trc1'"

    #     cmd4 = f"CALC1:FORM {format}"  # SWR, MAGEN, OFF

    #     cmd5 = f":CALC1:TRAN:TIME:STAT {time_state}"  # LPAS / BPAS
    #     cmd6 = f"CALC1:TRAN:TIME {td_filter}"

    #     cmd7 = f"CALC1:PHOLD {smooth_shift}"

    #     cmd8 = ":TRACE:COPY 'Mem1x[Trc1]',CH1DATA"
    #     cmd9 = f":DISPLAY:WINDOW1:TRACE1:FEED 'Mem1x[Trc1]'"
    #     cmd10 = f"CALC1:PAR:DEL:{memdelete}"

    #     cmd11 = ":CALC1:FILT:TIME:STAT ON"
    #     cmd12 = "CALC1:FILT:GATE:TIME:START 0.31ns"
    #     cmd13 = "CALC1:FILT:GATE:TIME:STOP 0.371ns"
    #     cmd14 = "CALC1:FILT:TIME:SHOW ON"
    #     cmd15 = "CALC1:FILT:TIME NOTCH"

    # def Assign_tracewindow(self, ch_number, sParam, format trc):
    #     cmd =  f':CALCULATE{1}:PARAMETER:SDEFINE "Trc{ch_number}","{sParam}"'
    #     cmd1 = f":DISPLAY:WINDOW{ch_number}:TRACE{ch_number}:FEED 'Trc{ch_number}'"
    #     cmd2 = f"CALC{1}:FORM {format}"

    #     print(cmd)
    #     print(cmd1)
    #     print(cmd2)
    #     self.inst.write(cmd)
    #     self.inst.write(cmd1)
    #     self.inst.write(cmd2)

    # def Assign_tracewindow2(self, ch_number, trace_number, trc):
    #     cmd1 = f":DISPLAY:WINDOW{ch_number}:TRACE{trace_number}:FEED 'Trc{trc}'"
    #     self.inst.write(cmd1)
    #     cmd2 = ':CALCULATE1: PARAMETER:SELECT "Trc1"'
    #     cmd3 = ':CALCULATE1:PARAMETER:SDEFINE "Trc2","S22"'
    #     cmd4 = ":DISPLAY:WINDOW2:TRACE2:FEED 'Trc2'"
    #     cmd5 = ':CALCULATE1: PARAMETER:SELECT "Trc2"'
    #     cmd6 = ':CALCULATE1:PARAMETER:SDEFINE "Trc3","S21"'
    #     cmd7 = ":DISPLAY:WINDOW3:TRACE3:FEED 'Trc3'"
    #     cmd8 = ':CALCULATE1: PARAMETER:SELECT "Trc2"'
    #     self.inst.write(cmd2)
    #     self.inst.write(cmd3)
    #     self.inst.write(cmd4)
    #     self.inst.write(cmd5)
    #     self.inst.write(cmd6)
    #     self.inst.write(cmd7)
    #     self.inst.write(cmd8)

    @classmethod
    def Assign_layout(self):
        cmd = ":DISPlay:LAYout:DEFine 1, Horizontal, '0.50,0.50,0.50'"
        cmd1 = ':DISPlay:LAYout:APPLy 1'
        self.inst.write(cmd)
        self.inst.write(cmd1)

    def set_sweep_points(self, params):
        type, points, start, stop, power, unit1, unit2 = params
        cmd1 = "SENSe1:SWEEp:TYPE LINear"
        cmd2 = f"SENSe1:SWEEp:POINts {points}"
        # cmd3 = f"SENSe1:FREQuency:STARt {start}{unit1}"
        # cmd4 = f"SENSe1:FREQuency:STOP {stop}{unit2}"
        cmd5 = f"SOURce1:POWer {power}DBM"
        self.inst.write(cmd1)
        self.inst.write(cmd2)
        # self.inst.write(cmd3)
        # self.inst.write(cmd4)
        self.inst.write(cmd5)
    
    def save_S2P_new(self,filename, frmat):
        cmd3 = "CALC:PAR:DEF:SGR 1,2"
        cmd4 = "CALC:PAR:DEF:SGR 1"
        cmd5 = f"MMEM:STOR:TRAC 'TRC1', 'D:\\{filename}.s2p', FORM, {frmat}, POIN, SEM"
        print(cmd5)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        self.inst.write("HCOP:DEST 'MMEM'; :HCOP")

    def save_S2P(self,filename,test):
        print(test)
        # folderpath = f"C:\\Users\\Public\\Documents\\Rohde-Schwarz\\ZNA\\2585"
        # folderpath = f"D:\\2825"
        #os.makedirs(folderpath, exist_ok=True)
        cmd3 = "CALC:PAR:DEF:SGR 1,2"
        cmd4 = "CALC:PAR:DEF:SGR 1"
        if test == 'inter':
            for i in self.res:
                if i in filename:
                    subfold=os.path.join(self.sfolinter,i)
            cmd5 = f"MMEM:STOR:TRAC 'TRC1', '{subfold}\\{filename}.s2p', FORM, COMP, POIN, SEM"

        elif test == 'two':
            for i in self.res:
                if i in filename:
                    subfold=os.path.join(self.sfol,i)
            cmd5 = f"MMEM:STOR:TRAC 'TRC1', '{subfold}\\{filename}.s2p', FORM, COMP, POIN, SEM"
        # cmd5 = f"MMEM:STOR:TRAC 'TRC1', 'C:\\Users\\Public\\Documents\\Rohde-Schwarz\\ZNA\\{filename}.s2p', FORM, COMP, POIN, SEM"
        # print(cmd5)

        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        self.inst.write("HCOP:DEST 'MMEM'; :HCOP")

    def save_S1P(self,filename):
        cmd4 = "CALC:PAR:DEF:SGR 1"
        cmd5 = f"MMEM:STOR:TRAC 'TRC1', 'D:\\{filename}.s1p'"
        self.inst.write(cmd4)
        self.inst.write(cmd5)
        # self.inst.write("HCOP:DEST 'MMEM'; :HCOP")

    def marker_coupled(self,state):
        cmd = f"CALC:MARK:COUP {self.states[state]}"
        self.inst.write(cmd)

    @classmethod
    def Assign_layout(self):
        cmd = ":DISPlay:LAYout:DEFine 3, Horizontal, '1.00,0.50,0.50;1.00,0.50'"
        cmd1 = ':DISPlay:LAYout:APPLy 3'
        self.inst.write(cmd)
        self.inst.write(cmd1)

########################        MARKER SETTINGS         #################################
    def setchannelEnable(self, ch_number, marker_number, state):
        cmd = f":CALC{ch_number}:MARK{marker_number} {self.states[state]}"
        self.inst.write(cmd)

    def setChannelFrequency(self, ch_number, marker_number, frequency: float, unit: str="GHz"):
        cmd = f":CALC{ch_number}:MARK{marker_number}:X {frequency}{unit}"
        print(cmd, "channel Frequency")
        self.inst.write(cmd)

    def setChannelMaxHold(self,ch_number, marker_number, state):
        cmd = f":CALC{ch_number}:MARK{marker_number}:FUNC:EXEC {self.maxHoldState[state]}"
        print(cmd)
        self.inst.write(cmd)

    def setChannelTracking(self, ch_number, marker_number, state):
        cmd = f":CALC{ch_number}:MARK{marker_number}:SEAR:TRAC {self.states[state]}"
        print(cmd)
        self.inst.write(cmd)

    def markerValue(self, ch_number, marker_number):
        cmd = f":CALC{ch_number}:MARK{marker_number}:X?"
        return self.inst.query(cmd)

    def setRange(self, channel_no, marker_no, start_freq, stop_freq, unit, user_no):
        cmd1 = f":CALC{channel_no}:MARK{marker_no} ON"
        cmd2 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER {user_no}"
        cmd3 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER:STARt {start_freq}{unit}"
        cmd4 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER:STOP {stop_freq}{unit}"
        cmd7 = f"CALC{channel_no}:MARK{marker_no}:FUNC:DOM:USER:SHOW {user_no}"
        cmd8 = f" CALC{channel_no}:STAT:DOM:USER {user_no}"
        self.inst.write(cmd1)
        print("range vna", cmd2)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd7)
        self.inst.write(cmd8)

##########################################################################################

    def VNA_savescreen(self, filename):
        print(filename)
        import time
        # time.sleep(5)
        cmd = "HCOP:DEV:LANG BMP"
        self.inst.write(cmd)
        cmd1 = "MMEMory:LOAD:LIMit"
        self.inst.write(cmd1)
        cmd2 = "MMEMory:STORe:LIMit"
        self.inst.write(cmd2)
        cmd3 = f"MMEM:NAME 'D:\\{filename}.BMP'"
        self.inst.write(cmd3)
        self.inst.write("HCOP:DEST 'MMEM'; :HCOP")

    def twoport_VNA_savescreen(self, filename,test):
        print(filename)
        import time
        # time.sleep(5)
        cmd = "HCOP:DEV:LANG BMP"
        self.inst.write(cmd)
        # cmd1 = "MMEMory:LOAD:LIMit"
        # self.inst.write(cmd1)
        cmd2 = "MMEMory:STORe:LIMit"
        self.inst.write(cmd2)
        #folderpath = f"D:\\2585"
        #os.makedirs(folderpath, exist_ok=True)
        if test == 'inter':
            for i in self.res:
                if i in filename:
                    subfold=os.path.join(self.sfolinter,i)
                    cmd3 = f"MMEM:NAME '{subfold}\\{filename}.BMP'"
                    self.inst.write(cmd3)
                    self.inst.write("HCOP:DEST 'MMEM'; :HCOP")
        elif test == 'two':
            for i in self.res:
                if i in filename:
                    subfold = os.path.join(self.sfol, i)
                    cmd3 = f"MMEM:NAME '{subfold}\\{filename}.BMP'"
                    self.inst.write(cmd3)
                    self.inst.write("HCOP:DEST 'MMEM'; :HCOP")

    def save_znxnml(self,filename):
        cmd1 = f"MMEM:STOR:STAT 1,'C:\\Users\\Public\\Documents\\Rohde-Schwarz\\ZNA\\RecallSets\\amal\\{filename}.znxml'"
        self.inst.write(cmd1)
        # self.inst.write("HCOP:DEST 'MMEM'; :HCOP")


    def sre(self,state='0'):
        '''
        Enable bits in the Status Byte enable register
        :parameter  : state-##########
        :returns    : None
        '''
        cmd = '*SRE %s' % (state)
        self.inst.write(cmd)

    def getSre(self):
        '''
        Queries the Status Byte Enable register. The power supply returns a decimal
        value which corresponds to the binary-weighted sum of all bits sets in the enable register

        :parameter  : None
        :returns    : dict
        '''
        cmd = '*SRE?'
        return {'sre': str(self.inst.query(cmd))}

    def getStb(self):
        '''
        Queries the status byte summary register
        :parameter  : None
        :returns    : dict
        '''
        cmd = '*STB?'
        return {'stb': str(self.inst.query(cmd))}

    def wait(self):
        '''
        The Wait–to–Continue (WAI) command causes the signal generator to wait until
        all pending commands are completed,before executing any other commands.
        :parameter  : None
        :returns    : None
        '''

        cmd = '*WAI'
        self.inst.write(cmd)

    def getIdn(self):
        '''
        The Identification (IDN) Queries outputs an identifying string.
        The response will show the following information:<manufacturer's name>, <model number>, <not used-always 0>, <revision number>

        :parameter  : None
        :returns    : dict
        '''
        cmd = '*IDN?'
        return {'Idn': self.inst.query(cmd)}
    
    def scale_div(self, window: int, pDiv:int, rLev:int, rPos:int):

        cmd4 = f"DISP:WIND{window}:STAT ON"
        # cmd5 = "DISP:WIND2:STAT ON"
        # cmd6 = "DISP:WIND2:STAT ON"
        cmd10=f"DISP:WIND{window}:TRAC1:Y:PDIV {pDiv}"        
        cmd13=f"DISP:WIND{window}:TRAC1:Y:RLEV {rLev}"
        cmd16=f"DISP:WIND{window}:TRAC1:Y:RPOS {rPos}"

        self.inst.write(cmd4)
        # self.inst.write(cmd5)
        # self.inst.write(cmd6)
        self.inst.write(cmd10)
        self.inst.write(cmd13)
        self.inst.write(cmd16)

    # def create_folder(self,filename):
    #     #creating folder name by file name entered by user
    #     self.folderpath = f"D:\\{filename}"
    #     os.makedirs(self.folderpath, exist_ok=True)
    #     #creating subfolders by port names
    #     with open("text.txt", 'r') as file:
    #         con = file.read()
    #     data = ast.literal_eval(con)  # Parse data from the file
    #     self.res = [item[1] for item in data]
    #     for i in self.res:
    #         subfolder_path=os.path.join(self.folderpath,i)
    #         os.makedirs(subfolder_path,exist_ok=True)

    def create_folder_two_port(self,filename):
        #creating folder name by file name entered by user
        self.path = f"D:\\"
        self.folderpathold = f"D:\\{filename}"
        # if os.path.exists(self.folderpathold):
        #     timestamp= datetime.now().strftime("%Y%m%d_%H%M%S")
        #     self.name=f"{filename}_{timestamp}"
        #     self.folderpath=os.path.join(self.path,self.name)
        # else:
        self.folderpath=os.path.join(self.path,filename)

        os.makedirs(self.folderpath, exist_ok=True)

        self.sfol=os.path.join(self.folderpath,f"S-Parameter")
        os.makedirs(self.sfol,exist_ok=True)
        #creating subfolders by port names
        with open("text.txt", 'r') as file:
            con = file.read()
        data = ast.literal_eval(con)  # Parse data from the file
        self.res = [item[1] for item in data]
        for i in self.res:
            subfolder_path=os.path.join(self.sfol,i)
            os.makedirs(subfolder_path,exist_ok=True)

    def create_folder_interBand_port(self,filename):
        #creating folder name by file name entered by user
        self.folderpath = f"D:\\{filename}"
        os.makedirs(self.folderpath, exist_ok=True)

        self.sfolinter=os.path.join(self.folderpath,f"InterBand")
        os.makedirs(self.sfolinter,exist_ok=True)
        #creating subfolders by port names
        with open("text.txt", 'r') as file:
            con = file.read()
        data = ast.literal_eval(con)  # Parse data from the file
        self.res = [item[1] for item in data]
        for i in self.res:
            subfolder_path=os.path.join(self.sfolinter,i)
            os.makedirs(subfolder_path,exist_ok=True)

    # def Marker_Text(self,filename):
    #     for i in self.res:
    #         if i in filename:
    #             subfold = os.path.join(self.folderpath, i)
    #             #path=f"{subfold}\\Marker{filename}.txt"
    #             path = os.path.join(subfold, f"Marker{filename}.txt")
    #             cmd1 = f"MMEM:STOR:MARK '{path}'"
    #     self.inst.write(cmd1)
    #     self.inst.write("HCOP:DEST 'MMEM'; :HCOP")
    #     print(f"path from marker_text{subfold}")
    #     excel.get_port_name_from_filename(path, subfold)

    def Marker_Text(self,filename,test):
        print(filename, "filename 716")
        if test == 'two':
            for i in self.res:
                if i in filename:
                    ex = self.sfol
                    subfold = os.path.join(self.sfol, i)
                    # path=f"{subfold}\\Marker{filename}.txt"
                    path = os.path.join(subfold, f"Marker{filename}.txt")
                    cmd1 = f"MMEM:STOR:MARK '{path}'"
                    self.inst.write(cmd1)
                    # self.inst.write("HCOP:DEST 'MMEM'; :HCOP")
            print(f"path from marker_text single or two port{subfold}")
            excel.get_port_name_from_filename(path, subfold, ex)
        elif test == 'inter':
            for i in self.res:
                if i in filename:
                    subfold = os.path.join(self.sfolinter, i)
                    # path=f"{subfold}\\Marker{filename}.txt"
                    path = os.path.join(subfold, f"Marker{filename}.txt")
                    cmd1 = f"MMEM:STOR:MARK '{path}'"
                    self.inst.write(cmd1)
                    # self.inst.write("HCOP:DEST 'MMEM'; :HCOP")
            print(f"path from marker_text interband{subfold}")
            NewInterband.get_interband(path, subfold)

    def smooth_multi_trace(self,smooth_shift):

        cmd1 = f"CALC1:PHOLD {smooth_shift}"
        self.inst.write(cmd1)

    def format_multi_trace(self, format):

        cmd4 = f"CALC1:FORM {format}"
        self.inst.write(cmd4)

    def trace_window_multi_trace(self, S_parameter):

        # cmd1 = f':DISPLAY:WINDOW1:STATE ON'
        cmd2 = f':CALCULATE1:PARAMETER:SDEFINE "Trc1","{S_parameter}"'
        cmd3 = f":DISPLAY:WINDOW1:TRACE1:FEED 'Trc1'"
        # self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)

    def Assign_layout_four_win(self):
        cmd = ":DISPlay:LAYout:DEFine 4, Horizontal, '1.00,0.50,0.50;1.00,0.50,0.50'"
        cmd1 = ':DISPlay:LAYout:APPLy 4'
        self.inst.write(cmd)
        self.inst.write(cmd1)

    def smooth_off(self,smooth_shift):
        cmd1 = f"CALC1:PHOLD {smooth_shift}"
        self.inst.write(cmd1)

    def mark_multitrace(self,m1state,m2state,m3state,m4state,start_freq, stop_freq,trackmax,trackstate,range1,range_start_freq1,range_stop_freq1,show_range1,range2,range_start_freq2,range_stop_freq2,show_range2):

        cmd16 = f":CALC1:MARK1 {m1state}"
        cmd17 = f":CALC1:MARK2 {m2state}"
        cmd18 = f":CALC1:MARK3 {m3state}"
        cmd19 = f":CALC1:MARK4 {m4state}"
        cmd20 = f":CALC1:MARK1:X {start_freq}MHz"
        cmd21 = f":CALC1:MARK2:X {stop_freq}MHz"

        cmd22 = f"CALC1:MARK3:FUNC:DOM:USER {range1}"
        cmd23 = f"CALC1:MARK3:FUNC:DOM:USER:STARt {range_start_freq1}MHz"
        cmd24 = f"CALC1:MARK3:FUNC:DOM:USER:STOP {range_stop_freq1}MHz"
        cmd25 = f":CALC1:MARK3:FUNC:EXEC {trackmax}"
        cmd26 = f":CALC1:MARK3:SEAR:TRAC {trackstate}"
        cmd27 = f"CALC1:MARK5:FUNC:DOM:USER:SHOW {show_range1}"
        cmd28 = f" CALC1:STAT:DOM:USER {show_range1}"

        cmd29 = f"CALC1:MARK4:FUNC:DOM:USER {range2}"
        cmd30 = f"CALC1:MARK4:FUNC:DOM:USER:STARt {range_start_freq2}MHz"
        cmd31 = f"CALC1:MARK4:FUNC:DOM:USER:STOP {range_stop_freq2}MHz"
        cmd32 = f":CALC1:MARK4:FUNC:EXEC {trackmax}"
        cmd33 = f":CALC1:MARK4:SEAR:TRAC {trackstate}"
        cmd34 = f"CALC1:MARK4:FUNC:DOM:USER:SHOW {show_range2}"
        cmd35 = f" CALC1:STAT:DOM:USER {show_range2}"

        self.inst.write(cmd16)
        self.inst.write(cmd17)
        self.inst.write(cmd18)
        self.inst.write(cmd19)
        self.inst.write(cmd20)
        self.inst.write(cmd21)
        self.inst.write(cmd22)
        self.inst.write(cmd23)
        self.inst.write(cmd24)
        self.inst.write(cmd25)
        self.inst.write(cmd26)
        self.inst.write(cmd27)
        self.inst.write(cmd28)
        self.inst.write(cmd29)
        self.inst.write(cmd30)
        self.inst.write(cmd31)
        self.inst.write(cmd32)
        self.inst.write(cmd33)
        self.inst.write(cmd34)
        self.inst.write(cmd35)

    def scale_division_multi_trace(self,pDiv: int, rLev: int, rPos: int):

        cmd4 = f"DISP:WIND{1}:STAT ON"
        cmd10 = f"DISP:WIND{1}:TRAC1:Y:PDIV {pDiv}"
        cmd13 = f"DISP:WIND{1}:TRAC1:Y:RLEV {rLev}"
        cmd16 = f"DISP:WIND{1}:TRAC1:Y:RPOS {rPos}"
        self.inst.write(cmd4)
        self.inst.write(cmd10)
        self.inst.write(cmd13)
        self.inst.write(cmd16)

    # def inter_band(self,freq_range,b,tilt,filename,znxmlname):
    #
    #     # freq_range = ['2500','2690']#, "698,824", "1695,2360", "1427,2690", "1695,2690", "3300,5500"]
    #     # print(freq_range)
    #     freq_range1 = ['1427','2690']
    #     # window_num = [1, 2, 3, 4]
    #     window_num = [1, 2, 3]
    #     # format = ["SWR", "SWR", "MAGN"]
    #     smooth_shift_hold = ["OFF", "MAX"]
    #     #pDiv = [0.1, 0.1, 5]
    #     #rlev = [1.5, 1.5, -25]
    #     #s_param = ["S13", "S14", "S23", "S24"]
    #     # tilt = [2.5,5,10]#,[2,7,12],[3,7,12]]
    #     # b = [['R1','R2']]#,['Y1','Y4'],['Y2','Y3']]
    #     # freq = ["'698','960'"]#, "'1695','2690'", "'1427','2690'"]
    #
    #     # filename = input("enter filename:")
    #
    #     with open("text.txt",'r') as file:
    #         x=file.read()
    #         i = eval(x)
    #         c = []
    #         for ports in b:
    #             for po in ports:
    #                 for _ in i:
    #                     if po in _:
    #                         c.append(i[i.index(_)][0])
    #         # print(c)
    #
    #     port1 = c
    #     print(port1)
    #     start_fr = freq_range[0]
    #     print(start_fr)
    #     stop_fr = freq_range[-1]
    #     print(stop_fr)
    #     rev = port1[::-1]
    #     cde = []
    #     cde.append(port1)
    #     cde.append(rev)
    #
    #     # for fr in freq:
    #     #     start_fr, stop_fr = fr.split(",")
    #     #     print(start_fr, stop_fr)
    #     #     print(fr)
    #     #     print(freq_range1)
    #
    #     for index in range(len(cde)):
    #
    #         if index % 2 == 0:
    #             port1 = cde[index]
    #             # s_param = ["S13", "S14", "S23", "S24"]
    #             s_param = ["S13", "S14", "S23"]
    #             p = b[0][0]
    #             # znxmlname = znxmlname1
    #         else:
    #             port1 = cde[index]
    #             # s_param = ["S31", "S32", "S41", "S42"]
    #             s_param = ["S31", "S32", "S41"]
    #             p = b[0][1]
    #             #znxmlname = znxmlname2
    #
    #         if freq_range != freq_range1:
    #
    #             for a in smooth_shift_hold:
    #
    #                 if a == 'OFF':
    #
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency( start_fr, stop_fr, "MHz")
    #
    #                     for port in port1:
    #                         newtilt = int(tilt[0] * 10)
    #                         print(newtilt)
    #                         self.ccuLib.settilt(port, newtilt)
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(newtilt)
    #                         time.sleep(16)
    #
    #                 if a == 'MAX':
    #
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency(start_fr, stop_fr, "MHz")
    #
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i],"MAGN","ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)
    #                         self.Assign_layout()
    #
    #                     for i in range(3):
    #                         self.scale_div(window_num[i],5,'-25',50)
    #                         self.updated_set_sweep_points()
    #
    #                     for port in port1:
    #                         newtilt = int(tilt[-1] * 10)
    #                         print(newtilt)
    #                         self.ccuLib.settilt(port,newtilt)
    #                         print("before time sleep")
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(newtilt)
    #                         time.sleep(15)
    #                             # self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase")
    #                             # self.save_S2P(f"{filename}_{p}_{tilt[-1]}_wrostcase")
    #                             # time.sleep(5)
    #                             # print("passed")
    #
    #                     for port in port1:
    #                         newtilt = int(tilt[0] * 10)
    #                         print(newtilt)
    #                         self.ccuLib.settilt(port, newtilt)
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(newtilt)
    #                         time.sleep(16)
    #                         print(p,"ports is completed. ")
    #
    #                     self.VNA_savescreen(f"{filename}")
    #
    #         else:
    #
    #             for a in smooth_shift_hold:
    #
    #                 if a == 'OFF':
    #
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency( start_fr, stop_fr, "MHz")
    #
    #                     for port in port1:
    #                         newtilt = int(tilt[0] * 10)
    #                         print(newtilt)
    #                         self.ccuLib.settilt(port, newtilt)
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(newtilt)
    #                         time.sleep(16)
    #
    #                 if a == 'MAX':
    #
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency(start_fr, stop_fr, "MHz")
    #
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], "MAGN", "ON", "ON", "ON",
    #                                                             "OFF", start_fr, stop_fr, "MAX", "ON", a, range1=None,
    #                                                             range_start_freq1=None, range_stop_freq1=None,
    #                                                             show_range1=None, range2=None, range_start_freq2=None,
    #                                                             range_stop_freq2=None, show_range2=None)
    #                         self.Assign_layout()
    #
    #                     for i in range(3):
    #                         self.scale_div(window_num[i], 5, '-25', 50)
    #                         self.updated_set_sweep_points()
    #
    #                     for port in port1:
    #                         newtilt = int(tilt[-1] * 10)
    #                         print(newtilt)
    #                         self.ccuLib.settilt(port, newtilt)
    #                         print("before time sleep")
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(newtilt)
    #                         time.sleep(15)
    #                             # self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase")
    #                             # self.save_S2P(f"{filename}_{p}_{tilt[-1]}_wrostcase")
    #                             # time.sleep(5)
    #                             # print("passed")
    #
    #                     for port in port1:
    #                         newtilt = int(tilt[0] * 10)
    #                         print(newtilt)
    #                         self.ccuLib.settilt(port, newtilt)
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(newtilt)
    #                         time.sleep(16)
    #                         print(p, "ports is completed. ")
    #
    #                     self.VNA_savescreen(f"{filename}")

    def interband(self,freq_range,b,tilt,filename,znxmlname):
        freq_range1 = ['1427', '2690']
        window_num = [1, 2, 3, 4]
        smooth_shift_hold = ["OFF", "MAX"]
        # s_param = ["S12","S14","S32","S34"]
        with open("text.txt", 'r') as file:
            x = file.read()
            i = eval(x)
            c = []
            for ports in b:
                for po in ports:
                    for _ in i:
                        if po in _:
                            c.append(i[i.index(_)][0])

        port1 = c
        print(port1)
        start_fr = freq_range[0]
        print(start_fr)
        stop_fr = freq_range[-1]
        print(stop_fr)
        rev = port1[::-1]
        cde = []
        cde.append(port1)
        cde.append(rev)
        print(cde)
        for index in range(len(cde)):

            if index % 2 == 0:
                port1 = cde[index]
                s_param = ["S13", "S14", "S23","S24"]
                p = b[0][0]
                # znxmlname = znxmlname1
            else:
                port1 = cde[index]
                s_param = ["S31", "S32", "S41","S42"]
                p = b[0][1]
                #znxmlname = znxmlname2

            if freq_range != freq_range1:

                for a in smooth_shift_hold:

                    if a == 'OFF':
                        DSOX3054T.smooth_off(self,a)

                        # self.RST()
                        # DSOX3054T.load_znxnml(self,znxmlname)
                        # DSOX3054T.Frequency(self, start_fr, stop_fr, "MHz")

                        for port in port1:
                            newtilt = int(tilt[0] * 10)
                            print(newtilt)
                            self.ccuLib.settilt(port, newtilt)
                            time.sleep(2)
                            self.ccuLib.getcommandresults()
                            time.sleep(16)

                    if a == 'MAX':

                        # self.RST()
                        self.load_znxnml(znxmlname)
                        self.Frequency(start_fr, stop_fr, "MHz")

                        for i in range(4):
                            self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], "MAGN", "ON", "ON", "ON",
                                                            "OFF", start_fr, stop_fr, "MAX", "ON", a, range1=None,
                                                            range_start_freq1=None, range_stop_freq1=None,
                                                            show_range1=None, range2=None, range_start_freq2=None,
                                                            range_stop_freq2=None, show_range2=None)
                        self.Assign_layout_four_win()


                        for i in range(4):
                            self.scale_div(window_num[i],5,'-25',50)
                            self.updated_set_sweep_points()

                        for port in port1:
                            newtilt = int(tilt[-1] * 10)
                            print(newtilt)
                            self.ccuLib.settilt(port,newtilt)
                            print("before time sleep")
                            time.sleep(2)
                            self.ccuLib.getcommandresults()
                            print(newtilt)
                            time.sleep(15)

                        for port in port1:
                            newtilt = int(tilt[0] * 10)
                            print(newtilt)
                            self.ccuLib.settilt(port, newtilt)
                            time.sleep(2)
                            self.ccuLib.getcommandresults()
                            print(newtilt)
                            time.sleep(16)
                            print(p,"ports is completed. ")

                        self.VNA_savescreen(f"{filename}",f"inter")
                        self.Marker_Text(f"R1_constant",f"inter")

            else:
                for a in smooth_shift_hold:

                    if a == 'OFF':
                        DSOX3054T.smooth_off(self, a)

                        # self.RST()
                        # DSOX3054T.load_znxnml(self,znxmlname)
                        # DSOX3054T.Frequency(self, start_fr, stop_fr, "MHz")

                        for port in port1:
                            newtilt = int(tilt[0] * 10)
                            print(newtilt)
                            self.ccuLib.settilt(port, newtilt)
                            time.sleep(2)
                            self.ccuLib.getcommandresults()
                            print(newtilt)
                            time.sleep(16)

                    if a == 'MAX':

                        # self.RST()
                        self.load_znxnml(znxmlname)
                        self.Frequency(start_fr, stop_fr, "MHz")

                        for i in range(4):
                            self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], "MAGN", "ON", "ON", "ON",
                                                            "OFF", start_fr, stop_fr, "MAX", "ON", a, range1=None,
                                                            range_start_freq1=None, range_stop_freq1=None,
                                                            show_range1=None, range2=None, range_start_freq2=None,
                                                            range_stop_freq2=None, show_range2=None)
                        self.Assign_layout_four_win()

                        for i in range(4):
                            self.scale_div(window_num[i], 5, '-25', 50)
                            self.updated_set_sweep_points()

                        for port in port1:
                            newtilt = int(tilt[-1] * 10)
                            print(newtilt)
                            self.ccuLib.settilt(port, newtilt)
                            print("before time sleep")
                            time.sleep(2)
                            self.ccuLib.getcommandresults()
                            print(newtilt)
                            time.sleep(15)

                        for port in port1:
                            newtilt = int(tilt[0] * 10)
                            print(newtilt)
                            self.ccuLib.settilt(port, newtilt)
                            time.sleep(2)
                            self.ccuLib.getcommandresults()
                            print(newtilt)
                            time.sleep(16)
                            print(p, "ports is completed. ")

                        self.VNA_savescreen(f"{filename}", f"inter")


    # def two_port(self,freq_range,b,tilt,filename,znxmlname):
    #
    #     # freq_range = ['2500','2690']#, "698,824", "1695,2360", "1427,2690", "1695,2690", "3300,5500"]
    #     # print(freq_range)
    #     freq_range1 = ['1427','2690']
    #     window_num = [1, 2, 3]
    #     format = ["SWR", "SWR", "MAGN"]
    #     smooth_shift_hold = ["OFF", "MAX"]
    #     pDiv = [0.1, 0.1, 5]
    #     rlev = [1.5, 1.5, -25]
    #     # tilt = [2.5,5,10]#,[2,7,12],[3,7,12]]
    #     # b = [['R1','R2']]#,['Y1','Y4'],['Y2','Y3']]
    #     # freq = ["'698','960'"]#, "'1695','2690'", "'1427','2690'"]
    #
    #     # filename = input("enter filename:")
    #
    #     with open("text.txt",'r') as file:
    #         x=file.read()
    #         i = eval(x)
    #         c = []
    #         for ports in b:
    #             for po in ports:
    #                 for _ in i:
    #                     if po in _:
    #                         c.append(i[i.index(_)][0])
    #         # print(c)
    #
    #     port1 = c
    #     print(port1)
    #     start_fr = freq_range[0]
    #     print(start_fr)
    #     stop_fr = freq_range[-1]
    #     print(stop_fr)
    #
    #     # for fr in freq:
    #     #     start_fr, stop_fr = fr.split(",")
    #     #     print(start_fr, stop_fr)
    #     #     print(fr)
    #     #     print(freq_range1)
    #
    #     for index in range(len(port1)):
    #
    #         if index % 2 == 0:
    #             port = port1[index]
    #             s_param = ["S11", "S22", "S21"]
    #             p = b[0][0]
    #             # znxmlname = znxmlname1
    #         else:
    #             port = port1[index]
    #             s_param = ["S33", "S44", "S43"]
    #             p = b[0][1]
    #             #znxmlname = znxmlname2
    #
    #         if freq_range != freq_range1:
    #
    #             for a in smooth_shift_hold:
    #
    #                 if a == 'OFF':
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency( start_fr, stop_fr, "MHz")
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i],"ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)
    #
    #                     self.Assign_layout()
    #                     for i in range(3):
    #                         self.scale_div(window_num[i],pDiv[i],rlev[i],50)
    #                     self.updated_set_sweep_points()
    #
    #                     for degree in tilt:
    #                         degName = int(degree * 10)
    #                         self.ccuLib.settilt(port,degName)
    #                         print("before time sleep")
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(degree)
    #                         time.sleep(15)
    #                         self.VNA_savescreen(f"{filename}_{p}_{degree}")
    #                         self.save_S2P(f"{filename}_{p}_{degree}")
    #                         time.sleep(1)
    #                         print("passed")
    #
    #                     new_tilt = int(tilt[0] * 10)
    #                     print(new_tilt)
    #                     self.ccuLib.settilt(port, new_tilt)
    #                     print(port,new_tilt)
    #                     time.sleep(2)
    #                     self.ccuLib.getcommandresults()
    #                     print(new_tilt)
    #                     time.sleep(15)
    #
    #                 if a == 'MAX':
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency(start_fr, stop_fr, "MHz")
    #
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i],"ON","ON","ON","OFF",start_fr, stop_fr,"MAX","ON",a,range1 = None,range_start_freq1 = None,range_stop_freq1 = None,show_range1 = None,range2 = None,range_start_freq2 = None,range_stop_freq2 = None,show_range2 = None)
    #                     self.Assign_layout()
    #
    #                     for i in range(3):
    #                         self.scale_div(window_num[i],pDiv[i],rlev[i],50)
    #                     self.updated_set_sweep_points()
    #
    #                     newtilt = int(tilt[-1] * 10)
    #                     print(newtilt)
    #                     self.ccuLib.settilt(port,newtilt)
    #                     print("before time sleep")
    #                     time.sleep(2)
    #                     self.ccuLib.getcommandresults()
    #                     print(newtilt)
    #                     time.sleep(15)
    #                     self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_wrostcase")
    #                     self.save_S2P(f"{filename}_{p}_{tilt[-1]}_wrostcase")
    #                     time.sleep(5)
    #                     print("passed")
    #
    #                     newtilt = int(tilt[0] * 10)
    #                     print(newtilt)
    #                     self.ccuLib.settilt(port, newtilt)
    #                     time.sleep(2)
    #                     self.ccuLib.getcommandresults()
    #                     print(newtilt)
    #                     time.sleep(16)
    #                     print(p,"ports is completed. ")
    #
    #         else:
    #
    #             for a in smooth_shift_hold:
    #
    #                 if a == 'OFF':
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency( start_fr,stop_fr,"MHz")
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i],"ON")
    #                         self.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
    #                     self.Assign_layout()
    #                     for i in range(3):
    #                         self.scale_div(window_num[i], pDiv[i], rlev[i], 50)
    #                     self.updated_set_sweep_points()
    #
    #                     for degree in tilt:
    #                         degName = int(degree * 10)
    #                         self.ccuLib.settilt(port, degName)
    #                         print("before time sleep")
    #                         time.sleep(2)
    #                         self.ccuLib.getcommandresults()
    #                         print(degree)
    #                         time.sleep(16)
    #                         self.VNA_savescreen(f"{filename}_{p}_{degree}")
    #                         self.save_S2P(f"{filename}_{p}_{degree}")
    #                         time.sleep(1)
    #                         print("passed")
    #
    #                     new_tilt = int(tilt[0] * 10)
    #                     print(new_tilt)
    #                     self.ccuLib.settilt(port, new_tilt)
    #                     print(port, new_tilt)
    #                     time.sleep(2)
    #                     self.ccuLib.getcommandresults()
    #                     print(new_tilt)
    #                     time.sleep(16)
    #
    #                 if a == 'MAX':
    #                     self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency( start_fr,stop_fr,"MHz")
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i],"ON")
    #                         self.updated_Assign_tracewindow(window_num[i],"ON",s_param[i],format[i],"ON","ON","ON","ON",start_fr,stop_fr,"MAX","ON",a,1,1427,1518,1,2,1695,2690,1)
    #                     self.Assign_layout()
    #                     for i in range(3):
    #                         self.scale_div(window_num[i],pDiv[i],rlev[i],50)
    #                     self.updated_set_sweep_points()
    #
    #                     newtilt = int(tilt[-1] * 10)
    #                     print(newtilt)
    #                     self.ccuLib.settilt(port, newtilt)
    #                     time.sleep(2)
    #                     self.ccuLib.getcommandresults()
    #                     print(newtilt)
    #                     time.sleep(16)
    #                     self.VNA_savescreen(f"{filename}_{p}_{newtilt}_worstcase")
    #                     self.save_S2P(f"{filename}_{p}_{newtilt}_worstcase")
    #                     time.sleep(1)
    #                     print("passed")
    #
    #                     new_tilt = int(tilt[0] * 10)
    #                     print(new_tilt)
    #                     self.ccuLib.settilt(port, new_tilt)
    #                     time.sleep(2)
    #                     self.ccuLib.getcommandresults()
    #                     print(new_tilt)
    #                     time.sleep(15)
    #                     print(p, "ports is completed. ")
    # def two_port(self, freq_range, b, tilt, filename, znxmlname):
    #
    #     # freq_range = ['2500','2690']#, "698,824", "1695,2360", "1427,2690", "1695,2690", "3300,5500"]
    #     # print(freq_range)
    #     print(b, "ports")
    #     self.create_folder_two_port(filename)
    #     freq_range1 = ['1427', '2690']
    #     window_num = [1, 2, 3]
    #     format = ["SWR", "SWR", "MAGN"]
    #     smooth_shift_hold = ["OFF", "MAX"]
    #     pDiv = [0.1, 0.1, 5]
    #     rlev = [1.5, 1.5, -25]
    #     # tilt = [2.5,5,10]#,[2,7,12],[3,7,12]]
    #     # b = [['R1','R2']]#,['Y1','Y4'],['Y2','Y3']]
    #     # freq = ["'698','960'"]#, "'1695','2690'", "'1427','2690'"]
    #
    #     # filename = input("enter filename:")
    #
    #     with open("text.txt", 'r') as file:
    #         x = file.read()
    #         i = eval(x)
    #         c = []
    #         for ports in b:
    #             for po in ports:
    #                 for _ in i:
    #                     if po in _:
    #                         c.append(i[i.index(_)][0])
    #         # print(c)
    #
    #     port1 = c
    #     print(port1)
    #     start_fr = freq_range[0]
    #     print(start_fr)
    #     stop_fr = freq_range[-1]
    #     print(stop_fr)
    #
    #     # for fr in freq:
    #     #     start_fr, stop_fr = fr.split(",")
    #     #     print(start_fr, stop_fr)
    #     #     print(fr)
    #     #     print(freq_range1)
    #
    #     for index in range(len(port1)):
    #
    #         if index % 2 == 0:
    #             port = port1[index]
    #             s_param = ["S11", "S22", "S21"]
    #             p = b[0][0]
    #             # znxmlname = znxmlname1
    #         else:
    #             port = port1[index]
    #             s_param = ["S33", "S44", "S43"]
    #             p = b[0][1]
    #             # znxmlname = znxmlname2
    #
    #         if freq_range != freq_range1:
    #
    #             for a in smooth_shift_hold:
    #
    #                 if a == 'OFF':
    #                     # self.RST()
    #                     DSOX3054T.load_znxnml(self, znxmlname)
    #                     DSOX3054T.Frequency(self, start_fr, stop_fr, "MHz")
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i], "ON", "ON",
    #                                                         "ON", "OFF", start_fr, stop_fr, "MAX", "ON", a, range1=None,
    #                                                         range_start_freq1=None, range_stop_freq1=None,
    #                                                         show_range1=None, range2=None, range_start_freq2=None,
    #                                                         range_stop_freq2=None, show_range2=None)
    #
    #                     self.Assign_layout()
    #                     for i in range(3):
    #                         self.scale_div(window_num[i], pDiv[i], rlev[i], 50)
    #                     self.updated_set_sweep_points()
    #
    #                     for degree in tilt:
    #                         a = ['min', 'mid', 'max']
    #                         degName = int(degree * 10)
    #                         self.ccuLib.settilt(port, degName)
    #                         print("before time sleep")
    #                         time.sleep(2)
    #                         # self.ccuLib.getcommandresults()
    #                         # print(degree)
    #                         # time.sleep(15)
    #                         # self.Marker_Text(f"{filename}_{p}_{a[tilt.index(degree)]}")
    #                         self.VNA_savescreen(f"{filename}_{p}_{a[tilt.index(degree)]}", f"two")
    #                         self.save_S2P(f"{filename}_{p}_{a[tilt.index(degree)]}", f"two")
    #                         self.Marker_Text(f"{filename}_{p}_{a[tilt.index(degree)]}", f"two")
    #                         # time.sleep(1)
    #                         print("passed")
    #
    #                     new_tilt = int(tilt[0] * 10)
    #                     print(new_tilt)
    #                     self.ccuLib.settilt(port, new_tilt)
    #                     print(port, new_tilt)
    #                     # time.sleep(2)
    #                     # self.ccuLib.getcommandresults()
    #                     # print(new_tilt)
    #                     # time.sleep(15)
    #
    #                 if a == 'MAX':
    #                     # self.RST()
    #                     self.load_znxnml(znxmlname)
    #                     self.Frequency(start_fr, stop_fr, "MHz")
    #
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i], "ON", "ON",
    #                                                         "ON", "OFF", start_fr, stop_fr, "MAX", "ON", a, range1=None,
    #                                                         range_start_freq1=None, range_stop_freq1=None,
    #                                                         show_range1=None, range2=None, range_start_freq2=None,
    #                                                         range_stop_freq2=None, show_range2=None)
    #                     self.Assign_layout()
    #
    #                     for i in range(3):
    #                         self.scale_div(window_num[i], pDiv[i], rlev[i], 50)
    #                     self.updated_set_sweep_points()
    #
    #                     newtilt = int(tilt[-1] * 10)
    #                     print(newtilt)
    #                     self.ccuLib.settilt(port, newtilt)
    #                     print("before time sleep")
    #                     # time.sleep(2)
    #                     # self.ccuLib.getcommandresults()
    #                     # print(newtilt)
    #                     # time.sleep(15)
    #                     self.Marker_Text(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
    #                     self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
    #                     self.save_S2P(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
    #                     # time.sleep(5)
    #                     print("passed")
    #
    #                     newtilt = int(tilt[0] * 10)
    #                     print(newtilt)
    #                     self.ccuLib.settilt(port, newtilt)
    #                     # time.sleep(2)
    #                     # self.ccuLib.getcommandresults()
    #                     # print(newtilt)
    #                     # time.sleep(16)
    #                     print(p, "ports is completed. ")
    #
    #         else:
    #
    #             for a in smooth_shift_hold:
    #
    #                 if a == 'OFF':
    #                     # self.RST()
    #                     DSOX3054T.load_znxnml(self, znxmlname)
    #                     DSOX3054T.Frequency(self, start_fr, stop_fr, "MHz")
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i], "ON", "ON",
    #                                                         "ON", "ON", start_fr, stop_fr, "MAX", "ON", a, 1, 1427,
    #                                                         1518, 1, 2, 1695, 2690, 1)
    #                     self.Assign_layout()
    #                     for i in range(3):
    #                         self.scale_div(window_num[i], pDiv[i], rlev[i], 50)
    #                     self.updated_set_sweep_points()
    #
    #                     for degree in tilt:
    #                         at = ['min', 'mid', 'max']
    #                         degName = int(degree * 10)
    #                         self.ccuLib.settilt(port, degName)
    #                         print("before time sleep")
    #                         # time.sleep(2)
    #                         # self.ccuLib.getcommandresults()
    #                         # print(degree)
    #                         # time.sleep(16)
    #                         self.Marker_Text(f"{filename}_{p}_{at[tilt.index(degree)]}", f"two")
    #                         self.VNA_savescreen(f"{filename}_{p}_{at[tilt.index(degree)]}", f"two")
    #                         self.save_S2P(f"{filename}_{p}_{at[tilt.index(degree)]}", f"two")
    #                         # time.sleep(1)
    #                         print("passed")
    #
    #                     new_tilt = int(tilt[0] * 10)
    #                     print(new_tilt)
    #                     self.ccuLib.settilt(port, new_tilt)
    #                     print(port, new_tilt)
    #                     # time.sleep(2)
    #                     # self.ccuLib.getcommandresults()
    #                     # print(new_tilt)
    #                     # time.sleep(16)
    #
    #                 if a == 'MAX':
    #                     # self.RST()
    #                     DSOX3054T.load_znxnml(self, znxmlname)
    #                     DSOX3054T.Frequency(self, start_fr, stop_fr, "MHz")
    #                     for i in range(3):
    #                         self.Trace_window(window_num[i], "ON")
    #                         self.updated_Assign_tracewindow(window_num[i], "ON", s_param[i], format[i], "ON", "ON",
    #                                                         "ON", "ON", start_fr, stop_fr, "MAX", "ON", a, 1, 1427,
    #                                                         1518, 1, 2, 1695, 2690, 1)
    #                     self.Assign_layout()
    #                     for i in range(3):
    #                         self.scale_div(window_num[i], pDiv[i], rlev[i], 50)
    #                     self.updated_set_sweep_points()
    #
    #                     newtilt = int(tilt[-1] * 10)
    #                     print(newtilt)
    #                     self.ccuLib.settilt(port, newtilt)
    #                     # time.sleep(2)
    #                     # self.ccuLib.getcommandresults()
    #                     print(newtilt)
    #                     # time.sleep(16)
    #                     # self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase")
    #                     self.Marker_Text(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
    #                     self.VNA_savescreen(f"{filename}_{p}_{tilt[-1]}_worstcase", f"two")
    #                     self.save_S2P(f"{filename}_{p}_{newtilt}_worstcase", f"two")
    #                     # time.sleep(1)
    #                     print("passed")
    #
    #                     new_tilt = int(tilt[0] * 10)
    #                     print(new_tilt)
    #                     self.ccuLib.settilt(port, new_tilt)
    #                     # time.sleep(2)
    #                     # self.ccuLib.getcommandresults()
    #                     # print(new_tilt)
    #                     # time.sleep(15)
    #                     print(p, "ports is completed. ")
    #
    def mem_multi_trace(self,num):

        cmd1 = f':DISPLAY:WINDOW1:STATE ON'
        cmd2 = f":TRACE:COPY 'Mem{num}x[Trc{num}]',CH{1}DATA"
        cmd3 = f":DISPLAY:WINDOW{1}:TRACE{num}:FEED 'Mem{num}x[Trc{num}]'"
        cmd4 = f":TRACE: COPY MDATA{1}, CH{1}DATA"
        cmd5 = f":DISPLAY: WINDOW{1}:TRACE{1}: FEED'Mem{num}[Trc{num}]'"

        self.inst.write(cmd1)
        self.inst.write(cmd2)
        self.inst.write(cmd3)
        self.inst.write(cmd4)
        self.inst.write(cmd5)

    def multi_trace(self,freq_range,b,tilt,filename,znxmlname):

        freq_range1 = ['1427','2690']
        smooth_shift_hold = ['OFF','MAX']
        start_fr = freq_range[0]
        print(start_fr)
        stop_fr = freq_range[-1]
        print(stop_fr)
        l = len(tilt)-1

        with open("text.txt",'r') as file:
            x=file.read()
            i = eval(x)
            c = []
            for ports in b:
                for po in ports:
                    for _ in i:
                        if po in _:
                            c.append(i[i.index(_)][0])
            # print(c)

        port1 = c

        z = len(tilt)
        print(z)
        mem = []
        for i in range(z):
            mem.append(i + 2)
        print(mem)

        zipped = zip(tilt, mem)

        for index in range(len(port1)):

            if index % 2 == 0:
                port = port1[index]
                s_param = "S11"
                p = b[0][0]

            else:
                port = port1[index]
                s_param = "S11"
                p = b[0][1]
            if freq_range != freq_range1:

                self.RST()
                self.load_znxnml( znxmlname)
                self.Frequency( start_fr, stop_fr, "MHz")
                self.trace_window_multi_trace(s_param)
                self.smooth_multi_trace('OFF')
                self.format_multi_trace("SWR")
                self.mark_multitrace("ON","ON","ON","OFF",start_fr,stop_fr,"MAX","ON",range1=None,range_start_freq1=None,range_stop_freq1=None, show_range1=None, range2=None,range_start_freq2=None, range_stop_freq2=None, show_range2=None)
                self.scale_division_multi_trace(0.1,1.5,50)
                self.updated_set_sweep_points()

                for degree,memnum in zipped:
                    degName = int(degree * 10)
                    self.ccuLib.settilt(port, degName)
                    time.sleep(2)
                    self.ccuLib.getcommandresults()
                    time.sleep(18)
                    DSO_OBJ.mem_multi_trace(memnum)

                new_tilt = int(tilt[0] * 10)
                print(new_tilt)
                self.ccuLib.settilt(port, new_tilt)
                print(port, new_tilt)
                time.sleep(2)
                self.ccuLib.getcommandresults()
                print(new_tilt)
                time.sleep(18)

                self.smooth_multi_trace("MAX")

                new_tilt = int(tilt[-1] * 10)
                print(new_tilt)
                self.ccuLib.settilt(port, new_tilt)
                time.sleep(2)
                self.ccuLib.getcommandresults()
                print(new_tilt)
                time.sleep(18)
                print("passed")

                new_tilt = int(tilt[0] * 10)
                print(new_tilt)
                self.ccuLib.settilt(port, new_tilt)
                time.sleep(2)
                self.ccuLib.getcommandresults()
                print(new_tilt)
                time.sleep(18)
                print(p, "ports is completed. ")
                self.VNA_savescreen(f"{filename}_{p}_Multitrace")
                self.save_S2P(f"{filename}_{p}_Multitrace")


            else:

                self.RST()
                self.load_znxnml( znxmlname)
                self.Frequency( start_fr, stop_fr, "MHz")
                self.trace_window_multi_trace(s_param)
                self.smooth_multi_trace('OFF')
                self.format_multi_trace("SWR")
                self.mark_multitrace("ON", "ON", "ON", "ON", start_fr, stop_fr, "MAX", "ON", 1,1427,1518,1,2,1695,2690,1)
                self.scale_division_multi_trace(0.1, 1.5, 50)
                self.updated_set_sweep_points()

                for degree,memnum in zipped:
                    degName = int(degree * 10)
                    self.ccuLib.settilt(port, degName)
                    time.sleep(2)
                    self.ccuLib.getcommandresults()
                    time.sleep(18)
                    DSO_OBJ.mem_multi_trace(memnum)

                new_tilt = int(tilt[0] * 10)
                print(new_tilt)
                self.ccuLib.settilt(port, new_tilt)
                print(port, new_tilt)
                self.ccuLib.getcommandresults()
                self.ccuLib.updated_fetch_command_results()
                print("Current Tilt:", new_tilt)

                self.smooth_multi_trace("MAx")

                new_tilt = int(tilt[-1] * 10)
                print(new_tilt)
                self.ccuLib.settilt(port, new_tilt)
                time.sleep(2)
                self.ccuLib.getcommandresults()
                print(new_tilt)
                time.sleep(18)
                print("passed")

                new_tilt = int(tilt[0] * 10)
                print(new_tilt)
                self.ccuLib.settilt(port, new_tilt)
                time.sleep(2)
                self.ccuLib.getcommandresults()
                print(new_tilt)
                time.sleep(18)
                print(p, "ports is completed. ")
                self.VNA_savescreen(f"{filename}_{p}_Multitrace")
                self.save_S2P(f"{filename}_{p}_Multitrace")

if __name__ == "__main__":
    # DSO_OBJ=DSOX3054T('USB1::0xOAAD::0x0199::100067::INSTR')
    DSO_OBJ=DSOX3054T('USB0::0x0AAD::0x0199::101436::INSTR')
    IDN2450 = DSO_OBJ.getIdn()
    print(IDN2450)
    
    DSO_OBJ.cls()
    
    DSO_OBJ.rst()
    DSO_OBJ.Remote('ON')
    DSO_OBJ.Trace_window('ON')
    DSO_OBJ.Assign_tracewindow()
    DSO_OBJ.Assign_layout2()
    DSO_OBJ.VNA_savescreen("Plot1")