#!/usr/bin/python3
import pyfiglet
import socket
from validate_addresses import Validate
from validate_services import ValidateService
from find_target import TargetIP
from telnet_check import PortOpen
from validate_policy import Policies
from net_module import SSHLogin
import time
import getpass
from datetime import datetime

banner= pyfiglet.figlet_format("Automating Network Security through Adaptive Policy Driven Access Control")
print(banner)
#print(" This Script takes the input from the user validates the IP Addresses and Ports\n & displays it!\n")

acl_dict = {}
acl_builder = []

print("=" * 30 + " Enter Info " + "=" * 35 + "\n")
src_add = input("Source IP Address: ")
dst_add = input("Destination IP Address: ")
src_port = input("Source Port: ")
dst_port = input("Destination Port: ")
protocol = input("Protocol[TCP/UDP]: ")
action = input("Action [Permit/Deny]: ") 
remark = input("Comment/[OPS ticket]: ")

print("=" * 30 + " IP Validation " + "=" * 35 + "\n")

src = Validate(src_add)
src_ip = src.address_check()
ip_list=['Source IP:','CIDR:','Net Mask:','Private IP:']

if src_ip is None:
    print("=" * 80 + "\n")
    exit(1)
else:
    for i, j in zip(ip_list,src_ip):
        print(i, j, sep=' ')
    
    print("=" * 80)

src_ip= src_ip[0]

dst = Validate(dst_add)
dst_ip = dst.address_check()

ip_list=['Destination IP:','CIDR:','Net Mask:','Private IP:']

if dst_ip is None:
    print("=" * 80 + "\n")
    exit(1)
else:     
    for i, j in zip(ip_list,dst_ip):
        print(i, j, sep=' ')
dst_ip=dst_ip[0]

print("=" * 30 + " Service Info " + "=" * 35 + "\n")

src_serv = ValidateService(src_port, protocol)
src_serviceName = src_serv.get_service()
src_service = src_serviceName[1]
src_port = src_serviceName[2]
print("Source Port: " +  protocol+"/"+src_service+"["+src_port+"]") #(str(src_serviceName))

dst_serv = ValidateService(dst_port, protocol)
dst_serviceName = dst_serv.get_service()
dst_service = dst_serviceName[1]
dst_port = dst_serviceName[2]
print("Destination Port: " + protocol+"/"+dst_service+"["+dst_port+"]") #(str(dst_serviceName))

dst_service_port = dst_service+"["+dst_port+"]"

print()
print("=" * 30 + " Sample ACL Builder - Cisco " + "=" * 25 + "\n")

# Action Protocol SourceAddress SourcePort DestinationAddres eq DestinationPort
acl_dict.update({'permission': action})
acl_dict.update({'protocol': protocol})
acl_dict.update({'source address': src_ip})
acl_dict.update({'source port': src_serviceName})
acl_dict.update({'destination address': dst_ip})
acl_dict.update({'operator' : 'eq'})
acl_dict.update({'destination port': dst_serviceName})
# ACL Rule Builder
acl_builder.insert(0, action)
acl_builder.append(protocol)
acl_builder.append('host/network')
acl_builder.append(src_ip)
acl_builder.append(src_serviceName[2])
acl_builder.append('host/network')
acl_builder.append(dst_ip)
acl_builder.append('eq')
acl_builder.append(dst_serviceName[2])
# Making the ACL Rule with join
print(' '.join(acl_builder))
#print(acl_dict)
print()
print("=" * 30 + " Connection Check for Port Open " + "=" * 20 + "\n")

if not dst_port.isdigit():
    dst_srv = ValidateService(dst_port, protocol)
    dst_servi = dst_serv.get_service()
    dst_port = dst_srv.get_port_number()
    portopen = PortOpen(dst_ip, dst_port)
else:
    portopen = PortOpen(dst_ip, dst_port)
    
if portopen.is_open() and portopen.check_host():
    print(f'{dst_service_port} is open for {dst_ip}')
else:
    print(f'{dst_service_port} is not open for {dst_ip}')
                        
print()
print("="*30 + " Fetching Target IP Address " + "="* 20 + "\n")

target_ip = TargetIP(dst_ip)
ip = target_ip.get_target_ip()
ip = ip.strip()
print("Target IP: " + ip)

print("=" * 30 + " Pulling Access Control Policy " + "="*22 + "\n")

pol_check = Policies(src_ip, src_port, dst_ip, dst_port, protocol, action)
print()
policy = pol_check.get_policy()
print(policy)
print()
if policy is None:
    print("Please Contact Network Security to check the Policy")


print("\n" + "=" * 30 + " Choose SSH or Telnet for login " + "="*20 +"\n")


login_option = (
    "1. SSH\n"
    "2. Telnet\n"
    "0. Exit"
    "\nEnter your choice[1/2]: "
)
option = input(login_option)


