#!/usr/bin/python3
import json
class Policies:

    
    def __init__(self,src_ip, src_port, dst_ip, dst_port, protocol, action):
        
        self.src_ip = src_ip
        self.src_port = src_port
        self.dst_ip = dst_ip
        self.dst_port = dst_port
        self.protocol = protocol
        self.action = action


    def get_policy(self):
        
        with open('policies.json') as f:
            access_policies = json.load(f)
            pol_dict = {}
            for key, values in access_policies.items():
                
                if (self.dst_port in access_policies['ssh']['port']) and (self.src_ip in
                access_policies['ssh']['source_ip']) and (self.protocol in access_policies['ssh']['protocol']) and (self.action in access_policies['ssh']['action']):
                    

                    pol_dict['ssh'] = access_policies['ssh']
                    
                    return pol_dict

                if (self.dst_port in access_policies['http']['port']) and (self.src_ip in   
                access_policies['http']['source_ip']) and (self.protocol in access_policies['http']['protocol']) and (self.action in access_policies['http']['action']):

                    pol_dict['http'] = access_policies['http']

                    return pol_dict

                if (self.dst_port in access_policies['dmz']['port']) and (self.src_ip in
                access_policies['dmz']['source_ip']) and (self.action in access_policies['dmz']['action']):
                    
                    pol_dict['dmz'] = access_policies['dmz']

                    return pol_dict
                
                break
            else:
                print("Access Rule not found!")
                exit(1)
        
