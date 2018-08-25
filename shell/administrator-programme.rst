.. index:: Superuser, Root,
.. _Administrator-Programme:

Administrator-Programme
=======================

Als SuperUser (manchmal auch "Root" genannt) kann man neben den
:ref:`Standard-Programmen <Standard-Programme>` auch zusätzliche Werkzeuge
nutzen, die systemweite Veränderungen bewirken können. Im Folgenden ist eine
kleine Auswahl dieser Programme aufgelistet.

.. _Datei-Verwaltung (SuperUser):

Datei-Verwaltung
----------------
.. {{{

.. index:: chown, chgrp
.. _chown und chgrp:

``chown``, ``chgrp``
^^^^^^^^^^^^^^^^^^^^
.. {{{

Mit ``chown benutzername dateien`` kann der Eigentümer einer oder mehrerer
Dateien festgelegt werden; entsprechend können mit ``chgrp gruppenname
datei(en)`` eine oder mehrere Datei(en) einer anderen Benutzer-Gruppe zugewiesen
werden. [#]_ Mit der Option ``-R`` lassen sich beide Werkzeuge auch rekursiv auf
Verzeichnisse mitsamt Unterverzeichnissen anwenden. Um den Benutzer- und
Gruppennamen auf einmal zu ändern, kann ``chown`` mit der Syntax ``chown
benutzername:gruppenname datei(en)`` verwendet werden.

Eine Datei hat als Eigentümer stets den Namen des Benutzer-Accounts, von dem aus
die Datei erstellt wurde; der Eigentümer kann anschließend nur mit
SuperUser-Rechten geändert werden. Der Gruppenname einer Datei kann hingegen
mittels ``chgrp`` auch vom Eigentümer der Datei geändert werden, sofern dieser
auch Mitglied in der neuen Benutzer-Gruppe ist.

Datei-Rechte für die einzelnen Benutzer können mittels :ref:`chmod <chmod>`
geändert werden.

.. setgid-bit..

..  Beispiel: ``chgrp audio soundfile.mp3`` -> Datei wird der Gruppe "audio"
..  zugewiesen.

.. }}}

.. }}}

.. _Benutzer-Verwaltung:

Benutzer-Verwaltung
-------------------
.. {{{

.. index:: adduser, addgroup
.. _adduser:
.. _addgroup:
.. _adduser, addgroup:
.. _adduser und addgroup:

``adduser``, ``addgroup``
^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

Mit ``adduser benutzername`` wird ein neues Benutzer-Konto erstellt und der
entsprechende Ordner im ``/home``-Verzeichnis angelegt. Hierbei wird der Inhalt
des Verzeichnisses ``/etc/skel`` als Vorlage in das Verzeichnis des neuen
Benutzers kopiert. Alle diese Dateien bekommen dann den Benutzernamen als
Eigentümer- und Gruppennamen zugewiesen.

Mit ``addgroup gruppenname`` kann eine neue Benutzer-Gruppe erstellt werden.
Eine neu erstellte Gruppe hat zunächst keine Mitglieder; diese können
anschließend mittels :ref:`usermod <usermod>` hinzugefügt werden.

.. index:: deluser, delgroup
.. _deluser:
.. _delgroup:
.. _deluser, delgroup:
.. _deluser und delgroup:

.. }}}

``deluser``, ``delgroup``
^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

Mit ``deluser benutzername`` kann entsprechend ein bestehendes Benutzer-Konto
gelöscht werden. Standardmäßig bleibt dabei das Home-Verzeichnis des Benutzers
erhalten; möchte man dieses gleich mit entfernen, kann ``deluser`` mit der
Option ``--remove-home benutzername`` aufgerufen werden.

Mit ``delgroup`` kann eine Benutzer-Gruppe wieder entfernt werden. Mit der
Option ``--only-if-empty`` kann man sicherstellen, dass die Gruppe nur dann
gelöscht wird, wenn kein Benutzer Mitglied der Gruppe ist. "Primäre" Gruppen,
also Gruppen, deren Namen zugleich Benutzernamen sind, können nicht gelöscht
werden (zumindest nicht, solange die zugehörigen Benutzer existieren).

.. index:: su
.. _su:
.. _sudo:
.. _su, sudo:
.. _su und sudo:

.. }}}

