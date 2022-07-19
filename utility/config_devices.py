#!/usr/bin/python3
from netmiko import ConnectHandler
import getpass

with open('devices.txt') as f:
    devices = f.read().splitlines()

device_list = list()
password = getpass.getpass("Password: ")
for ip in devices:
    cisco_device = {
        'device_type': 'cisco_ios',
        'host': ip,
        'port': 22,
        'username': 'netlab',
        'password': password,
        'verbose': True
    }
    device_list.append(cisco_device)

#print(device_list)
#exit(1)

for device in device_list:
    conn = ConnectHandler(**device)
    print("You are in Privilege Mode...")

    file = input(f'Enter a configuration file (Use valid Path) for {device["host"]}: ')

    print(f'Running commands from file: {file} on device: {device["host"]}: ')
    output = conn.send_config_from_file(file)
    print(output)

    print(f'Closing Connection to {cisco_device["host"]}')
    conn.disconnect()
    print('#' * 40)