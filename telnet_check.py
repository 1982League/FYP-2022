#!/usr/bin/python3

import socket
import time
from validate_services import ValidateService

class PortOpen:

    def __init__(self, dst_ip, dst_port):

        self.dst_ip = dst_ip
        self.dst_port = dst_port
      

    def get_port(self):

        if not dst_port.isdigit():
            portNumber = socket.getservbyname(dst_port)
            print(str("portNumber"))
            self.dst_port = portNumber

            return self.dst_port
        else:
            self.dst_port = dst_port
            return self.dst_port

    def is_open(self):
        
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
        if self.check_host():
            print(f"Port {self.dst_port} is open for {self.dst_ip}")  # is UP")
        else:
            print(f"Port {self.dst_port} is not open for {self.dst_ip}")  # is not up


#def main():
#    dst_ip = input("IP: ")
#    dst_port = input("Port: ")
#    p = PortOpen(dst_ip, dst_port)
    
#    print("is Open :" + str(p.is_open()))
#    print("check host: " + str(p.check_host()))

#    p.result()

#main()
