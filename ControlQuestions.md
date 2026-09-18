# Kapitel 1
1.1 [typ 1 • Kontrollfråga] Varför går det att komma in på en switch över konsolen även
när nätverket är nere?
1.2 [typ 1 • Kontrollfråga] Vilka tre lägen finns, och hur ser du i prompten vilket du är i?
1.3 [typ 1 • Kontrollfråga] Vilket kommando tar dig från användarläge till privilegierat
läge?
1.4 [typ 1 • Kontrollfråga] Vad är skillnaden mellan running-config och startup-config?
22
Sladden, prompten och lådorna
1.5 [typ 1 • Kontrollfråga] Vad händer med en osparad ändring vid ett strömavbrott?
1.6 [typ 1 • Kontrollfråga] Räkna upp de sju OSI-lagren i ordning.
1.7 [typ 1 • Kontrollfråga] Vilket lager arbetar en switch på? Vilket arbetar en router på?
1.8 [typ 1 • Kontrollfråga] Vad gör en brandvägg som en router inte gör?
1.9 [typ 1 • Kontrollfråga] Nämn två saker show version berättar om en okänd enhet.
1.10 [typ 1 • Kontrollfråga] Vilken hastighet ska den seriella porten ha, och vad ser du om
den är fel?
1.11 [typ 3 • Läs utdatan] Här är ett utdrag ur show interfaces status. En av
portarna har kabel i men kommer ändå inte upp, och orsaken är inte kabeln. Vilken
port, och vilket kommando skulle du köra härnäst?
Port Name Status Vlan
,→ Duplex Speed Type
Gi0/1 connected 1 a-
,→ full a-1000 10/100/1000BaseTX
Gi0/2 notconnect 1
,→ auto auto 10/100/1000BaseTX
Gi0/3 disabled 1
,→ auto auto 10/100/1000BaseTX
1.12 [typ 3 • Läs utdatan] En kurskamrat visar dig det här och säger att switchen “inte
tar emot kommandon”. Vad har hänt, och vad säger du åt hen att göra?
Switch> hostname SW-Bertil
^
% Invalid input detected at '^' marker.
1.13 [typ 6 • Förklara för någon annan] Skriv fem meningar till en kollega som aldrig sett
en switch, där du förklarar skillnaden mellan running-config och startup-config.
Använd inga engelska termer utom de två namnen.

# Kapitel 2
2.1 [typ 1 • Kontrollfråga] Vad står först i en ram: avsändarens eller mottagarens adress?

2.2 [typ 1 • Kontrollfråga] Hur många tecken har en MAC-adress, och vad betyder den
första halvan?

2.3 [typ 1 • Kontrollfråga] Var får switchen sina anteckningar ifrån? Vem fyller i tabellen?

2.4 [typ 1 • Kontrollfråga] Vad gör switchen med en ram vars mottagare den inte känner
igen?

2.5 [typ 1 • Kontrollfråga] Hur länge sitter en anteckning kvar i MAC-tabellen, och varför
försvinner den?

2.6 [typ 1 • Kontrollfråga] Vilken adress används vid broadcast, och vad betyder den?

2.7 [typ 1 • Kontrollfråga] Varför går en ARP-fråga till alla, medan svaret går till en?

2.8 [typ 1 • Kontrollfråga] Din dator vill nå en server i ett annat land. Vilken MAC-adress
frågar den efter?

2.9 [typ 1 • Kontrollfråga] Vad betyder DYNAMIC respektive STATIC i kolumnen Type?

2.10 [typ 1 • Kontrollfråga] Nämn två saker som gör att en port visar notconnect.

2.11 [typ 3 • Läs utdatan] Några veckor senare ringer Anna igen. Här är ett utdrag ur
MAC-tabellen. Hon har adressen a4c3.f011.3ab7 och når ingen alls, trots att
hennes port är uppe. Vad är fel, och vilken kolumn avslöjar det?
Vlan Mac Address Type Ports
---- ----------- -------- -----
1 3cd9.2b77.0142 DYNAMIC Gi0/5
99 a4c3.f011.3ab7 DYNAMIC Gi0/7
1 3cd9.2bd2.1188 DYNAMIC Gi0/12

2.12 [typ 3 • Läs utdatan] Här är ett utdrag ur show interfaces status. Tre portar
har trafik. En av dem kommer att fungera sämre än de andra. Vilken, och vad
skulle du kontrollera härnäst?
Port Name Status Vlan
,→ Duplex Speed Type
Gi0/1 connected 1 a-
,→ full a-1000 10/100/1000BaseTX
Gi0/2 connected 1 a-
,→ half a-100 10/100/1000BaseTX
Gi0/3 connected 1 a-
,→ full a-1000 10/100/1000BaseTX

