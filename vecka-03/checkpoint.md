R-Nordvik-1>enable
R-Nordvik-1#show ip dhcp binding
IP address       Client-ID/              Lease expiration        Type
                 Hardware address
192.168.1.21     00D0.588E.1725           --                     Automatic
192.168.1.20     00D0.BAC9.BD40           --                     Automatic
192.168.1.22     000B.BE9E.EC92           --                     Automatic
192.168.1.23     000C.CF5E.89E5           --                     Automatic
192.168.1.25     00E0.F7B0.6BD4           --                     Automatic
192.168.1.24     0060.2F6C.807D           --                     Automatic
192.168.1.26     0001.64C5.EDBB           --                     Automatic
192.168.1.133    0001.64C5.EDBB           --                     Automatic
192.168.1.131    0060.2F6C.807D           --                     Automatic


Adresserna som slutar på 131 och 133 är p.g.a. att jag konfigurerade gästnätverket med separat switch istället för kontor och ekonomi som står på samma.  
Detta är för att undvika massa omkonfiguration av switchar för kommande uppgift att sätta up VLAN.