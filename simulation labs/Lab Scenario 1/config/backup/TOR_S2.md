# TOR_S2's Hardware/Software Information
```bash
QEMU VM TOR_S2 is started
  Running on server netlab with port 3080
  Local ID is 34 and server ID is fe523ec6-6820-4de5-80e5-1dcb0c19715a
  Number of processors is 1 and amount of memory is 768MB
  Console is on port 5156 and type is telnet
     Gi0/0 connected to Switch4 on port Ethernet0
       MAC address is 0c:52:3e:c6:00:00
     Gi0/1 connected to Switch5 on port Ethernet0
       MAC address is 0c:52:3e:c6:00:01
     Gi0/2 connected to Core_S1 on port Gi0/2
       MAC address is 0c:52:3e:c6:00:02
     Gi0/3 is empty
       MAC address is 0c:52:3e:c6:00:03
     Gi1/0 is empty
       MAC address is 0c:52:3e:c6:00:04
     Gi1/1 is empty
       MAC address is 0c:52:3e:c6:00:05
     Gi1/2 is empty
       MAC address is 0c:52:3e:c6:00:06
     Gi1/3 is empty
       MAC address is 0c:52:3e:c6:00:07
     Gi2/0 is empty
       MAC address is 0c:52:3e:c6:00:08
     Gi2/1 is empty
       MAC address is 0c:52:3e:c6:00:09
     Gi2/2 is empty
       MAC address is 0c:52:3e:c6:00:0a
     Gi2/3 is empty
       MAC address is 0c:52:3e:c6:00:0b
     Gi3/0 is empty
       MAC address is 0c:52:3e:c6:00:0c
     Gi3/1 is empty
       MAC address is 0c:52:3e:c6:00:0d
     Gi3/2 is empty
       MAC address is 0c:52:3e:c6:00:0e
     Gi3/3 is empty
       MAC address is 0c:52:3e:c6:00:0f
```
## TOR_S2's Configuration
```bash
Current configuration : 4553 bytes
!
! Last configuration change at 11:13:38 UTC Tue May 31 2022
!
version 15.2
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
service compress-config
!
hostname TOR_S2
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
ip domain-name netlab.net
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
 switchport access vlan 700
 switchport trunk encapsulation dot1q
 switchport mode access
 media-type rj45
 negotiation auto
!
interface GigabitEthernet0/1
 switchport access vlan 100
 switchport trunk encapsulation dot1q
 switchport mode access
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
 switchport access vlan 700
 switchport trunk allowed vlan 11,20,30,55,80,100,700,800,900
 switchport mode access
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/1
 switchport access vlan 100
 switchport mode access
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/2
 switchport access vlan 700
 switchport mode access
 media-type rj45
 negotiation auto
!
interface GigabitEthernet1/3
 switchport access vlan 100
 switchport mode access
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
 media-type rj45
 negotiation auto
!
interface GigabitEthernet3/3
 media-type rj45
 negotiation auto
!
interface Vlan11
 ip address 10.1.11.3 255.255.255.0
!
interface Vlan20
 no ip address
!
interface Vlan30
 no ip address
!
interface Vlan55
 no ip address
!
interface Vlan80
 no ip address
!
interface Vlan100
 no ip address
!
interface Vlan700
 no ip address
!
interface Vlan800
 no ip address
!
interface Vlan900
 no ip address
!
router ospf 1
 network 0.0.0.0 255.255.255.255 area 0
!
ip forward-protocol nd
!
no ip http server
no ip http secure-server
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
