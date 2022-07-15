#!/usr/bin/python3
import logging

logger = logging.getLogger(__name__)

class ACLGEN:
    """
        This class Generates ACL for Multiple Network devices,
        Cisco, Arista, Juniper, Fortinet
        returns: proposed config file, rollback config and config plan file
    """

    proposed_config_output = 'acl_proposed.txt'
    rollback_config_output = 'acl_rollback.txt'
    combine_config_output  = 'acl_combine_config.txt'

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
            acl_rule.append(self.src_ip)
            ace = ' '.join(map(str, acl_rule))
        else:
            print("No source IP Provided!")

        if self.src_port:
            acl_rule.append(self.src_port)
            ace = ' '.join(map(str, acl_rule))
        if self.dst_ip:
            acl_rule.append(self.dst_ip)
            ace = ' '.join(map(str, acl_rule))

        if self.dst_port:
            acl_rule.append('eq')
            acl_rule.append(self.dst_port)
            ace = ' '.join(map(str, acl_rule))

        return ace

    def proposed_rule(self):
        """ This method creates a file for ACE rule, ACL entry will be placed in the file
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
            print(rule)
        with open(self.rollback_config_output, 'w') as f:
            rollback = 'no ' + rule
            print(rollback)
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
        #with open(self.combine_config_output, 'r') as fr:
        #    readfile = fr.read()
        #    print(readfile)

        return output


class CISCO(ACLGEN):
    """ Cisco child class
    """
    proposed_config_output = 'cisco_proposed.txt'
    rollback_config_output = 'cisco_rollback.txt'
    combine_config_output = 'cisco_combine_config.txt'

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        super().__init__(src_ip, dst_ip, src_port, dst_port, protocol, action)

class ARISTA(ACLGEN):
    """ Arista child class
        """
    proposed_config_output = 'arista_proposed.txt'
    rollback_config_output = 'arista_rollback.txt'
    combine_config_output  = 'arista_combine_config.txt'

    def __init__(self, src_ip, dst_ip, src_port, dst_port, protocol, action):
        super().__init__(src_ip, dst_ip, src_port, dst_port, protocol, action)


class JUNIPER(ACLGEN):
    """ Juniper child class
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
