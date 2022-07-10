#!/usr/bin/python3

import socket

class ValidateService():

    def __init__(self, service, protocol):
        
        self.service = service
        self.protocol = protocol

    
    def get_service(self):
        """ Gets Port/Service checkes given parameter and returns the correct port and service"""
        try:
            if self.service.strip().isdigit():
    
                self.service = int(self.service)
                serviceName = socket.getservbyport(self.service, self.protocol)
                self.service = str(self.service)
                #print(f'{self.protocol.upper()}/{serviceName.upper()}[{self.service}]')
                protocol = self.protocol
                protocol = protocol.upper()
                service = serviceName.upper()
                port = self.service
                return protocol, service, port
                #return self.protocol.upper(), serviceName.upper(), self.service
                #return serviceName
            else:
                portNumber = socket.getservbyname(self.service, self.protocol)
                portNumber = str(portNumber)
                print(f'{self.protocol.upper()}/{self.service.upper()}[{portNumber}]')
                protocol = self.protocol
                protocol = protocol.upper()
                service = self.service.upper()
                port = portNumber
                return protocol, service, port
                #return  self.protocol.upper(), self.service.upper(), portNumber
                #return str(portNumber)
        except OSError:
           return '{OSError} Service not found!'
        

    def get_port_number(self):
        portNumber = self.get_service()
        return portNumber

    def get_service_name(self):
        serviceName = self.get_service()
        return serviceName.upper()
    
    def get_protocol(self):
        self.protocol = self.protocol.upper()
        return self.protocol
