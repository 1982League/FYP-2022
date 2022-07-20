#!/usr/bin/python3
import os
from datetime import datetime
import logging
from utility.file_creator import Utility
from lib.validate_addresses import Validate

logger = logging.getLogger(__name__)

class Error(Exception):
    """Base error class."""

class ACLGEN:
    """
        This class Generates ACL for Multiple Network devices,
        Cisco, Arista, Juniper, Fortinet
        returns: proposed config file, rollback config and config plan file
    """
    path= path= r'C:\Users\sjoshi\Desktop\code\FYP-2022\acl_rules\_'
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    path = r'C:\Users\sjoshi\Desktop\code\FYP-2022\acl_rules\acl'
    proposed_config_output =  f'ACL_proposed_{day}_{month}_{year}_{hour}_{minute}.txt'
    rollback_config_output =  f'ACL_rollback_{day}_{month}_{year}_{hour}_{minute}.txt'
    combine_config_output  =  f'ACL_configPlan_{day}_{month}_{year}_{hour}_{minute}.txt'
    print("="*40 + " ACL Configuration Files Created " + "=" *22 + "\n")
    print("\n"+ proposed_config_output + "\n" + rollback_config_output + "\n" + combine_config_output + "\n")

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        """
            Class constructor instantiate the class with parameters provided by the user to create
            an Access Control List Statement as per the network platform.
        """

        self.src_ip = src_ip
        self.dst_ip = dst_ip
        self.src_port = src_port
        self.dst_port = dst_port
        self.protocol = protocol
        self.action = action


    def srcport(self):
        """
           If the Source Port is not assigned it Returns the source Port as any, any port
        """
        if self.src_port is None:
            self.src_port = 'any'
            return self.src_port
        else:
            print(self.src_port)
            return self.src_port

    def dstport(self):
        """
            If the destination port is not assigned  Returns the Destination Port to any, any port
        """
        if self.dst_port is None:
            self.dst_port = 'any'
            return self.dst_port

        else:
            print(self.dst_port)
            return self.dst_port

    def acl(self):
        """
            This Function builds Access Control Entry for Cisco and Arista Platform as they have similar
            syntax.
        """
        acl_rule = []

        if 'permit' in self.action:
            acl_rule.append(self.action)
            ace = ' '.join(map(str, acl_rule))
        else:
            print("Check action")

        if self.protocol:
            acl_rule.append(self.protocol)
            ace = ' '.join(map(str, acl_rule))
        else:
            self.protocol = 'ip'
            acl_rule.append(self.protocol)
            ace = ' '.join(map(str, acl_rule))
            print("No Protocol")

        if self.src_ip:
            host = 'host'
            acl_rule.append(host)
            acl_rule.append(self.src_ip)
            ace = ' '.join(map(str, acl_rule))
        elif self.src_ip.network():
            net = 'network'
            acl_rule.append(net)
            acl_rule.append(self.src_ip)
            ace = ' '.join(map(str, acl_rule))
        else:
            print("No source IP Provided!")

        if self.src_port:
            acl_rule.append(self.src_port)
            ace = ' '.join(map(str, acl_rule))

        if self.dst_ip:
            host= 'host'
            acl_rule.append(host)
            acl_rule.append(self.dst_ip)
            ace = ' '.join(map(str, acl_rule))
        elif self.dst_ip.network():
            net ='network'
            acl_rule.append(net)
            acl_rule.append(self.dst_ip)
            ace = ' '.join(map(str, acl_rule))

        if self.dst_port:
            acl_rule.append('eq')
            acl_rule.append(self.dst_port)
            ace = ' '.join(map(str, acl_rule))

        return ace

    def proposed_rule(self):
        """ This method creates a file for AC Entry(ACE) rule, ACL entry will be placed in the file
         and be used to configure the ACL."""

        with open(self.proposed_config_output, 'w') as f:
            proposed_config = f.write(self.acl())
            return proposed_config

    def rollback_rule(self):
        """ This method creates a rollback plan from the proposed config rule, which can be used to rollback
        configuration
            """

        with open(self.proposed_config_output, 'r') as cnf:
            rule = cnf.readline()
            rule = rule.strip()
            #print(rule)
        with open(self.rollback_config_output, 'w') as f:
            rollback = 'no ' + rule
            #print(rollback)
            rollback_config = f.write(rollback)
            return rollback_config

    def file_combine(self):
        """ This method creates a full config plan with proposal and the rollback plan,
         which can later be used for auditing purpose and change tracking.  """

        with open(self.proposed_config_output) as f1:
            file1 = f1.readline()
        with open(self.rollback_config_output) as f2:
            file2 = f2.readline()
        with open(self.combine_config_output, 'w') as f:
            f.write("Proposed Config: \n")
            f.write("================ \n")
            output = f.write(file1)
            output = f.write('\n\n')
            f.write("Rollback Config: \n")
            f.write("================ \n")
            output = f.write(file2)
        with open(self.combine_config_output, 'r') as fr:
            readfile = fr.read()
            print(readfile+"\n")

        return output


