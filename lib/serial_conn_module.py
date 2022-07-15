#!/usr/bin/python3
import logging
import time
import serial

logger = logging.getLogger(__name__)

class Serial_con:

    def __init__(self,port=None, baudrate=None, parity=None, stopbits=None, bytesize=None, timeout=None):

        self.port = port
        self.baudrate = baudrate
        self.parity = parity
        self.stopbits = stopbits
        self.bytesize = bytesize
        self.timeout = timeout
        self.console = self.open_console()

    def open_console(self):
        """This method will create serial connection to the given network device
        port may need to be changed as per hardware.
        """
        self.port = 'com8'
        self.baudrate = 9600
        self.parity = 'N'
        self.stopbits = 1
        self.bytesize = 8
        self.timeout = 8
        self.console = serial.Serial(self.port, self.baudrate, self.parity, self.stopbits, self.bytesize, self.timeout)
        if self.console.isOpen():
            return self.console
        else:
            return False

    def run_command(self, cmd='\n', sleep=2):
        """This method sends commands via serial connection, slower."""
        print('Sending command ' + cmd)
        self.console.write(cmd.encode() + b'\n')
        time.sleep(sleep)

    def check_intial_config(self):
        """This method deals with initial configuration dialog in devices."""
        self.run_command(self.console,'\n')
        prompt = self.read_from_console(self.console)
        if 'Would you like to enter initial configuration dialog?' in prompt:
            self.run_command(self.console, 'no\n', 15)
            self.run_command(self.console, '\r\n')

    def read_from_console(self):
        """This function Reads output from the console"""
        bytes_to_be_read = self.console.inWaiting()
        if bytes_to_be_read:
            output = self.console.read(bytes_to_be_read)
            return output.decode()
        else:
            return False
