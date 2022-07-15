# Cork_Router01's Hardware/Software Information
```bash
Router Cork_Router01 is started
  Running on server netlab with port 3080
  Local ID is 7 and server ID is 0c92cd38-e437-457c-8f4f-9937aaa1b29f
  Dynamips ID is 2
  Hardware is Dynamips emulated Cisco c3725  with 256MB RAM and 256KB NVRAM
  Console is on port 5065 and type is telnet, AUX console is on port None
  IOS image is "c3725-adventerprisek9-mz.124-15.T14.image"
  with no idlepc value
  PCMCIA disks: disk0 is 0MB and disk1 is 0MB
    slot 0 hardware is GT96100-FE with 2 ports
      FastEthernet0/0 connected to Core_S1 on port Gi0/0
      FastEthernet0/1 connected to Switch2 on port Ethernet4
    slot 1 hardware is NM-1FE-TX with 1 port
      FastEthernet1/0 is empty
    slot 2 hardware is NM-4T with 4 ports
      Serial2/0 is empty
      Serial2/1 connected to R1 on port Serial2/1
      Serial2/2 connected to R3 on port Serial2/2
      Serial2/3 is empty
    WIC-1T installed in WIC slot 0 with 1 port
      Serial0/0 is empty
    WIC-2T installed in WIC slot 1 with 2 ports
      Serial0/1 is empty
      Serial0/2 is empty
```
* [Network Topology](https://github.com/1982League/NetworkAutomationLabs/blob/main/Lab%201%20-%20Cisco/layout/Network_Lab.jpg)
* [GNS3 Network Project file](https://github.com/1982League/NetworkAutomationLabs/tree/main/Lab%201%20-%20Cisco/GNS3%20Project)

### 1.1. Cork_Router01's configuration
#### Router's Interfaces
```bash
interface Loopback0
 ip address 1.1.1.2 255.255.255.255
!
interface FastEthernet0/0
 ip address 10.1.11.254 255.255.255.0
 duplex auto
 speed auto
!
interface Serial0/0
 no ip address
 shutdown
 clock rate 2000000
!
interface FastEthernet0/1
 description Up link to Core_S1 on Gi0/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex auto
 speed auto
!

interface Serial2/1
 ip address 8.1.1.2 255.255.255.252
 serial restart-delay 0
!
interface Serial2/2
 ip address 8.1.3.1 255.255.255.252
 serial restart-delay 0
```
#### Username Configuration
```bash
hostname Cork_Router01
!
ip domain name netlab.net
ip name-server 8.8.8.8
!
logging buffered 4096 critical
logging console alerts
enable password 7 011D0310570A04

username netlab privilege 15 password 7 000A1612085A09
```

#### Default Routes
```bash
ip forward-protocol nd
ip route 0.0.0.0 0.0.0.0 8.1.1.1
ip route 0.0.0.0 0.0.0.0 10.1.11.1
```

#### OSPF Internal Routing configuration
```bash
router ospf 1
 log-adjacency-changes
 network 0.0.0.0 255.255.255.255 area 0
!
```
#### BGP routing protocol configuration
```bash
router bgp 65001
 no synchronization
 bgp log-neighbor-changes
 network 8.1.1.0 mask 255.255.255.252
 network 8.1.2.0 mask 255.255.255.252
 network 8.1.3.0 mask 255.255.255.252
 network 10.1.2.0 mask 255.255.255.0
 network 10.1.3.0 mask 255.255.255.0
 network 10.1.11.0 mask 255.255.255.0
 network 10.1.12.0 mask 255.255.255.0
 network 10.1.20.0 mask 255.255.255.0
 network 10.1.21.0 mask 255.255.255.0
 network 10.1.30.0 mask 255.255.255.0
 network 10.1.31.0 mask 255.255.255.0
 network 10.1.55.0 mask 255.255.255.224
 network 10.1.80.0 mask 255.255.255.0
 network 10.1.81.0 mask 255.255.255.0
 network 10.1.250.0 mask 255.255.255.240
 network 10.1.251.0 mask 255.255.255.240
 network 10.10.10.0 mask 255.255.255.0
 neighbor 1.1.1.3 remote-as 65001
 neighbor 1.1.1.3 update-source Loopback0
 neighbor 8.1.1.1 remote-as 65000
 no auto-summary
```

#### DHCP Scope configuration for virtual interfaces
```bash
ip dhcp relay information option
no ip dhcp use vrf connected
ip dhcp excluded-address 10.1.20.1 10.1.20.5
ip dhcp excluded-address 10.1.30.1 10.1.30.5
ip dhcp excluded-address 10.1.55.1
ip dhcp excluded-address 10.1.55.129
ip dhcp excluded-address 10.1.2.1
ip dhcp excluded-address 192.168.100.1
!
ip dhcp pool FirstFloor_VLAN20
   network 10.1.20.0 255.255.255.0
   default-router 10.1.20.1
   domain-name netlab.net
   dns-server 8.8.8.8
!
ip dhcp pool SecondFloor_VLAN30
   network 10.1.30.0 255.255.255.0
   default-router 10.1.30.1
   domain-name netlab.net
   dns-server 8.8.8.8
!
ip dhcp pool Printers_VLAN55
   network 10.1.55.0 255.255.255.224
   default-router 10.1.55.1
   domain-name netlab.net
   dns-server 8.8.8.8
!
ip dhcp pool Utilities_VLAN100
   network 10.1.2.128 255.255.255.128
   default-router 10.1.2.129
   domain-name netlab.net
   dns-server 8.8.8.8
!
ip dhcp pool Wireless_VLAN700
   network 10.1.2.0 255.255.255.128
   default-router 10.1.2.1
   domain-name netlab.net
   dns-server 8.8.8.8
!
ip dhcp pool GUEST_VLAN900
   network 192.168.100.0 255.255.255.0
   default-router 192.168.100.1
   domain-name wr
   dns-server 8.8.8.8
!
ip dhcp pool Printers_VLAN80
   network 10.1.80.0 255.255.255.0
   default-router 10.1.80.1
   domain-name wr
   dns-server 8.8.8.8
!
ip dhcp pool Network_Management_VLAN11
   network 10.1.11.0 255.255.255.128
   default-router 10.1.11.1
   domain-name netlab.net
   dns-server 8.8.8.8
!
ip dhcp pool LAN
   network 192.168.20.0 255.255.255.0
   default-router 192.168.20.1
   domain-name wr
   dns-server 8.8.8.8

```
#### Line configuration
```bash
line con 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line aux 0
 exec-timeout 0 0
 privilege level 15
 logging synchronous
line vty 0 4
 transport input all
!
ntp server 188.168.3.28

```
