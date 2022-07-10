#!/usr/bin/python3

import ipaddress
import os
import sys
import IPy

class Validate:

    def __init__(self, address):

        self.address = address


    def address_check(self):
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


    def get_valid_ip(self):
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return valid_ip
    
    def get_ip_cidr(self):
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return ip_cidr

    def get_netmask(self):
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return net_mask

    def is_ip_private_or_public(self):
        valid_ip, ip_cidr, net_mask, priv_add = self.address_check()
        return priv_add
