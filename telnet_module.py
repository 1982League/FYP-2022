#!/usr/bin/python3
import time
import  telnetlib

class Device:
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

"""
Testing of telnet class
"""
router = {'host': '192.168.1.39','username': 'netlab', 'password':'netlab'}

tconn = Device(host=router['host'], username=router['username'], password=router['password'])
tconn.connect()
print("\n" + "=" * 20 + f" Connecting to {router['host']} " + "=" * 22 + "\n")
tconn.authenticate()

print(f"=" * 20 + " Executing Commands " + "=" * 30 + "\n")
cmd_list = ['conf t', 'int loopback 0', 'ip address 1.1.1.1 255.255.255.255',
                'exit', 'router ospf 1', 'network 0.0.0.0 255.255.255.255 area 0', 'end', 'show ip protocols' ]

tconn.send_list_command(cmd_list)
print(f"=" * 20 + " Configuration Output " + "=" * 30 + "\n")
output = tconn.show()
print(output)
print(f"=" * 20 + f" Closing Connection to {router['host']} " + "=" * 30 + "\n")
tconn.close()

'''
Commands can be entered individually
    tconn.send('configure terminal')
    tconn.send('terminal length 0')
    tconn.send('inter lo0')
    tconn.send(f'ip address {r["loopback_ip"]}1.1.1.1 255.255.255.255')
    tconn.send('router ospf 1')
    tconn.send('network 0.0.0.0 0.0.0.0 area 0')
    tconn.send('end')
    tconn.send('show ip protocols')
'''
"""
==================== Connecting to 192.168.1.39 ======================

==================== Executing Commands ==============================

Sending command: conf t
Sending command: int loopback 0
Sending command: ip address 1.1.1.1 255.255.255.255
Sending command: exit
Sending command: router ospf 1
Sending command: network 0.0.0.0 255.255.255.255 area 0
Sending command: end
Sending command: show ip protocols

==================== Configuration Output ==============================

R1#conf t
Enter configuration commands, one per line.  End with CNTL/Z.
R1(config)#int loopback 0
R1(config-if)#ip address 1.1.1.1 255.255.255.255
R1(config-if)#exit
R1(config)#router ospf 1
R1(config-router)#network 0.0.0.0 255.255.255.255 area 0
R1(config-router)#end
R1#show ip protocols
*** IP Routing is NSF aware ***

Routing Protocol is "ospf 1"
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Router ID 192.168.1.39
  Number of areas in this router is 3. 3 normal 0 stub 0 nssa
  Maximum path: 4
  Routing for Networks:
    192.168.1.0 0.0.0.255 area 0
    192.168.2.0 0.0.0.255 area 2
    192.168.3.0 0.0.0.255 area 3
    0.0.0.0 255.255.255.255 area 0
  Routing Information Sources:
    Gateway         Distance      Last Update
  Distance: (default is 110)

R1#
==================== Closing Connection to 192.168.1.39 ==============================
"""