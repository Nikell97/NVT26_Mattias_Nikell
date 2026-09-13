# Vekca 1
Onsdag - Läste fram till kapitel 2.1 it boken och gick igenom kontrollfrågorna.  
Torsdag - Gjorde Python övningen och satte upp GitHub repo.  
Fredag - Gjorde första checkpoint övningen i Packet Tracer. Kunde inte utföra kommandot show startup-config | include hostname.
Detta verkar inte vara p.g.a. fel läge då jag prövade i användarläge, priviligierat läge, och konfigurationsläge. Gjorde istället en reboot för att kolla att ändringar sparats till startup-config.  

# Vecka 2  
Onsdag - Läste fram till kapitel 2.3 samt tog anteckningar  
Torsdag - Läste fram till kapitel 3.1. Gjorde Python övning oui.py.  Uppdaterade filstruktur i GitHub repo för att bättre matcha utseendet visat i boken.

Återblick

Vilka tre lägen finns på en Cisco-switch, och hur ser du i prompten vilket du är i?  
Svar: De tre lägena är användarläge, det du alltid startar i, privilegierat läge, där du har access till mer information och funktioner, och konfigurationsläget, där du kan göra ändringar till switchens konfiguration. Du ser vilket läge du är i baserat på symbolen som följer switchens namn i kommandoraden. Om switchen har namnet SW-Mattias så ser du att du är i användarläge om det står SW-Mattias>, privilegierat läge om det står SW-Mattias#, och konfigurationsläge om det står SW-Mattias(config)#.  

Vad händer med din konfiguration om du stänger av switchen utan att spara, och vilket kommando sparar du med?  
Svar: Om du inte sparat dina ändringar i konfigurationen till startup-config så kommer de att vara borta om du startar om switchen. För att spara dina konfigurationer använder du kommandot copy running-config startup-config, eller write memory, eller wr. Alla dessa tre gör samma sak men är förkortningar för att göra det snabbare att skriva.

Räkna upp de sju OSI-lagren i ordning. Vilket lager arbetar en switch på?  
Svar: 1 Fysiskt, 2 Datalänk, 3 Nätverk, 4 Transport, 5 Session, 6 Presentation, 7 Applikation. Switchen arbetar på lager 2.

# Vecka 3
Måndag - Läste fram till kapitel 3.4 om subnätmasker och tog anteckningar  
Tisdag - Läste resterande kapitel 3 och testade att sätta statisk ip på en router i packet tracer.  
Torsdag (under lektion) - Fick två datorer att kunna pinga till varandra mellan två nätverk via router. Först med statisk ip och sedan med konfigureread dhcp för båda nätverken.  

Observation under labb steg 6 och 7:  
6 - Efter att nätmasken var satt till 255.255.255.0 så gick det fortfarande att nå default gateway. Jag antar att detta är för att med ip 192.168.1.66/24 så anser datorn att den och default gateway 192.168.1.65 ligger i samma nätverk.
7 - Efter att default gateway var borttagen så går det fortfarande att nå lokala adresser men den når inte ut på internet. 

Återblick

Vad är skillnaden mellan running-config och startup-config?  
Svar: running-config är de inställningar och ändringar du gjort sedan senaste sparningen eller start av maskinen medan startup-config är de sparade inställningarna som informerar konfigurationen som gäller vi uppstart av maskinen.

Vilket lager arbetar en switch på, och vilket arbetar en router på?  
Svar: Vanligen arbetar en switch på lager 2, datalänk, medan en router arbetar på lager 3, nätverk.

Din dator vill nå en server i ett annat land. Vilken MAC-adress frågar den efter, och varför?  
Svar: Den frågar efter MAC-adressen till default gateway eftersom all trafik som går utanför det lokala nätet går genom den.

# Vecka 4
Måndag - Gjorde moduler 1-5 i koans och skrivit klart python scriptet för subnät.   
Tisdag - Gjorde moduler 6-7 i koans och läste fram till kapitel 4.5.1 i boken.  
Ondsdag - Har testat konfiguration av VLAN i Cisco switch i Packet Tracer.  