``su``, ``sudo``
^^^^^^^^^^^^^^^^
.. {{{

Mit ``su`` kann man sich in einer Shell als SuperUser (``root``) anmelden;
hierbei muss das Passwort des ``root``-Benutzers korrekt angegeben werden.
Hierbei gibt es folgenden Unterschied zwischen Debian und Ubuntu/LinuxMint:

* Bei Debian ist eine Anmeldung als Root via ``su`` zunächst der einzige Weg, um
  als gewöhnlicher Benutzer SuperUser-Rechte zu bekommen. Das Passwort für den
  ``root``-Benutzer wird erstmalig bei der Installation festgelegt.

* Bei Ubuntu/LinuxMint existiert die ``su``-Anweisung zwar, es gibt aber kein
  gültiges Passwort für ``root``. Anstelle dessen kann sich ein befugter Nutzer
  mittels ``sudo`` temporär SuperUser-Rechte verschaffen.

  Derjenige Benutzer-Account, der bei einer Neu-Installation eines
  Ubuntu/LinuxMint-Systems als zunächst einziger Account angelegt wird, kann
  sich automatisch mittels des gewöhnlichen Account-Passworts mittels ``sudo``
  SuperUser-Rechte verschaffen. Mit ``sudo -i`` kann sich dieser Benutzer in
  einer Shell auch dauerhaft Superuser-Rechte verschaffen.

Bei Ubuntu-Systemen ist das Programm ``sudo`` standardmäßig installiert. Bei
Debian muss man sich einmalig mittels ``su`` als SuperUser-Rechte verschaffen,
und kann anschließend ``sudo`` über das gleichnamige Paket nachinstallieren:

.. code-block:: sh

    apt-get install sudo

Damit ein "normaler" Benutzer mittels ``sudo`` SuperUser-Rechte erhalten kann,
muss ein entsprechender Eintrag folgender Form in der Datei ``/etc/sudoers``
existieren:

.. code-block:: bash

    # User privilege specification
    benutzername	ALL=(ALL:ALL) ALL

Es ist empfehlenswert, die Datei ``/etc/sudoers`` ausschließlich mittels der
Anweisung ``visudo`` zu bearbeiten. Dieses Programm ist Teil des ``sudo``-Pakets
und somit bei Ubuntu/LinuxMint standardmäßig installiert; bei Debian ist es nach
der Installation von ``sudo`` ebenfalls vorhanden.

Durch den Aufruf von ``visudo`` mit SuperUser-Rechten wird die Datei
``/etc/sudoers`` mit dem Standard-Editor geöffnet. Der Vorteil von ``visudo``
liegt darin, dass das Programm vor dem Speichern der Datei erst noch
ein Syntax-Check durchführt. Damit soll vermieden werden, dass es auf einem
System durch eine unbeabsichtigte Eingabe plötzlich keinen Administrator-Zugang
mehr gibt.

Mittels SuperUser-Rechten kann man sich auch auf jedem "normalen"
Benutzer-Account einloggen: Hierzu gibt man ``sudo su benutzername`` an. Jeder
Benutzerwechsel kann mit ``exit`` wieder beendet werden.


.. index:: usermod
.. _usermod:

.. }}}

.. umask

