device_1 = "SW-Nordvik-1"
model_1 = "WS-C3560G-48TS"
role_1 = "Switch, access"

device_2 = "R-Nordvik-1"
model_2 = "CISCO2951"
role_2 = "Router, lager 3"

device_3 = "SW-Nordvik-2"
model_3 = "WS-C85562G-48TS"
role_3 = "Switch, access"

print("UTRUSTNINGSLISTA")
print("-" * 52)

print(f"{device_1}     {model_1}    {role_1}")
print(f"{device_2}      {model_2}         {role_2}")
print(f"{device_3}     {model_3}   {role_3}")

print("-" * 52)
print("Antal enheter: 3")