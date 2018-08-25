.. index:: Mailserver
.. _Mailserver:

Mailserver mit ``postfix`` und ``dovecot``
==========================================
.. {{{

Mittels eines Mailservers kann ein Rechner Emails empfangen, in Mailboxen
beziehungsweise Mailverzeichnisse ablegen oder an andere Rechner weiterleiten.
Auch ein Versenden von Emails funktioniert nicht ohne Mailserver.

Ein Mailserver ist ein verhältnismäßig komplexer Dienst:

* Sollen Emails an andere Rechner verschickt werden, ist unter anderem eine
  Namens-Auflösung der Zieldomain nötig. Ein Mailserver muss somit mit einem
  DNS-Server zusammenarbeiten können.

* Möchte beispielsweise ein Benutzer Emails abrufen, so muss eine
  Benutzer-Authentifizierung erfolgen. Das Passwort sollte nicht im Klartext
  übertragen werden, so dass SSL/TLS-Verschlüsselungen sowie SSH-Zertifikate
  benötigt werden.

* Zum Abholen der Emails sind die Protokolle IMAP und POP3 üblich. Ein
  Mailserver muss also mit unterschiedlichen Protokollen funktionieren.


Zusätzlich kommen bei einem Mailserver häufig zusätzliche Werkzeuge zum Einsatz,
wie beispielsweise Spamfilter, Web-Frontends, oder auch Programme zum Verwalten
von Mailing-Listen.

Um nicht als möglicher Spam-Roboter angesehen zu werden, laufen über das
Internet zugängliche Mailserver fast ausschließlich auf Rechnern, die eine feste
IP-Adresse haben. Möchte man als Privatperson einen solchen Mailserver
aufsetzen, ist das Anmieten eines VServers die wohl einfachste und günstigste
Möglichkeit.

Im folgenden wird knapp beschrieben, wie ein eigener Mailserver mittels der genannten
Programme ``postfix`` und ``dovecot`` aufgebaut werden kann. [#]_


.. index:: Postfix
.. _Postfix:

.. }}}

Postfix
-------
.. {{{

`Postfix <https://wiki.ubuntuusers.de/Postfix/>`__ ist ein so genannter "Mail
Transfer Agent" (MTA). Ein solcher Dienst übernimmt den Transport von Emails
zwischen verschiedenen Mailservern. Das wichtigste Protokoll, mit dem Emails
zwischen verschiedenen Rechnern ausgetauscht werden, heißt SMTP.

Postfix wird meist auf eine der folgenden zwei Arten genutzt:

* Als "lokaler" Mailserver, der Mails innerhalb eines lokalen Netzwerkes
  zustellt. Damit können beispielsweise auftretende Fehlermeldungen an die
  zentrale Mailbox des Systemadministrators weitergereicht werden.

  Manche Server-Dienste wie beispielsweise Samba setzen einen zumindest lokal
  arbeitenden Mailserver voraus.

* Als "richtiger" Mailserver, der zum Empfangen und Versenden von Emails über
  das Internet gedacht ist. Ein Mailserver dieser Art sollte unbedingt auf einem
  Server mit einer festen IP-Adresse laufen, da ansonsten verschickte Emails von
  anderen Email-Providern meist als Spam klassifiziert werden.

  Üblicherweise wird ein solcher Mailserver in Kombination mit einem Webserver
  wie :ref:`Apache <Apache>` betrieben, um im Rahmen des Webhostings einer
  Domain nicht nur eine Webseite auszuliefern, sondern für diese Domain auch
  eigene Email-Adressen zu definieren. In diesem Fall ist es sinnvoll, zunächst
  Webserver-Einstellungen der Domain vorzunehmen.

Zusätzlich kann Postfix auch als Backup-Server verwendet werden, um im Falle
eines Ausfalls des Hauptservers Emails anzunehmen, zwischenzuspeichern und an
den Hauptserver weiterzuleiten, sobald dieser wieder einsatzbereit ist.

.. _Installation und Erst-Konfiguration:

.. }}}

Installation und Erst-Konfiguration
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

Postfix kann via :ref:`aptitude <aptitude>` folgendermaßen installiert werden:

.. code-block:: sh

    sudo aptitude install postfix

Im Rahmen der Installation wird gefragt, wie der Mailserver agieren soll, und
welche anderen grundlegenden Einstellungen gesetzt werden sollen:

* Soll Postfix als "richtiger" Mailserver und nicht nur lokal genutzt werden, so
  ist "Internet-Site" die richtige Wahl.

* Bei dieser Auswahl muss man als nächstes den Haupt-Domain-Namen angeben, für
  den Postfix konfiguriert werden soll; dieser lautet beispielsweise
  ``example-one.de``.

* Als Empfänger für Emails an ``Root`` wäre in diesem Fall
  ``webmaster@example-one.de`` üblich; diese Adresse kann später auch auf eine
  Adresse bei einem anderen Email-Provider umgeleitet werden.

* Als Liste der Rechner, für die Postfix zuständig sein soll, gibt man für
  dieses Beispiel ``example-one.de, localhost`` ein.

* Eine synchrone Aktualisierung der Email-Warteschlangen soll erzwungen werden,
  damit keine Emails verloren gehen können; somit sollte man bei dieser Frage
  "Ja" wählen.

* Die Einstellungen bezüglich der lokalen Netze können beim Vorgabe-Wert
  belassen werden, beispielsweise ``127.0.0.0/8`` für ``localhost`` (IPv4).

* Auch die maximale Postfachgröße kann beim Standardwert ``0`` für unbegrenzt
  große Postfächer belassen werden, ebenso das Zeichen ``+`` für lokale
  Adress-Erweiterungen.

* Bei der Frage, welche Internet-Protokolle genutzt werden sollen, kann man
  wahlweise ``alle`` oder ``IPv4`` wählen. Im ersten Fall werden auch
  ``IPv6``-Adressen unterstützt, meistens ist allerdings eine Betrieb mit
  IPv4-Adressen ausreichend.

.. nur, wenn Procmail installiert ist?
.. Möchten Sie procmail zur lokalen E-Mail-Zustellung nutzen? JA

Ist noch keine Domain mit Apache konfiguriert worden, so werden nicht alle
obigen Einstellmöglichkeiten abgefragt. Die Basis-Konfiguration kann dann auch
zu einem späteren Zeitpunkt vorgenommen beziehungsweise beliebig oft wiederholt
werden. Hierzu gibt man folgendes ein:

.. code-block:: sh

    # Basis-Konfiguration vornehmen:
    sudo dpkg-reconfigure postfix

Der Mailserver wird nach der Installation automatisch gestartet und künftig bei
jedem Systemstart automatisch geladen.

Für Postfix stellt jeder Benutzer-Account, den es auf dem System gibt, einen
validen Empfänger beziehungsweise Sender von Emails dar. Wird beispielsweise
eine Email an ``benutzername`` geschickt, so wird diese standardmäßig in der
Datei ``/var/mail/banutzername`` abgelegt. Auch System-Accounts wie ``www-data``
können mit Postfix Emails verschicken und theoretisch auch empfangen. Wurde
bereits mit Apache eine Webdomain eingerichtet, beispielsweise
``example-one.de``, so sind automatisch auch Email-Adressen der Form
``benutzername@example-one.de`` gültig.

.. }}}