2.13 [typ 6 • Förklara för någon annan] Skriv fem meningar till en kollega som aldrig hört
talas om en switch, där du förklarar varför switchen skickar en ram till alla portar
första gången. Använd inga engelska termer utom switch.

# Kapitel 3
3.1 [typ 1 • Kontrollfråga] Vad säger en IP-adress som en MAC-adress inte säger?

3.2 [typ 1 • Kontrollfråga] Vad gör nätmasken?

3.3 [typ 1 • Kontrollfråga] Vilken adress i ett nät får ingen enhet ha, och varför är det två
stycken?

3.4 [typ 1 • Kontrollfråga] Vad är blocksteget för /26, och vad använder du det till?

3.5 [typ 1 • Kontrollfråga] Varför måste gatewayen ligga i samma nät som du?

3.6 [typ 1 • Kontrollfråga] Vad händer med en dator som har rätt adress men ingen
gateway?

3.7 [typ 1 • Kontrollfråga] Vilka fyra saker får en dator av DHCP, och vilken av dem säger
hur länge de gäller?

3.8 [typ 1 • Kontrollfråga] Vilka enheter ska ha statisk adress, och varför?

3.9 [typ 1 • Kontrollfråga] Hur skiljer du ett DNS-problem från ett DHCP-problem?

3.10 [typ 1 • Kontrollfråga] Vad betyder det att en dator har en adress som börjar på
169.254?

3.11 [typ 2 • Räkneövning] Räkna ut nätadress, broadcast och adressintervall för
192.168.1.200/26. Visa alla fyra stegen.

3.12 [typ 2 • Räkneövning] Räkna ut samma sak för 10.0.0.6/30. Hur många enheter
får plats?

3.13 [typ 2 • Räkneövning] Nordviks lager i Borås har fått 192.168.2.0/24 och behöver
tre nät: lager, trådlöst gäst och drift. Föreslå en uppdelning i /26 och skriv ut nät,
broadcast och intervall för varje.

3.14 [typ 3 • Läs utdatan] Här är ett utdrag från en dator som inte kommer ut på internet,
men som når filservern på 192.168.1.10. Vad är fel?
Ethernet-kort Ethernet:
IPv4-adress . . . . . . . . . . : 192.168.1.42
Nätmask . . . . . . . . . . . . : 255.255.255.192
Standardgateway . . . . . . . . : 192.168.1.65

3.15 [typ 3 • Läs utdatan] Här är ett utdrag från routern. En student säger att DHCP inte
fungerar, för hens dator får ingen adress. Vad frågar du efter härnäst?
R-Nordvik-1# show ip interface brief
Interface IP-Address OK? Method
,→ Status Protocol
Embedded-Service-Engine0/0 unassigned YES NVRAM
,→ administratively down down
GigabitEthernet0/0 192.168.1.1 YES manual up
,→ up
GigabitEthernet0/1 unassigned YES NVRAM
,→ administratively down down
GigabitEthernet0/2 unassigned YES NVRAM
,→ administratively down down

3.16 [typ 6 • Förklara för någon annan] Skriv fem meningar till en kollega som aldrig hört
talas om nätmask, där du förklarar varför två datorer med samma adressbörjan
ändå kan hamna i olika nät.

# Kapitel 4
4.1 [typ 1 • Kontrollfråga] Vad är skillnaden mellan ett VLAN och ett IP-nät?
Svar: Ett VLAN ligger på lager 2 och handlar om vilka portar som hör ihop. IP-nät ligger på lager 3 och handlar om adresser. De följs nästan alltid åt men är två skilda saker.

4.2 [typ 1 • Kontrollfråga] Vad skiljer en access-port från en trunk?
Svar: En access-punkt tillhör bara ett VLAN, och där sitter en dator. En trunk bär flera VLAN samtidigt, och där sitter andra switchar eller router.

4.3 [typ 1 • Kontrollfråga] Vilka två rader behövs för att lägga en port i ett VLAN, och
varför räcker inte den ena?
Svar: switchport mode access och switchport access vlan <nummer>. Utan den första står porten kvar i sitt automatiska läge och kan välja något annat än du tänkt.

4.4 [typ 1 • Kontrollfråga] Vad gör taggningen, och var i nätet finns taggen?
Svar: Taggningen skriver VLAN-nummret i ramen. Taggen lever bara på trunkar, mellan switchar, och till router. Den sätts där när ramen går in i trunk och tas bort när den går ut på access-port.

4.5 [typ 1 • Kontrollfråga] Varför ska en trunk aldrig kopplas till en dator?
Svar: För att en dator inte förstår taggade ramar. Den kastar dem eller behandlar dem fel, och ingenting fungerar.

