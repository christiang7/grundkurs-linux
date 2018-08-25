.. _Linux-Dateisystem:
.. _Aufbau des Linux-Dateisystems:

Aufbau des Linux-Dateisystems
=============================
.. {{{

Die Bezeichnungen für die grundlegenden Verzeichnisse sind auf allen
Linux-Systemen (nahezu) identisch. Für "normale" Benutzer sind vor allem zwei
Verzeichnisse von Bedeutung:

* Das "Home"-Verzeichnis, häufig mit ``~`` abgekürzt, ist unter dem
  Verzeichnis-Pfad ``/home/benutzername``  abgelegt. Innerhalb dieses
  Verzeichnisses kann der Benutzer beliebige weitere Verzeichnisse anlegen
  und/oder Dateien speichern.

  Eine Besonderheit unter Linux ist die Kenntlichmachung von persönlichen
  Konfigurations-Dateien und -Verzeichnissen: Diese befinden sich ebenfalls im
  Home-Verzeichnis des jeweiligen Benutzers und beginnen üblicherweise mit einem
  Punkt (``.``) vor dem eigentlichen Dateinamen. Man bezeichnet derartige
  Verzeichnisse und Dateien bisweilen auch als "versteckte" Dateien, da sie
  beispielsweise bei einem Aufruf der Shell-Anwendung :ref:`ls <ls>` ohne
  weitere Optionen nicht aufgelistet werden. In Datei-Managern mit graphischer
  Bedienoberfläche können die versteckten Dateien meist über die Menü-Zeile oder
  mittels einer Tastenkombination ein- oder ausgeblendet werden, beispielsweise
  bei :ref:`Caja <caja>` mittels ``Ctrl h``.

* Das "Media"-Verzeichnis ``/media`` wird von den meisten Linux-Systemen
  standardmäßig als Einhängepunkt für USB-Sticks, Speicherkarten und externe
  Festplatten verwendet. Unter Ubuntu/LinuxMint existieren in diesem Verzeichnis
  wiederum Unterverzeichnisses für die einzelnen Benutzer, so dass
  beispielsweise angeschlossene USB-Sticks automatisch in einen Verzeichnis-Pfad
  der Art ``/media/benutzername/geraetname`` eingehängt werden. Für derartige
  Verzeichnisse hat der jeweilige Benutzer ebenfalls vollen Lese- und
  Schreibrechte.

Auf alle anderen Verzeichnisse (mit Ausnahme von ``/tmp``) kann ein normaler
Benutzer ohne SuperUser-Rechte üblicherweise nur lesend zugreifen. [#]_

Im Gegensatz zu Windows unterscheidet Linux zwischen Groß- und Kleinbuchstaben
in Datei- und Verzeichnisnamen: Beispielsweise stellen die Dateien
``hallo-welt.txt`` und ``Hallo-Welt.txt`` also als zwei verschiedene Dateien dar
und können somit auch mit unterschiedlichen Inhalten innerhalb eines einzigen
Verzeichnisses vorhanden sein.

.. index:: Verzeichnisstruktur:
.. _Verzeichnisstruktur:
.. _Standard-Verzeichnisse:
.. _Standard-Verzeichnisse eines Linux-Systems:

.. }}}

Standard-Verzeichnisse
----------------------
.. {{{

Dieser Abschnitt ist -- ebenso sowie der folgende Abschnitt :ref:`Datei-Rechte
<Datei-Rechte>` -- für fortgeschrittene Linux-Benutzer sowie für interessierte
Leser gedacht, die sich für Grundmechanismen von Linux-Systemen interessieren.

Zur Organisation der Dateien halten sich die meisten Linux-Distributionen an
einen bestimmten Standard ("Filesystem Hierarchie Standard"). Dieser umfasst die
folgenden Verzeichnisse:

.. {{{

.. _Wurzelverzeichnis:

.. _/:

* ``/``
  Das Verzeichnis ``/`` (auch "Wurzelverzeichnis" genannt) stellt den Basispfad
  des Systems dar.


.. _/bin:

* ``/bin``
    In diesem Verzeichnis ("binaries") befinden sich wichtige Programme für
    Anwender, die immer verfügbar sein müssen, beispielsweise die Shell ``bash``
    oder das Programm ``ls`` zur Anzeige von Verzeichnis-Inhalten.

.. _/boot:

* ``/boot``
    In diesem Verzeichnis befinden sich die zum Hochfahren des Systems unbedingt
    erforderlichen Dateien. Am wichtigsten ist dabei der Kernel, üblicherweise
    eine Datei mit dem Namen ``vmlinuz-versionsname`` (andere Namen sind
    ebenfalls möglich).

.. _/dev:

* ``/dev``
    In diesem Verzeichnis ("devices") befinden sich ausschließlich
    Geräte-Dateien. Diese speziellen Dateien stellen eine einfach nutzbare
    Schnittstelle zur Hardware dar.

    Für jede Festplatte und ihre Partitionen existiert im ``/dev/``-Verzeichnis
    ein eigener Eintrag. Beispielsweise bezeichnet, sofern vorhanden,
    ``/dev/hda`` ist die erste IDE-Festplatte, ``/dev/sda`` die erste
    SCSI-Festplatte im System. Höhere Buchstaben (``sdb``, ``sdc``) stellen
    weitere Festplatten oder externe Speichermedien dar, Zahlen am Ende
    (``sda1``, ``sda2``) benennen die Partitionen der Festplatten. [#PAR]_

.. _/etc:

* ``/etc``
    In diesem Verzeichnis ("etcetera") befinden sich zahlreiche
    Konfigurationsdateien, die Einstellungen zu den installierten Programmen
    sowie grundlegende Systeminformationen enthalten; viele dieser Dateien haben
    eigene Manpage, die in einer Shell mittels eines Aufrufs der Form ``man
    /etc/fstab`` aufgerufen werden kann.

.. _/home:

* ``/home``
    In diesem Verzeichnis befinden sich die persönlichen Verzeichnisse der
    einzelnen Benutzer.

.. _/lib:

* ``/lib``
    In diesem Verzeichnis ("libraries") befinden sich die wichtigsten
    Code-Bibliotheken des Systems; diese Dateien werden von mehreren Programmen
    gemeinsam genutzt und sollten nicht manuell verändert werden.

.. _/media:

* ``/media``
     In diesem Verzeichnis werden externe Datenträger als Unterverzeichnisse
     eingebunden. Bei aktuellen Ubuntu- und LinuxMint-Versionen werden
     automatisch erkannte USB-Sticks, Speicherkarten, externe Festplatten usw.
     in ein Verzeichnis der Art ``/media/benutzername/name-des-datentraegers``
     eingebunden.

.. _/proc:

* ``/proc``
    In diesem Verzeichnis ("processes") sind keine gewöhnlichen Dateien
    enthalten, sondern Schnittstellen zum Linux-Kernel. Jedes laufende Programm
    wird hier in einem Unterverzeichnis geführt, dessen Dateien viele
    Informationen beispielsweise über den aktuellen Programmstatus enthalten.

..  Zudem gibt es eine umfangreiche Verzeichnisstruktur mit Daten über den
..  Kernel und die Hardware des Systems.

.. _/root:

* ``/root``
    In diesem Verzeichnis befinden sich die (persönlichen) Dateien des
    Systemverwalters ("Root", "SuperUser"). Das Verzeichnis liegt im
    Wurzelverzeichnis, damit der Systemverwalter auch dann auf seine
    (Konfigurations-)Dateien zugreifen kann, wenn durch einen Fehler der Zugriff
    auf andere Partitionen nicht mehr möglich ist. [#]_

.. _/sbin:

* ``/sbin``
    In diesem Verzeichnis ("superuser-binaries") befinden sich ebenfalls --
    ähnlich wie im ``/bin``-Verzeichnis -- wichtige Programme, die allerdings
    für den Systemverwalter gedacht sind. Sie erfüllen Funktionen, auf die ein
    normaler Benutzer keinen Zugriff hat.

.. _/tmp:

* ``/tmp``
    Dieses Verzeichnis ("temporary") kann von jedem Benutzer und jedem Programm
    als temporäre Ablage für Dateien verwendet werden. Hier gespeicherte Daten
    werden beim Booten üblicherweise gelöscht.

..  Damit sich Benutzer nicht gegenseitig ihre Dateien löschen, ist das
..  sogenannte Sticky-Bit dieses Verzeichnisses gesetzt.

.. _/usr:

* ``/usr``
    In diesem Verzeichnis ("unix system ressources") befinden sich der größte
    Teil der installierten Software. Auf vielen Systemen befinden sich innerhalb
    von ``/usr`` mehr Daten als in allen anderen Dateien zusammen. Die
    ausführbaren Programmdateien sind meist in ``/usr/bin``,
    Programmbibliotheken in ``/usr/lib`` abgelegt.

    In Netzwerken, an die viele gleichartige Systeme angeschlossen sind, wird
    dieses Verzeichnis häufig auf einem zentralen Server gespeichert, und alle
    anderen Computer greifen über das Netzwerk darauf zu.

..  Die umfangreichste Verzeichnisstruktur des Systems.

.. _/var:

* ``/var``
    In diesem Verzeichnis ("variables") befinden sich hauptsächlich
    Dateien, die sich ständig verändern. Beispielsweise werden hier Log-Dateien
    gespeichert.

.. _/opt:

* ``/opt``
    In diesem Verzeichnis ("optional") werden bei Bedarf sehr große Programme
    gespeichert, die nicht unmittelbar zum System gehören. Bei knappem
    Festplattenspeicher kann dieses Verzeichnis -- wie das ``/home``-Verzeichnis
    -- auf einer externen Festplatte oder einer anderen Partition abgelegt
    werden.

.. _~:

Als Abkürzungen ist ``~`` für das persönliche Home-Verzeichnis (also
``/home/benutzername``) üblich. Als weitere Abkürzung bezeichnet ``.`` den Namen
des aktuellen Verzeichnisses, und ``..`` den Namen des jeweils übergeordneten
Verzeichnisses. Zur Trennung einzelner Verzeichnis-Bezeichnungen sowie von
Verzeichnis- und Dateinamen wird stets ein ``/``-Zeichen gesetzt.

Soll eine konkrete Datei beispielsweise als Argument einer Shell-Anwendung
angegeben werden, so ist dies entweder relativ zum aktuellen Verzeichnis
möglich, oder über eine absolute Pfadangabe:

* Eine absolute Pfadangabe beginnt stets mit ``/``, geht also vom
  Wurzel-Verzeichnis aus.

* Eine relative Pfadangabe kann beispielsweise ``unterverzeichnis/dateiname``
  lauten, wenn sich die Datei in einem Unterverzeichnis des aktuellen
  Verzeichnisses befindet. Befindet sich die Datei hingegen im aktuellen
  Verzeichnis selbst, so kann dieses (insbesondere beim Aufruf von ausführbaren
  Dateien) optional mit ``./`` angegeben werden, ansonsten genügt auch
  ``dateiname`` als Pfadangabe. Dateien, die sich im übergeordneten Verzeichnis
  befinden, können mit ``../dateiname`` angesprochen werden, oder mit
  ``../../dateiname``, wenn es sich um eine Datei im über-übergeordneten
  Verzeichnis handelt.

Während es für die Angabe von Dateinamen (insbesondere für
:ref:`Shell-Anwendungen <Shell-Anwendungen>` ) von Bedeutung ist, in welchem
Verzeichnis man sich aktuell befindet, so können regulär installierte
Linux-Programme von jedem beliebigen Verzeichnis aus gestartet werden. [#]_

.. _Spezielle Dateien:

.. }}}

.. rubric:: Spezielle Dateien
.. {{{

Der Begriff "Datei" wird unter Linux sehr weit gefasst; letztlich verläuft
jeder Datenaustausch mit einem Speichermedium über eine Datei. Auch Verzeichnisse
sind demnach "Dateien", ebenso wie die Einhängepunkte der einzelnen Geräte im
``/dev``-Verzeichnis.

.. Pipes, ...

.. _Symlinks und Hardlinks:

.. }}}

.. rubric:: Symlinks und Hardlinks
.. {{{

Eine Besonderheit unter Linux sind so genannte "Symlinks": Damit sind
"Verknüpfungen" einer Datei auf eine andere Datei gemeint. Symlinks können
sowohl für Dateien als auch für Verzeichnisse angelegt werden.

Ob man die eigentliche Datei oder eine darauf verweisende Symlink-Datei öffnet
beziehungsweise verändert, spielt keine Rolle: Beide Dateinamen gelten als
Synonym für die selbe Datei. Der einzige Unterschied besteht darin, dass die
Symlink-Datei wieder gelöscht werden kann, ohne dass sich bezüglich der
eigentlichen Datei etwas ändert. Wird jedoch die eigentliche Datei gelöscht, so
zeigt der Symlink ins Leere und kann nicht mehr genutzt werden.

Symlinks werden üblicherweise in einer Shell mittels der Anweisung :ref:`ln
<ln>` generiert: ``ln -s zieldatei symlinkdatei`` erzeugt einen neuen Symlink,
wobei sowohl für die Ziel- als auch für die Symlink-Datei wahlweise ein
vollständiger Dateipfad als auch ein Pfad relativ zum aktuellen Verzeichnis
angegeben werden kann. Befindet sich die Zieldatei im aktuellen Verzeichnis, und
soll auch die Symlink-Datei dort erstellt werden, so können die Pfadangaben
weggelassen werden.

Neben Symlinks können mit :ref:`ln <ln>` auch so genannte Hardlinks erstellt
werden. In diesem Fall sind sowohl die eigentliche Datei als auch die
Hardlink-Datei nicht mehr unterscheidbar: Löscht man eine der beiden Dateien, so
bleibt der andere Eintrag erhalten. Die einzige Einschränkung für Hardlinks
besteht darin, dass sich sowohl die Ziel- als auch die Hardlink-Datei auf der
gleichen Partition befinden müssen. Sollen Verlinkungen über Partitionen hinweg
gesetzt werden, müssen Symlinks verwendet werden.

.. index:: Datei-Rechte
.. _Datei-Rechte:

.. }}}

.. }}}

Datei-Rechte
------------
.. {{{

Linux hat ein einfaches, aber gut konzipiertes System zur Verwaltung von
Datei-Rechten. Grundsätzlich können für jede Datei folgende Rechte vergeben
werden:

    +-----------------------+--------+
    | Recht                 | Symbol |
    +-----------------------+--------+
    | Lesen ("read")        | ``r``  |
    +-----------------------+--------+
    | Schreiben ("write")   | ``w``  |
    +-----------------------+--------+
    | Ausführen ("execute") | ``x``  |
    +-----------------------+--------+

* Ist eine Datei lesbar, so kann der Inhalt dieser Datei von Anwendungen mit
  graphischer Bedienoberfläche oder Shell-Programmen wie :ref:`cat <cat>` oder
  :ref:`less <less>` angezeigt beziehungsweise ausgelesen werden.

* Ist eine Datei schreibbar, so kann der Inhalt der Datei geändert werden.

* Ist eine Datei ausführbar, so kann diese aus einer Shell heraus mittels
  ``/pfad/dateiname`` aufgerufen werden. Diese Eigenschaft ist beispielsweise
  für Shell-Skript-Dateien nützlich.

  Für Verzeichnisse hat das Ausführungs-Recht eine andere Bedeutung: Ist dieses
  Recht gesetzt, so bedeutet dies, dass in dieses Verzeichnis gewechselt werden
  darf; man "betritt" dadurch das Verzeichnis und bekommt somit Zugriff auf die
  sich darin befindlichen Dateien.

  Ist bei einem Verzeichnis nur das Lese-Recht ``r`` gesetzt (das Ausführungs-
  Recht ``x`` hingegen nicht), so können zwar beispielsweise mittels :ref:`ls
  <ls>` die Inhalte des Verzeichnisses angezeigt werden; man hat allerdings
  keinen Zugriff auf die Dateien, kann sie also beispielsweise nicht ausführen.
  Sollen Dateien innerhalb des Verzeichnisses auch geändert oder gelöscht werden
  können, so muss das Verzeichnis die Rechte ``w`` und ``x`` aufweisen.

Um die Dateirechte aller Dateien eines Verzeichnisses anzuzeigen, kann man in
einer Shell ``ls -lh`` eingeben. Als Ergebnis erhält man eine zeilenweise
Auflistung mit etwa folgender Form:

::

    drwxrwsr-x 18 grund-wissen www-data 4,0K Feb 28 20:44 source
    -rw-rw-r--  1 grund-wissen www-data  172 Mär  1 09:47 tmp.txt

In diesem Beispiel sind zwei Einträge aufgelistet: Ein Verzeichnis namens
``source`` und eine gewöhnliche Datei namens ``tmp.txt``:

* Am ersten Buchstaben jeder Zeile kann man erkennen, um was für einen Datei-Typ
  es sich bei dem Eintrag jeweils handelt.

  Im obigen Beispiel steht beim ersten Eintrag ein ``d`` ("directory"), was
  charakteristisch für ein Verzeichnis ist. In der zweiten Zeile steht dort
  lediglich ein ``-``, was bedeutet, dass es sich um eine gewöhnliche Datei
  (ohne Besonderheiten) handelt.

* Die nächsten drei Buchstaben (``rwx`` beziehungsweise ``rw-``) bezeichnen die
  Dateirechte, die der Eigentümer der Datei hat.

  Im obigen Beispiel kann das Verzeichnis ``source`` vom Eigentümer gelesen
  (``r``), verändert (``w``) sowie betreten (``x``) werden. Die Datei
  ``tmp.txt`` kann vom Eigentümer gelesen (``r``), verändert (``w``), aber nicht
  ausgeführt werden. Der Eigentümer für beide Einträge ist in diesem Beispiel
  ``grund-wissen``.

* Die weiteren drei Buchstaben (``rws`` beziehungsweise ``rw-``) bezeichnen die
  Dateirechte, welche die Benutzer-Gruppe der Datei hat. Für jede Datei ist
  nämlich unter Linux nicht nur festgelegt, wer der Eigentümer der Datei ist,
  sondern ebenso, welche Benutzer-Gruppe Rechte bezüglich der Datei hat.

  Im obigen Beispiel kann das Verzeichnis ``source`` von der Benutzer-Gruppe
  ``www-data`` wiederum gelesen (``r``), verändert (``w``) sowie betreten werden
  (``s``). Auf den Unterschied zwischen ``s`` und ``x`` wird im übernächsten
  Abschnitt näher eingegangen. Die Datei ``tmp.txt`` kann von der
  Benutzer-Gruppe gelesen (``r``), verändert (``w``), aber nicht ausgeführt
  werden. Eigentümer und Gruppe haben in diesem Beispiel also gleiche Rechte.

* Die letzten drei Buchstaben (``r-x`` beziehungsweise ``r--``) bezeichnen die
  Dateirechte, die alle anderen Benutzer haben. Damit sind Benutzer gemeint, die
  nicht Mitglied in der angegebenen Benutzer-Gruppe sind.

Mittels der Shell-Anweisung :ref:`groups <groups>` kann man sich anzeigen
lassen, in welchen Gruppen der aktuelle Benutzer Mitglied ist. Die Rechte
einzelner Dateien oder Verzeichnisse können mit :ref:`chmod <chmod>` oder einem
Dateimanager wie :ref:`Caja <Caja>` oder :ref:`mc <mc>` geändert werden. 

Welche Rechte Datei Dateien und Verzeichnisse standardmäßig erhalten sollen,
kann mittels :ref:`umask <umask>` eingestellt werden.


.. _Zahlen-Codes für Datei-Rechte:

.. }}}

.. rubric:: Zahlen-Codes für Datei-Rechte
.. {{{

Um Datei-Rechte zu ändern, wird üblicherweise die Shell-Anwendung :ref:`chmod
<chmod>` genutzt. Um die einzelnen Rechte mit weniger Schreibaufwand bezeichnen
zu können, wurden folgende Zahlen-Codes eingeführt:

    +-----------------------+--------+-------------+
    | Recht                 | Symbol | Zahlen-Code |
    +-----------------------+--------+-------------+
    | Lesen ("read")        | ``r``  | ``4``       |
    +-----------------------+--------+-------------+
    | Schreiben ("write")   | ``w``  | ``2``       |
    +-----------------------+--------+-------------+
    | Ausführen ("execute") | ``x``  | ``1``       |
    +-----------------------+--------+-------------+

Gibt es für eine Datei nicht nur ein Lese-Recht (``r`` beziehungsweise ``4``),
sondern auch ein Schreibrecht (``w`` beziehungsweise ``2``), so können die
Zahlenwerte einfach addiert werden: Die Zahl ``6`` steht also für Lese- und
Schreibrechte. Kommt auch noch das Ausführungsrecht hinzu, ergibt sich die Zahl
``7``. Soll eine Datei nur les- und ausführbar, aber nicht veränderbar sein, so
hätte dies im Zahlen-Code ``5`` bedeuten.

Diese Rechte werden wiederum für den Eigentümer, die Benutzer-Gruppe sowie alle
anderen Benutzer definiert. Somit bedeutet beispielsweise ``750``, dass der
Eigentümer alle Datei-Rechte hat, die Benutzer-Gruppe Lese- und
Ausführungsrechte bekommt, und alle anderen Benutzer keinerlei Rechte besitzen.

Hat man sich einmal an diese Kurzschreibweise gewöhnt, können Datei-Rechte
sehr kurz und prägnant angegeben werden; diese Syntax ist daher auch häufig in
Lehrbüchern oder Hilfeseiten im Internet anzutreffen.

.. }}}

.. rubric:: Spezielle Rechte

Neben den üblichen Datei-Rechten ``r``, ``w``, ``x`` treten in seltenen Fällen
auch spezielle Rechte auf. Diese besonderen Rechte heißen ``setuid``, ``setgid``
und ``sticky``:

* Mit dem ``setuid``-Recht wird festgelegt, dass eine Datei (meist ein Programm)
  immer mit den Rechten des jeweiligen Eigentümers geöffnet beziehungsweise
  ausgeführt wird.

  Ein bekanntes Beispiel hierfür ist die Shell-Anweisung :ref:`passwd <passwd>`,
  mit der jeder Benutzer sein eigenes Passwort ändern kann. Letztlich ändert das
  Programm allerdings die Datei ``/etc/shadow``, die wiederum nur mit
  Superuser-Rechten (also vom Benutzer ``root``) geändert werden darf. Die beim
  Aufruf von ``passwd`` ausgeführte Datei ``/usr/bin/passwd`` gehört dem
  Benutzer ``root`` und muss, egal welcher Benutzer das Programm aufruft, auch
  stets vom ``root``-User ausgeführt werden.

  .. code-block:: sh

      # setuid-Beispiel:
      ls -lh /usr/bin/passwd
      -rwsr-xr-x 1 root root 53K Mai 17  2017 /usr/bin/passwd

  Das ``setuid``-Recht wird (beispielsweise beim Aufruf von ``ls -lh``) durch
  ein ``s`` beziehungsweise ``S`` anstelle einem ``x`` in den zum Benutzer
  gehörenden Datei-Rechten angezeigt. Ein großes ``S`` wird angezeigt, wenn die
  Datei nicht ausführbar ist (was selten der Fall ist), andernfalls wird ein
  kleines ``s`` an dieser Stelle angezeigt.


* Mit dem ``setgid``-Recht wird in ähnlicher Weise die Benutzer-Gruppe
  festgelegt, mit der eine Datei ausgeführt oder verändert wird.

  In der Praxis wird dies vor allem auf Verzeichnisse angewendet. Wird eine neue
  Datei erstellt, so entsprechen normalerweise sowohl Eigentümer als auch Gruppe
  dem aktuellen Benutzernamen. Soll ein Verzeichnis inklusive aller darin
  enthaltenen Dateien und Unterverzeichnisse hingegen von mehreren Benutzern,
  die einer bestimmten Gruppe angehören, genutzt werden können, so kann es
  sinnvoll sein, dass alle in diesem Verzeichnis neu erstellten
  Unterverzeichnisse und Dateien automatisch wieder unter dem jeweiligen
  Gruppen-Namen erstellt werden. 
  
  Beispielsweise kann das ``setgid``-Recht genutzt werden, um der Gruppe
  ``www-data`` des Webservers :ref:`Apache <Apache>` Leserechte für ein
  bestimmtes Verzeichnis zu geben. Damit ist jede hinzukommende Datei
  automatisch auch neu hinzukommende Dateien für den Webserver lesbar, ohne dass
  explizit jedes mal die Benutzer-Gruppe der neuen Datei geändert werden muss.
  Das ``setgid``-Recht wird wiederum durch ein ``s`` beziehungsweise ``S`` in
  den zur Gruppe gehörenden Datei-Rechten angezeigt.

* Mit dem ``sticky``-Recht kann für ein Verzeichnis festgelegt werden, dass die
  darin enthaltenen Dateien nur vom jeweiligen Eigentümer wieder gelöscht werden
  dürfen. 
  
  Dieses nur sehr selten anzutreffende Sonder-Recht findet beispielsweise beim
  Verzeichnis ``/tmp`` Anwendung, das von vielerlei Programmen als Ablagestelle
  für temporäre Dateien genutzt wird. Es wird durch ein ``t`` beziehungsweise
  ``T`` in den für die restlichen Benutzer geltenden Datei-Rechten angezeigt.

Auch für diese speziellen Rechte existieren Zahlen-Codes, und zwar wiederum
``4`` für das ``setuid``-Recht, ``2`` für das ``setgid``-Recht und ``1`` für das
``sticky``-Recht. Sollen diese Rechte für eine Datei beziehungsweise ein
Verzeichnis mittels :ref:`chmod <chmod>` gesetzt werden, so wird nicht wie
üblich eine dreistellige Zahl, sondern eine vierstellige Zahl angegeben, und an
der ersten Stelle das Sonder-Recht gesetzt. Beispielsweise wird so aus einem
Verzeichnis-Recht ``750``, das dem Eigentümer alle Rechte und der Gruppe
Leserechte einräumt, durch Setzen des ``setgid``-Rechts der Zahlen-Code
``2750``.


.. }}}

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Unter Ubuntu/LinuxMint sind auch die Home-Verzeichnisse der einzelnen
    Benutzer-Accounts standardmäßig für alle Benutzer lesbar. Aus meiner Sicht
    ist dies in den meisten Fällen nicht sinnvoll. Eine mögliche Abhilfe wird im
    Abschnitt :ref:`chmod <chmod>` näher beschrieben.
    Mehr Infos zu SuperUser-Rechten gibt es im Abschnitt :ref:`sudo <sudo>`.

.. [#PAR] Da auf einer Festplatte nur vier primäre Partitionen möglich sind,
    wird häufig eine erweiterte Partition angelegt, die den größten Teil der
    Festplatte umfasst. In der erweiterten Partition können dann "logische
    Laufwerke" angelegt werden. Diese erhalten grundsätzlich die
    Partitionsnummern ab ``5``. Enthält eine Festplatte also eine primäre und
    eine erweiterte Partition, in der sich wiederum zwei logische Laufwerke
    befinden, gibt es auf dieser Platte die Partitionen ``1``, ``2``, ``5`` und
    ``6``. Die primäre Partition ist ``1``, die erweiterte ist ``2``, und die
    beiden logischen Laufwerke sind ``5`` und ``6``.

.. [#] Häufig wird bei der Installation eines Linux-Systems für das
    ``/home``-Verzeichnis eine eigene Festplatte verwendet oder eine eigene
    Partition angelegt, um bei einer möglichen Neuinstallation des Systems die
    persönlichen Daten unverändert übernehmen zu können.

.. [#] Bei jedem Programm-Aufruf sucht Linux nach einem gleichnamigen Eintrag in
    der System-Variablen ``PATH``. Welche Verzeichnisse also standardmäßig
    nach einer gleichnamigen ausführbaren Datei durchsucht werden, kann in einer
    Shell mittels ``echo $PATH`` angezeigt werden. Welche ausführbare Datei
    beispielsweise hinter dem Programm ``firefox`` steht, kann in einer Shell
    mit ``which firefox`` geprüft werden.

