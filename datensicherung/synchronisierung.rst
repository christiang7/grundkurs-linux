
.. _Datenabgleich:
.. _Daten-Abgleich:
.. _Daten-Synchronisierung:
.. _Datenabgleich mit unison und bsync:

Datenabgleich mit ``unison`` und ``bsync``
==========================================

Die beiden in diesem Abschnitt vorgestellten Programme ``unison`` und ``bsync``
ermöglichen eine (manuelle) Synchronisierung zweier Verzeichnisse. Ein
automatisierter Einsatz dieser Programme via :ref:`Cron <Cron>` ist nicht
vorgesehen, da die beiden einander sehr ähnlichen Programme stets eine
Bestätigung seitens des Benutzers verlangen, in welcher Richtung ein
Datenabgleich vorgenommen werden soll.


.. index:: Unison

Unison
------

Das Programm `unison <https://wiki.ubuntuusers.de/Unison>`_  (beziehungsweise
``unison-gtk`` für das gleiche Programm mit graphischer Oberfläche) ermöglicht
einen Datenabgleich zweier Verzeichnisse. Egal, in welchem der beiden
Verzeichnisse Änderungen vorgenommen werden, kann ``unison`` auf dem jeweils
anderen Verzeichnis die entsprechenden Änderungen vornehmen, um beide
Verzeichnisse wieder auf den gleichen Stand zu bringen.

Unison kann folgendermaßen via :ref:`apt <aptitude>` installiert werden:

.. code-block:: bash

    sudo apt-get install unison unison-gtk

Nach der Installation kann Unison mittels ``unison-gtk`` aufgerufen werden.
Unison eignet sich gut, um beispielsweise ein lokales Verzeichnis gegenüber
einem USB-Stick synchron zu halten: Egal ob Dateien lokal oder auf dem USB-Stick
geändert wurden, bringt Unison beide Verzeichnisse wieder auf den gleichen
Stand.

Unison kann ebenso verwendet werden, um Verzeichnisse auf zwei Rechnern über via
:ref:`SSH <SSH>` zu synchronisieren. Hier kann es allerdings Komplikationen
geben, wenn auf den beiden Rechnern Unison in unterschiedlich alten Versionen
läuft: Eine Synchronisation ist mit Unison dann unter Umständen nicht möglich;
man kann in diesem Fall allerdings den Python-Nachbau :ref:`bsync <bsync>`
nutzen, wobei es für dieses Programm keine graphische Bedienoberfläche gibt.


.. rubric:: Unison-Profile

Intern verwendet Unison das Shell-Programm :ref:`rsync <rsync>` zur
Synchronisierung von Daten. Um Unison zu benutzen, erstellt man ein "Profil", in
welchem man zwei zu synchronisierende Verzeichnisse auswählt. Öffnet man dieses
im Auswahlmenü, so scannt Unison die Verzeichnisse automatisch nach
Veränderungen und zeigt diese mitsamt der Richtung und der Art der Veränderung
graphisch an. Mit einem Klick auf "Go" (Hotkey ``g``) werden die Änderungen
übernommen.

Persönlich habe ich lange Zeit zur Synchronisierung von Dateien zwischen meinem
Rechner und einem (mit :ref:`cryptsetup <cryptsetup>`  verschlüsselten)
USB-Stick folgende Methode verwendet: In einem eigenen Verzeichnis namens
``shared`` wird für jede zu synchronisierende Datei oder jeden zu
synchronisierenden Ordner einen gleichnamigen Symlink abgelegt, dessen Name
allerdings als (zusätzliche) Endung ``.sync`` erhält. Dieses Verzeichnis mit den
entsprechenden Symlinks muss sowohl auf der Festplatte wie auch auf dem
USB-Stick vorhanden sein. Die Ziele der Symlinks sind allerdings logischerweise
unterschiedlich, beispielsweise:

::

    /home/user/shared
        code.sync       # ---> /home/user/data/code
        configs.sync    # ---> /home/user/data/configs
        homepage.sync   # ---> /home/user/data/homepage

    /media/user/usb0/shared
        code.sync       # ---> /media/user/usb0/code
        configs.sync    # ---> /media/user/usb0/configs
        homepage.sync   # ---> /media/user/usb0/homepage

Falls noch nicht vorhanden, so wird anschließend das Verzeichnis ``~/.unison``
angelegt. In diesem Verzeichnis lassen sich beliebig viele
Synchronisations-Profile als Textdateien mit der Endung ``.prf`` anlegen. Für
die Synchronisation mit dem USB-Stick kann ein solches Profil beispielsweise
folgendermaßen ausssehen:

