.. _Sichere Datenübertragung mit SSH und GPG:

Sichere Datenübertragung mit ``ssh`` und ``gpg``
================================================
.. {{{

Im folgenden Abschnitt sollen das Datenübertragungs-Protokoll SSH sowie die
Dateiverschlüsselung GPG anhand von einigen praktischen Beispielen vorgestellt
werden.

.. index:: SSH
.. _Verwendung von ssh:
.. _Arbeiten auf entfernten Rechnern:
.. _SSH -- Arbeiten auf entfernten Rechnern:

.. }}}

SSH -- Arbeiten auf entfernten Rechnern
---------------------------------------
.. {{{

SSH steht für "Secure Shell" und ermöglicht sichere, verschlüsselte
Netzwerkverbindungen mit anderen Computern.

Um sich -- beispielsweise in einem Heim-Netzwerk -- wechselseitig auf einem
entfernten Rechner einloggen zu können, sollten auf beiden Rechnern folgende
Pakete installiert werden:

.. code-block:: bash

    sudo aptitude install openssh-client openssh-server

Hat man hingegen mehrere Clients, die unter einem jeweiligen Benutzernamen
Zugriff auf einen Server haben sollen, so genügt es, bei diesen
``openssh-client`` und auf dem Server ``openssh-server`` zu installieren. Durch
die Installation wird automatisch der SSH-Hintergrund-Dienst ``sshd`` gestartet;
nach jedem Neustart des Rechners ist dieser ebenfalls aktiv.

Um sich von einem Client aus in einem externen Rechner einzuloggen, kann man in
einer Shell folgendes eingeben:

.. code-block:: bash

    # SSH-Verbindung aufbauen:
    ssh benutzername@ip-adresse

.. Begrüßungstext: ``/etc/motd``

Die Adresse des eigenen Rechners im lokalen Netzwerk kann man sich mittels ``ip
r`` oder ``hostname --all-ip-addresses`` anzeigen lassen; sie lautet
beispielsweise ``192.168.2.103``. Daraus kann man entnehmen, dass der Router
lokale Netzwerk-Adressen von ``192.168.2.1`` bis ``192.168.2.255`` vergibt. Die
Netzwerkadressen von anderen Rechnern im lokalen Netzwerk kann man dann
beispielsweise erhalten, indem man in einer Shell beispielsweise ``nmap -sP
192.168.2.0/24`` oder (als Superuser) ``nast -m`` eingibt.

Existiert für den angegebenen Benutzername auf dem Rechner und wird das Passwort
(des Benutzers auf dem externen Rechner) richtig eingegeben, so werden alle
folgenden Anweisungen auf dem entfernten Rechner ausgeführt, nur die
Bildschirmausgabe erfolgt lokal. Durch Eingabe von ``exit`` kann die SSH-Sitzung
wieder verlassen werden.


.. _scp und ssh -X:

.. rubric:: ``scp``: Datenaustausch im Netzwerk

Mittels ``scp`` kann via SSH eine einzelne Datei (oder ein einzelnes
Verzeichnis) auf den entfernten Rechner kopiert werden. Die Syntax dafür lautet:

.. code-block:: bash

    # Datei via SSH kopieren:
    scp lokale-datei benutzername@ip-adresse:zielpfad

Um mehrere Dateien auf einmal zu kopieren, können diese entweder mittels
:ref:`tar <tar>` gebündelt oder in ein Verzeichnis kopiert werden; mittels ``scp
-r`` kann dieses Verzeichnis dann (wie eine einzelne Datei) rekursiv kopiert
werden. Manche Dateimanager wie :ref:`Midnight Commander <mc>` nutzen ebenfalls
intern ``scp``, um Dateien auf einfache Weise vom lokalen auf einen externen
Rechner oder umgekehrt zu kopieren; der Benutzer spart sich dabei Tipp-Arbeit.

.. rubric:: ``ssh -X``: Starten von GUI-Programmen

Möchte man auf dem entfernten Rechner nicht nur Shell-Programme, sondern auch
Programme mit graphischer Bedienoberfläche (GUI) aufrufen, kann ``ssh`` mit der
Option ``-X`` aufrufen werden, also mittels:

.. code-block:: bash

    # SSH-Verbindung mit X-Forwarding aufbauen:
    ssh -X benutzername@ip-adresse

In diesem Fall bekommt man nach einer richtigen Passwort-Eingabe ebenfalls ein
Shell-Fenster angezeigt; aus diesem heraus lassen sich allerdings auch
Anwendungen mit graphischen Bedienoberflächen starten, die dann lokal auf dem
Monitor angezeigt werden (so, als würden GUI-Programme des eigenen PCs aus der
Shell heraus gestartet).

Damit dies funktioniert, muss allerdings auf dem entfernten Rechner folgender
Eintrag in der Konfigurations-Datei ``/etc/ssh/sshd_config`` vorhanden sein:

.. code-block:: sh

    # File: /etc/sshd/sshd_config

    X11Forwarding yes

War dieser Eintrag noch nicht vorhanden oder das X11-Forwarding bislang
deaktiviert, so muss der ``ssh``-Dienst auf dem entfernten Rechner mittels
``/etc/init.d/ssh restart`` nochmal neu gestartet werden.

.. Port für sshd kann auf beispielsweise 2212 geändert werden... wirklich mehr
.. Sicherheit dadurch?

.. ``PermitRootLogin`` sollte auf ``no`` gesetzt werden.

.. Explizit erlaubte Benutzer:

.. AllowUsers waldgeist

.. Das verbietet allen anderen Usern den Zugriff

.. sudo systemctl restart ssh
.. geht service ssh restart auch? sollte..


.. _SSH-Key:
.. _SSH-Schlüssel:
.. _Anmeldung mit Public Key anstelle eines Passworts:

Anmeldung mit Public Key anstelle eines Passworts
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Sicherer als Passwörter sind für die Authentifizierung eines Benutzers so
genannte Schlüsselpaare: Ein privater Schlüssel auf dem eigenen PC, und ein
öffentlicher Schlüssel, der an beliebig viele andere Stellen kopiert werden
kann. Ein Login ist damit nur noch dann möglich, wenn der private und der
öffentliche Schlüssel zusammenpassen.

Ein Schlüsselpaar kann in einer Shell folgendermaßen erzeugt werden:

.. code-block:: bash

    # SSH-Schlüssel generieren:
    ssh-keygen

Zu Übungszwecken kann bei der Nachfrage nach einem Passwort einfach ``Enter``
eingegeben werden; der private Schlüssel wird somit nicht mit einem Passwort
versehen.

Durch den Aufruf von ``ssh-keygen`` werden im Verzeichnis ``~/.ssh`` zwei
Dateien angelegt: Die Datei ``id_rsa`` enthält den privaten Schlüssel, der nicht
in falsche Hände geraten sollte, und die Datei ``id_rsa.pub`` ("public") den
öffentlichen Schlüssel, der auf alle Rechner kopiert werden kann, auf denen man
sich via SSH einloggen will.

Zum Kopieren des öffentlichen Schlüssels kann folgendes in einer Schell
eingegeben werden:

.. code-block:: bash

    # SSH-Public-Key auf Zielrechner kopieren:
    ssh-copy-id benutzername@ip-adresse

Hierbei muss nochmals das Passwort des Benutzers auf dem Zielsystem eingegeben
werden. Durch den Aufruf von ``ssh-copy-id`` wird der Standard-Schlüssel (oder
durch Angabe von ``-i pfad`` eine explizit angegebene Schlüsseldatei) auf dem
Zielrechner der Datei ``~/.ssh/authorized_keys`` hinzugefügt.

Gibt man anschließend ``ssh benutzername@ip-adresse`` ein, so erfolgt das
Einloggen via Schlüsselpaar anstelle der Eingabe eines Passworts. [#]_

Für ein wechselseitiges Verbinden zweier Rechner mittels SSH muss das oben
beschriebene Verfahren auf beiden Rechnern erfolgen.


.. _Passwortschutz für private Schlüssel:

Passwortschutz für private Schlüssel
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Gelangt der private Schlüssel an eine eigentlich unbefugte Person, so kann sich
auch diese ebenso unmittelbar wie ungewollt auf dem Zielrechner einloggen. Um
zu verhindern, dass der alleinige "Besitz" des privaten Schlüssels ausreicht,
kann man diesen mit einem Passwort versehen; bevor er für das Einloggen
verwendet werden kann, muss er erst mittels des Passworts freigegeben werden.

Üblicherweise werden passwortgeschützte SSH-Schlüssel in Verbindung mit
``ssh-agent`` genutzt. Dieses Programm wird im Allgemeinen automatisch mit dem
X-Server und/oder zu Begin einer Login-Shell gestartet und bleibt aktiv, bis
sich der Benutzer wieder abmeldet. Beim der erstmaligen Verwendung des
Schlüssels in einer laufenden Sitzung muss das Schlüssel-Passwort eingegeben
werden; alle weiteren Zugriffe auf den Schlüssel sind anschließend erlaubt.
Läuft der ``ssh-agent`` noch nicht, kann er folgendermaßen für eine
Shell-Sitzung aktiviert werden:

.. code-block:: sh

    # SSH-Agent aktivieren:
    eval `ssh-agent`

Ein passwortgeschützter Schlüssel, beispielsweise ``~/.ssh/id_rsa`` kann
folgendermaßen zur Schlüsselverwaltung mittels ``ssh-agent`` hinzugefügt werden:

.. code-block:: sh

    # SSH-Schlüssel freischalten:
    ssh-add

Hierbei muss einmalig das Passwort des Schlüssels angegeben werden. Wird
``ssh-agent`` ohne die explizite Angabe eines Schlüsselpfads gestartet, so
werden automatisch alle im Verzeichnis ``~/.ssh`` liegenden Schlüssel
hinzugefügt. Mittels ``ssh add -l`` können die von ``ssh-agent`` verwalteten
Schlüssel angezeigt werden.

.. _SSH-Rechnername:
.. _SSH-Rechnernamen:
.. _Aliases für häufige Login-Adressen:

Aliases für häufige Login-Adressen
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

In der Datei ``~/.ssh/config`` können Kurzbezeichnungen
für häufig besuchte externe Rechner vergeben werden. Um beispielsweise auf einen
"Server" im Home-Netzwerk mit der lokalen Netzwerkadresse ``192.168.1.100``
zuzugreifen, fügt man der Datei ``~/.ssh/config`` folgenden Eintrag hinzu:

.. code-block:: sh

    Host server
        HostName 192.168.1.100
        User benutzername
        IdentityFile ~/.ssh/id_rsa

Anschließend muss man nicht mehr ``ssh benutzername@192.168.1.100`` eingeben, um
sich mit dem Server zu verbinden: Von nun an genügt es ``ssh server``
einzugeben.

.. index:: GPG
.. _GnuPG:
.. _Signieren von Dateien:
.. _Verschlüsseln von Dateien:
.. _Signieren und Verschlüsseln von Dateien:

.. }}}

GPG -- Signieren und Verschlüsseln von Dateien
----------------------------------------------
.. {{{

GPG steht für "GNU Privacy Guard" und ist die wohl am weitesten verbreitete
Implementierung von PGP ("Pretty Good Privacy"). Letzteres stellt einen Standard
dar, mit dem u.a. Emails verschlüsselt verschickt werden können, sofern die
Software sowohl beim Sender wie auch beim Empfänger installiert ist.

GPG gehört bei fast allen Linux-Distributionen zum Standard, muss also nicht
extra installiert werden.

GPG nutzt -- ebenso wie SSH -- zum Verschlüsseln der Daten ein Schlüsselpaar:
Der private Schlüssel bleibt auf dem eigenen Rechner und kann zum Entschlüsseln
von Nachrichten verwendet werden; der öffentliche Schlüssel hingegen wird
üblicherweise frei verteilt. Mit ihm können Nachrichten an den Eigentümer des
Schlüssels verschlüsselt, jedoch nicht entschlüsselt werden.


.. _Erstellen eines GPG-Schlüsselpaars:
.. _Erstellen eines Schlüsselpaars:

Erstellen eines GPG-Schlüsselpaars
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Zum Erstellen eines neuen Schlüsselpaars gibt man in einer Shell folgendes ein:

.. code-block:: sh

    gpg --gen-key

Hierbei wird man zunächst nach dem gewünschten Verschlüsselungsverfahren
gefragt, wobei die Vorgabe "RSA und RSA" mit ``1`` ausgewählt werden kann. Als
Schlüssellänge sollte man einen möglichst großen Wert nehmen -- 2048 Bit sind
ok, 4096 Bit sind sicherer und somit besser. Als letztes muss man angeben, wie
lange der Schlüssel gültig bleiben soll. Hier sollte durchaus eine Zeitvorgabe,
beispielsweise ``1y`` für "1 Jahr" eingegeben werden, da Schlüssel ohne
Verfallsdatum auch dann im Umlauf bleiben, wenn beispielsweise die zugehörige
Emailadresse nicht mehr existiert oder die Schlüssellänge durch immer schnellere
Rechner zu klein geworden ist. [#]_ Anschließend muss man als eindeutige
Benutzerkennung noch den Namen und die Emailadresse angeben, zu dem der
Schlüssel gehören soll.

Das Passwort beziehungsweise, das man für den Schlüssel vergibt, sollte zwar gut
merkbar, aber zugleich ausreichend sicher sein:

* Das Passwort sollte nicht leicht zu erraten sein

* Das Passwort darf Sonderzeichen beinhalten (muss es aber nicht)

* Klein- und Großbuchstaben innerhalb des Passworts werden als unterschiedliche
  Buchstaben angesehen.

* Lange Passwörter sind in der Regel sicherer als kurze, aber kryptische und
  damit schwer zu merkende Passwörter (siehe `xkcd <https://xkcd.com/936/>`__).

* Als Passwort kann auch ein ganzer Passwort-Satz (ein "Mantra") verwendet
  werden, da auch Leerzeichen im Passwort erlaubt sind.

Ohne einen Passwortschutz des privaten Schlüssels könnte jede Person, die
Zugriff auf die Schlüsseldatei bekommt, alle mit dem zugehörigen öffentlichen
Schlüssel gesicherten Dateien öffnen. Zudem sollte der private Schlüssel nicht
verloren gehen: Eine Sicherheits-Kopie des privaten Schlüssels auf eine externe
:ref:`verschlüsselte Partition <Partitions-Verschlüsselung>` (beispielsweise
eine USB-Stick oder eine externe Festplatte) ist dringend zu empfehlen!


.. _Widerrufungs-Zertifikat:
.. _Erstellen eines Widerrufungs-Zertifikats:

.. rubric:: Erstellen eines Widerrufungs-Zertifikats

Nachdem man ein Schlüsselpaar erzeugt hat, sollte man gleich im Anschluss daran
eine Widerrufsurkunde erzeugen. Mit einer Widerrufsurkunde kann man seinen
Schlüssel bei Bedarf als ungültig markieren. Ein solcher Fall kann
beispielsweise eintreten, wenn man das Passwort vergessen hat oder der private
Schlüssel aufgrund eines Festplatten-Defekts nicht mehr zugänglich ist.

Mit einem als ungültig markierten Schlüssel können keine weiteren Emails mehr
verschlüsselt oder signiert werden; bestehende Nachrichten hingegen können
weiterhin entschlüsselt werden.

Das Widerrufungs-Zertifikat ist vor allem von Bedeutung, wenn der öffentliche
Schlüssel auf einen :ref:`Schlüssel-Server <Schlüssel-Server>` hochgeladen
wurde: Diese synchronisieren in regelmäßigen Abständen ihre Datenbanken. Wird
ein Schlüssel auf *einem* Server hinzugefügt, so ist er bald auch auf allen
anderen Servern zu finden. Würde man seinen Schlüssel nur von einem der
Schlüssel-Server löschen, so würde dieser sich nach der nächsten Synchronisation
trotzdem wieder auf dem Server befinden. Anstelle einen Schlüssel zu löschen,
setzt man daher ein Widerrufszertifikat ein.

Um ein Widerrufungs-Zertifikat zu einem GPG-Schlüssel zu erzeugen, gibt man in
einer Shell folgendes ein:

.. code-block:: sh

    gpg --gen-revoke vorname.nachname@email.de

Die Frage, ob man dieses Zertifikat wirklich erzeugen will, kann man mit ``Ja``
beantworten; als Grund für den Widerruf kann man beim voreingestellten Wert
``1`` ("Der Schlüssel ist nicht mehr sicher") bleiben. Optional kann noch ein
Grund für den Widerruf eingegeben werden. Sobald man die Eingabe mit dem
Passwort des GPG-Schlüssels bestätigt hat, kann man die auf dem Bildschirm
erscheinende Ausgabe in eine Textdatei, beispielsweise
``Widerrufungszertifikat-SchluesselID.txt`` kopieren. Diese sollte -- ebenso wie
den privaten GPG-Schlüssel -- auf einem externen Speichermedium sicher verwahren
werden.


.. _Schlüssel widerrufen:

.. rubric:: Bei Bedarf: Widerrufen eines Schlüssels

Möchte man einen eigenen Schlüssel tatsächlich widerrufen, so muss man ein zum
Schlüssel gehörende Widerrufszertifikat importieren. Ein solcher Schritt muss
allerdings gut überlegt sein, denn er kann nicht rückgängig gemacht werden.

.. code-block:: sh

    gpg --import /pfad/Widerrufungszertifikat-SchluesselID.txt

.. Alle Dokumente, Emails etc., die mit diesem Schlüssel verschlüsselt wurden, sind
.. nicht wiederherstellbar.  stimmt so vermutlich nicht??

Um das Widerrufen eines Schlüssels publik zu machen, sollte man den mit dem
Widerrufungszertifikat versehenen Schlüssel erneut an einen Schlüsselserver
senden.

.. code-block:: sh

    gpg --send-keys Schlüssel-ID

Ein so widerrufener Schlüssel kann nicht mehr genutzt werden, um Nachrichten
oder andere Dateien zu verschlüsseln oder zu signieren.


.. _Grundlegende GPG-Anweisungen:
.. _Schlüsselbund verwalten:

GPG-Schlüsselbund verwalten
^^^^^^^^^^^^^^^^^^^^^^^^^^^

Um mit GPG-Schlüsseln arbeiten zu können, wird bei der Erstellung eines
Schlüsselpaares automatisch auch ein Schlüsselbund für private und ein
Schlüsselbund für öffentliche Schlüssel erzeugt; diese werden im Verzeichnis
``~/.gnupg`` abgelegt.

.. Im folgenden sind einige grundlegende Anweisungen näher beschrieben, die sich
.. unmittelbar aus einer Shell heraus nutzen lassen, sobald ein GPG-Schlüsselpaar
.. erzeugt wurde.
.. Auch Email-Programme wie :ref:`mutt <mutt>` greifen auf diese Funktionen zurück.

.. _Schlüssel auflisten:

.. rubric:: Schlüssel auflisten

Mit folgender Anweisung kann man alle öffentlichen Schlüssel auflisten, die im
eigenen Schlüsselbund ("Public Key Ring") gespeichert sind:

.. code-block:: sh

    # Öffentliche Schlüssel auflisten:
    gpg --list-keys

.. Bei FCC5040F handelt es sich also um die Schlüssel-ID meines öffentlichen
.. Schlüssels. 2004-04-26 ist das ISO-Datum (JJJJ-MM-TT) der Schlüsselerstellung.
.. Die mit uid beginnenden Zeilen zeigen meine Benutzer-IDs ("user id"), wie z. B.
.. Stephan Beyer <s-beyer@gmx.net>. 1024 bedeutet, dass der Schlüssel 1024 Bit lang
.. ist. Hinter der Länge steht jeweils das Verfahren: Ein D bedeutet DSA, g ist
.. ElGamal, R steht für RSA. sub steht für öffentliche und ssb für geheime
.. Unterschlüssel.
.. Sollte hinter ``sec`` ein ``#``-Zeichen stehen, so bedeutet dies, dass der
.. Schlüssel nicht mehr benutzbar ist .


Arbeitet man das erste mal mit GPG, so enthält der Public-Key-Ring nur den
eigenen öffentlichen Schlüssel. Im Laufe der Zeit kommen dann weitere Schlüssel
von anderen Personen oder Einrichtungen hinzu, die ebenfalls GPG verwenden
(beispielsweise wenn man einer solchen Person eine mit GPG verschlüsselte Email
schreiben möchte).

Alle öffentlichen Schlüssel sind in der Datei ``~/.gnupg/pubring.gpg`` abgelegt.
private Schlüssel ("Secret Keys") werden hingegen in der Datei
``~/.gnupg/secring.gpg`` gespeichert. Sie können folgendermaßen angezeigt
werden:

.. code-block:: sh

    # Private Schlüssel auflisten:
    gpg --list-secret-keys


.. _Schlüssel exportieren:

.. rubric:: Schlüssel exportieren

Möchte man, dass einem andere Personen eine verschlüsselte Email schreiben
können, so müssen diese einen Zugang zum öffentlichen Schlüssel haben. Hierzu
kann man den eigenen öffentlichen Schlüssel beispielsweise als Text-Datei auf
einer Homepage veröffentlichen oder der jeweiligen Person per Email schicken.

.. TODO oder, wie weiter unten beschrieben, auf einen Schlüsselserver hochladen.

Um einen Schlüssel zu exportieren, kann man ``gpg`` mit der Option ``--export``
aufrufen. Hierbei werden allerdings standardmäßig *alle* Schlüssel ausgegeben.
Möchte man nur den eigenen Schlüssel exportieren, so muss man die Auswahl
dadurch einschränken, indem man hinter ``--export`` beispielsweise die zum
Schlüssel gehörende Email-Adresse, den zum Schlüssel gehörenden Namen oder die
ersten Stellen der Schlüssel-ID angibt:

.. code-block:: sh

    # Eigenen Schlüssel exportieren:
    gpg -a -o ~/my-public-key.txt --export vorname.nachname@email.de

Über die Option ``-o`` wird der Name der Datei festgelegt, in die der Schlüssel
exportiert werden soll. Die Option ``-a`` als Kurzform für  ``--armor`` bewirkt,
dass der Schlüssel ausschließlich durch ASCII-Symbole dargestellt wird, so dass
die resultierende Datei ohne Probleme auf eine Homepage hochgeladen oder als
Anhang per Email verschickt werden kann (manchmal wird auch die Datei-Endung
``.asc`` oder ``.gpg`` anstelle von ``.txt`` verwendet).


.. _Schlüssel importieren:

.. rubric:: Schlüssel importieren

Mit folgender Anweisung kann ein öffentlicher Schlüssel aus einer Textdatei
importiert werden:

.. code-block:: sh

    # Schlüssel aus Datei importieren:
    gpg --import schluesseldatei

Die Schlüsseldatei muss hierbei mitsamt Endung (meist ``.txt``, ``.asc`` oder
``.gpg``) angegeben werden.

Sobald ein Schlüssel zum eigenen Schlüsselbund hinzugefügt wurde, kann er
verwendet werden, um beispielsweise der zugehörigen Person verschlüsselte Daten
zu senden.

Mittels ``gpg --delete-key`` kann man den öffentlichen Schlüssel mit der
angegebenen ID wieder aus dem eigenen Schlüsselbund entfernen:

.. code-block:: sh

    # Schlüssel aus Schlüsselbund entfernen:
    gpg --delete-key SchluesselID

Mittels ``gpg --delete-secret-key ID`` kann man entsprechend einen privaten
Schlüssel löschen.


.. _Schlüssel-Attribute ändern:

.. rubric:: Schlüssel-Attribute ändern

Mittels folgender Anweisung lassen sich auch nachträglich Änderungen an
einem GPG-Schlüssel vornehmen:

.. code-block:: sh

    # Schlüssel-Attribute editieren:
    gpg --edit-key SchluesselID

Nach Eingabe dieser Anweisung erscheint ein ``gpg>``-Eingabe-Prompt, in dem
weitere GPG-Anweisungen aufgerufen werden können

* Mit ``help`` bekommt man eine Liste aller möglichen Anweisungen mitsamt kurzen
  Beschreibungen angezeigt.
* Mit ``expire`` kann man das Verfalls-Datum (``expire``) eines eigenen
  Schlüssels ändern
* Mit ``passwd`` kann man das Passwort (Mantra) eines eigenen Schlüssels ändern

Mit ``quit`` kann das Editieren wieder beendet werden.


.. _Schlüssel-Server:
.. _Nutzung von Schlüssel-Servern:

.. rubric:: Nutzung von Schlüssel-Servern

Eine weit verbreitete Methode, öffentliche GPG-Schlüssel publik zu machen, ist
die Verwendung von so genannten Schlüssel-Servern. Man kann beispielsweise den
(beziehungsweise einen) eigenen Schlüssel auf einen solchen Server hochladen, so
dass er von anderen GPG-Nutzern in der ganzen Welt gefunden werden kann.
Umgekehrt kann man so auch nach den GPG-Schlüsseln von anderen Personen suchen.

Um einen Standard-Schlüssel-Server festzulegen, kann man in der
Konfigurationsdatei ``~/.gnupg/gpg.conf`` beispielsweise folgenden Eintrag
vornehmen::

    # Eintrag in der Datei ~/.gnupg.conf :
    keyserver sks-keyservers.net

Für die Nutzung von Schlüssel-Servern gibt es dann folgende ``gpg``-Anweisungen:

* Mit ``gpg --search Name`` oder ``gpg --search emailadresse`` kann man
  nach öffentlichen Schlüsseln anderer Personen suchen. Sind Einträge vorhanden,
  so werden diese automatisch nummeriert aufgelistet. Man erhält daraufhin eine
  Abfrage, ob man einen der gefundenen Schlüssel durch Eingabe der zugehörigen
  Nummer in den eigenen Schlüsselbund importieren möchte, oder ob man die
  Eingabe mittels ``b`` beenden möchte.

* Mit ``gpg --refresh`` werden alle öffentlichen Schlüssel aktualisiert. Auf
  diese Weise erhält man beispielsweise Informationen darüber, ob ein Schlüssel
  widerrufen wurde, andere Schlüssel-Signaturen hinzugekommen sind, usw.

* Mit ``gpg --recv SchluesselID`` wird der öffentliche Schlüssel mit der
  angegebenen ID direkt importiert. Ist der angegebene Schlüssel bereits im
  Schlüsselbund enthalten, so wird der Schlüssel aktualisiert.

* Mit ``gpg --send SchluesselID``  wird der öffentliche Schlüssel mit der
  angegebenen ID an den Schlüssel-Server geschickt; ``gpg`` gibt hierbei
  eine Fehler- oder Erfolgsmeldung auf dem Bildschirm aus.

  **Achtung:** Schlüssel, die einmal auf einen Schlüssel-Server hochgeladen
  wurden, können nie wieder gelöscht werden!

Wie bereits im Abschnitt :ref:`Widerrufungs-Zertifikat
<Widerrufungs-Zertifikat>` erwähnt, gibt es keine Möglichkeit, einen Schlüssel
wieder von einem Schlüssel-Server zu löschen. Schlüssel verlieren nur ihre
Gültigkeit, wenn sie verfallen oder widerrufen werden; das Erstellen eines
Widerrufungs-Zertifikats ist daher dringend zu empfehlen, bevor ein öffentlicher
Schlüssel an andere weitergegeben wird -- schließlich kann *jeder* öffentliche
Schlüssel auf einen Schlüssel-Server hochladen!


.. _Signatur:
.. _Daten signieren:

Daten signieren
^^^^^^^^^^^^^^^

Signaturen sollen als "digitale Unterschriften" die Authentizität beispielsweise
einer Nachricht beweisen. Würden Nachrichten von offizieller Seite konsequent
signiert, wäre es deutlich schwerer, mit gefälschten Nachrichten Unruhe oder
Schaden zu verursachen.

Ein Signatur einer Nachricht wird unter Verwendung des privaten Schlüssels
erzeugt; diese kann dann vom Empfänger anhand des öffentlichen Schlüssels des
Senders überprüft werden. Dabei wird nicht nur der Absender überprüft (nur
dieser hat den privaten Schlüssel), sondern auch, ob der Text unverändert
angekommen ist.

Eine Datei kann mit einer der folgenden Anweisungen signiert werden:

* Mit ``gpg -s`` beziehungsweise ``gpg --sign`` kann man eine Datei mit seinem
  privaten Schlüssel signieren; sie wird dabei gleichzeitig komprimiert und
  ist somit nicht mehr ohne weiteres lesbar.

* Mit ``gpg --clearsign`` kann man eine Datei signieren, wobei die Datei
  nicht komprimiert wird und somit lesbar bleibt.

* Mit ``gpg -b`` beziehungsweise ``gpg --detach-sign`` wird die Signatur in
  einer separaten Datei abgelegt. Diese Variante ist beispielsweise zum
  Signieren von Archiv-Dateien empfehlenswert (diese können allerdings auch ohne
  Überprüfung der Signatur entpackt werden).

Bei allen obigen Anweisungen kann die Option ``-a`` beziehungsweise ``--armor``
nützlich sein, um reine ASCII-Zeichen zu erzwingen; dies ist insbesondere beim
Versenden von signierten und/oder verschlüsselten Daten via Email
empfehlenswert.

Die Signatur einer (unverschlüsselten) Datei kann man folgendermaßen prüfen:

.. code-block:: sh

    # Signatur überprüfen:
    gpg --verify Datei

Wurde die Datei von einer anderen Person signiert, so muss man zur Überprüfung
der Signatur den öffentlichen Schlüssel dieser Person im eigenen Schlüsselbund
haben.

.. _Web of Trust:

.. rubric:: Das "Web of Trust"

Eine prinzipielle Schwachstelle der Public-Key-Methode ist die Verbreitung der
öffentlichen Schlüssel: Ein Angreifer könnte einen öffentlichen Schlüssel mit
einer falschen User-ID in Umlauf bringen. Wenn ein Sender diesen Schlüssel zur
Verschlüsselung einer Nachricht verwendet und der Angreifer die Nachricht
abfangen kann, so kann er diese dekodieren und lesen. Wenn der Angreifer die
Nachricht anschließend mit einem echten öffentlichen Schlüssel kodiert an den
eigentlichen Empfänger weiterleitet, fällt der Angriff unter Umständen nicht
einmal auf. Derartige potentielle Angriffe, die auch bei anderen
Verschlüsselungsverfahren möglich sind, nennt man daher
"Man-in-the-Middle"-Angriffe.

.. Vertrauen ist reflexiv, aber nicht symmetrisch oder transitiv. :-)

Eine von von PGP beziehungsweise GnuPG gewählte Strategie gegen derartige
Angriffe besteht im *Signieren der Schlüssel*: Jeder öffentliche Schlüssel kann
von anderen Personen unterschrieben werden. Eine solche Unterschrift soll
wiederum bestätigen, dass der Schlüssel authentisch ist, also zu der in der
User-ID angegebenen Person gehört.

Jeder Benutzer muss selbst entscheiden, welchen Unterschriften er wie weit
traut. Man kann einen Schlüssel beispielsweise dann als vertrauenswürdig
einstufen, wenn er von einer Person unterzeichnet wurde, der man vertraut.
Ebenso sollte man selbst einen anderen Schlüssel nur dann unterzeichnen, wenn
man die zum Schlüssel gehörende Person kennt und sich der Authentizität des
Schlüssels auch wirklich sicher ist.


.. _Daten verschlüsseln und entschlüsseln:

Daten verschlüsseln und entschlüsseln
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Beim Verschlüsseln von Daten gibt es nun zwei Möglichkeiten:

* Möchte man eine Datei mit dem eigenen privaten Schlüssel verschlüsseln (so
  dass man sie also nur selbst wieder entschlüsseln kann), so wird ohne weitere
  Vorgaben der Standard-Schlüssel verwendet; ebenso kann man mit der Option ``-u
  UserID`` gezielt einen Schlüssel auswählen. [#]_

* Möchte man eine Datei verschlüsselt an einen anderen Empfänger ("Recipient")
  schicken, so kann der Schlüssel dieses Empfängers mittels der Option ``-r
  UserID`` ausgewählt werden.

Die eigentliche Anweisung zum Verschlüsseln einer Datei lautet:

.. code-block:: sh

    # Datei verschlüsseln:
    gpg -e Empfaenger Datei

Hierbei steht ``-e`` als Kurzform für die gleichbedeutende Option ``--encrypt``.

Zusätzlich zu einer Verschlüsselung ist es stets sinnvoll, die Datei auch noch
zu signieren.

.. code-block:: sh

    # Datei verschlüsseln und signieren:
    gpg -u SenderID -r EmpfaengerID --armor --sign --encrypt Datei

    # Datei verschlüsseln und signieren (Kurzform):
    gpg -u SenderID -r EmpfaengerID -a -s -e Datei

Das rekursive Verschlüsseln eines Verzeichnisses mitsamt Unterverzeichnissen ist
nicht möglich; hierfür muss zunächst beispielsweise mittels :ref:`tar <tar>`
oder :ref:`zip <zip>` eine Archiv-Datei des Verzeichnisses erstellt werden.

.. Beispiel:
.. ``tar -c /home/user/* | gpg -r Empfaenger -e -o /tmp/home.tar.crypt``
.. verschlüsselt alle Dateien des Verzeichnisses ``/home/user`` in die Datei
.. ``/tmp/home.tar.crypt``. Folgende Anweisung stellt das Verzeichnis aus der
.. verschlüsselten Datei wieder her:
.. ``gpg -d /tmp/home.tar.crypt |tar -xvf -``

Wenn eine verschlüsselte Datei signiert ist, so wird beim Entschlüsseln die
Signatur automatisch mit geprüft. Die Anweisung zum Entschlüsseln einer Datei
lautet:

.. code-block:: sh

    # Datei entschlüsseln:
    gpg -d Datei

Hierbei steht ``-d`` als Kurzform für die gleichbedeutende Option ``--decrypt``.

Ohne weitere Vorgaben wird der Inhalt der Datei auf dem Standard-Ausgabe-Kanal
``stdout`` ausgegeben, üblicherweise also auf dem Bildschirm;  mittels der
Option ``-o Ausgabedatei``  wird die Ausgaben stattdessen in die angegebene
Datei geschrieben.


.. _Grenzen der Sicherheit:

.. rubric:: Grenzen der Sicherheit

Die von GPG verwendeten Algorithmen gelten allgemein bis heute als nicht
knackbar; dies bedeutet jedoch nicht automatisch, dass alle mit GPG
verschlüsselten Daten tatsächlich sicher sind. Bekommt beispielsweise ein
professionaler Angreifer (beispielsweise über einen Trojaner) Zugriff auf einen
privaten Schlüsselbund, der nur mit einem schlechten Passwort gesichert ist, so
kann er dieses weitaus leichter knacken als die mit GPG verschlüsselten Daten
selbst; mit dem privaten Schlüssel lassen sich die Daten allerdings regulär
entschlüsseln. Für die Datensicherheit ist somit auch die allgemeine
Systemsicherheit von Bedeutung.

Wie "sicher" ein Verschlüsselungs-System sein muss, hängt letztlich vom
konkreten Anwendungsfall ab: Möchte man "unkritische" private Daten nur vor
einem einfachen Fremdzugriff schützen (ähnlich wie das bei Verwendung eines
Kuverts bei einem Brief der Fall ist), so wird man sich wohl weniger Gedanken
über Sicherheit machen als wenn man beispielsweise Server-Passwörter, Bank-Daten
oder ähnlich sensible Daten verschlüsseln beziehungsweise vor Angreifern
schützen möchte.

Auch ohne Verschlüsselung ist der Einsatz von GPG sinnvoll, um beispielsweise
bei Quellcode-Paketen die Integrität der jeweiligen Daten sicherzustellen (also
ausschließen zu können, dass die jeweiligen Pakete nicht durch Dritte
manipuliert wurden); nicht umsonst gehört ``gpg`` daher zum Standard-Umfang
jeder Linux-Distribution. [#]_

.. Beim Verschlüsseln sollte man wissen, dass die verschlüsselten Dateien bzw.
.. E-Mails wirklich nur der Empfänger entschlüsseln kann, also, wenn man dieser
.. nicht ist, kann man sie auch selbst nicht mehr lesen (z. B. eine Kopie einer
.. gesendeten verschlüsselten Mail wird lokal archiviert, und man will diese später
.. wieder lesen). Um das zu ändern, ergänzt man encrypt-to eigeneID in der
.. ~/.gnupg/gpg.conf. So wird zusätzlich der eigene öffentliche Schlüssel zum
.. Verschlüsseln mitverwendet. Möchte man darauf in Ausnahmefällen wieder
.. verzichten, so gibt man die Option --no-encrypt-to an.

.. https://sks-keyservers.net/


.. rubric:: Links

* `GPG Wikibook <https://de.wikibooks.org/wiki/GnuPG>`__
* `GPG-Tutorial <http://www.online-tutorials.net/security/gnupg-gpg-tutorial/tutorials-t-69-124.html>`__
* `GPG-Anleitung <https://wiki.kairaven.de/open/krypto/gpg/gpganleitung>`__
* `GPG-Handbuch <https://www.gnupg.org/gph/de/manual/book1.html>`__

* `Seahorse -- ein GPG Frontend (Manual, en.) <https://help.gnome.org/users/seahorse/stable/>`__

.. }}}


.. {{{

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Nach einem erfolgreichen Test, ob der Login mit dem Schlüsselpaar
    funktioniert, kann man sogar, um die Sicherheit zu erhöhen, das Anmelden
    mittels Passworteingabe komplett verbieten. Hierzu werden (mit
    Superuser-Rechten) in der Datei ``/etc/ssh/sshd_config`` des Zielrechners
    folgende Einträge vorgenommen werden:

    | ``PasswordAuthentication no``
    | ``UsePAM no``

    | Damit können sich nur noch Benutzer einloggen, deren öffentliche Schlüssel
      in der jeweiligen Datei ``~/.ssh/authorized_keys`` stehen.
    | *Achtung*: Geht der SSH-Schlüssel verloren, so ist mit dieser Option kein
      Login via SSH mehr möglich!

    Sollen auch SSH-Schlüssel zugelassen werden, die nicht mit einem
    Passwort-Schutz versehen sind, muss zudem folgende Option deaktiviert sein:

    | ``StrictModes no``

    In der gleichen Datei sollte zudem ein Login als Root unbedingt verboten
    werden:

    | ``PermitRootLogin no``

    Gegebenenfalls kann ein :ref:`Benutzer mit Superuser-Rechten <su>` immer
    noch mit ``sudo`` systemweite Änderungen vornehmen oder sich mit ``sudo su
    root`` dauerhaft Superuser-Rechte verschaffen.

    Änderungen an der Datei ``/etc/ssh/sshd_config`` können mittels ``sudo
    systemctl reload sshd`` auf dem Zielrechner berücksichtigt werden.

.. [#] Die Freigabe gilt auch für andere Programme, sofern diese in der
    laufenden Sitzung vom gleichen Benutzer gestartet wurden.

.. [#] Hat man mehrere private Schlüssel, so kann man in der Konfigurationsdatei
    ``~/.gnupg/gpg.conf`` auch folgendermaßen einen Standard-Schlüssel festlegen:

    | ``# Eintrag in der Datei ~/.gnupg.conf :``
    | ``default-key  SchluesselID``

.. [#] Ein bekanntes Verfahren hierfür ist beispielsweise die so genannte
    "MD5-Prüfsumme": Nach diesem Verfahren wird zu der relevanten Datei zunächst
    über eine Hash-Funktion wie beispielsweise MD5 oder (besser) SHA-1 ein
    Hash-Wert berechnet (unter Linux gibt es dafür die Shell-Programme
    ``md5sum`` beziehungsweise ``sha1sum``). Dieser Hash-Wert wird anschließend
    vom Herausgeber mittels seines privaten Schlüssels signiert.

    Etwas vereinfacht kann man sich das so vorstellen, als würde man zu einer
    zehnstelligen Zahl die Quersumme ermitteln, also die Summe aller in der Zahl
    vorkommenden Ziffern zu berechnen. Das ist nicht wirklich schwer -- weitaus
    schwerer ist es hingegen, von dieser Quersumme auf die ursprüngliche Zahl zu
    schließen. Eine Hash-Funktion macht letztlich nichts anderes: Sie liefert zu
    einer bestimmten Dateneingabe stets einen eindeutigen Wert.

    Der Empfänger kann die Signatur wiederum mittels des öffentlichen Schlüssels
    des Herausgebers überprüfen.

    * Eine korrekte Signatur kann als Beweis dafür angesehen werden, dass der
      Hash-Wert tatsächlich vom Herausgeber stammt.

    * Anschließend kann geprüft werden, ob die Hash-Funktion bei Anwendung auf
      die heruntergeladene Datei einen identischen Hash-Wert erzeugt. Ist dies
      der Fall, so ist die Wahrscheinlichkeit sehr groß, dass die erhaltene
      Datei tatsächlich der Original-Datei entspricht.

    Inzwischen gilt `MD5 <https://de.wikipedia.org/wiki/Md5>`__ nicht mehr als
    sicher; man sollte daher besser auf einen `SHA
    <https://de.wikipedia.org/wiki/Secure_Hash_Algorithm>`__-Algorithmus
    zurückgreifen.

.. https://support.rackspace.com/how-to/connecting-to-a-server-using-ssh-on-linux-or-mac-os/

.. Aktuelle Internet-IP:
.. http://www.myipaddress.com/

.. }}}

