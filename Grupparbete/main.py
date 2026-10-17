from getpass import getpass

from netmiko import ConnectHandler

device_dict = {
    "device_type": "cisco_ios",
    "host": "192.168.1.193",
    "username": "drift",
    "password": getpass("Losenord: "),
}

with ConnectHandler(**device_dict) as anslutning:
    hostname = anslutning.send_command("show running-config | include hostname") # fetches only line with hostname from running config
    program_version = anslutning.send_command("show version | include Version") # fetches only line with program version
    device_model = anslutning.send_command("show version | include Cisco CISCO") # fetches only the line with device model
    interfaces = anslutning.send_command("show ip interface brief") # fetches lines showing interface status

print(f"Hostname: {hostname}")
print(f"Program Version: {program_version}")
print(f"Device Model: {device_model}")
print(f"Interfaces: {interfaces}")

with open("rapport.txt", "w") as f:
    f.write(hostname)
    f.write(program_version)
    f.write(device_model)
    f.write(interfaces)