``usermod``
^^^^^^^^^^^
.. {{{

Mit ``usermod`` kann das Konto eines Benutzers verändert werden. Beispielsweise
kann folgendermaßen ein Benutzer zur angegebenen Gruppe hinzugefügt werden:

.. code-block:: sh

    usermod -aG gruppenname benutzername

Dies ist beispielsweise nützlich, um Benutzer zu einer mittels :ref:`addgroup
<addgroup>` neu erstellten Gruppe hinzuzufügen. Ebenso kann ein Benutzer für
Entwicklungszwecke zu einer Gruppe hinzugefügt werden, die durch das
Betriebsystem vorgesehen sind: Beispielsweise kann ein Benutzer für  eigene,
lokale Web-Entwicklungen mit einem :ref:`Apache <Apache>`-Webserver mittels
``usermod -aG www-data benutzername`` die gleichen (Gruppen-)Rechte erhalten wie
der Apache-Server selbst.

Die Änderungen werden erst ab eines erneuten Logins des Benutzers wirksam.

.. _w:

.. }}}

``w``
^^^^^
.. {{{

Mit ``w`` wird angezeigt, welche Benutzer aktuell auf dem Rechner angemeldet
sind und welche Programme beziehungsweise Prozesse (zum Beispiel
Shell-Sitzungen) von den einzelnen Benutzern aktuell genutzt werden. Gibt man
``w benutzername`` ein, so bekommt man lediglich Informationen über die vom
angegebenen Benutzer genutzten Prozesse angezeigt.

.. }}}

.. }}}

.. _Netzwerk- und Internet-Programme:

Netzwerk- und Internet-Programme
--------------------------------
.. {{{

.. index:: iftop
.. _iftop:

``iftop``
^^^^^^^^^
.. {{{

Mit ``iftop`` kann der Datenaustausch angezeigt werden, der zwischen dem eigenen
und anderen Rechnern stattfindet. Das Programm kann folgendermaßen installiert
werden:

.. code-block:: bash

    sudo aptitude install iftop

Anschließend kann es in einer Shell mittels ``iftop`` gestartet werden. Die
Anzeige ist interaktiv (ebenso wie bei :ref:`top <top>`) und kann durch Drücken
von ``q`` wieder beendet werden. Drückt man ``h``, so bekommt man eine kurze
Hilfe angezeigt, wie sich das Programm durch Drücken einzelner Tasten steuern
lässt.

.. }}}

.. index:: nast
.. _nast:

``nast``
^^^^^^^^
.. {{{

Das Programm ``nast`` ist nicht standardmäßig auf jedem Linux-System
installiert, kann aber einfach nachinstalliert werden:

.. code-block:: bash

    sudo aptitude install nast

Mit ``nast -m`` können dann die IP-Adressen aller Rechner und Router, die sich
im lokalen Netzwerk befinden, aufgelistet werden; zusätzlich bekommt man bei
diesem Aufruf die zu jeder IP-Addresse die entsprechende MAC-Addresse angezeigt.

.. }}}

.. }}}

System-Verwaltung
-----------------

.. _Paket-Verwaltung:

Prozess- und Paket-Verwaltung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

.. index:: apt, aptitude, Paketverwaltung; aptitude
.. _apt:
.. _aptitude:
.. _apt, aptitude:

``apt``, ``aptitude``
"""""""""""""""""""""
.. {{{

Mit ``apt-cache search suchbegriff`` beziehungsweise  ``aptitude search
suchbegriff`` kann jeder Benutzer die lokale Pakete-Liste nach dem Namen oder
der Beschreibung eines Programms oder einer Code-Bibliothek (``lib``)
durchsuchen und somit beispielsweise nachsehen, ob ein bestimmtes Paket
installierbar beziehungsweise bereits installiert ist.

Als Super-User kann man zusätzlich weitere Funktionen von ``apt``
beziehungsweise ``aptitude`` nutzen: [#]_

* Mit ``apt-get update`` beziehungsweise ``aptitude update`` wird die lokale
  Pakete-Liste aktualisiert; hierbei wird auch die Liste der Server, von
  denen die Pakete heruntergeladen werden können, auf den aktuellen Stand
  gebracht. 
  
  Ein solcher Update sollte in regelmäßigen Abständen beziehungsweise stets vor
  neuen Paket-Installationen oder System-Aktualisierungen vorgenommen werden.

* Mit ``apt-get install paketname`` (oder einfacher: ``aptitude install
  paketname``) lässt sich ein Programm oder eine Bibliothek installieren. Es
  können optional auch mehrere Paketnamen auf einmal angegeben werden:
  ``aptitude install paket1 paket2 ...``.

  Führt eine Installation zu Versions-Konflikten, wird automatisch nach einer
  Lösung gesucht, welche die verletzten Abhängigkeiten auflösen kann,
  beispielsweise eine Installation zusätzlicher Pakete. Es erscheint eine
  entsprechende Rückmeldung, wobei es dem Benutzer überlassen wird, ob die
  Lösung akzeptiert wird oder ob weiter nach einer anderen Lösung gesucht werden
  soll.

.. * Mit ``aptitude reinstall paket`` kann ein einzelnes Paket (Programm oder
..   Bibliothek) neu installiert werden. Dabei wird gegebenenfalls automatisch ein
..   Update vorgenommen. Mögliche Konfigurationsdateien bleiben dabei unberührt.

* Mit ``apt-get remove paket`` (oder einfacher: ``aptitude remove paket`` kann
  ein installiertes Paket wieder deinstalliert werden. Die Konfigurationsdateien
  bleiben dabei erhalten. Sollen diese ebenfalls entfernt werden, kann ``apt-get
  purge paket`` beziehungsweise ``aptitude remove --purge paket`` genutzt
  werden.

* Mit ``apt-get autoclean`` beziehungsweise ``aptitude autoclean`` werden alle
  noch Pakete vom Rechner entfernt, die von den aktuell installierten Programmen
  nicht mehr genutzt werden.

* Mit ``apt-get source paket`` kann der Quellcode eines Pakets (Programm oder
  Bibliothek) herunter geladen werden. Somit können erfahrene Anwender im
  Bedarfsfall Programme mit abweichenden Konfigurationen selbst kompilieren,
  oder bei entsprechenden Programmier-Kenntnissen einen Blick in die eigentliche
  Funktionalität eines Programms werfen und/oder Teile des Quellcodes für eigene
  Projekte weiter verwenden.

* Mit ``apt-get upgrade`` beziehungsweise ``aptitude safe-upgrade`` werden alle
  Pakete auf den neuesten Stand gebracht; ein Installieren zusätzlicher Pakete
  ist dabei nicht vorgesehen. 

  Vor einem Upgrade sollte die lokale Paket-Liste stets mit ``apt-cach upgrade``
  beziehungsweise ``aptitude update`` aktualisiert werden.

* Mit ``apt-get dist-upgrade`` beziehungsweise ``aptitude full-upgrade`` werden
  nicht nur vorhandene Pakete aktualisiert, sondern gegebenenfalls auch
  zusätzliche, neue Pakete installiert. Zudem wird gegebenenfalls die gesamte
  Distribution aktualisiert; beispielsweise könnte so ein Wechsel von Ubuntu
  Version 14.04 auf Version 16.04 vorgenommen werden. Da ein solcher
  System-Upgrade zahlreiche Veränderungen mit sich bringen kann, ist von dieser
  Aktualisierungs-Variante meist abzuraten. [#]_


``aptitude`` kann auch ohne zusätzliche Kommandozeilen-Argumente aufgerufen
werden; in diesem Fall erscheint eine text-basierte Benutzeroberfläche.  In den
meisten Fällen wird ``aptitude`` allerdings als (bessere) Alternative ebenso wie
``apt`` verwendet: ``aptitude`` merkt sich nämlich bei Installationen, welche
zusätzlichen Pakete gegebenenfalls mitinstalliert werden. Dadurch kann
``aptitude`` bei Deinstallationen die installierten Pakete ohne Weiteres auch
wieder restlos entfernen.


.. In der oberen Hälfte werden Paketnamen (nach verschienenen Rubriken sortiert)
.. aufgelistet, in der unteren Hälfte erscheint zum jeweiligen Paket eine passende
.. Beschreibung.

.. Mit den Cursor-Tasten kann man sich in der oberen Bildschirmhälfte durch die
.. Paketzweige navigieren, mit der ``Enter``-Taste werden Unterkategorien ein-
.. beziehungsweise ausgeblendet. Wie in den obersten Zeilen kurz beschrieben,
.. kann mit ``q`` das Programm beendet werden.
..
.. Mit ``u`` werden die Paketquellen aktualisiert (entspricht ``aptitude
.. update``).
..
.. Mit ``+`` kann das Paket unter dem Cursor zur (Neu-)Installation, mit ``-``
.. zum Entfernen und mit ``_`` zum vollständigen Löschen vorgemerkt werden;
..
.. Mit ``g`` werden die vorgemerkten Änderungswünsche ausgeführt.

.. }}}

.. index:: dpkg
.. _dpkg:

``dpkg``
""""""""
.. {{{

Der Debian Package Manager (``dpkg``) ist die Basis-Anwendung zum Installieren
und Deinstallieren von Debian-Paketen; auch ``apt`` macht intern von ``dpkg``
Gebrauch. Auch wenn ein Programm oder ein Hardware-Treiber nicht in den
Paket-Quellen enthalten ist, kann das entsprechende Paket häufig von der
Webseite des Autors beziehungsweise Geräte-Herstellers heruntergeladen und aus
dem Download-Verzeichnis heraus folgendermaßen installiert werden: 

.. code-block:: sh

    sudo dpkg -i paket.deb

Als Hilfsprogramm mit graphischer Bedienoberfläche kann wahlweise auch
`gdebi <https://wiki.ubuntuusers.de/Paketinstallation_DEB/#gdebi>`__ genutzt
werden, das ebenfalls auf ``dpkg`` aufbaut.

Mit ``sudo dpkg -r paketname`` kann ein Paket unter Beibehaltung der
Konfigurationsdateien wieder deinstalliert oder mit ``dpkg -P paketname``
restlos entfernt werden.

Mit ``dpkg -l suchbegriff`` lassen sich alle Pakete auflisten, die auf einen
Suchbegriff zutreffen -- reguläre Ausdrücke können ebenfalls eingesetzt werden.
Mit ``dpkg -S paketname`` wird angezeigt, welche Datei(en) durch das
entsprechende Paket installiert wurden.

.. }}}


.. }}}

.. _Hardware-Monitoring:
.. _Hardware-Verwaltung:
.. _Hardware-Monitoring und -verwaltung:

Hardware-Monitoring und -verwaltung
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. index:: eject
.. _eject:

``eject``
"""""""""
.. {{{

Mit ``eject devicename``, beispielsweise ``eject /dev/cdrom0``, kann das
CD/DVD-Laufwerk geöffnet werden.

.. }}}