class CISCO(ACLGEN):
    """ Cisco child class
    """
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    proposed_config_output = f'_cisco_proposed_{day}_{month}_{year}_{hour}_{minute}.txt'
    rollback_config_output = f'_cisco_rollback_{day}_{month}_{year}_{hour}_{minute}.txt'
    combine_config_output = f'_cisco_combine_config_{day}_{month}_{year}_{hour}_{minute}.txt'

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        super().__init__(src_ip, dst_ip, src_port, dst_port, protocol, action)


class UnsupportedEosAccessListError(Error):
    """When a filter type is not supported in an EOS policy target."""

class ARISTA(ACLGEN):
    """ Arista child class
        """
    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    proposed_config_output = f'_arista_proposed_{day}_{month}_{year}_{hour}_{minute}.txt'
    rollback_config_output = os.path.join('/acl_rules/arista_rollback.txt')
    combine_config_output  = os.path.join('/acl_rules/arista_combine_config.txt')



    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        super().__init__(src_ip, dst_ip, src_port, dst_port, protocol, action)


    def _AppendTargetByFilterType(self, filter_name, filter_type):
        target = []
        if filter_type == 'standard':
            if filter_name.isdigit():
                target.append('no access-list %s' % filter_name)
            else:
                target.append('no ip access-list standard %s' % filter_name)
                target.append('ip access-list standard %s' % filter_name)
        elif filter_type == 'extended':
            target.append('no ip access-list %s' % filter_name)
            target.append('ip access-list %s' % filter_name)
        elif filter_type == 'object-group':
            target.append('no ip access-list %s' % filter_name)
            target.append('ip access-list %s' % filter_name)
        elif filter_type == 'inet6':
            target.append('no ipv6 access-list %s' % filter_name)
            target.append('ipv6 access-list %s' % filter_name)
        else:
            raise UnsupportedEosAccessListError('access list type %s not supported by %s' % (
                    filter_type, self._PLATFORM))
        return target

class JUNIPER(ACLGEN):
    """ Juniper child class
        Method to be configured at later stage
        """
    proposed_config_output = 'juniper_proposed.txt'
    rollback_config_output = 'juniper_rollback.txt'
    combine_config_output  = 'juniper_combine_config.txt'

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        super().__init__(src_ip, dst_ip, src_port, dst_port, protocol, action)

class FORTINET(ACLGEN):
    """ Fortinet child class
        proposed config,
        Rollback config
        combine planned config
        Method to be configured at later stage
        """
    proposed_config_output = 'forti_proposed.txt'
    rollback_config_output = 'forti_rollback.txt'
    combine_config_output  = 'forti_combine_config.txt'

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        super().__init__(src_ip, dst_ip, src_port, dst_port, protocol, action)

    def facl(self):
        pass


def main():

    src_ip = '10.10.20.1'
    dst_ip = '10.10.21.1'
    src_port = 'any'
    dst_port = 80
    protocol = 'tcp'
    action = 'permit'

    gen = ACLGEN(src_ip, dst_ip, src_port, dst_port, protocol, action)

    gen.acl()
    gen.proposed_rule()
    gen.rollback_rule()
    gen.file_combine()


if __name__ == "__main__":
    main()
    exit()