Die Konfigurationsdatei ``main.cf``
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{
.. {{{

Postfix wird im Wesentlichen über die Datei ``/etc/postfix/main.cf``
konfiguriert. Hierbei gibt es allgemein folgende Regeln zu beachten:

* Alle Einstellungen werden gemäß der Syntax ``variable = wert`` festgelegt. Die
  Angabe von ``wert`` kann sich dabei auch über mehrere Zeilen erstrecken, wobei
  ab der zweiten Zeile alle Angaben eingerückt sein müssen (üblicherweise mit
  vier Leerzeichen).

* Wurde der Wert einer bestimmten Variablen so festgelegt, kann man diesen Wert
  anschließend "wiederverwenden", also einer anderen Variablen zuweisen, indem
  man die Syntax ``weitere_variable = $variable`` verwendet. Vor den Namen der
  ursprünglichen Variablen muss also lediglich ein ``$``-Zeichen gesetzt werden,
  die neue Variable bekommt dann den selben Wert zugewiesen.

* Soll eine externe Liste ("Lookup-Tabelle") als Wert zugewiesen werden, so
  lautet die Syntax hierfür ``variable = type:dateiname``. Mit ``type`` wird
  angegeben, in welcher Form die tabellarischen Daten vorliegen. Mit
  ``dateiname`` wird der Name der externen Datei angegeben, aus der die Daten
  gelesen werden sollen.

Ein häufiger Datentyp für tabellarische Daten ist ``hash``. Wird dieser Datentyp
angegeben, so hängt Postfix automatisch die Endung ``.db`` an den angegebenen
Dateinamen an: Diese Endung steht für das binäre Datenbank-Format
"Berkeley Database"; durch die Verwendung binär gespeicherter Daten arbeitet
Postfix schneller als das Vorgänger-Programm ``sendmail``. Wichtig sind
derartige tabellarische Daten beispielsweise für :ref:`Alias-Definitionen
<Postfix-Alias>`.

Nach der im vorherigen Abschnitt beschriebenen Erst-Konfiguration hat die Datei
``/etc/postfix/main.cf`` etwa folgenden Inhalt, der an dieser Stelle lediglich
bezüglich der Kommentare abgeändert wurde:

.. code-block:: sh

    # smtpd_banner gibt den Text an, mit dem sich Postfix
    # gegenüber anderen MTAs ausgibt:
    smtpd_banner = $myhostname ESMTP $mail_name (Debian/GNU)

    # mydomain sollte den Namen der eigenen Domain beinhalten:
    mydomain = example-one.de

    # myhostname sollte als Wert den Hostnamen des Servers haben.
    # Dieser kann über die Shell-Anweisung hostnamectl angezeigt
    # bzw. mit hostnamectl set-hostname angepasst werden.
    myhostname = $mydomain

    # myorigin gibt den Domain-Namen für lokale E-Mails an, die ohne
    # explizite Domain-Angabe versendet werden. myorigin sollte mit
    # myhostname übereinstimmen. In der Datei /etc/mailname sollte also
    # als einziger Eintrag der richtige Hostname des Servers stehen!
    myorigin = /etc/mailname

    # mydestination gibt Domain-Namen an, für die eingehende Emails
    # in ein lokales Postfach gespeichert werden sollen.
    # (Postfix ist also für die hier angegebe(n) Domain(s)
    # als Zieldomain eingehender Emails verantwortlich)
    mydestination = $mydomain, localhost

    # relayhost gibt Domain-Namen oder IP-Adressen an, an die Emails
    # weitergeleitet werden sollen, die nicht für eine lokale Zustellung
    # vorgesehen sind. Sicherheitshalber sollten Email-Weiterleitungen
    # ("Relaying") an andere Hosts deaktiviert werden:
    relayhost =

    # mynetworks gibt an, von welchen Adressen Emails ohne
    # Authentifizierung versendet werden dürfen. Ein solcher
    # Versand sollte nur aus dem lokalen Netzwerk erlaubt sein:
    mynetworks = 127.0.0.0/8

    # biff ist ein Dienst, der lokale Benutzer über neue Mails informiert.
    # Ohne Verknüpfung von lokalen Accounts mit den Mail-Accounts ist dies
    # überflüssig:
    biff = no

    # Keine Größen-Beschränkungungen für lokale Email- und Postfach-Größen:
    mailbox_size_limit = 0

    # E-Mail-Empfang über alle Netzwerkschnittstellen aktivieren:
    # (Änderungen dieser Parameter erfordern einen Neustart von Postfix!)
    inet_interfaces = ipv4
    inet_protocols = ipv4

    # Keine automatische Domain-Vervollständigung von Email-Adressen:
    # (Dies ist höchstens Aufgabe der Mail-Clients)
    append_dot_mydomain = no

    # Allgemeine Parameter:
    recipient_delimiter = +
    readme_directory = no

    # Kompatibilitäts-Modus (Standard):
    compatibility_level = 2

    # Ort der Alias-Datei:
    alias_maps = hash:/etc/aliases
    alias_database = hash:/etc/aliases

    # TLS Verschlüsselungs-Parameter:
    smtpd_tls_cert_file=/etc/ssl/certs/ssl-cert-snakeoil.pem
    smtpd_tls_key_file=/etc/ssl/private/ssl-cert-snakeoil.key
    smtpd_use_tls=yes
    smtpd_tls_session_cache_database = btree:${data_directory}/smtpd_scache
    smtp_tls_session_cache_database = btree:${data_directory}/smtp_scache

    smtpd_relay_restrictions = permit_mynetworks
        permit_sasl_authenticated
        defer_unauth_destination

Werden Änderungen an der Konfigurations-Datei ``main.cf`` (oder in seltenen
Fällen auch der ``master.cf``) vorgenommen, so müssen die Einstellungen neu
geladen werden. Ratsam ist es, vor dem Neu-Laden der Konfigurationsdatei(en)
erst sicher zu gehen, dass diese keine Syntax-Fehler enthalten:

.. code-block:: sh

    # Syntax-Check für Konfigurationsdateien:
    postfix check

    # Mailserver-Konfigurationen neu laden:
    sudo systemctl reload postfix

Für weitere Einstellungen kann man beispielsweise einen Blick in die ausführlich
kommentierte Beispiel-Datei werfen, die standardmäßig unter
``/usr/share/postfix/main.cf.dist`` abgelegt ist. Dies ist empfehlenswert, da
die Datei einen guten Überblick über wichtige Einstellungsmöglichkeiten bietet.
Einen Überblick über *alle* Einstellungsmöglichkeiten mitsamt kurzen
Beschreibungen gibt es `hier <http://www.postfix.org/postconf.5.html>`__.

Die Einstellungen, die in Postfix nach einer neuen Installation standardmäßig
aktiv sind, können folgendermaßen angezeigt werden:

.. code-block:: sh

    # Standard-Einstellungen von Postfix anzeigen:
    postconf -d

Aus einer Shell heraus können einzelne Einstellungen auch mittels ``postconf -e
variable = wert`` vorgenommen werden; Postfix berücksichtigt dabei Änderung
automatisch. Sobald die grundlegenden Einstellungen getätigt sind und der
Mailserver "in Betrieb" ist, ist es ohnehin empfehlenswert, Änderungen nur
schrittweise vorzunehmen und dabei (beispielsweise mittels :ref:`tail <tail>`)
anhand möglicher Warnungen oder Fehlermeldungen in den Dateien
``/var/log/mail.warn`` beziehungsweise ``/var/log/mail.err`` zu testen, ob der
Mailserver auch weiterhin fehlerfrei funktioniert; mit ``postqueue -p`` erhält
man bei Bedarf eine Liste aller Emails, die zwar versendet werden sollen, aber
(aus welchem Grund auch immer) noch nicht versendet werden konnten.

Nach einer erfolgreichen Konfiguration des Mailservers ist auch ein Backup der
Konfigurationsdateien empfehlenswert (beispielsweise mittels :ref:`tar
<tar-Backup>`).

.. _Alias-Dateien:
.. _Postfix-Alias:

.. }}}

.. rubric:: Alias-Dateien
.. {{{

Wie bereits erwähnt, gibt es für jeden Benutzer-Account eine eigene valide
Email-Adresse namens ``accountname@domainname``. Üblicherweise möchte man
für eine Domain allerdings Email-Adressen haben, die nicht mit den Namen der
Benutzer-Accounts übereinstimmen; andererseits sollen möglicherweise mehrere
Email-Adressen für einen Benutzer möglich sein.

Dies ist durch Verwendung von so genannten Alias-Dateien möglich. Standardmäßig
achtet Postfix bei der Zustellung von Emails an lokale Konten auf die Datei
``/etc/aliases``. In dieser Alias-Datei werden zeilenweise neue Emailnamen für
existierende Benutzer-Accounts definiert, wobei die Syntax ``aliasname:
benutzername`` lautet. Wie das folgende Beispiel zeigt, sind hiermit auch
Mehrfach-Umleitungen möglich:

::

    # /etc/aliases
    mailer-daemon: postmaster
    postmaster: root
    webmaster: root
    www: root
    security: root

    # Weiterleitung an externe Adresse:
    root: externe-email@adresse.de

Diese Einstellungen würden bedeuten, dass Emails an ``mailer-daemon@domainname``
zunächst an das Konto ``postmaster`` weitergeleitet würden, welches wiederum als
Alias für das ``root``-Konto definiert ist. Ebenso können Alias-Namen der Art
``vorname.nachname`` eingetragen und mit dem Konto eines "normalen" Benutzers
verknüpft werden. Ebenso können, jeweils mit einem Komma und einem Leerzeichen
getrennt, auch mehrere Benutzer-Namen für ein Alias angegeben werden: Somit
könnte man beispielsweise mit ``support: user1, user2`` erreichen, dass zwei
Benutzer zugleich über Support-Anfragen benachrichtigt werden.

Um aus diesen Daten eine für Postfix lesbare, binäre ``.db``-Datenbank zu erstellen,
muss noch folgende Anweisung ausgeführt werden:

.. code-block:: sh

    # Alias-Datenbank erstellen/aktualisieren:
    sudo newaliases

    # Oder:
    sudo postaliases aliases

Die erste Anweisung existiert noch aus Kompatibilitäts-Gründen zum
Postfix-Vorgängerprogramm ``sendmail``; die zweite Anweisung arbeitet identisch,
kann allerdings gezielt auf einzelne Alias-Dateien angewendet werden und bei
Bedarf auch andere Datenbank-Varianten generieren. Änderungen, die sich durch
diese beiden Anweisungen ergeben, bekommt Postfix automatisch mitgeteilt (auch
im laufenden Betrieb).

In der Datei ``main.cf`` gibt die Variable ``alias_maps`` an, welche
Alias-Dateien von Postfix beachtet werden sollen. Die Einstellung
``alias_database`` gibt an, welche Alias-Dateien durch einen Aufruf von
``newaliases`` generiert beziehungsweise aktualisiert werden sollen.


.. _Virtuelle Domains:

.. }}}

.. rubric:: Virtuelle Domains
.. {{{

Über die Variable ``mydestination`` wird angegeben, für welche Domain(s) der
Mailserver die Zieladresse ist. Im obigen Beispiel wurde nur ``example-one.de``
als Domain angegeben, es können allerdings auch, jeweils durch ein Komma und
Leerzeichen getrennt, mehrere Domains angegeben werden, beispielsweise
``mydestination = example-one.de, example-two.de``:

::

    # Domain-Einstellung für einen gemeinsamen Benutzer:
    mydestination = localhost, example-one.de, example-two.de

In diesem Fall werden alle angegebenen Domains als Synonyme betrachtet: Gibt es
beispielsweise eine Email-Adresse ``info@example-one.de``, weil ein Benutzer
namens ``info`` existiert oder ein :ref:`Alias <Postfix-Alias>`  für ``info``
eingerichtet wurde, so werden Emails, die an ``info@example-two.de`` geschrieben
werden, an der selben Stelle abgelegt (standardmäßig in der Datei
``/var/mail/benutzername``). Dies kann sinnvoll sein, wenn eine Domain mit
verschiedenen Top-Level-Domains (TLDs) reserviert wurde, beispielsweise
``exampe-one.de`` und ``example-one.net``, beide Domains also gleichartig
konfiguriert sind und von der selben Person betreut werden.

Sind allerdings Emails an ``info@example-two.de`` und ``info@example-two.de`` an
zwei unterschiedliche Personen vorgesehen, so müssen "virtuelle" Domains genutzt
werden. In diesem Fall enthält ``mydestination`` weiterhin nur die Haupt-Domain
des Mailservers, also beispielsweise ``example-one.de``. Die weitere(n)
Domain(s) werden über die Variable ``virtual_alias_domains`` angegeben:

::

    # Domain-Einstellung für unterschiedliche Benutzer:
    mydestination = localhost, example-one.de
    virtual_alias_domains = example-two.de, example-three.de

Auch in diesem Fall können mehrere (virtuelle) Domains jeweils mit Komma und
Leerzeichen getrennt angegeben werden. Damit Postfix weiß, für welche Benutzer
die Nachrichten jeweils bestimmt sind, müssen zusätzlich auch "virtuelle Aliase"
festgelegt werden. Dies erfolgt ähnlich wie bei den normalen Alias-Definitionen,
mit dem Unterschied, dass jeweils nicht nur der Alias-Name, sondern auch die
zugehörige Domain angegeben werden muss.

::

    # /etc/postfix/virtual

    info@example-two.de user-two
    info@example-three.de user-three

    webmaster@example-one.de externe-email@adresse.de

Anstelle eines Benutzer-Accounts kann man für die einzelnen Email-Adressen auch
je eine externe Email-Adresse angeben; in diesem Fall wird die Post nicht lokal
in der Mailbox des Benutzers abgelegt, sondern an die externe Adresse
weitergereicht.

Zu beachten ist, dass bei Dateien wie der ``/etc/postfix/virtual`` kein
Doppelpunkt als Trennzeichen vorgesehen ist, sondern ein Whitespace-Zeichen (ein
oder mehrere Leerzeichen, oder ein Tab-Zeichen). Die Virtuelle-Alias-Datei kann
mittels ``postmap`` in eine binäre Form gebracht werden:

.. code-block:: sh


    # Virtuelle-Alias-Datenbank erstellen/aktualisieren:
    sudo postmap virtual

Die Datei ``main.cf`` kann anschließend um einen Eintrag für die so erstellte
Lookup-Tabelle ergänzt werden:

::

    # Ort der virtuellen Alias-Datei:
    virtual_alias_maps = hash:/etc/postfix/virtual

Die Konfigurationen müssen schließlich mit ``systemctl reload postfix`` neu
geladen werden. Der "eigene" Mailserver ist damit in seiner Grundfunktion
einsatzbereit, auch wenn mehrere Domains auf dem Server gehostet werden sollen:
Empfangene Emails werden unter ``/var/name/benutzername`` abgelegt und können
dort beispielsweise mittels :ref:`mutt <mutt>` gelesen werden; ebenso können
Emails vom Server mittels ``mutt`` oder anderen Programmen aus an externe
Mailserver verschickt werden. Ein wesentlicher Nachteil bleibt allerdings noch
bestehen: Zum Lesen und Schreiben der Emails muss erst ein SSH-Login auf dem
Server erfolgen. Um dies zu umgehen, kann beispielsweise :ref:`Dovecot
<Dovecot>` als Authentifizierungs-Dienst aushelfen.


.. rubric:: Mbox und Maildir, Virtuelle Postfächer

Mit den bisherigen Einstellungen legt Postfix Emails in Dateien Postfächern der
Art ``/var/mail/benutzername`` ab. Dies bedeutet, dass die Mails nur für
existierende Benutzer-Accounts zugestellt werden können, und damit für jeden
Maildienst-Nutzer ein eigener Account eingerichtet werden müsste. Diese
Unpässlichkeit lässt sich durch sich durch so genannte "virtuelle" Postfächer
beheben.

Mit der Ablage der eingehenden Emails ist auch noch eine zweite Frage verbunden:
Sollen die Emails in eine einzelne, möglicherweise recht große (Text-)Datei
geschrieben werden, oder soll jede Email einzeln in ein Verzeichnis abgelegt
werden?

* Die erste Variante, bei der beliebig viele Emails in eine einzige Datei
  geschrieben werden, wird ``mbox`` genannt; sie wird meist dann verwendet, wenn
  ein Email-Client wie :ref:`Thunderbird <Thunderbird>` oder :ref:`mutt <mutt>`
  mit ``POP3`` als Übertragungs-Protokoll konfiguriert wird.

* Bei der zweiten Variante wird jede Email einzeln in ein ``Maildir``
  geschrieben. Diese Konfiguration wird üblicherweise in Kombination mit dem
  Übertragungs-Protokoll ``IMAP`` genutzt.

Sowohl ``mbox`` wie auch ``Maildir`` sind als Postfach-Optionen weit verbreitet.
Die zweite Variante scheint sich allerdings immer mehr durchzusetzen, da sie
insbesondere eine einfachere Synchronisierung ermöglicht.

Um mit Postfix ``Maildir`` anstelle der Grundeinstellung ``mbox`` zu verwenden,
kann man in der Datei ``/etc/postfix/main.cf`` die Einstellung ``home_mailbox =
Maildir/`` setzen (diese Einstellung hat dann Vorrang gegenüber der
standardmäßig gesetzten Variablen ``mail_spool_directory``, die auf
``/var/mail`` verweist). Es kann auch ein von ``Maildir/`` abweichender Name
gewählt werden, entscheidend ist lediglich, dass ein Schrägstrich am Ende
gesetzt wird. Ohne weitere Einstellungen werden Emails damit als einzelne
Dateien im Verzeichnis ``/home/benutzername/Maildir`` gespeichert.


Möchte man die Emails (wahlweise im ``mbox`` oder im ``Maildir/``-Format)
unabhängig von den Benutzer-Accounts verwalten, so muss zunächst ein eigener
Benutzer zur Verwaltung der virtuellen Postfächer angelegt werden:

.. code-block:: sh

    # Benutzer und Gruppe für virtuelle Postfächer einrichten:
    sudo groupadd -g 5000 vmail
    sudo useradd -g vmail -u 5000 -s /usr/bin/nologin vmail

.. adduser --disabled-login --disabled-password --home /var/vmail vmail


.. .. code-block:: sh
..     # Check:
..     id vmail

Anschließend muss die ``main.cf`` noch abgeändert beziehungsweise um folgende
Einträge ergänzt werden:

::

    #Einstellungen für die virtuellen Mailboxen:

    virtual_uid_maps = static:5000
    virtual_gid_maps = static:5000

    # Zuordnung von Emailadressen und Postfächern:
    virtual_mailbox_maps    = hash:/etc/postfix/vmaps

    # In diesem Verzeichnis die Emails domainweise abgelegt werden:
    virtual_mailbox_base    = /var/vmail

    # Diese Domains sollen als virtuelle Domains gehandhabt werden:
    virtual_mailbox_domains = example-two.de, example-three.de

    # Domains, die als virtual_mailbox_domains gelistet sind, haben
    # keine zugewiesenen "echten" Benutzer. Daher müssen die Domains
    # bei den virtual_alias_domains wieder ausgetragen werden:
    virtual_alias_domains =


Die Einstellung für ``virtual_mailbox_base`` bewirkt, dass die Emails in
Verzeichnissen der Art ``/var/vmail/domainname.tld/benutzername`` abgelegt
werden.

Nun muss festgelegt werden, unter welchen virtuellen Benutzernamen die
eingehenden Emails abgelegt werden sollen. Meist stehen zwei unterschiedliche
Ziel-Emailadressen auch für zwei unterschiedliche Adressaten. Postfix sieht
daher wiederum eine Mapping-Datei vor, die jede Email-Adresse mit einem
Verzeichnispfad relativ zum Basispfad  ``/var/vmail`` der virtuellen
Benutzerkonten verknüpft:

::

    # Datei /etc/postfix/vmaps

    # Ablage im mbox-Format:
    user1@example-one.de  example-one.de/user1
    user2@example-one.de  example-one.de/user2

    # Ablage im Maildir-Format:
    user3@example-two.de  example-two.de/user3/

.. eine virtuelle Catch-All Adresse darf __niemals__ in der Datei virtual aufgeführt sein.

Wie man sieht, ist bei der Zuweisung von Emailadressen auf Postfächer mit
virtuellen Benutzern wiederum entscheidend, ob die Pfadangabe mit einem 
Schrägstrich endet oder nicht.

Es können auch mehrere Emails einem virtuellen Benutzer zugewiesen werden.
Ebenfalls möglich ist es, als Eintrag für eine Emailadresse nur ``@xample-one.de
user4`` ohne vorangehenden Adressnamen anzugeben, um ein "Catch-All"-Postfach
hinzuzufügen: In diesem Fall werden alle Emails, die nicht zugeordnet werden
können, im Postfach des angegebenen (virtuellen) Benutzers abgelegt.

Die Datei ``/etc/postfix/vmaps``  muss wiederum mittels ``postmap``
in eine binäre Datenbank-Datei umgewandelt werden:

.. code-block:: sh

    postmap /etc/postfix/virtual-mboxes

Schließlich müssen noch das Verzeichnis ``/var/vmail`` sowie die einzelnen
Domain-Verzeichnisse ``/var/mail/example-one`` usw. angelegt und Eigentümer und
Gruppe dieser Verzeichnisse jeweils auf ``vmail`` angepasst werden:

.. code-block:: sh

    # Ablage-Verzeichnisse für virtuelle Domains einrichten:

    mkdir /var/vmail
    chown vmail:vmail /var/vmail

    mkdir /var/mail/example-one
    chown vmail:vmail /var/vmail/example-one

    # (...)


Die Verzeichnisse für die virtuellen Benutzer der einzelnen Domains werden
automatisch angelegt.

.. Die virtuellen Nutzer sind Dovecot nicht bekannt!

.. }}}

.. Mailserver-Test mittels ``swaks``
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

.. Das Programm ``swaks`` steht für "Swiss Army Knife for SMTP``.
.. Tatsächlich ist es eine kleine, aber praktische Anwendung, um 
.. beispielsweise Test-Mails an einen Mailserver zu schicken.

.. https://liquidat.wordpress.com/2013/03/20/howto-sending-test-mails-with-swaks/
.. https://www.sefic.name/2016/09/28/how-to-send-mail-from-command-line-using-swaks/
.. https://debian-administration.org/article/633/Testing_SMTP_servers_with_SWAKS

.. ... to be continued ...

.. .. rubric:: Relaying

.. Betreibt man Postfix auf einem eigenständigen VServer, so ist es empfehlenswert,
.. kein "Relaying" zu erlauben. Mit diesem Begriff ist gemeint, dass der Mailserver
.. eine Mail, für deren Empfang er nicht verantwortlich ist, an einen anderen
.. Mailserver weiterleitet ("bounce"). Ein Mailserver ``A`` könnte mit dieser
.. Option den Mailserver ``B`` als "Trittbrett" verwenden, um mit dem Mailserver
.. ``C`` zu kommunizieren.


.. }}}