.. index:: fdisk
.. _fdisk:

``fdisk``
"""""""""
.. {{{

Mit ``fdisk`` können Informationen über interne und externe Festplatten
beziehungsweise Speichermedien angezeigt werden. Ebenso ist es möglich, mit
``fdisk`` Partitionen zu verwalten. ``fdisk`` 

Nützlich ist der Aufruf von ``fdisk -l``, um Disk-Informationen angeschlossener
Speichermedien anzuzeigen.

.. }}}

.. index:: lshw
.. _lshw:

``lshw``
""""""""

Mit ``lshw`` werden die Hardware-Informationen des Computers aufgelistet; mit
``lshw -short`` wird eine Kurzform dieser Informationen ausgegeben.

.. index:: mount, umount
.. _mount:
.. _umount:

``mount``, ``umount``
"""""""""""""""""""""

Mit ``mount device pfad`` kann ein Datenträger (Speichermedium, Partition oder
Ordner) in den angegebenen Pfad einbinden ("mounten"); entsprechend wird mit
``umount pfad`` die Einbindung gelöst, falls kein Programm aktuell auf das im
angegebenen Pfad eingebundene Medium zugreift.

Ruft man ``mount`` ohne weitere Argumente auf, so bekommt man eine Liste mit den
verschiedenen Devices, ihren Mount-Points, Lese- beziehungsweise
Schreib-Optionen und Datei-Systemen angezeigt; diese Liste kann durch
übersichtlicher ``mount | column -t`` in einer übersichtlicheren Form ausgegeben
werden.



