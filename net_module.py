#!/usr/bin/python3
import json
from netmiko import ConnectHandler
from netmiko.ssh_exception import NetMikoAuthenticationException, NetMikoTimeoutException
from paramiko.ssh_exception import SSHException
import net_devices
import ipaddress
from napalm import get_network_driver
from datetime import datetime
import json
import os
import socket
import logging
import re

logger = logging.getLogger(__name__)


class SSHLogin:

    def __init__(self, ip, user, password):

        self.host = ip
        self.get_hostname_ip()
        self.valid_ip = self.address_check()
        self.user = user
        self.password = password
        self.net_device = {'device_type': 'cisco_ios', 'ip': self.ip, 'username': self.user, 'password': self.password}
        self.conn = ConnectHandler(**self.net_device)
        self.version = self.check_ios()
        self.hostname = self.conn.find_prompt().strip('#')


    def check_ip_or_host(self):
        """ This method checks if the IP is valid or not
            socket_inet_aton converts IPV4 from dotted-quad string to 32 bit binary format
            IP address is valid
        """
        try:
            if socket.inet_aton(str(self.host)):
                return True
        except:
            return False

    def get_hostname_ip(self):
        """ This method is when host name is given instead of IP,
            if the check_ip method is false which means IP is not provided
            so storing the result from the h_name
            splitting the result with space and storing it in host.
            the last object is an IP in the list storing it in ip variable.
        """
        if self.check_ip_or_host() is False:
            h_name = os.popen("host " + self.host).read()
            host = h_name.split(" ")
            self.ip = host[-1].strip()
        else:
            self.ip = self.host

    def address_check(self):
        """ This method checks for the Valid IP Address
            and returns the subnet mask, CIDR and Network Address
            with private or Public IP Address flag.
        """
        try:
            interface = ipaddress.IPv4Interface(self.ip)
            check_ip = interface.ip
            network = interface.network

            if isinstance(check_ip, ipaddress.IPv4Address):
                valid_ip = self.ip
                ip_cidr = ipaddress.IPv4Network(self.ip)
                net_mask = network.netmask
                priv_add = interface.is_private
                return f'IP: {valid_ip}', f'CIDR: {ip_cidr}', f'Netmask:{net_mask}', f'Private: {priv_add}'
            else:
                return 'IP Address Error...'
        except ValueError as e:
            f'{self.ip}:{e} is not a valid IPv4 Network Address'

    def check_ios(self):
        """ This method checks for the version of networking
            devices and returns it.
        """
        version = self.conn.send_command(net_devices.common_cmnds['show']['version'], strip_command=False)
        #ver_frt = self.conn.send_command('get system status', strip_command=False)
        version = version.lower()
        #ver_frt = ver_frt.lower()

        if 'cisco nexus' in version:
            return 'cisco nexus'
        elif 'cisco ios' in version:
            return 'cisco ios'
        elif 'junos' in version:
            return 'juniper junos'
        elif 'fortigate' in ver_frt:
            return 'fortinet'
        else:
            raise Exception("Network OS Version not found!")

    def close_connection(self):
        """ This method closes the active connection gracefully.
                """
        self.conn.disconnect()

    def get_vlan_info(self, ip_route):
        """ This method is for getting vlan information, 'show ip route'
        information must be provided as an argument for this method to work.
        """
        for i in ip_route:
            if 'Vlan' in ip_route:
                vlan = re.findall(r'[Vlan0-9]{5,7}', ip_route)
                vlan_name = vlan[0]

                if vlan_name:
                    vlan_info = self.conn.send_command(net_devices.common_cmnds['show']['interface'] + vlan_name,
                                                       strip_command=False)
                    return vlan_info
            else:
                return 'No vlan Configured'

    def get_acl_name(self, vlan_info):
        """ This method gets the Access Control List Name configure in VLAN
        You must provide the vlan_information 'show run int vlan' with it
        for this to work.
                """
        vlan = vlan_info.split()
        counter = 0

        for agroup in vlan:
            if agroup == "access-group":
                if vlan[counter - 1] == "ip" and vlan[counter + 2] == "in":
                    acl_name = vlan[counter + 1]
                    return acl_name
            else:
                return 'No ACL configured on the Interface'
            counter += 1

    def set_commands(self, command, parameter):
        command_output = self.conn.send_command(command + " " + parameter, strip_command=False)
        return command_output

    def var_commands(self, command):
        """ This method simply take argument and executes the command
        """
        any_command = self.conn.send_command(command, strip_command=False)
        return any_command

    def get_ip_route(self, search_ip):
        """ This method would provide you information regarding specific ip address and its orginating
            routing information """
        show_route = self.conn.send_command(net_devices.common_cmnds['show']['ip route'] + " " + search_ip,
                                            strip_command=False)
        return show_route

    def get_vlan_config(self, vlan_name):
        """ This method provides you the specific vlan information, user must specify correct vlan name

        """
        vlan_config = self.conn.send_command(net_devices.common_cmnds['show']['interface'] + " " + vlan_name,
                                             strip_command=False)
        return vlan_config

    def get_acl_config(self, acl_name):
        """ This method executes the show ip access list commands along with the correct acl name to narrow down
        the result
       """
        acl_config = self.conn.send_command(net_devices.common_cmnds['show']['ip access-list'] + " " + acl_name,
                                            strip_command=False)
        return acl_config

    def get_object_groups(self):
        """ This method will get you the name of the network object groups
        """
        object_groups = self.conn.send_command(net_devices.common_cmnds['show']['object-group'], strip_command=False)
        return object_groups

    def config_command(self, command):
        """ This method by default configures the host as per given command argument from global config mode
                """
        command_output = self.conn.send_config_set(command, strip_command=False)
        return command_output

    def config_command_lists(self, commands):
        """ This method configures list of commands, given the commands is a list variable, execution of the commands
        are in top down order sequentially
        """
        commands_output = self.conn.send_config_set(commands.split('\n'), strip_command=False)
        return commands_output

    def config_from_file(self, filename):
        """This method configures commands from the file. The config file should be place in the same
        directory as the script or make sure to provide full absolute path for this to work.
        """
        commands_output = self.conn.send_config_from_file(filename)
        return commands_output

    def get_junos_uptime(self):
        uptime = self.conn.send_command(net_devices.junos['show']['uptime'], strip_command=False)
        return uptime
    
    def get_junos_sysinfo(self):
        sysinfo = self.conn.send_command(net_devices.junos['show']['sysinfo'], strip_command=False)
        return sysinfo

    def get_junos_interfaces(self):
        inter = self.conn.send_command(net_devices.junos['show']['interface'], strip_command=False)
        return inter

    def get_junos_bgp_info(self):
        bgpinfo = self.conn.send_command(net_devices.junos['show']['bgp'], strip_command=False)
        return bgpinfo

    def get_junos_config(self):
        config = self.conn.send_command(net_devices.junos['show']['config'], strip_command=False)
        return config

    def current_config_backup(self):
        """ This method takes the backup of host's current configuration in a text file, assigning name of the file
        with day month year hour minute followed by backup.txt.
        In case of misconfiguration rollback config from the backup file can be used.
        """
        config = self.conn.send_command(net_devices.common_cmnds['run']['config'], strip_command=False)
        #config =self.conn.send_command("show running-config", strip_command=False, delay_factor=3)
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        filename = f'{self.hostname}_{day}_{month}_{year}_{hour}_{minute}_backup.txt'
        with open(filename, 'w') as f:
            f.write(config)
        return filename

    def config_rollback(self, network_os):
        """ This method rollbacks the config to the previous config file just in case of misconfiguration.
         Needs testing in dev environment.
         NOT TO BE USED IN PROD.
        """
        
        driver = get_network_driver(network_os)
        nos = driver(hostname= self.ip, username= self.user, password= self.password)
        nos.open()
        output = nos.get_interfaces()
        dump = json.dumps(output,indent=4)
        return dump
        #nos.load_replace_candidate(filename='config.txt')
        #diff = nos.compare_config()
        #if len(diff):
        #    nos.commit_config()
        #else:
        #    nos.discard_config()

    def write_output_to_file(self, output):
        """This method writesall output to a file"""
        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day
        hour = now.hour
        minute = now.minute
        filename = f'{self.hostname}_{day}_{month}_{year}_{hour}_{minute}_config.txt'
        with open(filename, 'w') as f:
            f.write(output)
        return filename
