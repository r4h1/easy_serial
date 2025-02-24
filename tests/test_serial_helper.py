import unittest
from easy_serial import SerialHelper

class TestSerialHelper(unittest.TestCase):
    def test_connection(self):
        serial = SerialHelper(port="COM3", baudrate=115200)
        self.assertEqual(serial.port, "COM3")

if __name__ == "__main__":
    unittest.main()
