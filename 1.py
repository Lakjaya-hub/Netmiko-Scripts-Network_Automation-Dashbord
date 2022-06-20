import netmiko
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.43.207',
    'username': 'router',
    'password': 'cisco',
    'secret': 'cisco',

}

net_connect =ConnectHandler(**iosv_l2)
net_connect.enable()
output =net_connect.send_command('sh version | exclude line line')
print(output)

