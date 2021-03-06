#!/usr/bin/python3

import os
import sys
import ipaddress
import argparse

class TargetIP():
    """
        This class is used to find out Target IP address of the network boundary of the given destination ip address
     to check where should the ACL be applied. It uses MTR network diagnostic tool to find the network interface
     where network is configured.
    """
    def __init__(self, dst_ip):
        """Class constructure instantiation uses destination IP Address as a parameter"""
        
        self.dst_ip = dst_ip


    def get_target_ip(self):
        """ This method launches the mtr command and records all the hops, creates a reverse list
            and returns Target ip address with the last 3 hops to check network boundary in case of the last
            Hop may not be the correct one."""

        try: 
            if "/" not in self.dst_ip:
                mtr_result = os.popen("mtr -r " + self.dst_ip).read()
                mtr = mtr_result.split()
                target_ip = mtr[-17]
                target_hoplist=[]
                counter = 1
                for i in range(16, len(mtr), 9):
                   # print("Hop " + str(counter) + ". " + mtr[i])
                    counter += 1
                    target_hoplist.append(mtr[i])
                #print("\nTarget IP: " + target_ip + "\n")

                return target_ip #, target_hoplist[:-5:-1]

                #for addr in target_hoplist:
                #    if not ipaddress.IPv4Address(addr).is_private:
                #        target_hoplist.remove(addr)
                
                #return target_hoplist[-3:]


            elif ipaddress.ip_network(self.dst_ip) and "/" in self.dst_ip:
                
                #print("Network IP: " + self.dst_ip)
                self.dst_ip = self.dst_ip.split("/")
                self.dst_ip = self.dst_ip[0].strip()
                #print(self.dst_ip)

                mtr_result = os.popen("mtr -r " + self.dst_ip).read()
                #print(mtr_result)
                mtr = mtr_result.split()
                target_ip = mtr[-17]
                target_hoplist=[]
                counter = 1
                for i in range(16, len(mtr), 9):
                   # print("Hop " + str(counter) + ". " + mtr[i])
                    counter += 1
                    target_hoplist.append(mtr[i])
                #print("\nTarget IP: " + target_ip + "\n")
                return target_ip #, target_hoplist[:-5:-1]

                #for addr in target_hoplist:
                #    if not ipaddress.IPv4Address(addr).is_private:
                #        target_hoplist.remove(addr)

                #return target_hoplist[-3:]
                
        except:
            print(f"{self.dst_ip}")


    def get_ip(self):
        """ This method simply extracts the target IP address from the main method, for future scalability"""
        target_ip, target_hoplist  = self.get_target_ip()
        target_ip = target_ip.split()
        target_ip = target_ip[0]
        target_ip = target_ip.strip()
        return target_ip

    def get_hoplist(self):
        """ This method fetches the hop list from the main method for scalability"""
        target_ip, target_hoplist = self.get_target_ip()
        return target_hoplist
