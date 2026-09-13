def vlan_config(number, name):
    rader = []
    rader.append(f"vlan {number}")
    rader.append(f"  name  {name}")
    return rader

vlans = {
    number: f"NAT{number:02d}"
    for number in range(1, 41)
}

for number in vlans:
    for rad in vlan_config(number, vlans[number]):
        print(rad)