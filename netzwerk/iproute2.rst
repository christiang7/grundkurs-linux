
.. _iproute2:
.. _Netzwerk-Verwaltung mit iproute2:

Netzwerk-Verwaltung mit ``iproute2``
====================================

Das Programm-Paket ``iproute2`` zählt zum Standard-Umfang jedes modernen
Linux-Systems; es umfasst die im folgenden näher beschriebenen Programme ``ip``,
``ss`` und ``tc``. [#]_

.. index:: ip
.. _ip:
.. _Das Analyse- und Konfigurations-Programm ip:

.. rubric:: Das Analyse- und Konfigurations-Programm ``ip``:

Eines der wichtigsten Programme zur Verwaltung von Netzwerk-Geräten ist ``ip``:

.. index:: ip; address
.. _ip address:

* Um die Adressen aller Netzwerk-Geräte des eigenen Rechners  (sowohl physische
  als auch logische) anzuzeigen, kann man folgendes eingeben:

  .. code-block:: sh

      ip address show

      # Ausgabe (Beispiel):

      1: lo: <LOOPBACK,UP,LOWER_UP> mtu 4096 qdisc noqueue state UNKNOWN group default
          link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
          inet 127.0.0.1/8 scope host lo
             valid_lft forever preferred_lft forever
          inet6 ::1/128 scope host
             valid_lft forever preferred_lft forever
      2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP group default qlen 1000
          link/ether 00:1e:06:33:31:a3 brd ff:ff:ff:ff:ff:ff
          inet 192.168.2.103/24 brd 192.168.2.255 scope global dynamic eth0
             valid_lft 1732475sec preferred_lft 1732475sec
          inet6 fe80::21e:6ff:fe33:31a3/64 scope link
             valid_lft forever preferred_lft forever

  Durch den Eintrag ``lo`` wird das sogenante "Loopback"-Device bezeichnet. Ein
  Loopback hat die Eigenschaft, dass Pakete, die über dieses (logisch) Gerät
  verschickt werden, beim gleichen (logischen) Gerät wieder ankommen. Dieses
  logische Device hat als Standard-Adresse die lokale Netzwerk-Adresse
  ``127.0.0.1``, die üblicherweise mit dem Namen ``localhost`` verknüpft ist.
  Die Adresse ``eth0`` bezeichnet üblicherweise die erste (physische)
  Netzwerkkarte des Rechners.

  Anstelle von ``ip address show`` kann kürzer auch ``ip addr sh``, oder noch
  kürzer ``ip a s`` eingegeben werden: Da die Anweisungen hierdurch bereits
  eindeutig sind, werden sie von ``ip`` automatisch vervollständigt. Man kann
  sogar nur ``ip a`` angeben, da dann ``show`` als Standard-Anweisung genutzt
  wird.

.. index:: ip; link
.. _ip link:

* Informationen über die Schnittstellen der einzelnen Geräte (physische oder
  logische) liefert die Anweisung ``ip link show`` (beziehungsweise kürzer ``ip
  l``:

  .. Schnittstelle: Verbindung zwischen Geräten.

  .. code-block:: sh

      ip link show

      # Ausgabe (Beispiel):

      1: lo: <LOOPBACK,UP,LOWER_UP> mtu 4096 qdisc noqueue state UNKNOWN mode DEFAULT group default
          link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00
      2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc pfifo_fast state UP mode DEFAULT group default qlen 1000
          link/ether 00:1e:06:33:31:a3 brd ff:ff:ff:ff:ff:ff

  Mittels ``ip link`` lassen sich die Schnittstellen der einzelnen Geräte nicht
  nur auflisten, es können vielmehr auch mittels ``ip link set`` ihre
  Eigenschaften geändert werden; insbesondere können einzelne Geräte damit
  aktiviert beziehungsweise deaktiviert werden:

  .. code-block:: sh

      # Deaktivieren beziehungsweise Aktivieren einer Netzwerk-Karte:
      ip link set eth0 down
      ip link set eth0 up

  Dies ist insbesondere deshalb von Bedeutung, als dass die Eigenschaften eines
  physischen oder logischen Geräts nur geändert werden können, während das Gerät
  inaktiv ist. Um beispielsweise zu Test-Zwecken den Namen eines Geräts zu
  ändern oder manuell eine bestimmte MAC-Adresse für dieses Gerät festzulegen,
  kann man folgendes eingeben:

      # Änderung des Interface-Namens:
      ip link set eth0 name extern

      # Setzen einer neuen MAC-Adresse:
      ip link set eth0 address 00:80:41:ae:fd:7e

Hilfreich beim Erkunden der vielen Möglichkeiten, die ``ip`` bietet, ist die
``Tab``-Vervollständigung der :ref:`Z-Shell <Z-Shell>`, die an jeder Stelle der
Eingabe-Zeile genutzt werden kann. Gibt man beispielsweise ``ip address`` ein
und drückt die Tab-Taste, so bekommt man alle Möglichkeiten aufgelistet, die
ergäzend eingegeben werden können:

.. code-block:: sh

    ip address <TAB>
    add  -- add new protocol address
    change  -- change existing protocol address
    delete  -- delete protocol address
    flush  -- flush protocol address
    help  -- show help for command
    replace  -- add or update protocol address
    show  -- show protocol address

Gibt man beispielsweise ``ip address help`` ein, so bekommt man eine
detaillierte Hilfe zu den weiteren möglichen Argumenten angezeigt.

.. index:: ip; route
.. _ip route:

Wichtig ist ebenfalls das Unterprogramm ``ip route`` (beziehungsweise kürzer
``ip r``): Dieses zeigt in der ersten Zeile den Standard-Gateway an, also die
Netzwerk-Adresse des nächsten Routers, über den mit anderen Netzwerken
(gegebenenfalls auch dem Internet) kommuniziert werden kann; mittels ``ip route
add`` können zudem neue Routen definiert, oder mit ``ip route change``
bestehende Routen geändert werden.

.. todo: ändern!

.. nur ``route`` gibt ebenfalls Routen aus!

... to be continued ...

* https://wiki.ubuntuusers.de/ip/
* http://www.policyrouting.org/iproute2.doc.html


* https://lintut.com/how-to-use-linux-ip-command/?PageSpeed=noscript
* https://dougvitale.wordpress.com/2011/12/21/deprecated-linux-networking-commands-and-their-replacements/
* http://lartc.org/howto/lartc.iproute2.tour.html


.. address
..     manipuliert die IP-Adressen der Interfaces (Netzwerkschnittstellen) und
..     andere Parameter, wie Broadcast-Adressen, Multicast...
.. link
..     manipuliert die Netzwerkschnittstellen auf Ethernet-Ebene. Erlaubt
..     Einstellungen wie Promiscuous Mode ein/aus, ARP ein/aus, oder die MAC-Adresse zu
..     verändern.
.. maddr
..     ändert, entfernt, zeigt oder setzt Multicast-Adressen auf Ethernet- und
..     IP-Ebene.
.. monitor
..     zeigt Änderungen der Netzwerkinterfaces an (zum Beispiel
..     NDP-Router-Advertisements oder ARP-Nachrichten, die über Adressen und Routen
..     informieren)
.. mroute
..     Informationen über Multicast-Routing-Tabellen
.. neighbour
..     manipuliert und zeigt ARP- und NDP-Tabellen.

.. netns
    .. verwaltet Netzwerknamensräume
.. ntable
    .. informiert über NDP- und ARP-Tabellen
.. route
    .. manipuliert, zeigt und setzt IP-Routen (Ersatz für route)
.. rule
    .. manipuliert Regeln in der Routing Policy Database RPDB, die festlegt, für welche Subnetze welche Routing-Tabellen genutzt werden
.. tunnel
    .. erzeugt, verändert und löscht IP-Tunnel (z.B. Tunnelbroker-p41-Tunnel)
.. tuntap
    .. manipuliert TUN/TAP-Schnittstellen


.. rubric:: Der Socket-Monitor ``ss``:

Der Programmname ``ss`` ist der Nachfolger von `netstat
<https://wiki.ubuntuusers.de/netstat/>`_ und soll als Abkürzung für "Socket
Statistics" stehen. [#]_ Ein Socket besteht allgemein aus einer IP-Adresse und
einer Port-Nummer.

.. https://www.binarytides.com/linux-ss-command/

.. netstat 	ss 	Sockets anzeigen 

.. Display All Open Network Ports
.. ss -l entspricht netstat -tulpn

.. Display All TCP Sockets
.. # ss -t -a
.. # netstat -nat

.. Display All UDP Sockets
.. # ss -u -a
.. # netstat -nau

.. The tcptrack command displays the status of TCP connections that it sees on a
.. given network interface. tcptrack monitors their state and displays information
.. such as state, source/destination addresses and bandwidth usage in a sorted,
.. updated list very much like the top command.
.. # tcptrack -i eth0

.. The iftop command listens to network traffic on a given network interface such
.. as eth0, and displays a table of current bandwidth usage by pairs of hosts:
.. # iftop -i eth1

.. It can display or analyses packet flowing in and out of the 192.168.1.0/24
.. network:
.. # iftop -F 192.168.1.0/24

.. https://www.cyberciti.biz/tips/linux-investigate-sockets-network-connections.html

.. https://de.wikipedia.org/wiki/Address_Resolution_Protocol

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Die Programme des ``iproute2``-Pakets können die auf alten Systemen
    häufig genutzten Programme ``ifconfig``, ``route``, ``netstat``, ``arp``, und
    ``brctl`` vollkommen ersetzen; die zuletzt genannten sollten somit nicht
    mehr eingesetzt werden.

    - Anstelle des Programms ``ifconfig`` ("Interface Configuration") sollten
      die Programme :ref:`ip address <ip address>` und ``ip link`` verwendet
      werden.

    - Anstelle des Programms ``route`` sollte das Programm :ref:`ip route <ip
      route>` eingesetzt werden.

.. [#] Persönlich finde ich die Abkürzung ``ss`` nicht gelungen -- da würde mir
    ja ``sos`` noch besser gefallen.. ;-)




