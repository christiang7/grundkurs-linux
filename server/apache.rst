.. index:: Webserver, Apache
.. _Apache:
.. _Apache2:
.. _Webserver:
.. _Webserver Apache:

Der Webserver ``apache``
========================
.. {{{

Ein Webserver ist ein Dienst, der eingehende HTTP-Anfragen bearbeitet und die
angeforderten Dokumente ausgibt. Meist handelt es sich bei diesen Dokumenten um
HTML-Dateien; via HTTP können allerdings auch beliebige andere Dokumente
ausgeliefert werden.

Der Webserver ``apache`` ist der weltweit am weitesten verbreitete Webserver.
Unter Debian/Ubuntu/LinuxMint kann ``apache`` (aktuellen Version 2017: 2.4)
folgendermaßen installiert werden:

.. code-block:: sh

    sudo apt install apache2 apache2-utils

Für den Webserver wird bei der Installation standardmäßig ein eigener
Benutzer-Account namens ``www-data`` und eine angelegt; der Apache-Webserver
wird mit diesem Account als Eigentümer des Prozesses automatisch gestartet (und
künftig bei jedem Systemstart automatisch geladen). Öffnet man in einem
Webbrowser die Adresse ``http://localhost``, so bekommt man eine entsprechende
Willkommens-Seite angezeigt.


Inhalte, die der Webserver ausgeben soll, werden in einem als ``document root``
bezeichneten Verzeichnis abgelegt. Bei ``apache2`` ist dieses Verzeichnis
standardmäßig ``/var/www/html/``. Die oben genannte Willkommens-Seite liegt mit
dem Namen ``index.html`` in genau diesem Verzeichnis.


Möchte man den Webserver manuell starten, stoppen, oder neu laden, so ist dies
wie üblich via :ref:`systemd <systemd>` möglich:

.. code-block:: sh

    # Webserver starten:
    sudo systemctl start apache2

    # Webserver stoppen:
    sudo systemctl stop apache2

    # Webserver neu starten:
    sudo systemctl restart apache2

Als Alternative hierzu kann auch die Anweisung ``apache2ctl`` verwendet werden.
Neben ``apache2ctl start|stop|restart`` kann man auch folgende Anweisung 
aufrufen, um die Einstellungen auf Syntax-Korrektheit zu prüfen: 

.. code-block:: sh

    # Webserver-Einstellungen prüfen:
    apache2ctl configtest

Mit ``apache2ctl graceful`` kann man die Konfigurationen neu laden, ohne den
Server beziehungsweise bestehende Verbindungen zu unterbrechen.


.. _Apache-Konfigurationsdateien:

.. }}}

Apache-Konfigurationsdateien
----------------------------
.. {{{

Die grundlegende Konfigurationsdatei für den Apache-Webserver ist die Datei
``/etc/apache2/apache2.conf``. In früheren Zeiten war dies die einzige
Konfigurationsdatei. Inzwischen wurden zwecks einer besseren Übersichtlichkeit
und Wartbarkeit einzelne Konfigurations-Teile in andere Dateien ausgelagert;
diese werden nach Bedarf mittels ``Include``-Anweisungen geladen. Beispielsweise
wird so über die Datei ``/etc/apache2/ports.conf`` festgelegt, auf welche Ports
der Apache-Server achten soll.

Die zusätzlichen Apache-Konfigurationsdateien werden üblicherweise in folgenden
Verzeichnissen abgelegt:

* ``/etc/apache2/mods-available``

    Dieses Verzeichnis enthält verfügbare Erweiterungs-Module.

* ``/etc/apache2/conf-available``

    Dieses Verzeichnis enthält verfügbare Konfigurationen.

* ``/etc/apache2/sites-available``

    Dieses Verzeichnis enthält Definitionen bezüglich verfügbarer Webseiten.


Zu jedem der drei obigen Verzeichnisse existiert unter ``/etc/apache2`` ein
entsprechendes Verzeichnis, das auf ``-enabled`` endet. In diesen Verzeichnisses
befinden sich lediglich :ref:`Symlinks <Symlink>` auf gleichnamige Dateien, die
in den zugehörigen, auf ``-available`` endenden Verzeichnissen liegen. Anstelle
die Symlinks manuell anzulegen, können folgende Anweisungen genutzt werden:

* ``a2enmod`` und ``a2dismod``

    Mit diesen beiden Anweisungen können Erweiterungs-Module aktiviert
    beziehungsweise deaktiviert werden.

* ``a2enconf`` und ``a2disconf``

    Mit diesen beiden Anweisungen können einzelne Konfigurationen aktiviert
    beziehungsweise deaktiviert werden.

* ``a2ensite`` und ``a2dissite``

    Mit diesen beiden Anweisungen können einzelne Webseiten aktiviert
    beziehungsweise deaktiviert werden.

Standardmäßig gibt es im Verzeichnis ``/etc/apache2/sites-available`` der
verfügbaren Webseiten nur zwei Einträge, nämlich ``000-default.conf`` und
``default-ssl.conf``; diese beiden Dateien enthalten Grundeinstellungen für das
Verzeichnis ``/var/www/html``. Diese ``.conf``-Dateien sollte auch so beibehalten
werden, da sie grundlegende Standard-Einstellungen beinhalten.

.. _Viruelle Hosts:

.. }}}

