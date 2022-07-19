#!/usr/bin/python3
from datetime import datetime
from netmiko import ConnectHandler
#import getpass

with open('devices.txt') as f:
    devices = f.read().splitlines()
#password = getpass.getpass("Password: ")
for ip in devices:
    cisco_device ={
                    'device_type':'cisco_ios',
                    'host': ip,
                    'port': 22,
                    'username':'netlab',
                    'password':'netlab',
                    'verbose' : True
    }
    conn = ConnectHandler(**cisco_device)
    output = conn.send_command('show run')
    hostname = conn.find_prompt().strip('#')

    print("=" * 90 + "\n")
    print(f'Backing up {hostname}')

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day
    hour = now.hour
    minute = now.minute

    filename = f'{hostname}_{day}_{month}_{year}_backup.txt'
    with open(filename,'w') as backup:
        backup.write(output)
        print(f'Backup of {hostname} completed Successfully')
        print('=' * 90 + "\n")

    print(f'Closing Connection to {hostname}')
    conn.disconnect()
    print("=" *90 + "\n")