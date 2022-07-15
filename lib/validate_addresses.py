#!/usr/bin/python3
import ipaddress
import sys

import logging

logger = logging.getLogger(__name__)

class Validate:
    """"This class is created for validation IP addresses entered by user
            :parameter: ip address or network address
            :returns: valid ip address , network mask, network address with cidr notation
             many other different methods relating to IP Addressing scheme and Subnetting"""
    def __init__(self, address):
        """ Instantiation of the Validate class, takes IP/Network/address as a parameter
            :parameter address or network address
            Are used as an object to work on the different given methods for ipaddress python library
        """
        self.address = address
        self.ip_address = ipaddress.IPv4Interface(self.address)
        self.network = self.get_ip_cidr()

    def address_check(self):
        """
        :parameter: takes an ip address from init and converts into interface to manipulate
        :returns: Valid ip address, cidr block, network mask and boolean value if the ip is private
        or public, as we are dealing with only private(internal) addresses
        """
        try:
            interface = ipaddress.IPv4Interface(self.address)
            ip_addr = interface.ip
            network = interface.network

            if isinstance(ip_addr, ipaddress.IPv4Address):
                valid_ip = self.address
                ip_cidr = ipaddress.IPv4Network(self.address)
                net_mask = network.netmask
                priv_add = interface.is_private
                return valid_ip, ip_cidr, net_mask, priv_add
        except ValueError:
            print("=" * 80)
            print("{} is not a valid IPv4 Network Address".format(self.address))
            print("=" * 80)
            sys.exit()

################################## IP Address Validation #################################################

    def get_valid_ip(self):
        """
           :parameter: from address check method
           :returns: valid ip address
        """
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return valid_ip

    def get_ip_cidr(self):
        """
            :parameter: from address check method
            :returns: IP with CIDR block
                """
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return ip_cidr

    def get_netmask(self):
        """
                   :parameter: from address check method
                   :returns: network mask
                """
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return net_mask

    def is_ip_private_or_public(self):
        """
                   :parameter: from address check method
                   :returns: boolean value, private address
                """
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return priv_add

    def get_ip_version(self):
        """ :parameter: Ip address
        :returns: ip version integer value
        """
        ip_version = self.ip_address.version
        return ip_version

    def get_ip_multicast(self):
        """ :returns: IP Multicast, Boolean value """
        ip_multicast = self.ip_address.is_multicast
        #print("Is IP Multicast: " + str(ip_multicast))
        return ip_multicast

    def get_is_ip_global(self):
        """ :returns: IP Global, Boolean value  """
        ip_global = self.ip_address.is_global
        #print("Is IP Multicast: " + str(ip_global))
        return ip_global

    def get_is_ip_APIPA(self):
        """ :returns: If given address is Automatic private ip address
            range: 169.254.x.x, Boolean value"""
        apipa = self.ip_address.is_link_local
        #print("Is IP Link Local(APIPA): " + str(apipa))
        return apipa

    def check_is_loopback(self):
        """ :returns: Is ip loopback, Boolean Value """
        loopback = self.ip_address.is_loopback
        #print("Is IP Loopback: " + str(loopback))
        return loopback