::

    # Datei: ~/.unison/usb-sync.prf

    # Quell- und Zielverzeichnis:
    root = /home/user/shared
    root = /media/user/usb0/shared

    # Angabe der zu synchronisierenden Dateien:
    follow = Name *.sync

    # Folgende Dateien dennoch ignorieren:
    ignore = Regex .*/.backupdir/*
    ignore = Regex .*/.git/*
    ignore = Regex .*/.hg/*

    # Bei Unterschieden zwischen Dateien nur das Nötigste ausgeben:
    diff = diff -y -W 80 --suppress-common-lines

Diese Variante setzt voraus, dass der USB-Stick immer an der gleichen Stelle
eingebunden wird (im obigen Beispiel ``/media/user/usb0``). Anschließend muss
nur noch ``unison usb-sync`` aufgerufen werden, um eine Synchronisation der
angegebenen Inhalte zu erreichen.


.. rubric:: Shell-Modus

Im Shell-Modus wird die von Unison vorgeschlagene Synchronisationsrichtung mit
``<----`` oder ``---->`` angezeigt. Drückt man ``f`` ("follow"), so wird diese
Empfehlung übernommen. Wurden sowohl im Quell- wie auch im Zielverzeichnis
Änderungen vorgenommen, so zeigt Unison ``<-?->`` an. Der Benutzer muss in
diesem Fall die Unterschiede zwischen den Dateiversionen gegebenenfalls selbst
überprüfen (bei Textdateien beispielsweise mittels :ref:`vimdiff <vimdiff>`) und
kann anschließend entweder mittels ``>`` oder ``<`` eine
Synchronisationsrichtung manuell angeben.

.. Dies kann auch, beispielsweise mit dem Skript `watcher.py
.. <https://github.com/gregghz/Watcher>`_, automatisiert erfolgen.

Synchronisierungen mit ``rsync`` beziehungsweise  ``unison`` lassen sich nicht
rückgängig machen. Zu solch einem Zweck oder für Mehrbenutzer-Systeme, wenn es
zu konkurrierenden Entwicklungen kommen kann (wenn beispielsweise die gleiche
Datei in zwei Verzeichnissen auf unterschiedliche Weise verändert wird), sollte
eine Versionskontroll-Programm wie :ref:`git <git>` oder ``mercurial`` verwendet
werden.


.. _Bsync:

Bsync
-----

Eine mit der Programmiersprache :ref:`Python3 <gwip:Python>` geschriebene
Neu-Implementierung von Unison (allerdings ohne graphische Bedienoberfläche)
heißt `bsync <https://github.com/dooblem/bsync>`__.

.. rubric:: Installation

Die Installation von ``bsync`` ist äußerst einfach:

.. code-block:: sh

    # Lokales bin-Verzeichnis erstellen:
    mkdir ~/bin 

    # In dieses Verzeichnis wechseln:
    cd ~/bin

    # bsync herunterladen:
    wget https://raw.github.com/dooblem/bsync/master/bsync

    # bsync ausführbar machen:
    chmod +x bsync

Damit die ``bsync``-Datei gefunden wird, kann man das Verzeichnis ``~/bin``
folgendermaßen zur ``PATH``-Umgebung hinzufügen:

.. code-block:: sh

    # Eintrag in der ~/.bashrc beziehungsweise ~/.zshrc:
    export PATH=$HOME/bin:/usr/local/bin:$PATH

.. rubric:: Aufruf von ``bsync``

Die Syntax von ``bsync`` ist ebenfalls sehr einfach. Sie lautet:

.. code-block:: sh

    bsync originalverzeichnis zielverzeichnis

Das Zielverzeichnis kann wahlweise ein lokales Verzeichnis oder ein Verzeichnis
auf einem anderen Rechner sein, auf dem man sich via :ref:`SSH <SSH>` anmelden
kann. In diesem Fall kann man als Zielverzeichnis
``benutzername@rechnerip:/pfad/zum/zielverzeichnis`` angeben. Hat man in der
Datei ``~/.ssh/config`` eigene Namen für die einzelnen Rechner vergeben, so kann
auch ``benutzername@rechnername:/pfad/zum/zielverzeichnis`` als Zielverzeichnis
angegeben werden.

Um ein Verzeichnis erstmalig mit einem Zielverzeichnis zu synchronisieren, muss
lediglich das Zielverzeichnis angelegt werden. Die einzelnen Dateien und
Unterverzeichnisse des Original-Verzeichnisses werden beim Aufruf von ``bsync``
automatisch ins Zielverzeichnis kopiert.


.. rubric:: Dateien von der Synchronisierung ausschließen

Soll bei der Synchronisierung zweier Verzeichnisse eine bestimmte Datei oder ein
Unterverzeichnis unberücksichtigt bleiben, so kann im Original-Verzeichnis eine
Datei namens ``.bsync-ignore`` angelegt werden. In dieser Datei wird je Zeile
ein einzelner Datei- oder Verzeichnisname angegeben. Um beispielsweise alle
Versionskontroll-Dateien, die sich in einem ``.git`` oder
``_build``--Verzeichnis befinden, von der Synchronisierung auszuschließen, kann
man eine ``.bsync-ignore``-Datei mit folgendem Inhalt anlegen:

::

    _build
    .git

Werden so Verzeichnisse angegeben, so werden alle darin enthaltenen Dateien und
Unterverzeichnisse von der Synchronisierung ausgeschlossen.


.. rubric:: Synchronisierung mehrerer Verzeichnisse

Anders als ``unison`` unterstützt ``bsync`` keine Profile. Man kann sich
allerdings leicht behelfen, indem man ein kurzes Shell-Skript schreibt, das
je Zeile ein anderes Verzeichnis synchronisiert, beispielsweise: 

.. code-block:: sh

    #! /bin/sh
    
    echo "Updating Code"
    bsync /home/user/data/code     benutzer@rechnername:/home/user/data/code

    echo "Updating Configs"
    bsync /home/user/data/configs  benutzer@rechnername:/home/user/data/configs

    echo "Updating Homepage"
    bsync /home/user/data/homepage benutzer@rechnername:/home/user/data/homepage

Eine solches Skript kann beispielsweise als Datei ``bsyncrechnername`` im
Verzeichnis ``~/bin`` abgelegt werden; zudem sollte die Datei mittels ``chmod
+x`` ausführbar gemacht werden. Bei einer Synchronisierung via SSH ist ein Login
via :ref:`SSH-Schlüssel <SSH-Schlüssel>` empfehlenswert, da ansonsten für jede
einzelne ``bsync``-Anweisung erneut das Passwort eingegeben werden muss.


