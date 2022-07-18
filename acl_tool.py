#!/usr/bin/python3
import sys
import pyfiglet
from colorama import Fore, Style
from netmiko.ssh_exception import NetMikoAuthenticationException, SSHException, NetMikoTimeoutException
from lib.validate_addresses import Validate
from lib.validate_services import ValidateService
from lib.find_target import TargetIP
from lib.telnet_check import PortOpen
from lib.validate_policy import Policies
from lib.net_module import SSHLogin
from lib.telnet_module import Device
from aclgen import ACLGEN
import time
import getpass
from datetime import datetime

"""
-- ACL Tool --
- This tool is designed to be used in any network, and developed in python3 
- This tool will validate the ip address, network address
- Tool will validate the Service name or Port number before proceeding further
- The tool will find out if the given destination port is open for the destination address
- It will check Network Access Policy and pull the policy
- The tool will find out the network border interface and ip address
- The tool will connect to the network device securely
- The connection will return with Hostname and Network OS of the network device platform
- It will execute the commands asynchronously as per the requirements
- Tool will check IP route, VLAN Name, VLAN Information, Applied ACL name, Object Group Name
- The tool will generate an ACL as per the given parameters and network platform
- The tool will propose ACL configuration and Rollback Configuration in a text file, in the same directory of the tool
- It will configure the Access Control List on the network interface from propose acl config
- All the output will be stored in the Text file in the same directory as the tool
- Rollback method can be used in case of any unplanned outage or misconfiguration
"""

""" Author Information """
__author__ = "Siddharth Joshi"
__email__ = "siddharth.joshi@mycit.ie"
__project__ = "MTU - MSc in Cybersecurity"
__ProjectName__ = "Automating Network Security through Adaptive Policy Driven Access Control"

""" Project Banner print with some colour effects """
banner= pyfiglet.figlet_format("Automating Network Security through Adaptive Policy Driven Access Control")
print(Style.BRIGHT, Fore.GREEN)
print(banner)

""" Tool Usage Instructions """
print(Style.BRIGHT,Fore.GREEN)
print('=' * 30 + ' ACL Tool Usage Instructions ' + '=' * 30)
print('# \tEnter relevant information to allow source network to access\t\t\t\t\t\t#\n'
      '# \tresources from destination network with specific services\t\t\t\t\t\t\t#')
