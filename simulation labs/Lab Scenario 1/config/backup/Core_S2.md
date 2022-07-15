# Core_S2's Hardware/Software Information
```bash
QEMU VM Core_S2 is started
  Running on server netlab with port 3080
  Local ID is 1 and server ID is 9ce58adb-6825-4f57-9ae1-9f66045de1d3
  Number of processors is 1 and amount of memory is 768MB
  Console is on port 5054 and type is telnet
     Gi0/0 connected to London_Router01 on port FastEthernet0/0
       MAC address is 0c:e5:8a:db:00:00
     Gi0/1 connected to TOR_S3 on port Gi0/2
       MAC address is 0c:e5:8a:db:00:01
     Gi0/2 connected to TOR_S4 on port Gi0/0
       MAC address is 0c:e5:8a:db:00:02
     Gi0/3 is empty
       MAC address is 0c:e5:8a:db:00:03
     Gi1/0 is empty
       MAC address is 0c:e5:8a:db:00:04
     Gi1/1 is empty
       MAC address is 0c:e5:8a:db:00:05
     Gi1/2 is empty
       MAC address is 0c:e5:8a:db:00:06
     Gi1/3 is empty
       MAC address is 0c:e5:8a:db:00:07
     Gi2/0 is empty
       MAC address is 0c:e5:8a:db:00:08
     Gi2/1 is empty
       MAC address is 0c:e5:8a:db:00:09
     Gi2/2 is empty
       MAC address is 0c:e5:8a:db:00:0a
     Gi2/3 is empty
       MAC address is 0c:e5:8a:db:00:0b
     Gi3/0 is empty
       MAC address is 0c:e5:8a:db:00:0c
     Gi3/1 is empty
       MAC address is 0c:e5:8a:db:00:0d
     Gi3/2 is empty
       MAC address is 0c:e5:8a:db:00:0e
     Gi3/3 is empty
       MAC address is 0c:e5:8a:db:00:0f

There is no default password and enable password. There is no default configuration present.
```
## Core_S1's Configuration
```bash
Current configuration : 5177 bytes
!
! Last configuration change at 11:13:40 UTC Tue May 31 2022
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname Core_S2
!
boot-start-marker
boot-end-marker
!
!
enable password netlab
!
username netlab privilege 15 password 0 netlab
no aaa new-model
!
!
ip dhcp excluded-address 10.1.11.1 10.1.11.10
ip dhcp excluded-address 10.1.20.1 10.1.20.10
ip dhcp excluded-address 10.1.30.1 10.1.30.10
ip dhcp excluded-address 10.1.55.1
ip dhcp excluded-address 10.1.55.129
ip dhcp excluded-address 10.1.2.1
ip dhcp excluded-address 192.168.100.1
!
ip dhcp pool Management
 network 10.1.11.0 255.255.255.0
 default-router 10.1.11.1
 domain-name netlab.net
 dns-server 8.8.8.8
!
ip dhcp pool FirstFloor_VLAN20
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
 default-router 10.1.100.1
 domain-name google.com
 dns-server 8.8.8.8
!
!
ip name-server 8.8.8.8
ip cef
no ipv6 cef
!
!
spanning-tree mode pvst
spanning-tree extend system-id
!
vlan internal allocation policy ascending
!
!
interface GigabitEthernet0/0
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
 no cdp enable
!
interface GigabitEthernet0/1
 switchport trunk allowed vlan 11,20,30,55,80,100,700,800,900
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/3
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/1
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/2
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/3
 media-type rj45
 negotiation auto
!
interface GigabitEthernet2/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet2/1
 media-type rj45
 negotiation auto
!
interface GigabitEthernet2/2
 media-type rj45
 negotiation auto
!
interface GigabitEthernet2/3
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/0
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/1
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/2
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/3
 switchport trunk encapsulation dot1q
 switchport mode trunk
 media-type rj45
 negotiation auto
!
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
!
ip route 0.0.0.0 0.0.0.0 10.2.2.1
!
!
control-plane
!
banner exec ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner incoming ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
banner login ^C
**************************************************************************
* IOSv is strictly limited to use for evaluation, demonstration and IOS  *
* education. IOSv is provided as-is and is not supported by Cisco's      *
* Technical Advisory Center. Any use or disclosure, in whole or in part, *
* of the IOSv Software or Documentation to any third party for any       *
* purposes is expressly prohibited except as otherwise authorized by     *
* Cisco in writing.                                                      *
**************************************************************************^C
!
line con 0
line aux 0
line vty 0 4
 login local
 transport input all
!
!
end

```
