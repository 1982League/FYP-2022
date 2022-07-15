# ISP1's Hardware/Software Information
```bash
Router ISP1 is started
  Running on server netlab with port 3080
  Local ID is 6 and server ID is dde1e93b-151e-4d2a-867d-652226726d07
  Dynamips ID is 1
  Hardware is Dynamips emulated Cisco c3725  with 256MB RAM and 256KB NVRAM
  Console is on port 5064 and type is telnet, AUX console is on port None
  IOS image is "c3725-adventerprisek9-mz.124-15.T14.image"
  with no idlepc value
  PCMCIA disks: disk0 is 0MB and disk1 is 0MB
    slot 0 hardware is GT96100-FE with 2 ports
      FastEthernet0/0 connected to ISP2 on port eno1
      FastEthernet0/1 is empty
    slot 1 hardware is NM-1FE-TX with 1 port
      FastEthernet1/0 is empty
    slot 2 hardware is NM-4T with 4 ports
      Serial2/0 connected to R3 on port Serial2/0
      Serial2/1 connected to R2 on port Serial2/1
      Serial2/2 is empty
      Serial2/3 is empty
    WIC-1T installed in WIC slot 0 with 1 port
      Serial0/0 is empty
    WIC-2T installed in WIC slot 1 with 2 ports
      Serial0/1 is empty
      Serial0/2 is empty
```
* [Network Topology](https://github.com/1982League/NetworkAutomationLabs/blob/main/Lab%201%20-%20Cisco/layout/Network_Lab.jpg)
* [GNS3 Network Project file](https://github.com/1982League/NetworkAutomationLabs/tree/main/Lab%201%20-%20Cisco/GNS3%20Project)

### 1.1. ISP1's configuration
```bash
version 12.4
service timestamps debug datetime msec
service timestamps log datetime msec
no service password-encryption
!
hostname ISP1
!
boot-start-marker
boot-end-marker
!
enable password netlab
!
aaa new-model
!
!
aaa authentication login default local
aaa authorization exec default local none
!
!
aaa session-id common
memory-size iomem 5
no ip icmp rate-limit unreachable
ip cef
!
!
ip domain name isp.net
ip name-server 8.8.8.8
!
multilink bundle-name authenticated
!
!
username netlab privilege 15 password 0 netlab
archive
 log config
  hidekeys
!
!
!
!
ip tcp synwait-time 5
ip scp server enable
!
!
!
!
interface Loopback0
 ip address 1.1.1.1 255.255.255.255
!
interface FastEthernet0/0
 description Link to ISP Cloud
 ip address 192.168.1.100 255.255.255.0
 ip nat outside
 ip virtual-reassembly
 duplex auto
 speed auto
!
interface Serial0/0
 no ip address
 shutdown
 clock rate 2000000
!
interface FastEthernet0/1
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface Serial0/1
 no ip address
 shutdown
 clock rate 2000000
!
interface Serial0/2
 no ip address
 shutdown
 clock rate 2000000
!
interface FastEthernet1/0
 no ip address
 shutdown
 duplex auto
 speed auto
!
interface Serial2/0
 description Link to R3 - S2/0 - 8.1.2.2
 ip address 8.1.2.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly
 serial restart-delay 0
!
interface Serial2/1
 description Link to R2 - S2/1 - 8.1.1.2
 ip address 8.1.1.1 255.255.255.252
 ip nat inside
 ip virtual-reassembly
 serial restart-delay 0
!
interface Serial2/2
 no ip address
 shutdown
 serial restart-delay 0
!
interface Serial2/3
 no ip address
 shutdown
 serial restart-delay 0
!
router ospf 1
 log-adjacency-changes
 network 0.0.0.0 255.255.255.255 area 0
!
router bgp 65000
 no synchronization
 bgp log-neighbor-changes
 network 8.1.1.0 mask 255.255.255.252
 network 8.1.2.0 mask 255.255.255.252
 network 8.1.3.0 mask 255.255.255.252
 neighbor 8.1.1.2 remote-as 65001
 neighbor 8.1.2.2 remote-as 65001
 no auto-summary
!
ip forward-protocol nd
ip route 0.0.0.0 0.0.0.0 192.168.122.1
ip route 0.0.0.0 0.0.0.0 192.168.1.1
!
!
no ip http server
no ip http secure-server
ip nat inside source list 1 interface FastEthernet0/0 overload
!
access-list 1 permit any
no cdp log mismatch duplex
!
!
control-plane
!
!
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
!
end
```
