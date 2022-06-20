import netmiko
from netmiko import ConnectHandler

iosv_l2 = {
    'device_type': 'cisco_ios',
    'ip':   '192.168.43.212',
    'username': 'admin',
    'password': 'admin',
    'secret': 'admin',

}

net_connect =ConnectHandler(**iosv_l2)
net_connect.enable()
output =net_connect.send_command('sh version | exclude line line')
print(output)

