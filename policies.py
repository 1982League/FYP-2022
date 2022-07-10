{
 "ftp":{
    "ftp_policy": "FTP_Policy: FTP lacks security, lacks control and lack of reporting,all internal/external subnet should be deny access.",
    "source_ip": "any_ip",
    "protocol": "tcp",
    "port": 20,
    "permission": "deny",
    "destination_ip": "10.1.11.0/24",
    "acl_stndr": "deny tcp any any eq ftp",
    "acl_extnd": "deny tcp Source IP Destination_ip eq ftp"
  },
  "ssh": {
    "policy": "SSH_Policy: Secure Shell access can be permitted to only internal subnets.",
    "source_ip": "10.1.11.0/24",
    "protocol": "tcp",
    "port": 22,
    "permission": "permit",
    "destination_ip": "10.1.100.0/24, 10.1.200.0/24",
    "acl_stndr": "permit tcp any any eq ssh",
    "acl_extnd": "permit tcp host 192.168.40.1 eq 22 192.168.30.0 0.0.0.255"
  },
  "telnet": {
    "policy": "Telnet_Policy: telnet is denied in the network at any cost.",
    "source_ip": "any",
    "protocol": "tcp",
    "port": 23,
    "permission": "deny",
    "destination_ip": "10.1.11.0/25, 10.1.200.0/24"
  },
  "smtp": {
    "policy": "SMTP_Policy: Mail services are allowed, filter by third party. ",
    "source_ip": "any",
    "protocol": "tcp",
    "port": 25,
    "permission": "permit",
    "destination_ip": "10.0.0.0/8"
  },
  "ipsec": {
    "policy": "IPSec_Policy: Permitted only corporate subnets.",
    "source_ip": "10.1.0.0/24",
    "protocol": "tcp",
    "port": 50,
    "permission": "permit",
    "destination_ip": "10.1.100.0/24, 10.1.200.0/24"
  },
  "dns": {
    "policy": "DNS_Policy: DNS requests are permitted for domain lookup.",
    "source_ip": "10.1.20.0/24",
    "protocol": "tcp/udp",
    "port": 53,
    "permission": "permit",
    "destination_ip": "any_ip"
  },
  "dhcp": {
    "policy": "DHCP_Policy: DHCP requests are permitted for internal corp infra.",
    "source_ip": "any",
    "protocol": "udp",
    "port": [
      67,
      68
    ],
    "permission": "permit",
    "destination_ip": "any"
  },
  "tftp": {
    "policy": "TFTP_Policy: TFTP are not permitted.",
    "source_ip": "any",
    "protocol": "udp",
    "port": 69,
    "permission": "deny",
    "destination_ip": "any"
  },
  "http": {
    "policy": "HTTP_Policy: HTTP requests to dev is permitted for testing.",
    "source_ip": "10.1.10.0/24",
    "protocol": "tcp",
    "port": 80,
    "permission": "permit",
    "destination_ip": "10.1.100.0/24, 10.1.200.0/24"
  },
  "pop3": {
    "policy": "POP3_Policy: Mail protocol allowed for emails.",
    "source_ip": "10.1.20.0/24",
    "protocol": "tcp",
    "port": 110,
    "permission": "permit",
    "destination_ip": "any_ip"
  },
  "nntp": {
    "policy": "NNTP_Policy: Are allowed access.",
    "source_ip": "any",
    "protocol": "tcp",
    "port": 119,
    "permission": "permit",
    "destination_ip": "any"
  },
  "ntp": {
    "policy": "NTP_Policy: Denied access.",
    "source_ip": "any",
    "protocol": "tcp",
    "port": 123,
    "permission": "deny",
    "destination_ip": "any"
  },
  "ldap": {
    "policy": "LDAP_Policy: LDAP Access is permitted to internal corp.",
    "source_ip": "any",
    "protocol": "tcp",
    "port": 389,
    "permission": "permit",
    "destination_ip": "any"
  },
  "https": {
    "policy": "HTTPS_Policy: Access Permitted for specific subnets.",
    "source_ip": "10.1.10.0/24",
    "protocol": "tcp",
    "port": 443,
    "permission": "permit",
    "destination_ip": "10.1.100.0/24, 10.1.200.0/24"
  },
  "sql": {
    "policy": "SQL_Policy: Access permitted for specific Subnets.",
    "source_ip": "10.1.30.0/16",
    "protocol": "tcp",
    "port": 3306,
    "permission": "permit",
    "destination_ip": "10.1.200.0/24"
  },
  "rdp": {
    "policy": "RDP_Policy: Is only permitted for corp/ip-sec subnets, deny for external.",
    "source_ip": "10.0.0.0/8",
    "protocol": "tcp",
    "port": 3389,
    "permission": "permit",
    "destination_ip": "10.0.10.0/24"
  },
  "dmz": {
    "policy": "DMZ_Policy: Any DMZ Access request needs manual reviewed by CISO.",
    "source_ip": "any",
    "protocol": "tcp",
    "port": "any",
    "permission": "deny",
    "destination_ip": "any"
  }
}
