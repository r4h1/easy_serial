import serial
import time

class SerialHelper:
    def __init__(self, port, baudrate=115200, timeout=1):
        self.port = port
        self.baudrate = baudrate
        self.timeout = timeout
        self.serial = None

    def connect(self):
        try:
            self.serial = serial.Serial(self.port, self.baudrate, timeout=self.timeout)
            time.sleep(2)
            print(f"Connected to {self.port} at {self.baudrate} baud")
        except serial.SerialException as e:
            print(f"Error: {e}")

    def send(self, message):
        if self.serial and self.serial.is_open:
            self.serial.write(message.encode('utf-8'))
            print(f"Sent: {message}")
        else:
            print("Serial connection is not open!")

    def receive(self):
        if self.serial and self.serial.is_open:
            return self.serial.readline().decode('utf-8').strip()
        return None

    def close(self):
        if self.serial:
            self.serial.close()
            print("Serial connection closed.")
