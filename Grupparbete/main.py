from getpass import getpass
from netmiko import ConnectHandler
import json

#dict containing the device information neccessary for ConnectionHandler to establish ssh connection
device_dict = {
    "device_type": "cisco_ios",
    "host": "192.168.1.193",
    "username": "drift",
    "password": getpass("Enter device password: "),
}

# establishes connection with device through ConnectionHandler creates a new dict called report and saves the fetched values to it
with ConnectHandler(**device_dict) as c:
    report = {
        "hostname": c.send_command("show running-config | include hostname"), # fetches only line with hostname from running config
        "program_version": c.send_command("show version | include Version"), # fetches only line with program version
        "device_model": c.send_command("show version | include Cisco CISCO"), # fetches only the line with device model
        "interfaces": c.send_command("show ip interface brief"), # fetches information about device interfaces
    }

# Loop to display all information from the report dict
for key, value in report.items():
    print(f"{key.replace('_', ' ').title()}:")
    print(value)
    print()

# Save report dict as JSON file
with open("rapport.json", "w", enconding="utf-8") as file:
    json.dump(report, file, indent=4, ensure_ascii=False)

print("Report saved to rapport.json")

    # hostname = c.send_command("show running-config | include hostname") 
    # program_version = c.send_command("show version | include Version") 
    # device_model = c.send_command("show version | include Cisco CISCO") 
    # interfaces = c.send_command("show ip interface brief") 

# print(f"Hostname: {hostname}")
# print(f"Program Version: {program_version}")
# print(f"Device Model: {device_model}")
# print(f"Interfaces: {interfaces}")

# hostname_json = json.dumps(hostname)
# program_version_json = json.dumps(program_version)
# device_model_json = json.dumps(device_model)
# interfaces_json = json.dumps(interfaces)

#with open("rapport.json", "w") as f:
#    f.write(hostname_json)
#    f.write(program_version_json)
#    f.write(device_model_json)
#    f.write(interfaces_json)