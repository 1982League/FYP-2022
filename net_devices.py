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
