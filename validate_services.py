#!/usr/bin/python3

import socket

class ValidateService():
    """
        This class gets service either from protocol name or number
        :returns  Protocol/Service[PortNumber]
    """
    def __init__(self, service, protocol):
        """Instantiation of the class,
        :parameter: service or port number [0 - 65535]
        :parameter: protocol[tcp/udp/ip/icmp]
        :returns: Protocol/ServiceName[PortNumber]
        """
        self.service = service
        self.protocol = protocol

    def get_service(self):
        """ This method checks if the given service is number or string and checks for the service name and
        portnumber by using socket """

        try:
            if self.service.strip().isdigit():

                self.service = int(self.service)
                serviceName = socket.getservbyport(self.service, self.protocol)
                self.service = str(self.service)
                # print(f'{self.protocol.upper()}/{serviceName.upper()}[{self.service}]')
                self.protocol = self.protocol.upper()
                service = serviceName.upper()
                port = self.service
                return self.protocol, service, port
                # return self.protocol.upper(), serviceName.upper(), self.service
                # return serviceName
            else:
                if self.service is None:
                    print("Service cant be empty")
                    exit(1)
                portNumber = socket.getservbyname(self.service, self.protocol)
                portNumber = str(portNumber)
                # print(f'{self.protocol.upper()}/{self.service.upper()}[{portNumber}]')
                self.protocol = self.protocol.upper()
                service = self.service.upper()
                port = portNumber
                return self.protocol, service, port
                # return  self.protocol.upper(), self.service.upper(), portNumber
                # return str(portNumber)
        except OSError:
            return '{OSError} Service not found!'

    def get_port_number(self):
        protocol, service, portNumber = self.get_service()
        return portNumber

    def get_service_name(self):
        protocol, serviceName, portNumber = self.get_service()
        return serviceName.upper()

    def get_protocol(self):
        self.protocol, serviceName, portNumber = self.get_service()
        return self.protocol.upper()