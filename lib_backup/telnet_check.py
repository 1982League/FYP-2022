#!/usr/bin/python3
import socket
import time
import logging

logger = logging.getLogger(__name__)

class PortOpen:
    """Class to check the port open using socket
    """
    def __init__(self, dst_ip, dst_port):
        """Instantiating PortOpen
                        :parameter: destination ip address & destination port
        """
        self.dst_ip = dst_ip
        self.dst_port = dst_port

    def is_open(self):
        """Method checks for the socket connection
                                :parameter: connect, shutdown
                                :returns: boolean if the connection successful or fails
        """
        timeout = 3
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(timeout)
        try:
            s.connect((self.dst_ip, int(self.dst_port)))
            s.shutdown(socket.SHUT_RDWR)
            return True
        except:
            return False
        finally:
            s.close()

    def check_host(self):
        """Check host
         :parameter: if connection is open
         :returns: boolean if the connection is open
        """
        ipup = False
        retry = 3
        delay = 2
        for i in range(retry):
            if self.is_open():
                ipup = True
                break
            else:
                time.sleep(delay)
        return ipup

    def result(self):
        """Prints the result for destination ip and destination port is open or not open
            :returns: prints the string message port open
        """
        if self.check_host():
            print(f"Port {self.dst_port} is open for {self.dst_ip}")  # is UP")
        else:
            print(f"Port {self.dst_port} is not open for {self.dst_ip}")  # is not up

"""
============================== Connection Check for Port Open ====================
Example 1:
SSH[22] is open for 10.20.1.1
Example 2:
TELNET[23] is not open for 10.40.1.1
"""