.. index:: Systemd, systemctl
.. _systemd:
.. _System-Manager:

Der System-Manager ``systemd``
==============================

Bei `systemd <https://wiki.ubuntuusers.de/systemd/>`__ handelt es sich um einen
Sitzungs-Manager (ein "Init"-System), der für die Verwaltung aller laufenden
Dienste zuständig ist. Mittels ``systemd`` können Dienste also gestartet,
gestoppt, oder neu geladen werden; ebenso kann der aktuelle Status eines
Dienstes ausgegeben werden, oder festgelegt werden, ob ein Dienst automatisch
beim Booten des Computers gestartet werden soll.

Da ``systemd`` bei Debian/Ubuntu/LinuxMint seit einiger Zeit das Standard-System
zur Dienste-Verwaltung ist, muss kein zusätzliches Paket installiert werden.

In einem Shell-Fenster kann ``systemd`` mittels der Anweisung ``systemctl``
gesteuert werden; üblicherweise sind dabei SuperUser-Rechte erforderlich.
Die allgemeine Syntax lautet:

.. code-block:: sh

    systemctl <ANWEISUNG> <DIENST>

``systemctl`` kennt folgende Anweisungen:

* ``start``
      Hiermit wird der angegebene Dienst gestartet.
* ``stop``
      Hiermit wird der angegebene Dienst gestoppt.
* ``reload``
      Hiermit werden die Konfigurationen des Dienstes neu geladen.
* ``restart``
      Hiermit wird der angegebene Dienst gestoppt und anschließend neu gestartet.
* ``status``
      Hiermit wird der Status des angegebenen Dienstes angezeigt.
* ``enable``
      Hiermit wird der Dienst künftig beim Booten automatisch gestartet.
* ``disable``
      Hiermit wird der Dienst künftig beim Booten nicht gestartet.

Zusätzlich kann mittels ``systemctl is-enabled dienstname`` geprüft werden, ob
ein Dienst automatisch beim Systemstart geladen wird.

Manche Dienste, wie beispielsweise der :ref:`Apache <Apache>`-Webserver, stellen
eigene Init-Skripte zum Starten und Stoppen des Dienstes bereit; man kann den
Dienst dann wahlweise mittels dieser Anweisungen oder auch mittels ``systemctl``
steuern.


.. _hostnamectl:
.. _localectl:
.. _timedatectl:
.. _hostnamectl, localectl und timedatectl:

.. rubric:: hostnamectl, localectl und timedatectl


``systemd`` bietet neben der Anweisung ``systemctl`` noch weitere Hilfsprogramme
zur Einstellung des Rechnernamens ("Hostname"), der System-Sprache und der
Zeitzone. Führt man die Anweisungen ``hostnamectl``, ``localectl``
beziehungsweise ``timedatectl`` ohne weiteren Argumente/Optionen aus, so bekommt
man jeweils die aktuellen System-Einstellungen angezeigt.

* Mit ``sudo hostnamectl set-hostname neuername`` kann der Rechnername
  (Hostname) neu festgelegt werden.

* Mit ``timedatectl list-timezones`` werden alle Zeitzonen aufgelistet, die
  eingestellt werden können. Für Mitteleuropa ist dies beispielsweise
  ``Europe/Berlin``. Um die Zeitzone des Rechners neu festzulegen, kann man
  beispielsweise folgende Zeile eingeben:

  .. code-block:: sh

      sudo timedatectl set-timezone Europe/Berlin

* Mit ``localectl list-locales`` werden alle Locale-Varianten aufgelistet, die
  auf dem System verfügbar sind und somit eingestellt werden können. Diese
  Einstellungen betreffen einerseits die Sprache und Zeichenkodierung, in der
  beispielsweise Menü-Einträge von Programmen oder System-Rückmeldungen
  angezeigt werden, und andererseits den Tastatur-Zeichensatz.

  Um die System-Sprache auf "Deutsch" einzustellen, kann man beispielsweise
  folgendes eingeben:

  .. code-block:: sh

      sudo localectl set-locale "LANG=de_DE.utf8"

  Der Zeichensatz "utf8" hat sich seit einigen Jahren als Standard etabliert;
  mit ihm werden auch Umlaute und andere Sonderzeichen problemlos dargestellt.

  Um zusätzliche Locale-Varianten nutzen zu können, sollte folgende Anweisung
  aufgerufen werden:

  .. code-block:: sh

      sudo dpkg-reconfigure locales

  In dem erscheinenden Menü können zusätzliche Locale-Varianten markiert werden;
  diese werden anschließend automatisch eingerichtet. Zusätzliche Sprachpakete
  müssen bei Bedarf manuell installiert werden; eine Liste möglicher Pakete
  bekommt man mittels ``aptitude search language-pack`` angezeigt.


.. Journaling!


.. https://wiki.ubuntuusers.de/systemd/Units/
.. https://wiki.ubuntuusers.de/systemd/systemctl/

