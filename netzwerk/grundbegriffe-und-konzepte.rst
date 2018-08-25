.. _Grundbegriffe und Konzepte:

Grundbegriffe und Konzepte
==========================

Im folgenden Abschnitt sollen wichtige Netzwerk-Begriffe kurz allgemein
(unabhängig vom Betriebsystem) erklärt werden; auf Linux-spezifische Anwendungen
wird dann im übernächsten Abschnitt eingegangen.


.. _Zugriff auf das Internet:

Zugriff auf das Internet
------------------------

Um mit einem Computer ins Internet zu gelangen, ist ein Modem notwendig; dieses
"übersetzt" lokale Netzwerk-Signale in eine "Sprache", die der jeweilige
Internet-Anbieter ("Internet Service Provider", kurz ISP)  versteht. [#]_

Die einzelnen Geräte, die heutzutage für einen Internet-Zugang von Bedeutung
sind, haben folgende Aufgaben:

* Um in einem Haushalt nicht nur mit einem einzelnen, sondern mit mehreren
  Geräten gleichzeitig Zugang zu haben, wird das Modem im Allgemeinen mit einem
  so genannten "Router" verbunden.

  Mittels Routern ist es möglich, mehrere logisch voneinander getrennte
  Teil-Netzwerke zu definieren. [#]_ Beispielsweise kann es der Fall sein, dass
  es in einem Mehrfamilien-Haus nur eine Internet-Verbindung gibt, die von
  mehreren Familien genutzt werden soll. Jede Familie kann dann einen eigenen
  Router nutzen, der jeweils ein lokales Netzwerk bereitstellt. Die Router der
  einzelnen Familien sind wiederum mit dem Haupt-Router verbunden und haben über
  diesen Zugang zum Internet, nicht jedoch zu den übrigen Teil-Netzwerken.
  Router können somit -- sofern sie einen eingebauten Switch haben -- einen
  einzigen Internet-Zugang in mehrere logisch voneinander getrennte Teil-Zugänge
  aufteilen.

* Router werden üblicherweise in Kombination mit einer so genannten Firewall
  betrieben, die das lokale Netzwerk gegen Hacker-Angriffe absichern soll.
  Früher waren Firewalls stets eigenständige Geräte; inzwischen sind sie oftmals
  ebenfalls in Router-Geräte integriert und stellen somit zwar nicht aus
  physischer, wohl aber aus logischer Sicht eigenständige Geräte dar. Zudem gibt
  es Software-Firewalls, so dass bei größeren Firmen-Netzwerken die Firewall
  unter Umständen auch heute noch auf einem eigenen Server läuft.

* Um das Internet-Signal schließlich auf mehrere Rechner aufzuteilen, kommt
  stets ein so genannter "Switch" zum Einsatz; auch dieser kann unter Umständen
  bereits in die Box des Routers integriert sein, es gibt jedoch auch
  eigenständige Switch-Geräte (mit bis zu 48 Anschluss-Ports).

  An einen Switch kann gegebenenfalls auch ein Wireless Access Point
  angeschlossen werden, um ein drahtloses Netzwerk bereitzustellen.


Die wichtigsten Netzwerk-Geräte sind also Switches und Router; auf wichtige
Eigenschaften dieser Geräte wird in den Abschnitten :ref:`Switches <Switches>`
und :ref:`Router <Router>` näher eingegangen.


.. _OSI-Modell:

Das OSI-Modell
--------------

Damit Geräte miteinander kommunizieren können, müssen sie nicht nur physisch
miteinander verbunden sein, sondern auch einige Regeln beispielsweise bezüglich
der Daten-Formate und des zeitlichen Ablaufs der Daten-Übertragung einhalten.
Derartige Regeln werden auch "Protokolle" genannt; beispielsweise wird über
Netzwerk-Protokolle (ähnlich einer Straßenverkehrs-Ordnung) festgelegt, wie
Daten-Übertragungen in einem Computer-Netzwerk strukturell ablaufen müssen.

Das OSI-Modell untergliedert den Netzwerk-Verkehr in sieben verschiedene Ebenen
("Layer"):

1. Ebene: "Physical"

   In dieser Ebene geht es darum, ob überhaupt ein physischer Kontakt zwischen
   verschiedenen Geräten besteht, ob diese also über Netzwerkkabel (oder eine
   Wireless-Verbindung) miteinander verbunden sind.

2. Ebene: "Data Link"

   Auf dieser Ebene arbeiten :ref:`Switches <Switches>`: Sie können
   beispielsweise mehrere angeschlossene Geräte in logische Teil-Netzwerke
   untergliedern. Eine Kommunikation ist dann nur innerhalb dieser Teilnetzwerke
   möglich, jedoch nicht zwischen den einzelnen Teilnetzwerken.

3. Ebene: "Network"

   Auf dieser Ebene arbeiten Router: Hier werden unter anderem IP-Adressen,
   Subnetz-Masken, Gateways usw. festgelegt.

   Im Abschnitt :ref:`TCP/IP <TCP/IP>` ist diese Ebene näher beschrieben.

4. Ebene: "Transport"

   Auf dieser Ebene wird festgelegt, wie viel Daten auf einmal transportiert
   werden sollen.

   Im Abschnitt :ref:`TCP/IP <TCP/IP>` ist auch diese Ebene näher beschrieben.

5. Ebene: "Session"

    Um auf einen Dienst eines (Web-)Servers zugreifen zu können, muss jedes mal
    eine "Session" zu diesem aufgebaut werden. Im Session-Layer werden derartige
    "Sitzungen" zu anderen Rechnern aufgebaut und verwaltet.

6. Ebene: "Presentation"

   Hiermit ist im Wesentlichen das Betriebsystem gemeint. Eine
   funktionierende Kommunikation setzt auf dieser Ebene beispielsweise voraus,
   dass die Geräte-Treiber richtig funktionieren und der Benutzer die
   entsprechenden Rechte besitzt.

7. Ebene: "Application"

   Auf dieser Ebene befinden sich Programme wie Firefox oder Thunderbird. Der
   Benutzer nutzt diese Ebene, um Daten mit anderen Rechnern auszutauschen.


Die Unterteilung der Netzwerk-Kommunikation in diese sieben Ebenen ist
insbesondere dann nützlich, wenn eine solche *nicht* funktioniert, und man bei
der Fehlersuche eingrenzen möchte, um welche Art von Fehler es sich wohl
handelt. Hat beispielsweise das Netzwerk-Kabel einen Wackelkontakt, so muss
nicht auf der Anwendungs-Ebene nach Bugs gesucht werden..

Um sich die Bezeichnungen der einzelnen Ebenen besser merken zu können, kann man
folgenden Merksatz zur Hilfe nehmen:

    +----------+--------------+
    | Please   | Physical     |
    +----------+--------------+
    | Do       | Data Link    |
    +----------+--------------+
    | Not      | Network      |
    +----------+--------------+
    | Tell     | Transport    |
    +----------+--------------+
    | Secret   | Session      |
    +----------+--------------+
    | Passwort | Presentation |
    +----------+--------------+
    | Anyone   | Application  |
    +----------+--------------+




.. _Switch:
.. _Switches:

Switches
--------

Ein Switch ist ein Gerät, das mehreren Rechnern eines lokalen Netzwerks
ermöglicht, miteinander zu kommunizieren. Ein Switch ist somit gewissermaßen das
"Herzstück" eines Netzwerks und sollte in seiner Bedeutung daher nicht
unterschätzt werden.


.. _Hubs und Switches:

.. rubric:: Hubs und Switches

Um die Funktionsweise von Switches besser verstehen zu können, mag es sinnvoll
sein, kurz auf die Vorgänger dieser Geräte einzugehen, nämlich den sogenannten
"Hubs".

Ein Hub ist/war ein Gerät, das ein einzelnes Netzwerk-Signal gleichmäßig auf
mehrere Anschlüsse verteilen kann (ähnlich wie in einer Netzwerk-Dose das
Leitungskabel beispielsweise über eine Wago-Klemme aufgeteilt werden kann).
Dies hat zwar in der Anfangszeit des Internets den Vorteil mit sich gebracht,
auch mit zwei oder drei Geräten einen Internet-Zugang haben zu können und
Computer miteinander kommunizieren zu lassen; diese Technik bringt allerdings
gravierende Nachteile mit sich, weswegen Hubs heutzutage auf keinen Fall mehr
verwendet werden sollten:

* Ein gravierender Nachteil von war/ist es, dass diese es nicht erlauben, eine
  exklusive Kommunikation zwischen nur zwei Rechnern aufzubauen, während noch
  weitere Computer mit dem gleichen Hub verbunden sind -- auch bekommen ja stets
  alle Informationen mit.

* Ein weiterer gravierender Nachteil betrifft die Datenübertragung im Netzwerk.
  Im Ethernet werden Daten allgemein in Form von so genannten "Paketen"
  übertragen. Soll beispielsweise eine Datei an einen anderen Computer geschickt
  werden, so wird dieses in tausende kleine Einzel-Pakete unterteilt; diese
  werden dann einzeln zum Ziel-Computer geschickt und dort wieder
  zusammengesetzt.

  Damit ein Computer Daten über einen Hub senden kann, darf dort nicht
  gleichzeitig ein anderer Daten-Verkehr vorliegen. Ein sendender Computer muss
  also warten, bis gerade kein sonstiger Datenstrom über den Hub fließt, und
  beginnt dann Pakete zu schicken. Dies wird beispielsweise dann zu einem
  Problem, wenn bei vier angeschlossenen Computern je zwei Computer "über Kreuz"
  miteinander kommunizieren wollen. Senden zwei Computer gleichzeitig ein Paket,
  so kommt es zu einer Daten-Kollision. Die sendenden Computer warten dann einen
  zufällig langen Bruchteil einer Millisekunde, und beginnen dann erneut die
  einzelnen Datenpakete zu versenden.

Man kann sich leicht vorstellen, dass bei einer zunehmenden Zahl an
angeschlossenen Geräten bei Hubs sehr schnell die Daten-Kollisionen überwiegen
und der eigentliche Daten-Verkehr zum Erliegen kommt.

Switches arbeiten in vielerlei Hinsicht besser. Am wichtigsten ist wohl, dass
sich diese Geräte "merken", welches Gerät mit welchem Anschluss verbunden ist.
Dieses "Gedächtnis" funktioniert anhand der sogenannten "MAC-Adressen": Jedes
netzwerkfähige Gerät bekommt bei seiner Herstellung einen solche, weltweit
einmalige Kennzeichnung. Sendet also ein Computer Daten an einen Switch, so
merkt sich dieser automatisch die MAC-Adresse der entsprechenden Netzwerk-Karte.
Die Daten werden dann nur einmalig an komplett unbekannte Geräte, ansonsten aber
nur an den Zielrechner weitergeleitet, der wiederum über seine MAC-Adresse
identifiziert ist. Eine gleichzeitige Kommunikation auch vieler angeschlossener
Geräte ist somit problemlos möglich.


.. _Wichtige Eigenschaften von Switches:

.. rubric:: Wichtige Eigenschaften von Switches

Allgemein können sich Switch-Geräte die Identitäten der angeschlossenen Geräte
merken. Darüber hinaus gibt es allerdings weitere Eigenschaften, bezüglich denen
sich Switch-Geräte unterscheiden (und die meist auch einen preislichen
Unterschied zur Folge haben):

* Managed/Unmanaged Switches:

  Die meisten Switch-Geräte für Privathaushalte sind sogenannte "Managed
  Switches" -- sie funktionieren automatisch, jedoch ohne weitere 
  Konfigurations-Möglichkeit seitens des Anwenders. 

  Unmanaged Switches hingegen laufen zwar standardmäßig ebenfalls im
  "managed"-Modus, der Anwender hat allerdings die Möglichkeit, für jeden
  einzelnen Anschluss-Port individuelle Konfigurationen vorzunehmen.

* Geschwindigkeit:

  Alte Switches konnten Datenübertragungen von bis zu :math:`\unit[10]{Mb/s}`
  handhaben, neuere können auch Geschwindigkeiten von :math:`\unit[100]{Mb/s}`
  oder sogar :math:`\unit[>1]{Gb/s}` erreichen. Beachten sollte man allerdings,
  dass mit :math:`\unit{Mb}` Mega-Bit gemeint sind, nicht Mega-Byte: Ein Byte --
  die übliche Basis-Einheit für Datei-Größen auf Festplatten -- besteht aus
  :math:`8` Bits. Eine Geschwindigkeit von einem Giga-Bit je Sekunde
  entspricht somit einem möglichen Daten-Transfer von :math:`125` Mega-Byte je
  Sekunde.

  Neben der Geschwindigkeit der einzelnen Ports ist auch von Bedeutung, wie groß
  der maximale Datenstrom ist, den das Gerät insgesamt (also über alle
  Anschluss-Ports hinweg) bereitstellen kann. Es ist beispielsweise möglich,
  dass auch ein :math:`\unit[1]{Gb/s}`-Switch mit :math:`48` Ports insgesamt nur
  :math:`\unit[32]{Gb/s}` an Datenstrom umsetzen kann.

* "Trunk"-Anschlüsse:

  Switches mit vielen Ports haben oftmals zusätzlich zu den "normalen" Ports
  zwei sogenannte "Trunk"-Ports, die für eine Kommunikation zwischen mehreren
  Switch-Geräten vorgesehen sind. So ist es beispielsweise möglich, dass es in
  einer Firma einen Switch für jede Etage gibt. Möchte ein Computer mit einem
  Computer auf einer anderen Etage kommunizieren, so sendet der sich auf der
  gleichen Etage befindliche Switch das Signal an die übrigen Switches weiter,
  die wiederum prüfen, ob bei ihnen der Ziel-Computer angeschlossen ist.

.. Stichwort Spanning Tree Protocol

* VLAN:

  Auf konfigurierbaren Switch-Geräten (unmanaged) sind so genannte "virtual
  local network areas" (VLANs) möglich: Die Anschlüsse eines solchen Switches
  können somit in mehrere logische Teil-Netzwerke untergliedert werden. Eine
  Kommunikation ist dann nur innerhalb dieser Teil-Netzwerke möglich, nicht
  jedoch zwischen den einzelnen Teil-Netzwerken. Dies kann beispielsweise von
  Bedeutung sein, wenn nicht nur Computer, sondern auch Telefon-Geräte (Voice
  over IP) an dem Switch angeschlossen sind.

* Power over Ethernet:

  Manche Switches bieten ein sogenanntes Power over Ethernet (PoE); damit können
  die Netzwerk-Kabel in gewissem Maß auch zur Spannungsversorgung der
  angeschlossenen Geräte verwendet werden. Möglich sind (ohne Gewähr) bis zu
  :math:`\unit[24]{V}` und :math:`\unit[0,5]{A}` je Port, also maximal
  :math:`\unit[12]{W}` je angeschlossenem Gerät. Damit können beispielsweise
  Telefone, Wireless Access Points oder andere Switches beziehungsweise Router
  mit Spannung versorgt werden, auch wenn an dieser Stelle keine Steckdose
  verfügbar ist.

  Bietet ein Switch Power over Ethernet, so muss darauf geachtet werden, dass
  die auch mögliche Aufnahme-Leistung ausreichend groß ist. Möchte man
  beispielsweise an :math:`10` Ports :math:`\unit[12]{W}` an Leistung über PoE
  für Endgeräte bereitstellen, so muss die Aufnahme-Leistung des Switches
  entsprechend auch mindestens :math:`\unit[120]{W}` betragen.

* Quality of Services:

  Für verschiedene Geräte sind schnelle Datentransfer-Geschwindigkeiten
  unterschiedlich wichtig: Während Downloads von Emails oder System-Updates
  durchaus auch langsam sein dürfen, so sollte der Datentransfer für
  Live-Stream-Videos stets um einiges höher sein. Am wichtigsten sind schnelle
  Daten-Übertragungen allerdings für eine Echtzeit-Kommunikation, also
  beispielsweise Voice over IP.

  Mittels konfigurierbaren Switches (unmanaged) können für die verschiedenen
  Arten von Daten-Paketen unterschiedliche Prioritäten festgelegt werden. Damit
  kann beispielsweise garantiert werden, dass die Daten-Übertragung von
  Echtzeit-Kommunikations-Geräten stets Vorrang hat.

Die grundlegenden Eigenschaften von Switches liegen im :ref:`OSI-Modell
<OSI-Modell>` auf Ebene :math:`2` ("Data Link"); bietet ein Switch auch eine
Konfigurations-Möglichkeit für die Quality of Services, so entspricht dies im
OSI-Modell bereits der Ebene :math:`3`.


.. _Router:

Router
------

Router regeln die Kommunikation zwischen verschiedenen Teil-Netzwerken.
Abgesehen von meist extrem teuren Geräten, die *ausschließlich* diese Aufgabe
übernehmen (und somit auch nur zwei Anschluss-Buchsen haben), sind in Routern
meist Switch-Geräte integriert, so dass Router meist eine Aufteilung eines
Netzwerkes in verschiedene logisch getrennte Teil-Netzwerke ermöglichen.

| Die meisten Router lassen sich über ein Web-Frontend konfigurieren, indem man
  in der Adress-Zeile eines Webbrowsers die Adresse des Routers eingibt. 
| Zu den wichtigsten Aufgaben eines Routers zählen folgende:

* DHCP:

  Das "Dynamic Host Configuration Protocol" (DHCP) ermöglicht eine dynamische
  Zuweisung von IP-Adressen an individuelle, neu mit dem Router verbundene
  Geräte. Die Adressen für die neu angeschlossenen Geräte werden vom Router
  automatisch anhand eines "Address-Pools" vergeben, der vom Benutzer festgelegt
  wird. Hat beispielsweise der Router die lokale Netzwerk-Adresse
  ``192.168.1.1``, so könnten die Adressen von ``192.168.1.100`` bis
  ``192.168.1.200`` für DCHP freigegeben werden.

  Stationäre, für das Netzwerk wichtige Geräte wie Email-Server, Webserver, usw.
  hingegen sollten stets statische IP-Adressen haben, die allerdings auch
  manuell festgelegt werden müssen.

* DNS:

  Über das "Domain Name System" (DNS) kann man Computer-Namen für bestimmte
  IP-Adressen zuweisen, beispielsweise ``PC1`` für ``192.168.2.15``. Dies ist
  für Webadressen von großer Bedeutung, für lokale Netzwerke spielt diese
  Router-Fähigkeit hingegen meist nur eine untergeordnete Rolle.

* Port Forwarding



* Firewall


.. _TCP-IP:
.. _TCP/IP:
.. _Subnetz-Maske:
.. _Subnetz-Masken:
.. _TCP/IP und Subnetz-Masken:

.. rubric:: TCP/IP und Subnetz-Masken

In diesem Abschnitt soll kurz auf das Protokoll-Paket TCP/IP Version 4, kurz
TCP/IPv4 eingeangen werden. Unter dieser Bezeichnung werden das jeweilige IP-
und TCP-Protokoll zusammengefasst.

* Das IP-Protokoll regelt, wie die Syntax von Netzwerkadressen aufgebaut ist.
  Eine IPv4-Adresse besteht allgemein aus 


.. _Netzwerkkabel:
.. _Netzwerk-Kabel:
.. _Netzwerk-Verkabelungen:
.. _Exkurs Netzwerk-Verkabelungen:

Exkurs: Netzwerk-Verkabelungen
------------------------------

Ein Netzwerk-Kabel besteht allgemein aus acht einzelnen Datenleitungen, wobei
diese innerhalb des Kabels stets in vier Kabel-Paare untergliedert sind, die
jeweils ineinander verdrillt sind ("Twisted Pair"). Dies bewirkt eine bessere
Abschirmung der übertragenen Signale gegenüber äußeren elektromagnetischen
Störfeldern. Zusätzlich werden die vier Kabelpaare meist durch eine
Kunststoff-Folie sowie ein dünnes Metall-Gitter abgeschirmt.

Die Abschirmung und somit auch die Qualität der Daten-Übertragung ist bei
verschiedenen Netzwerk-Kabeln unterschiedlich gut; die maximale Länge eines
Netzwerk-Kabels beträgt :math:`\unit[100]{m}`.

* Die günstigste Variante, die auch heute noch oftmals verwendet wird, heißt
  CAT5 beziehungsweise CAT5e; falls solche Kabel verbaut werden sollen, so
  sollte zumindest CAT5e genutzt werden, um zumindest prinzipiell eine
  Daten-Übertragung im Gigabit-Bereich zu ermöglichen.

* Besser (und aus meiner Sicht empfehlenswert) sind CAT6-Kabel. In diesen
  befindet sich eine zusätzliche Abschirmung zwischen den einzelnen
  Kabel-Paaren, und diese haben einen größeren Leitungs-Querschnitt; es treten
  dadurch weniger Störsignale auf (auch zwischen den einzelnen Datenleitungen).

* Nochmals besser, aber auch wesentlich teurer, sind CAT7-Kabel. Diese haben
  einen nochmals größeren Querschnitt der einzelnen Kupfer-Leitungen, und eine
  nochmals bessere Abschirmung. Mit diesen Kabeln sind prinzipiell die zur Zeit
  höchsten Datenübertragungs-Raten möglich.


Die Geschwindigkeit, die bei der Datenübertragung in einem Netzwerk tatsächlich
erreicht werden kann, wird durch das langsamste Gerät begrenzt. Es bringt
beispielsweise nichts, CAT7-Kabel in Kombination mit einem "langsamen" Switch
oder Router zu verwenden. Gegenüber den einfachen CAT5-Kabeln haben die
hochwertigeren CAT6- und CAT7-Kabel zudem einen etwas höheren Durchmesser, so
dass man beim Anbringen von Steckern beziehungsweise Netzwerk-Dosen ebenfalls
darauf achten sollte, dass diese für den jeweiligen Kabel-Typ geeignet sind
(eine Abwärts-Kompatibilität ist stets gegeben).

... to be continued ...

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] In den Anfangszeiten des Internets konnte man, ähnlich wie immer noch bei
    Fax-Geräten, eine Art von akustischen "Morse-Signalen" bei dieser
    Datenübertragung hören; inzwischen findet die Datenübertragung meist über
    optische Signale statt.

.. [#] Streng genommen regeln Router nur die Kommunikation zwischen
    verschiedenen Teil-Netzwerken; für die Aufteilung des Datenstroms kommen
    hingegen "Switch"-Geräte zum Einsatz. Oftmals werden heutzutage allerdings
    beide Geräte in ein einziges physisches Gerät verbaut, das dann ebenfalls
    schlichtweg "Router" genannt wird.