Sitzungs-Verwaltung
^^^^^^^^^^^^^^^^^^^

.. index:: chroot
.. _chroot:

``chroot``
""""""""""
.. {{{

Mit ``chroot pfad`` kann der angegebene Pfad als Basispfad ``/`` des
Betriebsystems festgelegt werden. Dies ist insbesondere praktisch, um ein
"Live-System" von einem USB-Stick zu booten und von diesem System aus Wartungen
am eigentlich installierten Betriebsystem vorzunehmen (falls dieses aus
irgendwelchen Gründen nicht mehr booten sollte). Nützlich ist dabei folgende
Routine:

.. code-block:: bash

    # Vorab: Die System-Partition eingebinden:
    # -- falls unbekannt: fdisk -l eingeben! --
    # mount /dev/[systempartition] pfad

    cd pfad 
    mount --bind /sys  ./sys 
    mount --bind /dev  ./dev 
    mount --bind /proc ./proc 
    chroot .

Hierbei werden (nach einem Wechsel in den Pfad der Systempaftition) zunächst die
Systemdaten (abgelegt in ``/sys``), die Daten der angeschlossenen Geräte
(abgelegt in ``/dev``) und der laufenden Prozesse (abgelegt in ``/proc``) in das
zu wartende System eingebunden. Anschließend kann man mit ``chroot .`` das
aktuelle Verzeichnis als Basispfad nutzen und somit innerhalb des Shell-Fensters
Programme direkt auf dem zu wartenden System ausführen. Mit ``exit`` kann man in
das eigentlich laufende (Live-)System zurück gelangen.

.. }}}

.. index:: halt, reboot
.. _halt:
.. _reboot:

``halt``, ``reboot``
""""""""""""""""""""
.. {{{

* Mit ``halt`` kann das System herunter gefahren und der Computer ausgeschaltet
  werden.

* Mit ``reboot`` kann das System neu gestartet werden.

.. }}}



.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Gegebenenfalls muss eine neue Gruppe erst mittels :ref:`addgroup
    <addgroup>` erstellt werden. Existiert die angegebene Benutzer-Gruppe nicht,
    so bricht ``chgrp`` mit einer Fehlermeldung ab.

.. [#] In der Datei ``/etc/apt/sources.list`` ist festgelegt, auf welchen
    Servern ``apt`` nach verfügbarer Software suchen beziehungsweise diese
    installieren soll. Je nach Vorlieben können stets die aktuellsten
    Entwicklungen oder nur ältere, bereits bewährte Pakete abgefragt werden.

    Durch Aufruf von ``apt-get update`` beziehungsweise ``aptitude update`` wird
    die Liste an verfügbaren Paketen aktualisiert. Zusätzlich zu jeder Quelle,
    die durch einen ``deb``-Eintrag festgelegt wird, kann ein
    ``deb-src``-Eintrag stehen, wenn von dort auch Quellcode heruntergeladen
    werden soll (interessant für Entwickler beziehungsweise um Programme selbst
    zu kompilieren).

.. [#] Hat man bei der Installation eigene :ref:`Partitionen <Partitionen
    einrichten>` für das System und das Home-Verzeichnis eingerichtet, so ist es
    meist einfacher, anstelle eines Versions-Upgrades eine Neu-Installation
    durchzuführen. Bei Debian, Ubuntu LTS und LinuxMint sollte dies etwa alle
    drei Jahre erfolgen.

.. .. [#] Tip für private Desktop-PCs: Zwei lauffähige Linux-Varianten parallel
..     installieren! So kann das weniger genutzte System als
..     "Experimentier-Umgebung" genutzt werden.

.. todo: Backup

.. .. [#]  Mit ``.`` wird der Pfad des aktuellen Verzeichnisses bezeichnet.

.. todo lscpu

