#!/usr/bin/python3
import time
import  telnetlib
import logging

logger = logging.getLogger(__name__)

class Device:
    """This class is created for instantiating telnet connection.
        The method is provided as an optional choice for the tool, it is shown in tool in case of ssh failure,
        We are using SSH through out the tool, telnet is not fully developed to be used for ACL, but
        can be used for configuring set of command and network automation.
    """

    def __init__(self,host, username, password, tnet=None):
        """Instantiating of Telnet device Class
        :parameter: host/ip, Username, Password, tnet
        :returns: tnet conection object
        """
        self.host = host
        self.username = username
        self.password = password
        self.tnet = tnet

    def connect(self):
        """ Connecting to device via telnet
                :parameter: connecting on port 23 via host/ip address
                :returns: tnet conection object to be used
        """
        self.tnet = telnetlib.Telnet(self.host)

    def authenticate(self):
        """Authentication to networking device
                :parameter: host/ip, Username, Password, tnet
                :returns: established connection to network device
        """
        self.tnet.read_until(b'Username: ')
        self.tnet.write(self.username.encode() + b'\n')
        self.tnet.read_until(b'Password: ')
        self.tnet.write(self.password.encode() + b'\n')

    def send(self, command, timeout=0.15):
        """Send individual commands to the networking device
                :parameter: write method encoding commands
                :returns: executed command
                """
        print(f'Sending command: {command}')
        self.tnet.write(command.encode() + b"\n")
        time.sleep(timeout)

    def send_list_command(self, commands):
        """Send list of commands to the networking device
                        :parameter: writing encoded commands to the network device
                        :returns: executed commands
        """
        for cmd in commands:
            self.send(cmd)
        print()

    def show(self):
        """Reads all output from the terminal
                        :parameter: Reading and decoding all the content
                        :returns: Display output in readable form
        """
        output = self.tnet.read_all().decode()
        return output

    def close(self):
        """Gracefully closing the connection with network device
                        :parameter: close connection
                        :returns: disconnecting from network device
        """
        self.tnet.close()