4.6 [typ 1 • Kontrollfråga] Vad är native VLAN, och vad är standardvärdet?
Svar: Det VLAN som går ottaggat över trunken. Standardvärdet är VLAN 1 på alla Cisco switchar.

4.7 [typ 1 • Kontrollfråga] Vad går fel om två switchar har olika native VLAN?
Svar: Ottaggad trafik från det ena nätet skulle hamna i det andra. Mellan två Cisco-switchar stänger Ciscos spanning-tree av de två inblandade VLAN:en på porten, och loggen fylls med rader om RECV_PVID_ERR. Mot en switch från en annan tillverkare finns ingen sådan spärr, och då hoppar trafiken mellan näten tyst.

4.8 [typ 1 • Kontrollfråga] Vad förhindrar STP, och hur gör den det?
Svar: STP (Spanning-Tree-Protocol) förhindrar att ramar går runt i cirkel för evigt. Den gör det genom att stänga av de portar som skulle skapa cirkeln, och öppna dem igen om den öppna vägen går sönder.

4.9 [typ 1 • Kontrollfråga] Vad betyder BLK i show spanning-tree, och vad ska du
göra åt det?
Svar: Att STP stängt porten avsiktligt. Du ska inte göra någonting åt det, porten är en reserv, och att dra ur kabeln är ett säkert sätt att ta ner nätet.

4.10 [typ 1 • Kontrollfråga] Vad händer om du kör switchport trunk allowed
vlan två gånger med olika nummer?
Svar: Den andra listan skriver över den första. Du får bara de VLAN du skrev sist. Om du vill lägga till VLAN måste du skriva switchport allowed vlan add <vlansnummer>.

4.11 [typ 1 • Kontrollfråga] Skriv den engelska termen för vart och ett av följande: accessport, trunk, taggning, native VLAN och root bridge. Provet frågar efter dem.
Svar: Access port, trunk, tagging, native VLAN, och root bridge.

4.12 [typ 2 • Räkneövning] Nordviks fyra VLAN delar 192.168.1.0/24 i fyra lika stora
delar. Räkna ut nätadress, gatewayadress, första och sista användbara adress samt
broadcastadress för alla fyra. Använd schemat i bilaga C och skriv svaret som en
tabell.
Svar: 
Vlan    Nät             Gateway         Användbara          Broadcast
10   192.168.1.0/26    192.168.1.1     192.168.1.1-62       192.168.1.63
20   192.168.1.64/26   192.168.1.65    192.168.1.65-126     192.168.1.127
30   192.168.1.128/26  192.168.1.129   192.168.1.129-190    192.168.1.191
99   192.168.1.192/26  192.168.1.193   192.168.1.193-254    192.168.1.225

4.13 [typ 2 • Räkneövning] Ekonomiavdelningen växer till 70 datorer. Räcker /26? Räkna
ut hur många adresser en /26 ger, hur många av dem som går att använda, och
vilken mask som skulle behövas i stället.
Svar: Ett /26 nätverk har 64 adresser, varav 62 är användbara. Det räcker inte för ett nätverk med 70 datorer. Du hade minst behövt ett /25 nätverk med 128 adresser, varav 126 är användbara (inte upptagna av gateway och broadcast)

4.14 [typ 3 • Läs utdatan] Här är ett utdrag från två switchar som är hopkopplade. Datorer
i VLAN 20 når inte varandra över trunken, men VLAN 10 fungerar. Vad är fel?
SW-Nordvik-1# show interfaces trunk
Port Vlans allowed on trunk
Gi0/24 10,30,99
SW-Nordvik-2# show interfaces trunk
Port Vlans allowed on trunk
Gi0/24 10,20,30,99
4.15 [typ 3 • Läs utdatan] Här är ett utdrag från en switch. En dator i port Gi0/5 får ingen
adress från DHCP-servern, som sitter i VLAN 10. Vad frågar du efter härnäst?SW-Nordvik-1# show vlan brief
VLAN Name Status Ports
---- -------------------------------- ---------
,→ -------------------------------
1 default active Gi0/5,
,→ Gi0/6
10 KONTOR active Gi0/7,
,→ Gi0/8
20 EKONOMI active Gi0/9
4.16 [typ 4 • Konfigurationsövning] Skriv den fullständiga konfigurationen för trunken
mellan SW-Nordvik-1 och SW-Nordvik-2. Den ska bära VLAN 10, 20, 30 och 99, ha
native VLAN 999 och inte förhandla om läget. Skriv varje rad, i rätt ordning, från
configure terminal till end.
4.17 [typ 4 • Konfigurationsövning] Port Gi0/11 till Gi0/14 på SW-Nordvik-1 ska läggas i
VLAN 20 och slippa vänta på STP när en dator kopplas in. Skriv konfigurationen
med så få rader som möjligt.
4.18 [typ 5 • Översätt kravet] Nordviks gäster ska kunna nå internet men ingenting annat i
huset. Ekonomiavdelningen ska ha ett eget nät som varken kontoret eller gästerna
når. Driftpersonalen ska kunna nå switcharna från sitt eget nät. Skriv den VLANkonfiguration switchen behöver, och säg vilken del av kravet du inte kan lösa med
VLAN ensamt.
4.19 [typ 6 • Förklara för någon annan] Skriv fem meningar till en kollega som aldrig hört
talas om VLAN, där du förklarar varför två datorer i samma switch ändå inte kan
nå varandra.

