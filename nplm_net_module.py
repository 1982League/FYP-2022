#!/usr/bin/python3
from napalm import get_network_driver
import json

class NETCONN:

    def __init__(self, netos, ip, username, password):
        
        self.netos = netos
        self.ip = ip
        self.username = username
        self.password = password
        self.driver = get_network_driver(self.netos)
        self.npconn = self.driver(self.ip, self.username, self.password)
        self.npconn.open()


    def close(self):
        self.npconn.close()

    def dumpoutput(self,output):
        dump = json.dumps(output, indent=2)
        return dump
    
    def get_result(self, dump):
        result = self.dumpoutput(dump)
        return result

    def get_interfaces_info(self):
        output = self.npconn.get_interfaces()
        result = self.dumpoutput(output)
        return result
    
    def get_arp_info(self):
        output = self.npconn.get_arp_table()
        result = self.dumpoutput(output)
        return result

    def get_bgp_config_info(self):
        output = self.npconn.get_bgp_config()
        result = self.dumpoutput(output)
        return result

    def get_bgp_neighbors_info(self):
        output = self.npconn.get_bgp_neighbors()
        result = self.dumpoutput(output)
        return result

    def get_bgp_neighbors_detail_info(self):
        output = self.npconn.get_bgp_neighbors_detail()
        result = self.dumpoutput(output)
        return result


    def get_config_info(self):
        output = self.npconn.get_config(retrieve='all')
        result = self.dumpoutput(output)
        return result

    def get_environment_info(self):
        output = self.npconn.get_environment()
        result = self.dumpoutput(output)
        return result

    def get_facts_info(self):
        output = self.npconn.get_facts()
        result = self.dumpoutput(output)
        return result

    def get_interfaces_counters_info(self):
        output = self.npconn.get_interfaces_counters()
        result = self.dumpoutput(output)
        return result

    def get_interfaces_ip_info(self):
        output = self.npconn.get_interfaces_ip()
        result = self.dumpoutput(output)
        return result

    def get_lldp_neighbors_info(self):
        output = self.npconn.get_lldp_neighbors()
        result = self.dumpoutput(output)
        return result

    def get_lldp_neighbors_detail_info(self):
        output = self.npconn.get_lldp_neighbors_detail()
        result = self.dumpoutput(output)
        return result

    def get_mac_address_table_info(self):
        output = self.npconn.get_mac_address_table()
        result = self.dumpoutput(output)
        return result

    def get_network_instances_info():
        output = self.npconn.get_lldp_network_instances()
        result = self.dumpoutput(output)
        return result

    def get_ntp_peers_info(self):
        output = self.npconn.get_ntp_peers()
        result = self.dumpoutput(output)
        return result

    def get_ntp_servers_info(self):
        output = self.npconn.get_ntp_servers()
        result = self.dumpoutput(output)
        return result
    
    def get_ntp_stats_info(self):
        output = self.npconn.get_ntp_stats()
        result = self.dumpoutput(output)
        return result

    def get_optics_info(self):
        output = self.npconn.get_optics()
        result = self.dumpoutput(output)
        return result

    def get_probes_config_info(self):
        output = self.npconn.get_probes_config()
        result = self.dumpoutput(output)
        return result

    def get_probes_results_info(self):
        output = self.npconn.get_probes_results()
        result = self.dumpoutput(output)
        return result

    def get_route_to_info(self, destination, protocol):
        output = self.npconn.get_route_to(destination, protocol)
        result = self.dumpoutput(output)
        return result

    def get_snmp_info(self):
        output = self.npconn.get_snmp_information()
        result = self.dumpoutput(output)
        return result

    def get_users_info(self):
        output = self.npconn.get_users()
        result = self.dumpoutput(output)
        return result

    def get_vlans_info(self):
        output = self.npconn.get_vlans()
        result = self.dumpoutput(output)
        return result

    def has_pending_commit_info(self):
        output = self.npconn.has_pending_commit()
        result = self.dumpoutput(output)
        return result

    def is_alive_info(self):
        output = self.npconn.is_alive()
        result = self.dumpoutput(output)
        return result

    def load_merge_candidate_config(self, filename):
        output = self.npconn.load_merge_candidate(filename)
        result = self.dumpoutput(output)
        return result

    def load_replace_candidate_config(self, filename):
        output = self.npconn.load_replace_candidate_config(filename)
        result = self.dumpoutput(output)
        return result

    def load_template_config(self, template_name, tsource, tpath, **template_vars):
        output = self.npconn.load_template(template_name, tsource, tpath, **template_vars)
        result = self.dumpoutput(output)
        return result

    def ping_info(self, dst, src, src_int):
        output = self.npconn.ping(dst, src, src_int)
        result = self.dumpoutput(output)
        return result

    def post_connection_tests_info(self): 
        output = self.npconn.post_connection()
        result = self.dumpoutput(output)
        return result
    
    def pre_connection_tests_info(self):
        output = self.npconn.pre_connection_tests()
        result = self.dumpoutput(output)
        return result

    def rollback_change(self):
        output = self.npconn.rollback()
        result = self.dumpoutput(output)
        return result

    def traceroute_info(self, dst, src, vrf):
        output = self.npconn.traceroute(dst, src, vrf)
        result = self.dumpoutput(output)
        return result

    def config_compare_info(self):
        diff = self.npconn.compare_config()
        if len(diff):
            return True
        else:
            return False
    
    def commit_config(self):
        commit = self.npconn.commit_config()
        result = self.dumpout(commit)
        return result

    def discared_config(self):
        discard = self.npconn.discard_config()
        result = self.dumpout(discard)
        return result
    
    def load_merge_config(self, filename, mergefilename):
        self.npconn.load_replace_candidate(filename)
        merge = self.npconn.load_merge_candidate(mergefilename)
        self.compare_config_info()
        if len(self.diff):
            print(self.diff)
            print("Applying Config...")
            self.npconn.commit_config()
        else:
            print("No Changes to the config..")
            self.npconn.discard_config()
    
    def load_replace_config(self, filename):
        self.npconn.load_replace_canddiate(filename)
        diff = self.npconn.compare_config()
        if len(diff):
            print(diff)
            self.commit_config()
        else:
            print("Changes discarded")
            self.discard_config()
    


    


