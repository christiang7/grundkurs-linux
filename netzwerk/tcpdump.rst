Netzwerk-Monitoring mit ``tcpdump``
===================================

Bei `tcpdump <https://wiki.ubuntuusers.de/tcpdump/>`__ handelt es sich um einen
so genannten "Paket-Sniffer", also ein Programm, das einzelne, über die lokalen
Schnittstellen ein- und ausgehende Pakete "beobachten" kann. Man kann damit
sowohl live den Bit-Strom verfolgen, der über die einzelnen Netzwerkkarten
hinweg fließt, als auch die Bits und Bytes der einzelnen Pakete als ASCII-Text
darstellen und in diesem Buchstaben-Fluss gezielt nach bestimmten Mustern
suchen.

Unter Debian/Ubuntu/LinuxMint kann ``tcpdump`` folgendermaßen installiert
werden:

.. code-block:: sh

    sudo aptitude install tcpdump

Anschließend kann das Programm mittels der gleichnamigen Anweisung gestartet
werden; es setzt allerdings SuperUser-Rechte voraus.



https://wiki.ubuntuusers.de/tcpdump/

