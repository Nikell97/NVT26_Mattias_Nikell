import ipaddress

text = "192.168.1.64/26"

net = ipaddress.ip_network(text, strict=False)

usable = list(net.hosts())

print(f"Nat:                 {net.network_address}")
print(f"Natmask:             {net.netmask}")
print(f"Broadcast:           {net.broadcast_address}")
print(f"Forsta adress:       {usable[0]}")
print(f"Sista adress:        {usable[-1]}")
print(f"Amtal enheter:       {len(usable)}")