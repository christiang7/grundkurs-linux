.. _Backups:

Backups
=======
.. {{{

Um sich gegen Datenverlust zu schützen, der beispielsweise durch einen
Hardware-Defekt verursacht werden kann, sollten regelmäßig Backups von allen
relevanten Daten angefertigt werden. Darüber hinaus kann es beispielsweise bei
Server-Verwaltungen sinnvoll sein, sicherheitshalber ein Backup aller
Konfigurationsdateien zu erstellen, bevor die eigentlichen Änderungen
vorgenommen werden.

Für die persönlichen Daten auf einem Desktop-Rechner oder Notebook ist unter
Umständen bereits viel gewonnen, wenn diese beispielsweise auf eine externe
Festplatte kopiert werden ("Sicherheitskopie"). Dieses Verfahren ist simpel,
allerdings stellen sich u.a. auch folgende Fragen:

* Wie regelmäßig werden manuelle Backups vorgenommen?
* Wurden Verzeichnisse möglicherweise übersehen?
* Werden Konfigurations-Dateien ebenfalls gesichert?
* Werden Lösch-Vorgänge von Dateien in den Original-Verzeichnissen auch in den
  Sicherheits-Kopien berücksichtigt (Synchronisierung)?

Meist ist man besser beraten, anstelle eines einfachen Kopierens auf weitere
Hilfsmittel zurückzugreifen.

.. _tar-Backup:
.. _Backups mit tar:
.. _Backups mit tar-Archiven:
.. _Backups mittels tar-Archiven:

.. }}}

Backups mittels tar-Archiven
----------------------------
.. {{{

Um alle Daten eines Verzeichnisses in komprimierter Form abzuspeichern, kann ein
:ref:`tar <tar>`-Archiv des Verzeichnisses erstellt werden. Dies bietet sich
beispielsweise bei Servern für das Web-Verzeichnis ``/var/www`` oder das
Konfigurations-Verzeichnis ``/etc`` an:

.. code-block:: sh

    # Tar-Archiv anlegen:
    sudo tar -cvpzf backupname.tar.gz /etc

Wichtig bei dem obigen ``tar``-Aufruf ist insbesondere die Option ``p``
("preseve permissions"): Hierdurch werden auch die einzenen Datei-Rechte mit
archiviert.

Sollen einzelne Unter-Verzeichnisse ausgeschlossen werden, so ist dies mittels
der Option ``--exclude=pfadname`` vor Angabe des zu sichernden Verzeichnisses
möglich.

Um das so erstellte Archiv wieder zu entpacken, kann man folgende Anweisung
verwenden:

.. code-block:: sh

    # Tar-Archiv wieder entpacken:
    sudo tar -xvpzf backupname.tar.gz -C /recover

Durch die Option ``-C`` ("change output directory") kann ein anderes
Zielverzeichnis angegeben werden. Dies kann sinnvoll sein, um anschließend das
so wiederhergestellte Original mit den vorgenommenen Änderungen zu vergleichen
(beispielsweise mittels :ref:`vimdiff <vimdiff>`) und manuell einzelne Dateien
wieder durch die Originale zu ersetzen.


.. .. rubric:: Automatische Archivierung mittels Cronjob

.. _Backups mit rsync:
.. _Backups mittels rsync:
.. _Synchronisierung mit rsync:
.. _Synchronisierung mittels rsync:

.. }}}