# Kapitel 5
5.1 [typ 1 • Kontrollfråga] Vad gör en router som en switch inte gör?
5.2 [typ 1 • Kontrollfråga] Vad betyder bokstaven C respektive S i routingtabellen?
5.3 [typ 1 • Kontrollfråga] Varför får du två rader när du sätter en adress på ett interface?
5.4 [typ 1 • Kontrollfråga] Vad betyder longest prefix match, och vilken rad vinner om två
passar?
5.5 [typ 1 • Kontrollfråga] Varför är 0.0.0.0/0 alltid den sista utvägen?
5.6 [typ 1 • Kontrollfråga] Vad är ett sub-interface, och varför behövs de på en router med
få portar?
5.7 [typ 1 • Kontrollfråga] Vilken rad måste komma före adressen på ett sub-interface, och
varför?
5.8 [typ 1 • Kontrollfråga] En ping ger inget svar. Vilka två saker kan ha gått fel?
5.9 [typ 1 • Kontrollfråga] Vad är en blackhole-rutt, och varför är den svår att hitta?
5.10 [typ 1 • Kontrollfråga] Vad visar traceroute som ping inte visar?
5.11 [typ 1 • Kontrollfråga] Skriv den engelska termen för vart och ett av följande: routingtabell, ansluten rutt, statisk rutt, nästa hopp och sub-interface. Provet frågar efter
dem.
5.12 [typ 2 • Räkneövning] Länken mellan Göteborg och Borås är 10.0.0.0/30. Hur
många adresser innehåller nätet, hur många av dem går att sätta på ett interface,
och vilka är de? Räkna, skriv inte av.
5.13 [typ 2 • Räkneövning] En kollega föreslår 10.0.0.0/24 till länken i stället. Räkna
ut hur många adresser som då står oanvända, och skriv en mening om varför det
ändå kan vara ett rimligt val i ett stort nät.
5.14 [typ 3 • Läs utdatan] Här är en routingtabell. Ett paket ska till 192.168.2.50.
Vilken rad används, och vad händer med paketet?
Gateway of last resort is 203.0.113.1 to network 0.0.0.0
S* 0.0.0.0/0 [1/0] via 203.0.113.1
S 192.168.2.0/24 [1/0] via 10.0.0.2
C 192.168.1.0/26 is directly connected,
,→ GigabitEthernet0/0.10
C 10.0.0.0/30 is directly connected,
,→ GigabitEthernet0/2
5.15 [typ 3 • Läs utdatan] Här är ett utdrag från Nordviks router. Datorer i VLAN 20 når
varandra men inte sin gateway. Vad är fel?
R-Nordvik-1# show running-config interface
,→ GigabitEthernet0/0.20
interface GigabitEthernet0/0.20
encapsulation dot1Q 21
ip address 192.168.1.65 255.255.255.192
5.16 [typ 4 • Konfigurationsövning] Skriv den fullständiga konfigurationen för sub-interfacet
mot VLAN 30 på R-Nordvik-1: rätt namn, rätt VLAN, rätt adress och rätt mask
enligt bilaga G. Skriv raderna i den ordning routern kräver.
5.17 [typ 4 • Konfigurationsövning] Skriv de två rutter som behövs för att Göteborg och
Borås ska nå varandra — en på varje router. Ange på vilken router varje rad ska
skrivas.
5.18 [typ 5 • Översätt kravet] Nordviks ekonomiavdelning ska kunna nå filservern i kontorsnätet. Kontorspersonalen ska inte kunna nå ekonominätet. Driftpersonalen
ska nå bägge. Beskriv vad du kan lösa med routing den här veckan, och vad som
måste vänta till kapitel 9. Skriv den konfiguration du faktiskt kan göra nu.
5.19 [typ 6 • Förklara för någon annan] Skriv fem meningar till en kollega som aldrig hört
talas om routing, där du förklarar varför en ping kan gå fram utan att komma
tillbaka.
