# FYP-2022
Msc Cybersecurity - MTU Final Year Project 2022

# Auomation of Network ACL

Network ACL Automation tool is designed to automate Network Access Control list for multi-vendor network devices within corporate network inline with defined Access Control Policies. This tool is developed as a part of MTU Final Year project in 2022 for MSC Cybersecurity.

The tool consists of Network Module, Validate, Validate_services, Find_target, Telnet_check Clases and the main script for the tools.

# acl_tool.py

The Script would take all the parameters shown below

============================== Enter Info ======================================

Source IP Address: 10.1.1.1

Destination IP Address: 10.105.5.1

Source Port: 22

Destination Port: 22

Protocol[TCP/UDP]: tcp

Action [Permit/Deny]: permit

================================================================================

The given IP/Network addresses, Port/Service should be Validated before going further.
After the Validation, discovery of network path of the IP will be taken care of.

The Network Module will prompt for Username and Password for the Network device and establish SSH Connection.

#  Validate ValidateAddresses Class:
Parameter: IP Address or Subnet Address
It checkes the IP Address and
Returns Valid IP Address, IP with CIDR  Notation, Subnet Mask, Private or Public IP Address Boolean Flag

============================== IP Validation ===================================

Source IP: 10.1.1.1

CIDR: 10.1.1.1/32

Net Mask: 255.255.255.255

Private IP: True

================================================================================

#  Validate_Services ValidateServices Class:
Parameters: Protocol, Service or Port Number
Returns Protocol ServiceName and Port Number

============================== Service Info ====================================

Source Port: tcp/SSH[22]

Destination Port: tcp/SSH[22]

================================================================================

#  Telnet_Check PortOpen Class:
Parameters: Destination IP Address & Port Number
Returns: If the port for the given IP Address is open or not

============================== Connection Check for Port Open ==================

Example 1:

SSH[22] is open for 10.20.1.1

Example 2:

TELNET[23] is not open for 10.40.1.1

================================================================================

#  Find_target TargetIP Class:
Takes Destination IP Address as a parameter.

Returns with Target_IP Address &

Network Path: Last 3 IP Hops to the Border Router/Firewall/Switch

============================== Fetching Target IP Address ======================

Target IP: 10.20.1.1

Target hop lists Addresses: ('10.10.1.1', '10.30.1.1', '10.40.1.1')

================================================================================

# Network Access Policies GetPolicy Class:

============================== Pulling Access Control Policy ===================

{'ssh':
        {
          'policy': 'SSH_Policy: Secure Shell access can be permitted to only internal subnets.',
          'source_ip': '10.1.11.0/24',
          'protocol': 'tcp',
          'port': 22,
          'permission': 'permit',
          'destination_ip': '10.1.100.0/24, 10.1.200.0/24',
        }
}

Policy not found!

================================================================================

#  Network Module SSHLogin Class:
Network Moudle is designed to interact with various Network devices with SSH connection, Module takes IP/Host, Username, Password as a parameter and establishes SSH connection.
Returns with SSH Connection, Network Device Operating System Version and Network Device Hostname.

There are methods to execute show commands, network config commands, and many other methods for network admins.

============================== SSH Connection to 10.105.1.155 ==================

Username: netlab

Password:

============================== Host information ================================

Hostname: cork_router1

Version: cisco nexus

============================== Writing output to File ==========================

cork_router01_22_5_2022_18_28_config.txt

============================== Backing up Current Config =======================

cork_router01_22_5_2022_18_28_backup.txt

================================================================================

Closing connection 10.20.1.1

================================================================================

Execution Time: 57.09 Seconds, Timestamp: 22-May-2022 - 18:28:54

================================================================================

# Testing ACL Builder with List and Dictionary

============================== Sample ACL Builder - Cisco ======================

ACL_Builder List: permit tcp host/network 10.1.1.1 22 host/network 10.105.5.1 eq 22

ACL_Builder Dict:
{

  'permission': 'permit',

  'protocol': 'tcp',

  'source address': '10.1.1.1',

  'source port': ('TCP', 'SSH', '22'),

  'destination address': '10.105.5.1',

  'operator': 'eq',

  'destination port': ('TCP', 'SSH', '22')

 }

================================================================================