.. Die Konfigurationsdatei ``master.cf``
.. ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. .. {{{

.. Postfix ist modular aufgebaut. Der Grund dafür liegt insbesondere darin, dass
.. manche Teilprozesse zwingend Root-Rechte benötigen, andere hingegen nicht.
.. Um den Mailserver möglichst sicher zu halten, wurde Postfix so konzipiert, dass
.. jeder Teildienst mit den geringst möglichen Rechten abläuft.

.. Postfix startet zunächst stets (mit Root-Rechten) den Master-Prozess; dieser
.. kann über die Datei ``/etc/postfix/master.cf`` konfiguriert werden. Die
.. Standard-Einstellungen in dieser Datei sind für die meisten Systeme passend, so
.. dass oftmals gar keine Änderungen nötig sind.

.. .. Einige der wichtigen weiteren Teile von Postfix sind etwa der Queuemanager qmgr
.. .. (ist für alle Warteschlangen in denen Mails zwischengespeichert werden
.. .. zuständig), postdrop (nimmt lokale Mails auf), smtpd (lauscht auf Mails aus dem
.. .. Netzwerk), smtp (versendet Mails ins Netzwerk), trivial-rewrite (erledigt einige
.. .. einfache Headerumschreibungen) und local (legt Mails lokal in Postfächer).

.. .. }}}


