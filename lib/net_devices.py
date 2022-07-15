"""
Common commands between Cisco nexus and IOS
to access keys  net_devices.common_cmnds.['show']['version']
to access keys  net_devices.common_cmnds.['run']['interface']
"""
common_cmnds = {
                 'show': {
                           'version'           : 'show version',
                           'ip route'          : 'show ip route',
                           'vlan'              : 'show vlan brief',
                           'interface'         : 'show run interface ',
                           'ip access-list'    : 'show ip access-list ',
                           'object-group'      : 'show object-group '
                          },
                 'run' : {
                             'config'          : 'show running-config'
                         },
                 'config': {
                            'network_security' : [
                                                    "no ip directed-broadcast",
                                                    "no service tcp-small-server",
                                                    "no service udp-small-server",
                                                    "no ip source-route",
                                                    "no ip http-server",
                                                    "no ip http secure-server",
                                                    "no cdp enable",
                                                    "no ip bootp server",
                                                    "no boot network",
                                                    "no service config"
                                                ],



                 }
                }
"""
Cisco Commands both IOS and NXOS
to access keys  net_devices.cisco_cmnds.['cisco nexus']['show commands']['version']
to access keys  net_devices.cisco_cmnds.['cisco ios']['show commands']['ip route']
to access keys  net_devices.cisco_cmnds.['cisco nexus']['any command']['tcam']
to access keys  net_devices.cisco_cmnds.['cisco ios']['any command']['tcam']
"""
cisco_cmnds = {
                'cisco nexus' :{
                                'show commands': {**common_cmnds['show']},
                                'run commands' : {**common_cmnds['run']},
                                'any command'  : {'tcam' :  'show hardware access-list resource utilization'}

                               },
                'cisco ios'   :{
                               'show commands': {**common_cmnds['show']},
                               'run commands' : {**common_cmnds['run']},
                               'any command'  : {'tcam' :   'show tcam counts detail ip'}

                               }
             }

"""
Arista EOS Commands 
to access keys  net_devices.arista_vEOS.['show']['version']
to access keys  net_devices.arista_vEOS.['show']['interface']
"""
arista_vEOS = {
            'show' :{
                        'version': 'show version',
                        'ip route': 'show ip route',
                        'vlan': 'show vlan brief',
                        'interface': 'show run interface ',
                        'ip access-list': 'show ip access-list ',
                        'object-group': 'show object-group '
                    },
            'set' : {
                        'hostname'  : 'set system hostname ',    #hostname parameter needs to be provided
                        'domain'    : 'set system domain-name ', #domain parameter needs to be provided
                        'routing'   : 'edit routing-options',   #enable ip routing
                        'service'   : 'set system services ssh' #setup ssh services
                    }
        }

"""
Arista EOS Commands 
to access keys  net_devices.forti_ftos.['show']['version']
to access keys  net_devices.forti_ftos.['show']['sysinfo']
"""

forti_ftos = {
            'show' :{
                        'version'   : 'get system status',
                        'uptime'    : 'show system uptime',
                        'config'    : 'show configuration | display set',
                        'bgp'       : 'show bgp summary',
                        'interface' : 'show interfaces brief',
                        'acl'       : 'show access-list'
                    },
            'set' : {
                        'hostname'  : 'set system hostname ',    #hostname parameter needs to be provided
                        'domain'    : 'set system domain-name ', #domain parameter needs to be provided
                        'routing'   : 'edit routing-options',   #enable ip routing
                        'service'   : 'set system services ssh' #setup ssh services
                    }
        }

"""
Juniper Commands 
to access keys  net_devices.junos_cmds.['show']['sysinfo']
to access keys  net_devices.junos_cmds.['show']['sysinfo']
to access keys  net_devices.junos_cmds.['show']['sysinfo']
to access keys  net_devices.junos_cmds.['show']['sysinfo']
"""
junos = {
            'show' :{
                        'sysinfo'   : 'show system information',
                        'uptime'    : 'show system uptime',
                        'config'    : 'show configuration | display set',
                        'bgp'       : 'show bgp summary',
                        'interface' : 'show interfaces brief',
                        'acl'       : 'show access-list'
                    },
            'set' : {
                        'hostname'  : 'set system hostname ',    #hostname parameter needs to be provided
                        'domain'    : 'set system domain-name ', #domain parameter needs to be provided 
                        'routing'   : 'edit routing-options',   #enable ip routing
                        'service'   : 'set system services ssh' #setup ssh services
                    }   
        }

linux = {
    'show': {
        'ip': 'sudo ifconfig',
        'ports': 'netstat -ntulp',
        'ip_table': 'iptables -L',

    }
}