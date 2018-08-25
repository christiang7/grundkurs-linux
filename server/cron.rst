
.. _cron:
.. _crontab:
.. _Cronjob:
.. _Automatisierte Anweisungen:

Automatisierte Anweisungen mit ``cron``
=======================================

Der `cron <https://wiki.ubuntuusers.de/Cron/>`__-Dienst gehört bei
Debian/Ubuntu/LinuxMint zum Standard-Umfang. Der Dienst ist also standardmäßig
aktiv, auch wenn man ihn als normaler Linux-Benutzer zunächst wohl gar nicht
bewusst wahrnimmt.

Die Anweisungen, die ``cron`` zu bestimmten Zeiten ausführen soll, werden in
einer so genannten "Crontab" abgelegt. Hierbei handelt es sich letztlich um eine
einfache Text-Datei, die allerdings eine spezielle Syntax hat. Jeder Benutzer
eines Linux-Systems, auch der SuperUser ``root``, kann eine solche Crontab
anlegen. Hierzu genügt folgende Anweisung:

.. code-block:: sh

    # Cron-Tabelle editieren:
    crontab -e

Durch die Option ``-e`` wird die entsprechende Datei mit dem Standard-Texteditor
geöffnet.

In einer Cronjob-Datei können einzelne Zeilen durch ein ``#``-Zeichen am
Zeilenbeginn auskommentiert werden; diese Zeilen werden vom Cron-Dienst
ignoriert. Alle übrigen Zeilen stellen Anweisungen dar, die zeitgesteuert
ausgeführt werden sollen.

Jede einzelne Zeile steht für eine einzelne Anweisung. Als Format muss dabei
folgende Syntax beachtet werden:

::

    minute  stunde  tag  monat  wochentag    benutzer    anweisung

    # Beispiel:

    *       *       *       *       *     benutzername   echo "Hallo Welt!" > /dev/null

Die einzelnen Spalten in einer solchen Crontab haben folgende Bedeutung:

* Mittels der ersten fünf Stellen, im obigen Beispiel jeweils mit ``*``
  gekennzeichnet, werden Zeitangaben festgelegt; die einzelnen Stellen werden
  durch (ein oder mehrere) Leerzeichen voneinander getrennt.

* Handelt es sich um eine Crontab eines normalen Benutzers, die ohne
  SuperUser-Rechte mittels ``crontab -e`` editiert wird, so entfällt die
  ``benutzer``-Spalte.

  Bei systemweit relevanten und nur mit SuperUser-Rechten veränderlichen
  Crontabs (wie beispielsweise der Datei ``/etc/crontab`` oder den in
  ``/etc/cron.d/`` abgelegten Crontabs) muss hingegen angegeben werden, von
  welchem Benutzer-Account aus die jeweilige Anweisung ausgeführt werden soll.

* Als letzter Eintrag wird in jeder Zeile die auszuführende Shell-Anweisung
  angegeben. Beinhaltet diese Leerzeichen, so muss sie in Anführungszeichen
  gesetzt werden.

Die fünf Stellen für die Zeitangaben haben folgende Bedeutung:

1. Stelle: Minuten-Angabe (``0`` bis ``59``, oder ``*`` für "in jeder Minute")
2. Stelle: Stunden-Angabe (``0`` bis ``23``, oder ``*`` für "in jeder Stunde")
3. Stelle:   Tages-Angabe (``0`` bis ``31``, oder ``*`` für "an jedem Tag")
4. Stelle:  Monats-Angabe (``1`` bis ``12``, oder ``*`` für "in jedem Monat")
5. Stelle: Wochentags-Angabe (``0`` bis ``7``, oder ``*`` für "an jedem
   Wochentag")

Bei der Angabe eines Wochentags steht ``0`` beziehungsweise ``7`` für Sonntag,
``1`` für Montag, usw. Der obige Beispiel-Eintrag würde also bedeutet, dass die
angegebene Anweisung einmal in jeder Minute ausgeführt werden würde.

Eine zusätzliche Option für die Verwendung von ``*`` ist es, beispielsweise mit
einer Minuten-Angabe von ``*/2`` eine Ausführung in jeder zweiten Minute zu
bewirken.


*Beispiele:*

* Ein Backup-Skript einmal täglich um 3:00 Uhr nachts ablaufen lassen::

      0  3  *  *  *  /path/to/my/backupscript.sh

* Jeden dritten Tag prüfen, ob neue Paket-Quellen vorhanden sind (funktioniert
  nur mit SuperUser-Rechten!)::

      0  0  */3  *  *  root  "apt update"

* Eine Erinnerung zum 1. April um 6:30 Uhr morgens als Email verschicken::

      30  6  1  4  *  (echo "Gut aufpassen!" | mail -s "April, April!" mail@adresse.de)

  (Dieser Cronjob setzt voraus, dass das Paket ``mailutils`` installiert ist.)


Cronjobs sind insbesondere für Backups sehr nützlich, beispielsweise in
Verbindung mit :ref:`rsync <Backups mittels rsync>`.

.. 2>&1 bedeutet, das sowohl die normale Ausgabe als auch Fehler 
.. in die vorher angegebene Datei umgeleitet werden.


.. Die Ausgabe der Cronjobs wird standardmässig per Mail an den jeweiligen
.. System-User der den Cronjob eingerichtet hat gesendet. Um dies zu unterdrücken,
.. könnte man die Ausgabe in eine Datei umleiten oder mit Umleitung zu /dev/null
.. komplett verwerfen:

.. Cronjob-Ausgabe in Logfile umleiten

.. 0 8,17 * * * /usr/bin/script.sh >>/var/log/cron/send_reminder_mail 2>&1

.. Cronjob-Ausgabe verwerfen

.. 0 8,17 * * * /usr/bin/script.sh >/dev/null 2>&1


.. rubric:: Links

* `Crontab Syntax und Tutorial (de)
  <https://www.stetic.com/developer/cronjob-linux-tutorial-und-crontab-syntax.html>`__
* `Cronjobs Tutorial (en)
  <https://www.sitepoint.com/a-comprehensive-crash-course-into-cronjobs/>`__

.. Test

