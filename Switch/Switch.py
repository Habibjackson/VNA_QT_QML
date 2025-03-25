# import json
# import time
from PySide6.QtCore import QObject, QIODevice, QByteArray, Signal, Slot
# from PySide6.QtSerialPort import QSerialPort

# class SwitchController(QObject):
#     positionChanged = Signal(int, int)  # Signal to notify when position changes

#     def __init__(self):
#         super().__init__()
#         self._r1_position = 1  # Default position for relay 1
#         self._r2_position = 1  # Default position for relay 2

#         self.serial_port = QSerialPort(self)
#         self.serial_port.setPortName("COM4")
#         self.serial_port.setBaudRate(QSerialPort.Baud9600)
#         self.serial_port.setDataBits(QSerialPort.Data8)
#         self.serial_port.setParity(QSerialPort.NoParity)
#         self.serial_port.setStopBits(QSerialPort.OneStop)
#         self.serial_port.setFlowControl(QSerialPort.NoFlowControl)

#         if not self.serial_port.open(QIODevice.ReadWrite):
#             print("Failed to open serial port!")
#         else:
#             print("Serial port opened successfully.")

#     def set_r1_position(self, value):
#         if 1 <= value <= 6:
#             self._r1_position = value
#             print(self._r1_position, self._r2_position)
#             self.set_switch_position(self._r1_position, self._r2_position)
#             self.positionChanged.emit(self._r1_position, self._r2_position)
#         else:
#             print("Invalid position for R1. Must be between 1 and 6.")

#     def set_r2_position(self, value):
#         if 1 <= value <= 6:
#             self._r2_position = value
#             self.set_switch_position(self._r1_position, self._r2_position)
#             self.positionChanged.emit(self._r1_position, self._r2_position)
#         else:
#             print("Invalid position for R2. Must be between 1 and 6.")

#     def set_switch_position(self, r1, r2):
#         command = json.dumps({"r1_channel": r1, "r2_channel": r2}) + "\r\n"
#         byte_data = QByteArray(command.encode())
#         try:
#             self.serial_port.write(byte_data)
#             print(f"Sent command: {command}")
#             time.sleep(1.5)
#         except Exception as e:
#             print(f"Error sending command: {e}")

#     def set_r1_r2_pos(self, r1pos, r2pos):
#         self._r1_position = r1pos
#         self._r2_position = r2pos
#         self.set_switch_position(self._r1_position, self._r2_position)
#         self.positionChanged.emit(self._r1_position, self._r2_position)

#     def close_connection(self):
#         if self.serial_port.isOpen():
#             self.serial_port.close()
#         print("Serial connection closed.")

#     def get_r1_position(self):
#         return self._r1_position

#     def get_r2_position(self):
#         return self._r2_position

import serial
import json
import time

class SwitchController(QObject):
    positionChanged = Signal(int, int)

    def __init__(self):
        super().__init__()
        # Initialize default positions for relays
        self._r1_position = 1  # Default position for relay 1
        self._r2_position = 1  # Default position for relay 2

        # Set up the serial port with pyserial
        try:
            self.serial_port = serial.Serial(
                port="COM4",
                baudrate=9600,
                bytesize=serial.EIGHTBITS,
                parity=serial.PARITY_NONE,
                stopbits=serial.STOPBITS_ONE,
                timeout=1  # Timeout to prevent indefinite blocking
            )
            print("Serial port opened successfully.")
        except serial.SerialException as e:
            print(f"Failed to open serial port: {e}")
            self.serial_port = None  # Set to None if opening fails

    def set_r1_position(self, value):
        """Set the position of relay R1 and update the switch."""
        if 1 <= value <= 6:
            self._r1_position = value
            print(f"R1 set to {self._r1_position}, R2 is {self._r2_position}")
            self.set_switch_position(self._r1_position, self._r2_position)
        else:
            print("Invalid position for R1. Must be between 1 and 6.")

    def set_r2_position(self, value):
        """Set the position of relay R2 and update the switch."""
        if 1 <= value <= 6:
            self._r2_position = value
            print(f"R2 set to {self._r2_position}, R1 is {self._r1_position}")
            self.set_switch_position(self._r1_position, self._r2_position)
        else:
            print("Invalid position for R2. Must be between 1 and 6.")

    def set_switch_position(self, r1, r2):
        """Send a JSON command to set the positions of both relays."""
        if self.serial_port is None or not self.serial_port.is_open:
            print("Serial port is not open.")
            return

        # Create and encode the JSON command
        command = json.dumps({"r1_channel": r1, "r2_channel": r2}) + "\r\n"
        byte_data = command.encode()  # Convert string to bytes

        try:
            self.serial_port.write(byte_data)
            print(f"Sent command: {command.strip()}")
            time.sleep(1.5)  # Delay to allow the device to process the command
        except Exception as e:
            print(f"Error sending command: {e}")

    def set_r1_r2_pos(self, r1pos, r2pos):
        """Set the positions of both relays simultaneously."""
        self._r1_position = r1pos
        self._r2_position = r2pos
        print(f"Setting R1 to {r1pos}, R2 to {r2pos}")
        self.set_switch_position(self._r1_position, self._r2_position)

    def close_connection(self):
        """Close the serial port connection."""
        if self.serial_port and self.serial_port.is_open:
            self.serial_port.close()
            print("Serial connection closed.")

    def get_r1_position(self):
        """Return the current position of relay R1."""
        return self._r1_position

    def get_r2_position(self):
        """Return the current position of relay R2."""
        return self._r2_position