.. _Dovecot:

.. }}}

Dovecot
-------

`Dovecot <https://wiki.ubuntuusers.de/Dovecot_2/>`__ ist ein so genannter "Mail
Delivery Agent" (MDA). Ein solcher Dienst übernimmt die Zustellung von Emails an
die einzelnen Benutzer-Konten.

Dovecot kann eingehende Emails nicht nur in den passenden Benutzer-Konten
ablegen (was die eigetnliche Aufgabe eines MDAs ist), sondern ermöglicht zudem
auch eine Authentifizierung der Benutzer mittels SASL sowie ein Abholen der
Emails mittels Protokolle IMAP oder POP3. [#]_

.. Dovecot ist somit ein MDA und ein IMAP/POP-Server zugleich.

Installiert wird Dovecot mittels folgender Pakete:

.. code-block:: sh

    sudo aptitude install dovecot-core dovecot-lmtpd dovecot-imapd dovecot-pop3d


.. rubric:: SASL-Grundlagen

Das Mailversand-Protokoll SMTP wurde (ebenso wie das HTTP-Protokoll für
Webseiten) ohne Authentifizierungs-Mechanismen entwickelt. Nicht zuletzt
aufgrund der vielen Spam-Emails wurde später an dieser Stelle nachgebessert;
inzwischen ist SASL (Simple Authentication and Security Layer) zum Standard
geworden.

SASL ist immer dann von Bedeutung, wenn der angesprochene Mailserver nicht der
Ziel-Mailserver für eine Email ist. Dies ist beispielsweise der Fall, wenn eine
Email mit Absender ``webmaster@example-one.de`` nicht direkt vom Server aus
verschickt werden soll, sondern die Email von einem anderen Rechner aus
beispielsweise mittels eines installierten Mail-Clients wie :ref:`Thunderbird
<Thunderbird>` oder :ref:`mutt <mutt>` zunächst an den für ``example-one.de``
zuständigen Server geschickt wird, damit dieser sie wie gewünscht an den
Ziel-Mailserver ausliefert. 

SASL sieht eine Anfrage des Clients an den Server vor, ob zur angegebenen
Email-Adresse ein gültiger Benutzer existiert (oder gegebenenfalls ein
virtueller Benutzer). Ist dies der Fall, so meldet sich der Client anschließend
mittels eines Passworts an: Nur, wenn das angegebene Passwort mit demjenigen
überein stimmt, das auf dem Server für den jeweiligen Benutzer hinterlegt ist,
wird eine anschließende Mail-Übertragung erlaubt. 

SASL funktioniert prinzipiell unverschlüsselt, was bedeutet, dass die Daten im
Klartext vom und zum Server übertragen werden. Um diese potentielle
Sicherheitslücke zu beseitigen, sollten die in einer SASL-Sitzung übertragenen
Daten bevorzugt mit TLS verschlüsselt werden.

Die für eine erfolgreiche Authentifizierung via SASL notwendigen Einstellungen
können ebenso für ein Abholen von Emails via IMAP beziehungsweise POP3 genutzt
werden.


.. Mittels ``postfix -a`` kann man prüfen, ob die installierte Postfix-Version eine
.. Unterstützung von ``dovecot`` als SASL-Prüfstelle bietet; dies ist mittlerweile
.. bei jeder Standard-Installation der Fall.

... to be continued ...

.. ``dovecot -a`` Liste mit allen Einstellungen,
.. ``dovecot -n`` Liste mit allen Einstellungen, die von den Standard-Einstellungen abweichen.

.. * Werden Variablen mehrfach gesetzt, so gilt der zuletzt gesetzte Wert

.. * Kommen in den ``plugin``-Abschnitten so genannte "boolesche" Variablen vor,
..   die nur "wahr" oder "falsch" als Wert annehmen können, so werden diese *stets*
..   als wahr interpretiert, gleichgültig ob ihnen der Wert ``true``, ``false``,
..   ``no`` oder ``0`` zugewiesen wird.

.. To read the content of a file, for instance for the SSL certificate option,
.. prefix the filename with a <, e.g.: 

.. doveadm help


Links
-----

* `Postfix (Wikipedia) <https://de.wikipedia.org/wiki/Postfix_(Mail_Transfer_Agent)>`__
* `Postfix-Tutorial (de) <http://dozent.maruweb.de/material/postfix.shtml>`__

* `Postfix-Virtual README (en.) <http://www.postfix.org/VIRTUAL_README.html>`__

.. .

* `Dovecot (Wikipedia) <https://de.wikipedia.org/wiki/Dovecot>`__
* `Dovecot-Wiki (en.) <https://wiki2.dovecot.org/FrontPage>`__


.. Mailman Documantation (en.): https://docs.mailman3.org/en/latest/pre-installation-guide.html


.. postconf -a
.. saslauthd
.. plain

.. Digest-MD5 und CRAM-MD5 sind Verfahren bei dem nie das eigentliche Passwort über
.. die Leitung gesendet wird. Stattdessen sendet der Server eine "Challenge". Der
.. Client kombiniert die Challenge mit dem Passwort und bildet daraus einen
.. MD5-Hash. Dieser Hash wird dann dem Server gesendet. Der Server ermittelt dann
.. ob er auf das gleiche Ergebnis kommt, womit der Client das richtige Passwort
.. kennen muss.

.. Wird eine Email verschickt, so erfrägt der sendende Mailserver zunächst anhand
.. die IP-Adresse des Ziel-Servers von einem DNS-Server: Hierfür ist der
.. Domain-Name der Ziel-Email-Adresse von Bedeutung. Ist für die angegebene
.. Domain ein ``MX``-Eintrag vorhanden, so wird diese IP-Adresse als Ziel-Adresse der
.. Email verwendet; andererseits wird wird auf den ``A``-Eintrag (der eigentlich
.. für Web-Anfragen mittels ``http`` gedacht ist) zurückgegriffen. In einer Shell
.. kann man sich die zu einer Domain gehörende(n) Adresse(n) mittels :ref:`host
.. <host>` anzeigen:

.. .. code-block:: sh

..     host grund-wissen.de
..     # Ergebnis:
..     # grund-wissen.de has address 88.198.20.123
..     # grund-wissen.de mail is handled by 10 mail.grund-wissen.de.

..     host mail.grund-wissen.de
..     # Ergebnis:
..     mail.grund-wissen.de has address 88.198.20.123

.. Ist die IP-Adresse des Zielrechners ermittelt worden, so versucht der sendende
.. Server eine Verbindung mit diesem aufzubauen. Hierbei wird das Protokoll SMTP
.. verwendet, das standardmäßig den Port ``25`` nutzt.

.. und SSL/TLS

.. home_mailbox = Maildir/





.. .

.. `Swaks Projektseite <http://www.jetmore.org/john/code/swaks/>`__

.. Variante A: Einzelne Domain, ein User
.. Variante B: Mehrere Domains, mehrere User
.. Variante C: Mehrere Domains, mehrere virtuelle User
.. Variante D: Mehrere Domains, mehrere virtuelle User, MySQL


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Postfix ist das Nachfolge-Programm von ``sendmail``. Postfix bietet die
    gleichen Funktionen, ist allerdings wesentlich einfacher zu konfigurieren,
    und hat sich daher zum Standard entwickelt.

    Anstelle von Dovecot kann Postfix auch mit den ähnlichen Programmen `Courier
    <https://de.wikipedia.org/wiki/Courier_Mail_Server>`__ oder `Cyrus
    <https://de.wikipedia.org/wiki/Cyrus_(Server)>`__ betrieben werden; Dovecot
    scheint allerdings bei neu aufgesetzten Systemen zunehmend ebenfalls zum
    Standard zu werden.

.. [#] In der Fachsprache wird ein IMAP/POP-Dienst auch als "Mail Retrieval Agent" (MRA)
    bezeichnet. Email-Client-Programme wie :ref:`Thunderbird <Thunderbird>` oder
    :ref:`Mutt <Mutt>` bezeichnet man hingegen als "Mail User Agent" (MUA).
