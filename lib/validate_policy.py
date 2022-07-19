#!/usr/bin/python3
import json
import logging

logger = logging.getLogger(__name__)

class Policies:
    """ This Class provides policy validation and policy parser for ACL Tool,
        this class helps our tool in decision making to execute ACL configuration.
    """

    def __init__(self, src_ip, src_port, dst_ip, dst_port, protocol, action):
        """ This is a class instructor, it instantiating all the parameters required for ACL
            more parameters can be added at any stage.
        """
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.protocol = protocol
        self.action = action


    def get_policy(self):
        """ This method is a policy parser/checker for the corporate policy, It opens a policies.json file,
        and checks if the given parameter are internal resources to perform ACL on the network device
        Any DMZ access must be reviewed by Chief Information Security Officer has access to this file.
        All external resources will be denied access.
            """

        with open('policies.json') as f:
            access_policies = json.load(f)
            pol_dict = {}
            for key, values in access_policies.items():
                if (self.src_ip in access_policies['ftp']['source_ip']) and\
                   (self.dst_ip in access_policies['ftp']['destination_ip']) and \
                   (self.protocol in access_policies['ftp']['protocol']) and \
                   (self.dst_port in access_policies['ftp']['dst_port']) and \
                   (self.action in access_policies['ftp']['action']):

                    pol_dict['ftp'] = access_policies['ftp']
                    return pol_dict

                if (self.src_ip in access_policies['ssh']['source_ip']) and\
                   (self.dst_ip in access_policies['ssh']['destination_ip']) and \
                   (self.protocol in access_policies['ssh']['protocol']) and \
                   (self.dst_port in access_policies['ssh']['dst_port']) and \
                   (self.action in access_policies['ssh']['action']):

                    pol_dict['ssh'] = access_policies['ssh']
                    return pol_dict

                if (self.src_ip in access_policies['telnet']['source_ip']) and\
                   (self.dst_ip in access_policies['telnet']['destination_ip']) and \
                   (self.protocol in access_policies['telnet']['protocol']) and \
                   (self.dst_port in access_policies['telnet']['dst_port']) and \
                   (self.action in access_policies['telnet']['action']):

                    pol_dict['telnet'] = access_policies['telnet']
                    return pol_dict

                if (self.src_ip in access_policies['smtp']['source_ip']) and\
                   (self.dst_ip in access_policies['smtp']['destination_ip']) and \
                   (self.protocol in access_policies['smtp']['protocol']) and \
                   (self.dst_port in access_policies['smtp']['dst_port']) and \
                   (self.action in access_policies['smtp']['action']):

                    pol_dict['smtp'] = access_policies['smtp']
                    return pol_dict

                if (self.src_ip in access_policies['ipsec']['source_ip']) and\
                   (self.dst_ip in access_policies['ipsec']['destination_ip']) and \
                   (self.protocol in access_policies['ipsec']['protocol']) and \
                   (self.dst_port in access_policies['ipsec']['dst_port']) and \
                   (self.action in access_policies['ipsec']['action']):

                    pol_dict['ipsec'] = access_policies['ipsec']
                    return pol_dict

                if (self.src_ip in access_policies['dns']['source_ip']) and\
                   (self.dst_ip in access_policies['dns']['destination_ip']) and \
                   (self.protocol in access_policies['dns']['protocol']) and \
                   (self.dst_port in access_policies['dns']['dst_port']) and \
                   (self.action in access_policies['dns']['action']):

                    pol_dict['dns'] = access_policies['dns']
                    return pol_dict

                if (self.src_ip in access_policies['dhcp']['source_ip']) and\
                   (self.dst_ip in access_policies['dhcp']['destination_ip']) and \
                   (self.protocol in access_policies['dhcp']['protocol']) and \
                   (self.dst_port in access_policies['dhcp']['dst_port']) and \
                   (self.action in access_policies['dhcp']['action']):

                    pol_dict['dhcp'] = access_policies['dhcp']
                    return pol_dict

                if (self.src_ip in access_policies['tftp']['source_ip']) and\
                   (self.dst_ip in access_policies['tftp']['destination_ip']) and \
                   (self.protocol in access_policies['tftp']['protocol']) and \
                   (self.dst_port in access_policies['tftp']['dst_port']) and \
                   (self.action in access_policies['tftp']['action']):

                    pol_dict['tftp'] = access_policies['tftp']
                    return pol_dict

                if (self.src_ip in access_policies['http']['source_ip']) and\
                   (self.dst_ip in access_policies['http']['destination_ip']) and \
                   (self.protocol in access_policies['http']['protocol']) and \
                   (self.dst_port in access_policies['http']['dst_port']) and \
                   (self.action in access_policies['http']['action']):

                    pol_dict['http'] = access_policies['http']
                    return pol_dict

                if (self.src_ip in access_policies['pop3']['source_ip']) and\
                   (self.dst_ip in access_policies['pop3']['destination_ip']) and \
                   (self.protocol in access_policies['pop3']['protocol']) and \
                   (self.dst_port in access_policies['pop3']['dst_port']) and \
                   (self.action in access_policies['pop3']['action']):

                    pol_dict['pop3'] = access_policies['pop3']
                    return pol_dict

                if (self.src_ip in access_policies['nntp']['source_ip']) and\
                   (self.dst_ip in access_policies['nntp']['destination_ip']) and \
                   (self.protocol in access_policies['nntp']['protocol']) and \
                   (self.dst_port in access_policies['nntp']['dst_port']) and \
                   (self.action in access_policies['nntp']['action']):

                    pol_dict['nntp'] = access_policies['nntp']
                    return pol_dict

                if (self.src_ip in access_policies['ntp']['source_ip']) and\
                   (self.dst_ip in access_policies['ntp']['destination_ip']) and \
                   (self.protocol in access_policies['ntp']['protocol']) and \
                   (self.dst_port in access_policies['ntp']['dst_port']) and \
                   (self.action in access_policies['ntp']['action']):

                    pol_dict['ntp'] = access_policies['ntp']
                    return pol_dict

                if (self.src_ip in access_policies['ldap']['source_ip']) and\
                   (self.dst_ip in access_policies['ldap']['destination_ip']) and \
                   (self.protocol in access_policies['ldap']['protocol']) and \
                   (self.dst_port in access_policies['ldap']['dst_port']) and \
                   (self.action in access_policies['ldap']['action']):

                    pol_dict['ldap'] = access_policies['ldap']
                    return pol_dict

                if (self.src_ip in access_policies['https']['source_ip']) and\
                   (self.dst_ip in access_policies['https']['destination_ip']) and \
                   (self.protocol in access_policies['https']['protocol']) and \
                   (self.dst_port in access_policies['https']['dst_port']) and \
                   (self.action in access_policies['https']['action']):

                    pol_dict['https'] = access_policies['https']
                    return pol_dict

                if (self.src_ip in access_policies['sql']['source_ip']) and\
                   (self.dst_ip in access_policies['sql']['destination_ip']) and \
                   (self.protocol in access_policies['sql']['protocol']) and \
                   (self.dst_port in access_policies['sql']['dst_port']) and \
                   (self.action in access_policies['sql']['action']):

                    pol_dict['sql'] = access_policies['sql']
                    return pol_dict

                if (self.src_ip in access_policies['rdp']['source_ip']) and\
                   (self.dst_ip in access_policies['rdp']['destination_ip']) and \
                   (self.protocol in access_policies['rdp']['protocol']) and \
                   (self.dst_port in access_policies['rdp']['dst_port']) and \
                   (self.action in access_policies['rdp']['action']):

                    pol_dict['rdp'] = access_policies['rdp']
                    return pol_dict

                if (self.src_ip in access_policies['dmz']['source_ip']) and \
                   (self.dst_ip in access_policies['dmz']['destination_ip']) and \
                   (self.protocol in access_policies['dmz']['protocol']) and \
                   (self.dst_port in access_policies['dmz']['dst_port']) and \
                   (self.action in access_policies['dmz']['action']):

                    pol_dict['dmz'] = access_policies['dmz']
                    return pol_dict
                break
            else:
                print("Access Policy is not found, please contact security team!")
                exit(1)

    def add_policy(self):
        """ This method adds new policy to the corporate policy file in json format,
            Only Chief Information Security Officer has access to this file.
        """

        filename = 'policy_test.json'
        service = input("Service: ")
        policy = input("Policy Description: ")
        source_ip = input("Source IP: ")
        protocol = input("Protocol[TCP/UDP/IP]: ")
        src_port = input("Source Port: ")
        dst_port = input("Destination Port: ")
        action = input("Action: ")
        destination_ip = input("Destination IP: ")

        update_policy = {service:
                             {"policy": policy,
                              "source_ip": source_ip,
                              "protocol": protocol,
                              "src_port": src_port,
                              "dst_port": dst_port,
                              "action": action,
                              "destination_ip": destination_ip
                              }
                         }
        with open(filename, 'a') as f:
            new_policy = json.dumps(update_policy, indent=4)
            # s1 = '}'.replace('\n}', '\n')
            # f.write(s1)
            # s2 = '{'.replace('\n{', '')
            # f.write(s2)
            # f.write(",")
            f.write(new_policy)
            # f.write("\n")

    def remove_policy(self):
        """ This method removes the existing policy from the corporate policy,
        Only Chief Information Security Officer has access to this file.
        """
        policy ='policies.json'
        service=input("Remove Service: ")
        with open('../policy/policies.json') as f:
            obj = json.load(f)
            for i in range(len(obj)):
                if obj[i]['service'] == service:
                    obj.pop(i)
                    break
        print(f"{service } record removed from {policy}!")