Backups mittels ``rsync``
-------------------------
.. {{{

Das Programm :ref:`rsync <rsync>` kann genutzt werden, um eine Datei oder
ein Verzeichnis mit einer Zieldatei beziehungsweise einem Zielverzeichnis
synchron zu halten. Die allgemeine Syntax lautet dabei folgendermaßen:

.. code-block:: sh

    rsync optionen originaldatei zieldatei

Da unter Linux auch Verzeichnisse als spezielle Dateien angesehen werden, kann
für ``originaldatei`` beziehungsweise ``zieldatei`` auch ein Verzeichnisname
angegeben werden. Existiert das Ziel nicht, wird es automatisch erstellt.

Die wohl am häufigsten genutzten Optionen von ``rsync`` sind folgende:

* Mit ``-v`` wird der "verbose"-Modus aktiviert, so dass ausführliche Details
  zum Synchronisations-Vorgang auf dem Bildschirm ausgegeben werden.
* Mit ``-h`` werden Dateigrößen in einem "human readable"-Format ausgegeben,
  also nicht als Bits, sondern als kB oder MB.
* Mit ``-z`` werden die Dateien während der Übertragung komprimiert. Diese
  Option benötigt weniger Bandbreite, verursacht dafür allerdings mehr CPU-Last.
* Mit ``-r`` wird das Originalverzeichnis rekursiv mitsamt aller
  Unterverzeichnisse synchronisiert.
* Mit ``-l`` werden :ref:`Symlinks <Symlinks>`, die sich im Original-Verzichnis
  befinden, in identischer Form beibehalten. Als Alternative hierzu kann die
  Option(en) ``-LK`` verwendet werden: Anstelle der Symlinks werden in diesem
  Fall die jeweils verlinkten Dateien beziehungsweise Unterverzeichnisse ins
  Zielverzeichnis kopiert.
* Mit ``-p`` werden die Dateirechte ("permissions"), mit ``-t`` die Zeitstempel
  der einzelnen Dateien mitkopiert.
* Mit der Option ``-a`` (Archiv-Modus) werden die Optionen ``-r``, ``-l``,
  ``-p`` und ``-t`` automatisch gesetzt; zusätzlich werden der Eigentümer
  (Option ``-o``) sowie die Gruppe (Option ``-g``) der Datei(en) beibehalten. [#]_
* Mit der Option ``-u`` werden Dateien übersprungen, wenn diese im
  Zielverzeichnis aktueller sind .

Eine originalgetreue Archivierung eines Verzeichnisses (samt Unterverzeichnissen) kann somit
folgendermaßen erreicht werden:

.. code-block:: sh

    # Verzeichnis 1:1 archivieren:
    rsync -vahz originalverzeichnis zielverzeichnis

Die Synchronisierung erfolgt mittels ``rsync`` immer in eine Richtung, also vom
Originalverzeichnis zum Zielverzeichnis. Werden im Originalverzeichnis Dateien
hinzufgefügt, so fügt ``rsync`` diese beim nächsten Aufruf auch im
Zielverzeichnis hinzu. ``rsync`` kopiert hierbei standardmäßig immer nur
diejenigen Bits, die verändert wurden (außer die Option ``-W`` wurde gesetzt, so
dass geänderte Dateien immer komplett ersetzt werden).

Soll ein Löschen einer Datei im Original-Verzeichnis bei der nächsten
Synchronisierung auch ein Löschen der entsprechenden Datei im Zielverzeichnis
zur Folge haben, kann die Option ``--delete`` verwendet werden. Diese Option
sollte allerdings mit Bedacht gewählt werden, denn damit kann ein ungewolltes
Löschen einer Datei im Original-Verzeichnis zu einem tatsächlichen Datenverlust
führen.

.. _Synchronisierung via ssh:

.. }}}

.. rubric:: Synchronisierung via ``ssh``
.. {{{

Via :ref:`SSH <SSH>` kann eine Synchronisierung auch über das Netzwerk
vorgenommen werden. Soll ein lokales Original-Verzeichnis mit einem Verzeichnis
auf einem anderen Rechner synchronisiert werden, so kann man für das
Zielverzeichnis folgende Syntax nutzen:

.. code-block:: sh

    # Verzeichnis vis SSH archivieren:
    rsync -vauhzP originalverzeichnis benutzername@rechnerip:/pfad/zum/verzeichnis

Hat man in der Datei ``~/.ssh/config`` eigene Namen für die einzelnen Rechner
vergeben, so kann auch ``benutzername@rechnername:/pfad/zum/zielverzeichnis``
als Zielverzeichnis angegeben werden. Vertauscht man die Angaben für das
Original- und Zielverzeichnis, so kann auch ein Verzeichnis auf einem entfernten
Rechner als Original-Verzeichnis für einen lokalen Backup genutzt werden.

Wird ``rsync`` zusätzlich mit den Optionen ``-e ssh --progress`` aufgerufen, so
wird explizit der Fortschritt der Übertragung ausgegeben. Diese Option ist
insbesondere für das Kopieren großer Dateien nützlich (beispielsweise
:ref:`tar <tar>`-Archiven). Zusätzlich kann beim Kopieren großer Dateien über das
Netzwerk die Option ``--partial`` nützlich sein: Wird die Netzwerkverbindung
unterbrochen, so wird damit der Transfer bei einem erneuten Aufruf von ``rsync``
nahtlos fortgesetzt. Für die Kombination von diesen beiden Optionen kann man
auch kurz die Option ``-P`` setzen.

Soll bei einer Sicherung via SSH die maximal genutzte Bandbreite beschränkt
werden, so kann dies mittels der Option ``-bwlimit=zahl`` gesetzt. Der Wert für
die maximale Bandbreite wird normalierweise in Kilobyte (kB) angegeben;
alternativ kann auch beispielsweise ``1.5m`` für eine maximale Bandbreite von
1,5 MB je Sekunde angegeben werden.

.. _Automatische Synchronisierung mittels cron:

.. }}}

.. rubric:: Automatische Synchronisierung mittels ``cron``
.. {{{

Um Daten gegenüber einem Hardware-Ausfall oder Arbeitsverzeichnisse auf einem
Desktop-PC mit einem Notebook synchron zu halten, sind automatische Backups
hilfreich. Dafür kann der Hintergrund-Dienst :ref:`cron <cron>` genutzt werden.

Eine Cron-Tabelle für den aktuellen Benutzer kann mittels ``crontab -e``
angelegt beziehungsweise editiert werden. Um beispielsweise alle fünf Minuten
ein Backup eines Verzeichnis auf einem entfernten Rechner anzulegen, kann man
folgenden Eintrag in die Cron-Tabelle hinzufügen:

::

    # Eintrag in Cron-Tabelle
    5 * * * * rsync -avhzP /home/benutzernamename/verzeichnisname \
        ssh:benutzername@zielrechner/home/benutzername/ >> /home/benutzername/rsync.log

Die Anweisung in diesem Beispiel wurde nur aus Textsatzungsgründen auf zwei
Zeilen aufgeteilt; in der Cron-Tabelle werden Zeilen-Umbrüche innerhalb eines
Eintrags nicht unterstützt. Die obige Anweisung ruft ``rsync`` wie im letzten
Abschnitt beschrieben auf, und schreibt die Ausgabe ans Ende einer Logfile. Zu
beachten ist zudem, dass die Synchronisierung wiederum nur in eine Richtung
verläuft.

Die Backup-Anweisung kann noch optimiert werden: ``rsync`` sollte nämlich nur
dann aufgerufen werden, wenn der Zielrechner auch erreichbar ist. Hierzu kann
das Programm ``nc`` genutzt werden, das via :ref:`apt <apt>` über das Paket
``netcat`` installiert werden kann:

.. code-block:: sh

    sudo aptitude install netcat

Mittels dieser Anweisung kann man folgendermaßen prüfen, ob ein Zielrechner
erreichbar ist:

.. code-block:: sh

    # Test, ob Rechner erreichbar ist:
    nc -z -w1 zielrechner 22

Durch die Option ``-z`` prüft ``nc`` nur, ob ein Dienst über den angegebenen
Port erreichbar ist (ohne irgendwelche Daten zu senden). Mit der Option ``-w1``
wird festgelegt, dass ``nc`` maximal eine Sekunde lang auf eine Antwort des
Dienstes wartet.

``nc`` selbst gibt keine Rückmeldung auf dem Bildschirm aus. Das Programm endet
jedoch mit dem :ref:`exit <exit>`-Code ``0`` (kein Fehler), wenn es erfolgreich
war, und mit dem ``1`` (Fehler), wenn es nicht erfolgreich war. In der Shell
wird dieser Exit-Code in der Variablen ``$?`` gespeichert, so dass die Bedingung
in einem Shell-Skript mit ``if [ $? -eq 0 ]`` abgefragt werden kann (siehe
:ref:`Fallunterscheidungen <Fallunterscheidungen>` in Shell-Skripten).

Für die Verwendung in Cron gibt es eine noch kompaktere Schreibweise, da die
Anweisung ja in eine einzige Zeile geschrieben werden muss:

.. code-block:: sh

    # Backup nur, wenn entfernter Rechner erreichbar:
    nc -zw1 zielrechner 22 && rsync -avzhP quelle ziel >> logdatei

Bei dieser Schreibweise wird die zweite Anweisung (``rsync``) nur ausgeführt,
wenn die erste erfolgreich war (siehe :ref:`bedingte Anweisungen <bedingte
Anweisungen>`).

.. --log-file
.. The log file is specified as ``~/backup/rsync-$(date +"%F-%I%p").log``

.. }}}

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Zu beachten ist hierbei, dass das Speichern von Dateien, deren Eigentümer
    nicht der aktuell angemeldete Benutzer ist, grundsätzlich SuperUser-Rechte
    erfordert.

    Ist hingegen der aktuell angemeldete Benutzer (sowie gegebenenfalls der
    Anmeldename bei SSH-Verbindungen) der Eigentümer aller zu sichernden
    Dateien, so kann ``rsync`` bei der Verwendung der Option ``-a`` auch ohne
    SuperUser-Rechte genutzt werden.