print('# \tPlease enter Source IP Address or Network Address \t\t\t\t\t\t\t\t\t#')
print('# \tPlease enter Destination IP Address or Network Address\t\t\t\t\t\t\t\t#')
print('# \tPlease enter Source Port\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
print('# \tPlease enter Destination Port\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
print('# \tPlease enter Protocol\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t\t#')
print('# \tPlease enter the Action to be Taken for the given parameters\t\t\t\t\t\t#')
print('# \tOPS ticket number, a text file will be created of the number, all the,\t\t\t\t#\n'
      '# \tinformation will be stored in the file, file will be located with the tool\t\t\t#')
print("=" * 89 + "\n")
print(Style.RESET_ALL)

"""This works good in Network Automation Docker"""
""" Tool Usage Instructions """
"""
print(Style.BRIGHT,Fore.GREEN)
print('=' * 30 + ' ACL Tool Usage Instructions ' + '=' * 30)
print('# \tEnter relevant information to allow source network to access\t\t\t#\n'
      '# \tresources from destination network with specific services\t\t\t#')
print('# \tPlease enter Source IP Address or Network Address \t\t\t\t#')
print('# \tPlease enter Destination IP Address or Network Address\t\t\t\t#')
print('# \tPlease enter Source Port\t\t\t\t\t\t\t#')
print('# \tPlease enter Destination Port\t\t\t\t\t\t\t#')
print('# \tPlease enter Protocol\t\t\t\t\t\t\t\t#')
print('# \tPlease enter the Action to be Taken for the given parameters\t\t\t#')
print('# \tOPS ticket number, a text file will be created of the number, all the,\t\t#\n'
      '# \tinformation will be stored in the file, file will be located with the tool\t#')
print("=" * 89 + "\n")
print(Style.RESET_ALL)
"""


""" Getting Parameters from the user - User Request"""
print("=" * 30 + " Enter Info " + "=" * 47 + "\n")

src_add = input("Source IP Address: ")
dst_add = input("Destination IP Address: ")
src_port = input("Source Port: ")
dst_port = input("Destination Port: ")
protocol = input("Protocol[TCP/UDP]: ")
action = input("Action [Permit/Deny]: ")
OPS_Ticket = input("OPS-Ticket [OPS-123654]: ")

now = datetime.now()
year = now.year
month = now.month
day = now.day
hour = now.hour
minute = now.minute
OpsTicketInfo = f'{OPS_Ticket}_{day}_{month}_{year}_{hour}_{minute}.txt'

"""Creating a ticket file to store information with day_month_year_hour_minute to distinguish requests"""
with open(OpsTicketInfo, 'a') as f:
    print("=" * 30 + " " + OpsTicketInfo+ " Created " + "=" * 20 + "\n")
    f.write("=" * 30 + " " + OpsTicketInfo+ " Created " + "=" * 20 + "\n")
    print(Style.BRIGHT, Fore.CYAN + "All the operational data will be appended to the file for "
                                    "tracking and auditing purpose.\n" + Style.RESET_ALL)
    f.write(OpsTicketInfo + "\nAll the operational data will be appended to the file for "
                            "tracking and auditing purpose.\n")

    f.write("=" * 30 + " User Request " + "=" * 47 + "\n")
    f.write("Source IP Address: " + src_add + "\n")
    f.write("Destination IP Address: " + dst_add + "\n")
    f.write("Source Port: " + src_port + "\n")
    f.write("Destination Port: " + dst_port + "\n")
    f.write("Protocol[TCP/UDP]: " + protocol + "\n")
    f.write("Action [Permit/Deny]: " + action + "\n")
    f.write("OPS-Ticket [OPS-123654]:" + OPS_Ticket+ "\n" )
    f.write("\n")

    """ Validating - User Request parameters - IP/Network Address"""
    print("=" * 30 + " IP Validation " + "=" * 45 + "\n")
    src = Validate(src_add)
    src_ip = src.address_check()
    ip_list=['Source IP:','CIDR:','Net Mask:','Private IP:']
    f.write("=" * 30 + " IP Validation " + "=" * 45 + "\n")
    if src_ip is None:
        print("=" * 90 + "\n")
        sys.exit(1)
    else:
        for i, j in zip(ip_list,src_ip):
            print(i, j, sep=' ')
            f.write(str(i) + " " + str(j) + "\n")

        print("=" * 90)
        f.write("\n" + "=" * 90 + "\n")

    src_ip= src_ip[0]
    dst = Validate(dst_add)
    dst_ip = dst.address_check()

    ip_list=['Destination IP:','CIDR:','Net Mask:','Private IP:']

    if dst_ip is None:
        print("=" * 90 + "\n")
        exit(1)
    else:
        for i, j in zip(ip_list,dst_ip):
            print(i, j, sep=' ')
            f.write(str(i) + " " + str(j) + "\n")

    dst_ip=dst_ip[0]
    print("=" * 30 + " Service Info " + "=" * 46 + "\n")
    f.write("\n" + "=" * 30 + " Service Info " + "=" * 46 + "\n")

    """ Validating Service - User Request parameters - Source """
    src_serv = ValidateService(src_port, protocol)
    src_serviceName = src_serv.get_service()
    src_service = src_serviceName[1]
    src_port = src_serviceName[2]
    print("Source Port: " +  protocol.upper()+"/"+src_service+"["+src_port+"]") #(str(src_serviceName))
    f.write("Source Port: " +  protocol.upper()+"/"+src_service+"["+src_port+"]" + "\n")

    """ Validating Service - User Request parameters - Destination """
    dst_serv = ValidateService(dst_port, protocol)
    dst_serviceName = dst_serv.get_service()
    dst_service = dst_serviceName[1]
    dst_port = dst_serviceName[2]
    print("Destination Port: " + protocol.upper()+"/"+dst_service+"["+dst_port+"]") #(str(dst_serviceName))
    dst_service_port = dst_service+"["+dst_port+"]"
    f.write("Destination Port: " + protocol.upper()+"/"+dst_service+"["+dst_port+"]" + "\n")

    """ Port check using Telnet for Destination IP Address and Port  """
    print()
    print("=" * 30 + " Connection Check for Port Open " + "=" * 29 + "\n")
    f.write("=" * 30 + " Connection Check for Port Open " + "=" * 29 + "\n")
    if not dst_port.isdigit():
        dst_srv = ValidateService(dst_port, protocol)
        dst_servi = dst_serv.get_service()
        dst_port = dst_srv.get_port_number()
        portopen = PortOpen(dst_ip, dst_port)
    else:
        portopen = PortOpen(dst_ip, dst_port)

    if portopen.is_open() and portopen.check_host():
        print(f'{dst_service_port} is open for {dst_ip}')
        f.write(f'{dst_service_port} is open for {dst_ip}' + "\n")
    else:
        print(f'{dst_service_port} is not open for {dst_ip}')
        f.write(f'{dst_service_port} is not open for {dst_ip}' + "\n")

    """ Target IP - Network Boundary using MTR """
    print()
    print("="*30 + " Fetching Target IP Address " + "="* 33 + "\n")
    f.write("="*30 + " Fetching Target IP Address " + "="* 33 + "\n")
    target_ip = TargetIP(dst_ip)
    ip = target_ip.get_target_ip()
    ip = ip.strip()  #AttributeError: 'NoneType' object has no attribute 'strip'
    print("Target IP: " + ip)
    f.write("Target IP: " + ip + "\n")

    """ Policy Parsing/Policy Check with user request parameters """
    print("=" * 30 + " Pulling Access Control Policy " + "="*22 + "\n")
    f.write("=" * 30 + " Pulling Access Control Policy " + "="*22 + "\n")
    pol_check = Policies(src_ip, src_port, dst_ip, dst_port, protocol, action)
    print()
    policy = pol_check.get_policy()
    print(policy)
    f.write(policy + "\n")
    print()
    if policy is None:
        print(Style.BRIGHT,Fore.BLUE + "Please Contact Chief Security Officer to review the request!")
        f.write("Please Contact Chief Security Officer to review the request!")
        print(Style.RESET_ALL)
    elif 'dmz' in policy:
        print(Style.BRIGHT, Fore.RED + "Please Contact Chief Security Officer to review the request!")
        f.write("Please Contact Chief Security Officer to review the request!")
        print(Style.RESET_ALL)

    """ Prompting user for Login Option """
    print("\n" + "=" * 30 + " Choose SSH or Telnet for login " + "="*20 +"\n")
    f.write("\n" + "=" * 30 + " Choose SSH or Telnet for login " + "="*20 +"\n")
    login_option = (
        "1. SSH\n"
        "2. Telnet\n"
        "0. Exit"
        "\nEnter your choice[1/2]: "
    )
    f.write(
        "1. SSH\n"
        "2. Telnet\n"
        "0. Exit"
        "\nEnter your choice[1/2]: ")

    option = input(login_option)
    f.write("Login_Option" + option)

    """ Instatiating Network Connection using SSH - DO NOT USE Telnet - it is Optional """
    if option == "1" or option == "SSH" or option == "ssh":
        print("=" * 30 + f" Sshing to {ip} " + "="*20 +"\n")
        f.write("=" * 30 + f" Sshing to {ip} " + "="*20 +"\n")
        start = time.time()

        user = input("Username: ")
        f.write("Username: " + user + "\n")
        password = getpass.getpass()

        try:
            conn = SSHLogin(ip, user, password)
        except NetMikoAuthenticationException:
            print(Fore.RED + "=" * 89)
            print(f'Authentication failed on {ip}, please check your username and password.\n')
            print(Style.RESET_ALL)
        except NetMikoTimeoutException:
            print(Fore.RED + "=" * 89)
            print(f'{ip} is not reachable, check your network connection!! \n')
            print(Style.RESET_ALL)
        except SSHException:
            print(Fore.RED + "=" * 89)
            print(f'SSH is not enabled on {ip}, please configure SSH!\n')
            print(Style.RESET_ALL)

        hostname = conn.get_hostname_ip()
        print("Hostname: " + conn.hostname)
        print("Version: " + conn.version)
        f.write("Hostname: " + conn.hostname + "\n" + "Version: " + conn.version + "\n")
        version = conn.check_ios()
        print("=" * 89 + "\n")
        f.write("=" * 89 + "\n")

        from alive_progress import alive_bar; import time
        for total in 500, 0:#700, 400, 0:
            with alive_bar(total) as bar:
                for _ in range(500):
                    time.sleep(.001)
                    bar()

        if 'cisco nexus' in version:

            #get vlan name on the fly automated way
            ip_route_info = conn.get_ip_route(src_ip)
            f.write(ip_route_info + "\n")
            #vlan_name = 'VLAN444'
            vlan_name = conn.get_vlan_info(ip_route_info)
            print(conn.get_vlan_config(vlan_name))
            f.write(vlan_name + "\n")

            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")
            # Get tcam count before applying config
            var_cmd = 'show hardware access-list resource utilization'
            f.write(var_cmd + "\n")
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            # get ACL Name
            acl_name = 'ASNI_N9K_VTY_ACL'

            #acl_name = conn.get_acl_info(vlan_name)
            print(conn.get_acl_config(acl_name))
            f.write(conn.get_acl_config(acl_name) + "\n")

            print("=" *40 + " Backing up current Config " + "=" *17 + "\n")
            conn.get_acl_config("=" *40 + " Backing up current Config " + "=" *17 + "\n")
            conn.current_config_backup()
            f.write(conn.current_config_backup() + "\n")

            print(conn.current_config_backup())
            f.write(conn.current_config_backup() + "\n")

            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            print(conn.var_commands(var_cmd))
            f.write(conn.var_commands(var_cmd))

            print("=" * 40 + " Writing output to File " + "="* 20 + "\n")
            output = conn.get_object_groups()
            conn.write_output_to_file(output)
            print(conn.write_output_to_file(output))

            print("=" * 40 + " NAPALM Testing " + "="* 28 + "\n")

            print("=" * 40 + " Backing up Current Config " + "="* 17 + "\n")
            conn.current_config_backup()
            print(conn.current_config_backup())
            print("=" * 84 + "\n")

        elif 'cisco ios' in version:

            print(conn.get_ip_route(src_ip))
            print("=" * 89 + "\n")
            f.write(conn.get_ip_route(src_ip))
            f.write("=" * 89 + "\n")

            vlan_name = conn.get_vlan_info()
            print(vlan_name)
            f.write(vlan_name)

            print(conn.get_vlan_config(vlan_name))
            f.write(conn.get_vlan_config(vlan_name) + "\n")
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            acl_name = conn.get_acl_name()
            f.write(acl_name + "\n")
            print(conn.get_acl_config(acl_name))
            f.write(conn.get_acl_config(acl_name))
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            print("=" * 40 + " NAPALM Testing " + "="* 28 + "\n")
            f.write("=" * 40 + " NAPALM Testing " + "="* 28 + "\n")
            nos = 'ios'
            print(conn.config_rollback(nos))
            f.write(conn.config_rollback(nos) + "\n")
            print("=" * 89 + "\n")
            #print(conn.var_commands(var_cmd))

            print("=" * 40 + " Writing output to File " + "="* 20 + "\n")
            output = conn.get_object_groups()
            conn.write_output_to_file(output)
            print(conn.write_output_to_file(output))

            print("=" * 40 + " Backing up Current Config " + "="* 17 + "\n")
            f.write("=" * 40 + " Backing up Current Config " + "="* 17 + "\n")
            current_config_backup = conn.current_config_backup()

            conn.current_config_backup()
            f.write(conn.current_config_backup() + "\n")
            print(conn.current_config_backup())
            f.write(conn.current_config_backup()+ "\n")
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            print("=" * 40 + " Generating ACL " + "="* 40 + "\n")
            f.write("=" * 40 + " Generating ACL " + "="* 40 + "\n")
            gen = ACLGEN(src_ip,src_port,dst_ip,dst_port,protocol,action)
            gen.acl()
            f.write(gen.acl() + "\n")
            proposed_acl = gen.proposed_rule()
            rollback_acl = gen.rollback_rule()
            gen.file_combine()
            f.write(gen.file_combine() + "\n")

            config_acl = input("Do you want to configure proposed ACL [yes|no]? ")
            if config_acl == 'yes':
                print("=" * 40 + " Configuring ACL " + "="* 40 + "\n")
                conn.send_config_list(proposed_acl)
                rollback = ("Do you want to rollback the config [yes|no]?")
                if rollback == 'yes':
                    conn.send_config_list(rollback_acl)
                    print(Fore.RED +"ACL Configuration is removed.." + Style.RESET_ALL)
                else:
                    print("You have chose not to rollback the ACL config!!")
            else:
                print("=" * 40 + " No ACL is configured " + "="* 40 + "\n")


        elif 'juniper junos' in version:

            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")
            uptime = conn.get_junos_uptime()
            print(uptime)
            f.write(uptime + "\n")

            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            sysinfo = conn.get_junos_sysinfo()
            print(sysinfo)
            f.write(sysinfo + "\n")
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")

            inter = conn.get_junos_interfaces()
            print(inter)
            f.write(inter + "\n")

            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")
        elif 'arista eos' in version:
            print("Arista")
            f.write("Arista")
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")
        elif 'fortinet' in version:
            print("Fortinet")
            f.write("Fortinet")
            print("=" * 89 + "\n")
            f.write("=" * 89 + "\n")
        else:
            print("Version Not found, Please check the device!!")

        rule = ACLGEN(src_ip, dst_ip, src_port, dst_port, protocol, action)
        rule.acl()
        rule.proposed_rule()
        rule.rollback_rule()
        rule.file_combine()

        print(f'Closing connection {ip}')
        f.write(f'Closing connection {ip}')
        conn.close_connection()

        end = time.time()
        print("=" * 89 + "\n")
        f.write("=" * 89 + "\n")
        runtime = (end-start)
        runtime = ("%.2f" % runtime)
        dateTimeObj = datetime.now()
        today = dateTimeObj.strftime("%d-%b-%Y - %H:%M:%S")
        print("Execution Time: " + str(runtime) + " Seconds, Timestamp: " + str(today)+ "\n")
        f.write(("Execution Time: " + str(runtime) + " Seconds, Timestamp: " + str(today)+ "\n"))

    elif option == "2" or option == "Telnet" or option == "telnet":
        print("=" * 30 + f" Telnetting to {target_ip} " + "="*20 +"\n")
        f.write("=" * 30 + f" Telnetting to {target_ip} " + "="*20 +"\n")
        user = input("Username: ")
        f.write("Username: " + user + "\n")
        password = getpass.getpass()

        tnet = Device(target_ip, user, password)
        tnet.read_until(b'Username: ')
        tnet.write(user.encode() + b'\n')
        tnet.read_until(b'Password: ')
        tnet.write(password.encode() + b'\n')
        cmd_list = ['show version', 'show ip int brief', 'show run int vlan', 'show ip access list']
        f.write(cmd_list)
        for cmd in cmd_list:
            tnet.write(cmd.encode + b"\n")
        output = tnet.read_all().decode()
        print(output)
        f.write(output)

    elif option == "0" or option == "Exit":
        print("Exiting from the tool")
        f.write("Exiting from the tool")
        exit()
    else:
        print("Wrong choice!!")
        help()
        exit()

    print("=" * 89)

#@staticmethod
def help():
    #The Help is to guide a user how to use the script.

    print("===================================== Help ===============================================")
    print("For Help: ./acl_tool")  # if you dont enter any sys args the help is going to be called
    print("Usage of Script: python3 ./acl_tool")  # example usage for Script
    print("Source IP Address: 10.1.20.1")
    print("Destination IP Address: 10.1.30.1" )
    print("Source Port: any")
    print("Destination Port: 80 ")
    print("Protocol[TCP/UDP]: tcp")
    print("Action [Permit/Deny]: permit")
    print("OPS Ticket [OPS-135975]: OPS-453687")

