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