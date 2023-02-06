from serial import Serial

class Relay:
    def __init__(self, serial_port):
        self._serial = Serial(serial_port)

    def turn_on(self):
        self._serial.write(b"\xA0\x01\x01\xA2")

    def turn_off(self):
        self._serial.write(b"\xA0\x01\x00\xA1")