if option == "1" or option == "SSH" or option == "ssh":
    print("=" * 30 + f" Sshing to {ip} " + "="*20 +"\n")
    start = time.time()
    
    user = input("Username: ")
    password = getpass.getpass()
                                       
    conn = SSHLogin(ip, user, password)
    
    hostname = conn.get_hostname_ip()
    print("Hostname: " + conn.hostname)
    print("Version: " + conn.version)

    version = conn.check_ios()
    print("=" * 84 + "\n")

    from alive_progress import alive_bar; import time
    for total in 500, 0:#700, 400, 0:
        with alive_bar(total) as bar:
            for _ in range(500):
                time.sleep(.001)
                bar()

    #n ="neighbor"
    #route = 'show ip ospf '
    #print(conn.set_commands(route, n))
    #print("=" * 84 + "\n")

    if 'cisco nexus' in version:
        
        #get vlan name on the fly automated way
        ip_route_info = conn.get_ip_route(src_ip)

        #vlan_name = 'VLAN444'
        vlan_name = conn.get_vlan_info(ip_route_info)

        print(conn.get_vlan_config(vlan_name))
        print("=" * 84 + "\n")
        
        # Get tcam count before applying config 
        var_cmd = 'show hardware access-list resource utilization'
        print("=" * 84 + "\n")
        
        # get ACL Name
        acl_name = 'ASNI_N9K_VTY_ACL'
        #acl_name = conn.get_acl_info(vlan_name)
        print(conn.get_acl_config(acl_name))

        print("=" *40 + " Backing up current Config " + "=" *17 + "\n")
        conn.current_config_backup()
        print(conn.current_config_backup())
        print("=" * 84 + "\n")
        
        print(conn.var_commands(var_cmd))

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
        
        #search_ip = '10.105.5.1'
        print(conn.get_ip_route(src_ip))
        print("=" * 84 + "\n")

        var_cmd = 'show tcam counts detail ip'
        vlan_name = 'Vlan4'     #10.58.32.1 vlan444
        print(conn.get_vlan_config(vlan_name))
        print("=" * 84 + "\n")
        acl_name = 'BNET-GAMING'
        print(conn.get_acl_config(acl_name))
        print("=" * 84 + "\n")
        print("=" * 40 + " NAPALM Testing " + "="* 28 + "\n")
        nos = 'ios'
        print(conn.config_rollback(nos)) #testing get_interfaces
        print("=" * 84 + "\n")

        print(conn.var_commands(var_cmd))

        print("=" * 40 + " Writing output to File " + "="* 20 + "\n")
        output = conn.get_object_groups()
        conn.write_output_to_file(output)
        print(conn.write_output_to_file(output))

        print("=" * 40 + " Backing up Current Config " + "="* 17 + "\n")
        conn.current_config_backup()
        print(conn.current_config_backup())
        print("=" * 84 + "\n")

    elif 'juniper junos' in version:
     
        print("=" * 84 + "\n")
        uptime = conn.get_junos_uptime()
        print(uptime)
        print("=" * 84 + "\n")
        
        sysinfo = conn.get_junos_sysinfo()
        print(sysinfo)
        print("=" * 84 + "\n")
        inter = conn.get_junos_interfaces()
        print(inter)

        print("=" * 84 + "\n")
    elif 'arista eos' in version:
        print("Arista")      
        print("=" * 84 + "\n")
    elif 'fortinet' in version:
        print("Fortinet")
        print("=" * 84 + "\n")
    else:
        print("Version Not found, Please check the device!!")
    
    print(f'Closing connection {ip}')
    conn.close_connection()

    end = time.time()
    print("=" * 84 + "\n")
    runtime = (end-start)
    runtime = ("%.2f" % runtime)
    dateTimeObj = datetime.now()
    today = dateTimeObj.strftime("%d-%b-%Y - %H:%M:%S")
    print("Execution Time: " + str(runtime) + " Seconds, Timestamp: " + str(today)+ "\n")


elif option == "2" or option == "SSH" or option == "ssh":
    print("=" * 30 + f" Telneting to {target_ip} " + "="*20 +"\n")
    user = input("Username: ")
    password = getpass.getpass()
    tnet = Telnet(target_ip, user, password)
    tnet.read_until(b'Username: ')
    tnet.write(self.username.encode() + b'\n')
    tnet.read_until(b'Password: ')
    tnet.write(self.password.encode() + b'\n')
    cmd_list = ['show version', 'show ip int brief', 'show run int vlan', 'show ip access list']
    for cmd in cmd_list:
        tnet.write(cmd.encode + b"\n")
    output = tnet.read_all().decode()    
    print(output)

elif option == "0" or option == "Exit":
    print("Exiting from the tool")
    exit()
else:
    print("Wrong choice!!")
    help()
    exit()

print("=" * 80)


#@staticmethod
def help():
    #The Help is to guide a user how to use the script.

    print("===================================== Help ===============================================")
    print("For Help: ./ssh_login.py and hit enter ")  # if you dont enter any sys args the help is going to be called
    print("Usage of Script: python3 ssh_login.py -i 10.58.32.163")  # example usage for Script
    print("./ssh_login.py -i 10.60.32.103")
    print("./ssh_login.py -i lax1-r3ree-hl02.network.cloud.blizzard.net")
    print("./ssh_login.py -i ams1-c6k-switch.battle.net")
    print("./ssh_login.py -i 10.105.5.1")
    print("=" * 90 + "\n")

