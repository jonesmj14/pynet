import os
from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(
    "host": "cisco3.lasthop.io",
    "username": "pyclass",
    "password": password,
    "device_type": "cisco_ios",
)

output = net_connect.send_command(
    "show ip arp"
)
 
print(output)