############################# Network Validation ##########################################

    def get_network_address(self):
        """ :returns: Network Address from CIDR block """
        net_address = self.network.network_address
        #print("Network Address: " + str(net_address))
        return net_address

    def get_broadcast_address(self):
        """ :returns: Brodcast address from the given address """
        broadcast = self.network.broadcast_address
        #print("Broadcast Address: " + str(broadcast))
        return broadcast

    def get_prefixlength(self):
        """ :returns: Network prefix length, integer value """
        prelength = self.network.prefixlen
        #print("Network Prefix Length:" + str(prelength))
        return prelength

    def get_host_mask(self):
        """ :returns: Network host mask or wild card mask for the given subnet """
        host_mask = self.network.hostmask
        #print("Network Host Mask(Wildcard Mask): " + str(self.network.hostmask))
        return host_mask

    def get_reverse_pointer(self):
        """ :returns: reverse pointer of the subnet """
        rev_pointer = self.network.reverse_pointer
        #print("Network Reverse_pointer: " + str(rev_pointer))
        return rev_pointer

    def get_with_hostmask(self):
        """ :returns: wildcard mask with given ip address """
        with_hostmask = self.network.with_hostmask
        #print("Network With Host mask: " + str(with_hostmask))
        return with_hostmask

    def get_with_netmask(self):
        """ :returns: CIDR notation and the netmask """
        with_netmask = self.network.with_netmask
        #print("Network With Net mask: " + str(with_netmask))
        return with_netmask

    def get_with_prefixlen(self):
        """ :returns: Network prefix length """
        with_prefixlen = self.network.with_prefixlen
        #print("Network with Prefix Length: " + str(with_prefixlen))
        return with_prefixlen

    def get_subnet_version(self):
        """ :returns: Subnet version, integer value"""
        subnet_version = self.network.version
        #print("Version: " + str(subnet_version))
        return subnet_version

    def get_net_max_prefixlen(self):
        """ :returns: Maximum Network prefix length, integer value """
        net_max_prefixlen = self.network.max_prefixlen
        #print("Network Max Prefix Length: " + str(net_max_prefixlen))
        return net_max_prefixlen

    def get_hosts_from_subnet(self):
        """ :returns: returns list of from subnet as a list """
        hosts = self.network.hosts()
        return hosts

    def check_ip_address(self):
        """
        :parameter: ip address
        :return: valid IP address and network address
        """
        try:
            # if True:
            ip = ipaddress.ip_address(self.address)
            network = ipaddress.IPv4Network(self.address)

            if isinstance(ip, ipaddress.IPv4Address):
                print("=" * 80)
                print("{} is a valid IPv4 Address".format(self.address))
                print("IP Address: " + str(self.address) + "\nCIDR: " + str(ipaddress.IPv4Network(ip)))
                print("=" * 80)
            else:
                if isinstance(network, ipaddress.IPv4Network):
                    print("=" * 80)
                    print("{} is a valid IPv4 Network Address".format(self.address))
                    print("Network: " + str(self.address) + " Subnet Mask: " + str(network.netmask))
                    print("=" * 80)
        except ValueError:
            # else:
            print("=" * 80)
            print("{} is not a valid IPv4 Network Address".format(self.address))
            print("=" * 80)

    def check_network_address(self):
        """
                :parameter: network address
                :return: valid network address
                """
        try:
            network = ipaddress.IPv4Network(self.address)

            if isinstance(network, ipaddress.IPv4Network):
                print("=" * 80)
                print("{} is a valid IPv4 Network Address".format(self.address))
                print("Network: " + str(self.address) + " Subnet Mask: " + str(network.netmask))
                print("=" * 80)
        except ValueError:
            print("=" * 80)
            print("{} is not a valid IPv4 Network Address".format(self.address))
            print("=" * 80)


"""
IP: 192.168.0.0/22
============================== IP Validations =========================

IP Address: 192.168.0.0/22
CIDR: 192.168.0.0/22
Netmask: 255.255.252.0
Is IP Private: True
IP Version: 4
Is IP Multicast: False
Is IP Multicast: False
Is IP Link Local(APIPA): False
Is IP Loopback: False
============================== Network Validations =========================

Network Address: 192.168.0.0
Broadcast Address: 192.168.3.255
Network Prefix Length:22
Network Host Mask(Wildcard Mask): 0.0.3.255
Network Reverse_pointer: 0/22.0.168.192.in-addr.arpa
Network With Host mask: 192.168.0.0/0.0.3.255
Network With Net mask: 192.168.0.0/255.255.252.0
Network with Prefix Length: 192.168.0.0/22
Version: 4
Network Max Prefix Length: 32
192.168.0.1
192.168.0.2
192.168.0.3
192.168.0.4
192.168.0.5
--- Output cropped ---- 
Continued rest of the output
92.168.3.252
192.168.3.253
192.168.3.254

Process finished with exit code 0
"""
"""
IP: 192.168.1.0/28
============================== IP Validations =========================

IP Address: 192.168.1.0/28
CIDR: 192.168.1.0/28
Netmask: 255.255.255.240
Is IP Private: True
IP Version: 4
Is IP Multicast: False
Is IP Multicast: False
Is IP Link Local(APIPA): False
Is IP Loopback: False
============================== Network Validations =========================

Network Address: 192.168.1.0
Broadcast Address: 192.168.1.15
Network Prefix Length:28
Network Host Mask(Wildcard Mask): 0.0.0.15
Network Reverse_pointer: 0/28.1.168.192.in-addr.arpa
Network With Host mask: 192.168.1.0/0.0.0.15
Network With Net mask: 192.168.1.0/255.255.255.240
Network with Prefix Length: 192.168.1.0/28
Version: 4
Network Max Prefix Length: 32
192.168.1.1
192.168.1.2
192.168.1.3
192.168.1.4
192.168.1.5
192.168.1.6
192.168.1.7
192.168.1.8
192.168.1.9
192.168.1.10
192.168.1.11
192.168.1.12
192.168.1.13
192.168.1.14

Process finished with exit code 0
"""