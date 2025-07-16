from netmiko import ConnectHandler
from rich import print as r_print

devices = [
{
    'device_type': 'cisco_ios',
    'host': '10.55.1.2',
    'username': 'Marv',
    'password': 'cisco',
    'port': '22'
},
{
    'device_type': 'cisco_ios',
    'host': '10.55.1.3',
    'username': 'Marv',
    'password': 'cisco',
    'port': '22'
}
]

num = 0

for device in devices:

    num += 1

    not_connect = ConnectHandler(**device)

    output_show_version = not_connect.send_command(command_string="show run")
    output_host_name = not_connect.send_command(command_string="show run | i hostname")
    hostname = output_host_name.strip().split()[-1]  
    r_print(output_show_version)
    print(type(output_show_version))

    with open(f'show_version_output_{hostname}.txt', 'w') as f:
        f.write(str(output_show_version))