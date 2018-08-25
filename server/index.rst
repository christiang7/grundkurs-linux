
.. _Linux-Server:

Linux-Server
============

Im Sprachgebrauch bezeichnet man als "Server" häufig die Server-Racks, also die
(meist recht groß dimensionierte) Hardware. Im eigentlichen Sinn allerdings ist
ein "Server" vielmehr eine Software, die einen Dienst ("Service") für andere
bereitstellt -- oftmals über das lokale Netzwerk, oder auch über das Internet.
Einen Rechner, der eine oder mehrere derartige Dienste zur Verfügung stellt,
bezeichnet man als "Host", einen darauf zugreifenden Rechner beziehungsweise
ein entsprechendes Programme als "Client".

In Computer-Netzwerken werden die einzelnen Dienste auf unterschiedliche Rechner
aufgeteilt, die dann kurzerhand oft ebenfalls "Server" genannt werden. Die
Clients, die auf die einzelnen Dienste zugreifen, sind separate Programme, die
oftmals (aber nicht zwangsweise) auf anderen Rechnern aufgerufen werden.
Beispielsweise ist das Email-Programm :ref:`Thunderbird <Thunderbird>` eine
Client-Software, die Emails von einem externen Mailserver empfangen kann.

Einige wichtige Dienste werden in den folgenden Abschnitten kurz vorgestellt.

.. only:: latex

    .. rubric:: Links

    * `Client-Server-Modell (Wikipedia) <https://de.wikipedia.org/wiki/Client-Server-Modell>`__
    * `Server-Dienste (Ubuntuusers-Wiki)
      <https://wiki.ubuntuusers.de/Serverdienste/>`__




.. toctree::
    :maxdepth: 2

    systemd.rst
    ntp.rst
    cron.rst
    apache.rst
    postfix-und-dovecot.rst
    openssl.rst
    ldap.rst

.. only:: html

    .. rubric:: Links

    * `Client-Server-Modell (Wikipedia) <https://de.wikipedia.org/wiki/Client-Server-Modell>`__
    * `Server-Dienste (Ubuntuusers-Wiki)
      <https://wiki.ubuntuusers.de/Serverdienste/>`__


.. {{{

.. dns-server: https://wiki.ubuntuusers.de/Dnsmasq/
.. http://linuxwiki.org/dnsmasq

... to be continued ...

.. virtuelle-betriebsysteme.rst


.. Application-Server

.. Beispiel: Zope

.. Datenbankserver

..  Eine Datenbank speichert Daten, so dass sie nach dem Neustart des Rechners
.. wieder verfügbar sind. Das Dateisystem kann somit als eine einfache
.. hierarchische Datenbank angesehen werden. 

.. In Python, sowie vielen anderen Programmiersprachen, gibt es ein Modul um
.. Objekte zu serialisieren. Die Objekte werden zu einer Byte-Folge gewandelt, die
.. dann z.B. in eine Datei geschrieben werden. Kleine Anwendungen lassen sich so
.. leicht ohne Datenbank programmieren: Beim Start der Anwendung werden die
.. serialisierten Daten eingelesen (unpickle) und beim Beenden werden die Daten
.. wieder serialisiert (pickle).

.. Speichert man seine Daten in einer relationalen Datenbank, braucht man ein
.. objekt-relationales Mapping (OR-Mapping) um die Daten in die Objekte zu
.. bekommen. Es gibt kommerzielle und freie Bibliotheken, die einem bei einem
.. OR-Mapping behilflich sein sollen, doch früher oder später werden die Daten
.. mittels langen Select-Anweisungen ("SELECT A, B, C, FROM MYTABLE WHERE ID=....")
.. aus der Datenbank gelesen. Besonders unschön wird es, wenn man viele
.. verschachtelte Datenstrukturen hat.

.. Transaktionen werden nach dem ACID Prinzip definiert:

.. - A: Atomar. Transaktionen werden ganz oder garnicht durchgeführt.
.. - C: Consistency. Die Konsistenz der Daten muss nach der Transaktion gewährleistet sein.
.. - I: Isolation. Führt ein Thread eine Transaktion durch, darf ein zweiter Thread die geänderten Daten erst sehen, wenn die Transaktion abgeschlossen ist.
.. - D: Durability. Stürzt der Rechner während dem Betrieb ab, dürfen keine Daten verloren gehen. 


.. Dieser Mechanismus geht solange gut, bis die Daten größer als der verfügbare Haupspeicher werden. 

.. }}}