Viruelle Hosts
--------------
.. {{{

Ein ``apache``-Webserver kann gleichzeitig mehrere Domains hosten. Dies bedeutet
konkret, dass beispielsweise für die zwei verschiedenen Domains
``example-one.de`` und ``example-two.de`` keine zwei unterschiedlichen Server
benötigt werden. Stattdessen kommen bei ``apache`` so genannte "Virtuelle Hosts"
zum Einsatz, um mehrere eigenständige Webseiten nebeneinander nutzen zu können.

Üblicherweise wird für jeden derartigen virtuellen Host beziehungsweise eine
eigene Datei ``.conf``-Datei im Verzeichnis ``/etc/apace2/sites-available``
angelegt. Für die Beispiel-Domain ``example-one.de`` würde diese
``example-one.de.conf`` heißen. Diese kann beispielsweise folgenden Inhalt
haben:

::

    <VirtualHost *:80>

        ServerName www.example-one.de
        ServerAlias example-one.de www.example-one.de
        ServerAdmin webmaster@example-one.de

        DocumentRoot /var/www/example-one.de/
        DirectoryIndex index.html

        ErrorLog /var/log/apache2/error.log
        CustomLog /var/log/apache2/access.log combined

        <Directory /var/www/example-one.de/>
            Options +Indexes -FollowSymLinks
        </Directory>

    </VirtualHost>

Durch die Angabe von ``<VirtualHost *:80>`` wird festgelegt, dass die folgende
Konfiguration für Anfragen von beliebigen Adressen (``*``) für den HTTP-Port (``80``)
gültig ist. Die zusätzlichen Zeilen haben folgende Bedeutung:

* Über die Attribute ``ServerName`` und ``ServerAlias`` wird festgelegt, für
  welche Domain die folgenden Einstellungen relevant sind. Wird im obigen
  Beispiel der Webserver also über die Adresse ``www.example-one.de``
  kontaktiert (wahlweise mit oder ohne anfängliches ``www``), so wird der Inhalt
  des als ``DocumentRoot`` bezeichneten Verzeichnisses ausgegeben. Befindet sich
  in diesem Verzeichnis eine Datei namens ``index.html``, so wird diese
  automatisch geladen. [#]_

* Über die Einstellung ``ServerAdmin`` wird eine Email-Adresse angegeben, über
  die der Betreuer der Webseite für Rückfragen erreichbar ist. Eine
  Email-Adresse der Art ``webmaster@domain-name.tld`` hat sich dabei als
  Standard etabliert (TLD wird häufig als allgemeines Kürzel für den Begriff
  "Top-Level-Domain" verwendet, also beispielsweise für ``.de``, ``.com``,
  ``.org``, ``.net``, usw.). Damit eine Email-Adresse dieser Art funktioniert,
  muss neben dem Webserver auch ein :ref:`Mailserver <Mailserver>`  installiert
  werden.

* Mittels den Einstellungen für ``ErrorLog`` und ``CustomLog`` wird festgelegt,
  in welchen Dateien auftretende Fehler beziehungsweise Zugriffe auf den
  virtuellen Host protokolliert werden sollen. Neue Einträge in diesen Dateien
  kann beispielsweise mittels :ref:`tail -f <tail>` in einem separaten
  Shell-Fenster im Blick behalten.

.. _Directory-Einstellungen:

* Durch die ``Directory``-Einstellung werden zusätzliche Optionen festgelegt,
  die ausschließlich für das angegebene Verzeichnis gelten. Durch die Option
  ``+Indexes`` wird festgelegt, dass beim Aufruf eines Verzeichnisses (einer
  Webadresse, die mit ``/`` endet) eine Liste aller sich darin befindenden
  Dateien ausgegeben wird, sofern darin keine der mittels der Option
  ``DirectoryIndex`` definierten Dateien existiert. Das Plus-Zeichen ist bei der
  Angabe von ``+Indexes`` optional; soll andernfalls eine Auflistung des
  Ordnerinhalts unterdrückt werden, so ist dies mittels der Option ``-Indexes``
  möglich.

  Diese Art der Aktivierung beziehungsweise Deaktivierung einzelner Optionen
  funktioniert auch mit weiteren Einstellungs-Möglichkeiten, beispielsweise:

  - Mit ``AllowOverride`` wird festgelegt, ob einzelne Verzeichnis-Einstellungen
    durch so genannte :ref:`Access-Files <Access-Files>`  dezentral
    überschrieben werden dürfen. Standardmäßig ist dies seit der Apache-Version
    2.4 nicht erlaubt. Mit ``AllowOverride All`` wird eine Änderung aller `hier
    <http://httpd.apache.org/docs/2.4/de/mod/core.html#allowoverride>`__
    beschriebenen Einstellungen mittels Access-Files ermöglicht, mit
    ``AllowOverride AuthConfig Indexes`` dürfen nur die Zugriffs-Einschränkungen
    für Ordner-Inhalte/Dateien und Verzeichnis-Listen dezentral geändert werden,
    um beispielsweise einen Passwort-Schutz für einzelne Bereiche einer Webseite
    zu ermöglichen.

  - Mit ``FollowSymlinks`` wird festgelegt, ob :ref:`Symlinks <Symlinks>` in
    Web-Verzeichnissen erlaubt sind. Ist diese Option erlaubt, so können auch
    Dateien oder Verzeichnisse außerhalb des mit ``DocumentRoot`` festgelegten
    Verzeichnisses mittels Verlinkungen angezeigt/abgerufen werden.
    Standardmäßig ist dies erlaubt.

  - Mit ``ExecCGI`` wird das Ausführen von CGI-Skripten erlaubt. Standardmäßig
    ist dies nicht erlaubt.


Eine vollständige Liste mit allen derartigen Einstellungs-Möglichkeiten
("Direktiven") gibt es  `hier
<http://httpd.apache.org/docs/2.4/de/mod/core.html>`__ beziehungsweise `hier
<http://httpd.apache.org/docs/2.4/de/mod/quickreference.html>`__

.. http://httpd.apache.org/docs/2.4/de/vhosts/

Um den im obigen Beispiel definierten virtuellen Host zu aktivieren, würde man
``sudo a2ensite example-one.de.conf`` angeben. Hierdurch legt der Apache-Server
automatisch einen entsprechenden symbolischen Link in das
``sites-enabled``-Verzeichnis an. Schließlich müssen die Konfigurations-Dateien
noch neu geladen werden:

.. code-block:: sh

    # Webserver-Konfigurationen neu laden:
    sudo system reload apache2

Für weitere Domains können entsprechende ``.conf``-Dateien angelegt und
aktiviert werden.

.. AllowOverwrite: Damit wird erlaubt, dass Optionen mittels
.. ``.htaccess``-Dateien überschrieben werden.

.. Servername ?

.. _Certbot:
.. _SSL-Zertifikate:

.. }}}

SSL-Zertifikate
---------------
.. {{{

Es wird zunehmend zum Standard, dass Webseiten nicht über ``http://adresse``,
sondern über ``https://adresse`` angesprochen werden. Dieser Unterschied bringt
eine Verschlüsselung der übertragenen Daten mit sich, setzt allerdings auf der
Server-Seite ein valides SSL-Zertifikat voraus.

Eine Möglichkeit, ein solches Zertifikat zu erhalten, besteht darin, sich selbst
eines mittels ref:`openssl <OpenSSL>` auszustellen. Dies hat allerdings den
Nachteil, dass dies von nahezu allen Browsern als unsicher eingestuft wird, da
keinen externe Instanz die Echtheit des Zertifikats bestätigen kann. Wesentlich
besser ist es in diesem Fall, ein (kostenloses) Zertifikat über das `Let's
Encrypt <https://de.wikipedia.org/wiki/Let's_Encrypt>`-Projekt zu erhalten, das
seit einigen Jahren von der `EFF
<https://de.wikipedia.org/wiki/Electronic_Frontier_Foundation>`__ (Electronic
Frontier Foundation) getragen wird. Dies gelingt am einfachsten durch die
Verwendung des so genannten "Certbots".

Für die Installation von ``certbot`` gibt es `hier
<https://certbot.eff.org/all-instructions/>`__ eine ausführliche Liste mit
Installations-Anleitungen für verschiedene Linux-Systeme.

* Um ``certbot`` auf einem System mit Ubuntu 16.04 Xenial zu installieren, muss
  man das Entwickler-Paket (PPA) des Certbot-Teams hinzufügen. Dafür gibt man
  folgende Anweisungen ein:

  .. code-block:: sh

      sudo aptitude update
      sudo aptitude install software-properties-common

      sudo add-apt-repository ppa:certbot/certbot
      sudo aptitude update

  Anschließend kann ``certbot`` folgendermaßen installiert werden:

      sudo aptitude install python3-certbot-apache

* Für Debian 9 (Stretch) gibt es momentan (Stand: Feb. 2018) noch kein
  Repository. Man kann allerdings weiterhin das entsprechende Repository aus der
  Vorgänger-Version nutzen, indem man folgende Zeile in die Datei
  ``/etc/apt/sources.list`` hinzufügt::

      deb http://ftp.debian.org/debian stretch-backports main

  Anschließend kann ``certbot`` folgendermaßen installiert werden:

  .. code-block:: sh

      sudo aptitude -t stretch-backports install python-certbot-apache


Nach der Installation kann man ``certbot`` aufrufen:

.. code-block:: sh

    # Zertifikate einrichten:
    sudo certbot --apache

Es erscheint ein kurzer Abfrage-Dialog. In diesem muss einerseits den
Nutzungsbedingungen zustimmen, andererseits muss eine Email-Adresse angegeben
werden, an die bei Bedarf Fehlermeldungen geschickt werden können.
Einer Weitergabe der Email-Adresse an die EFF muss man nicht zustimmen.
Schließlich muss man noch auswählen, für welche (in Apache bereits aktivierte
und über das Internet zugängliche) Domain das Zertifikat ausgestellt werden
soll. Bei der Nachfrage, ob ``http``-Anfragen künftig automatisch in
``https``-Anfragen umgewandelt werden sollen ("Redirect"), ist es empfehlenswert
"Ja" auszuwählen.

Mit der obigen Anweisung erledigt ``certbot`` den Rest automatisch: Es erstellt
zur ``.conf``-Datei einer Domain / eines virtuellen Hosts im Verzeichnis
``/etc/apache2/sites-available`` automatisch eine gleichnamige Datei, die
allerdings auf ``le-ssl.conf`` endet und fügt die notwendigen Ergänzungen ein.
Anschließend ruft ``certbot`` automatisch ``a2ensite`` auf und lädt die neuen
Einstellungen für den Apache-Server neu. Für spezielle Anwendungsfälle hilft die
englischsprachige `Original-Anleitung
<https://certbot.eff.org/docs/using.html>`__ weiter.

Die von Let's Encrypt bereitgestellten Zertifikate haben eine Gültigkeitsdauer
von 90 Tagen. ``certbot`` richtet daher mit dem obigen Aufruf automatisch auch
einen :ref:`Cronjob <Cronjob>` ein, mit dem das Zertifikat beziehungsweise die
Zertifikate automatisch erneuert werden. Davon kann man sich in der neu
angelegten Datei ``/etc/cron.d/certbot`` selbst überzeugen; manuell können
Zertifikate mittels ``sudo certbot renew`` erneuert werden.

.. _Access-Files:
.. _Zugriffs-Beschränkungen mittels Access-Files:

.. }}}

Zugriffs-Beschränkungen mittels Access-Dateien
----------------------------------------------
.. {{{

Die Apache-Standard-Einstellungen erlauben grundsätzlich den Zugriff auf
alle Dateien des mit der Einstellung ``DocumentRoot`` festgelegten
Verzeichnisses einer Webseite. Möchte man diese Zugriffsmöglichkeiten einschränken
und beispielsweise ein Unterverzeichnis nur nach Eingabe eines Passworts
zugänglich machen, so können hierfür so genannte "Access-Dateien" genutzt
werden. Derartige Dateien haben oftmals den Namen ``.htaccess``.

Eine ``.htaccess``-Datei kann beispielsweise folgenden Inhalt haben:

.. code-block:: bash

    AuthUserFile /var/www/verzeichnis-der-zieldomain/.htpasswd
    AuthName "Bitte Benutzername und Passwort eingeben!"
    AuthType Basic

    Require valid-user

Eine solche Datei kann einfach mittels eines Text-Editors angelegt werden.
Um die zugehörige Passwort-Datei ``.htpasswd`` zu erstellen, muss hingegen das
Programm ``htpasswd`` (aus dem ``apache2-utils``-Paket) verwendet werden. Eine neue
``.htpasswd``-Datei kann folgendermaßen im aktuellen Verzeichnis erstellt werden:

.. code-block:: sh

    # Passwort-Datei .htpasswd erstellen:
    htpasswd -c .htpasswd BENUTZERNAME

Als Benutzername muss hierbei ein Name angegeben werden, mit dem künftig ein
Login im Passwort-geschützten Bereich möglich sein soll; anschließend muss das
zugehörige Passwort zweimal eingegeben werden. 

Soll ein Login auch mit einem anderen Benutzernamen-/Passwort-Paar möglich sein,
so kann man wie oben ``htpasswd`` aufrufen, allerdings ohne die Option ``-c``:
Diese Option steht für "create, erzeugt also jedes mal eine neue Datei. Ist
diese Option hingegen nicht aktiv, so wird ein zusätzlicher Benutzer-Eintrag der
bestehenden Datei hinzugefügt.

Sofern in den Apache-Einstellungen für die Ziel-Domain, genauer gesagt den
dortigen :ref:`Directory-Einstellungen <Directory-Einstellungen>` die Option
``AllowOverride AuthConfig`` gesetzt ist, so genügt es, die beiden Dateien
``.htaccess`` und ``.htpasswd`` in das künftig passwortgeschützte
Zielverzeichnis zu kopieren; die Pfad-Einstellung in der Datei ``.htaccess``
muss dabei mit dem dem Zielverzeichnis übereinstimmen. 

Der Vorteil dieser Methode liegt insbesondere darin, dass ein Webhosting-Nutzer
auf diese Weise Änderungen an den Zugriffs-Optionen vornehmen kann, ohne
selbst den Apache-Server modifizieren zu können. Ist man selbst der Betreiber
des Webservers, so kann die ``.htpasswd``-Datei auch in einem separaten
Verzeichnis, sogar außerhalb des ``DocumentRoots`` der Domain abgelegt und
von mehreren ``.htaccess``-Dateien gleichzeitig genutzt werden -- dazu brauchen
lediglich die Pfad-Angaben für die ``AuthUserFile`` angepasst werden.

.. }}}

... to be continued ...


.. configs usw: /etc/letsencrypt

.. Module: http://httpd.apache.org/docs/2.4/de/mod/


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Damit eine Browser-Anfrage für ``www.example-one.de`` überhaupt beim
  richtigen Webserver ankommt, muss diese Domain bei einem Domain-Anbieter
  (beispielsweise `do.de <https://www.do.de/>`__ oder `netcup.de <https://www.netcup.de>`__)
  registriert und die IP-Adresse des Webservers als Ziel-IP-Adresse angegeben
  werden.

