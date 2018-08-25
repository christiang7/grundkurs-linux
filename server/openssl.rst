
.. index:: OpenSSL, TLS-Zertifikat, Zertifikate
.. _openssl:
.. _Eigene Zertifikate mit openssl:

Eigene Zertifikate mit ``openssl``
===================================
.. {{{

Benötigt man einzelne TSL-Zertifikate für einen öffentlich erreichbaren Server,
beispielsweise einen Web- oder Mailserver, so ist es empfehlenswert, das
:ref:`Certbot <Certbot>`-Projekt zu nutzen.

Möchte man hingegen eine verschlüsselte Kommunikation zwischen verschiedenen
Rechnern innerhalb eines lokalen Netzwerkes erreichen, so macht es durchaus
Sinn, eine eigene Zertifizierungs-Stelle ("Certificat Authority, kurz CA) zu
betreiben: Zertifikaten, die man selbst erstellt hat, kann man guten Gewissens
vertrauen.

Zum Erstellen eigener TLS-Zertifikate ist das Paket ``openssl`` nötig, das
mittels des gleichnamigen Pakets installiert werden kann:

.. code-block:: sh

    sudo aptitude install openssl

.. Empfehleswert ist es, sich ein eigenes Verzeichnis für die Benutzung von
.. ``openssl`` anzulegen, beispielsweise ``/root/openssl``:

.. .. code-block:: sh

..     # OpenSSL-Verzeichnis erstellen:
..     sudo mkdir /root/openssl
..     cd /root/openssl

``openssl`` wird üblicherweise mit mehreren Argumenten aufgerufen; eine gut
navigierbare Übersicht bietet die `offizielle Dokumentation
<https://www.openssl.org/docs/manmaster/man1/openssl.html>`__.

.. }}}

Einrichten einer Zertifizierungs-Stelle (CA)
--------------------------------------------
.. {{{

Um eigene Zertifikate ausstellen und signieren zu können, muss zunächst eine so
genannte Zertifizierungs-Stelle (CA) erstellt werden. Dabei handelt es sich um
ein spezielles Zertifikat, mit dessen Hilfe weitere Zertifikate signiert werden
können.

Das CA-Zertifikat sollte nicht in falsche Hände geraten, denn damit könnten
weitere Zertifikate ausgestellt und signiert werden, die wiederum von allen
Clients im Netzwerk als glaubhaft eingestuft werden würden. Es ist daher ratsam,
diese Datei mit einem Passwort-Schutz zu versehen. Dies kann man erreichen,
indem für das CA-Zertifikat ein privater Schlüssel mit Passwort-Schutz erstellt
wird:

.. code-block:: sh

    # CA-Schlüssel erstellen:
    openssl genrsa -aes256 -out ca-key.pem 4096

    # Zugriffsrechte für den privaten Schlüssel einschränken:
    chmod 600 ca-key.pem

Beim Erstellen des Schlüssels muss ein möglichst sicheres Passwort (oder ein
Passwort-Satz) zweimal eingegeben werden. Dieses Passwort wird jedes Mal beim
Erstellen eines neuen Zertifikats benötigt, es ist also empfehlenswert, das
Passwort mit :ref:`keepassx <keepassx>` oder :ref:`pass <pass>` sicher und
leicht wieder auffindbar zu verwahren.


``openssl`` besteht aus mehreren Unterprogrammen; mit ``openssl genrsa`` wird
beispielsweise ein neuer RSA-Schlüssel erstellt. Die Option ``-aes256`` gibt den
Verschlüsselungs-Mechanismus an (optional kann auch ``-sha512`` verwendet
werden), die Zahl ``4096`` die Länge des zu erstellenden Schlüssels. Durch den
Aufruf dieser Anweisung wird im ``openssl``-Verzeichnis eine neuer privater
Schlüssel namens ``ca-key.pem`` erstellt (die Endung ``.pem`` ist sowohl für
Zertifikate als auch für die entsprechenden Schlüssel üblich).


Ein weiteres wichtiges Unterprogramm ist ``openssl req``, mit dem man einen
Antrag für ein neues Zertifikat (Certificate Signing Request, kurz CSR) stellen
kann. Mit der Option ``-key`` kann der zum künftigen Zertifikat gehörende
(private) Schlüssel, mit der Option ``-out`` der Name des künftigen Zertifikats
angegeben werden.

Zum Erstellen der CA wird ebenfalls ``openssl req`` verwendet, allerdings mit
der zusätzlichen Option ``-x509``. Diese Option bewirkt, dass ein
selbst-signiertes Zertifikat anstelle einer gewöhnlichen Zertifikats-Anfrage
ausgegeben wird:

.. code-block:: sh

    # CA-Zertifikat erstellen:
    openssl req -x509 -new -extensions v3_ca -key ca-key.pem \
            -out ca-cert.pem -days 3650

Beim Ausführen der obigen Anweisung erscheint ein Frage-Katalog. Die einzelnen
Einträge sind weitgehend selbsterklärend: Als ``Country Name`` gibt man
beispielsweise ``DE`` als Länderkennung für Deutschland ein. Für ``State or
Province`` gibt man den Namen des Bundeslandes an, für ``Locality`` den Namen
der Stadt, in deren Umfeld man wohnt (beziehungsweise die Firma/Domain
angesiedelt ist, für die das Zertifikat erstellt werden soll). Als
``Organization Name`` gibt man den Namen der Firma oder den Namen der Domain
an (meist ohne Endung). als ``Organization Unit Name`` kann man beispielsweise
``IT`` angeben. Als ``Common Name`` kann für das CA-Zertifikat der eigene Name
angegeben werden.

Die Option ``-extensions v3_ca`` bewirkt, dass die Einstellungen aus der Datei
``/etc/ssl/openssl.cnf``, die dort unter der Rubrik ``v3_ca`` aufgelistet sind,
berücksichtigt werden. Über die Option ``-days 3650`` wird festgelegt, dass
das CA-Zertifikat eine Gültigkeitsdauer von zehn Jahren erhalten soll. Der
Zeitraum ist deshalb so lange gewählt, da mit dem Ablauf des CA-Zertifikats auch
alle damit signierten (normalen) Zertikate ihre Gültigkeit verlieren.

Es ist alternativ auch möglich, das Zertifikat und den privaten Schlüssel mit
nur einer Anweisung zu generieren:

.. code-block:: sh

    # CA-Zertifikat und Schlüssel auf einmal (optional):
    openssl req -x509 -new -extensions v3_ca -newkey rsa:4096 -keyout ca-key.pem \
           -out ca-cert.pem -days 3650

Hierbei wir mittels ``-newkey rsa:4096`` die Schlüssel-Länge angegeben, und mit
:math:`-keyout ca-key.pem`` der Name des zu erstellenden Schlüssels.


Das CA-Zertifikat entspricht dem "Public Key" der Zertifizierungsstelle. Damit
ein Rechner selbst erstellte Zertifikate ohne Warnungen akzeptiert, muss neben
dem eigentlichen Zertifikat auch das CA-Zertifikat ``ca-cert.pem`` importiert
werden.


.. }}}

Erstellung eines signierten Zertifikats
---------------------------------------
.. {{

Auch für ein gewöhnliches Zertifikat, das für eine bestimmte Domain ausgestellt
wird, muss zunächst wieder ein privater Schlüssel generiert werden:

.. code-block:: sh

    openssl genrsa -out example-one-de-key.pem 4096

In diesem Fall soll der Schlüssel allerdings nicht mit einem Passwort versehen
werden, denn ansonsten müsste beispielsweise bei jedem Neustart des Webservers,
der das Zertifikat nutzt, ein Passwort für den Schlüssel eingegeben werden. Bei
der Passwort-Nachfrage wird somit lediglich ``Enter`` eingegeben, also kein
Passwort angegeben.

Anschließend wird mittels ``openssl req`` die eigentliche Zertifikats-Anfrage
gestellt. Hierbei sollte nun der Name des Zertifikats in Anlehnung an den Namen
der Domain gewählt werden, für die das Zertifikat bestimmt ist:

.. code-block:: sh

    # Zertifizierungs-Request:
    openssl req -new -key example-one-de-key.pem -out example-one-de-cert.csr

Wie beim CA-Zertifikat müssen auch hier Angaben zu Stadt, Land und Organisation
gemacht werden. Besonders wichtig ist an dieser Stelle das Attribut ``Common
Name``: Hier muss in diesem Fall der Domain-Name des Servers angegeben werden,
beispielsweise ``example-one.de``. Die letzten beiden Angaben -- das ``Challenge
Passwort`` und der ``Optional Company Name`` -- sind beide optional, können also
leer gelassen werden.

Gibt man optional als ``Common Name`` anstelle von ``example-one.de``
``*.example-one.de`` an, so wird ein so genanntes "Wildcard"-Zertifikat
erstellt, das für alle Subdomains der angegebenen Domain gültig ist -- jedoch
nicht für die Domain selbst.

Zusätzlich zum Zertifikat muss ein öffentlicher Schlüssel erstellt werden;
dieser wird zusammen mit dem privaten Schlüssel des Zertifikats für die
TLS-Verschlüsselung benötigt. Ein solcher Schlüssel kann mittels der Anweisung
``openssl x509`` erstellt werden:

.. code-block:: sh

    openssl x509 -req -in example-one-de-cert.csr -CA ca-cert.pem -CAkey ca-key.pem \
                -CAcreateserial -out example-one-de-pub.pem -days 365

Hierbei wird das Passwort für das CA-Zertifikat benötigt.

Nach dem Ausführen der obigen Anweisungen existieren drei Dateien im aktuellen
Verzeichnis: Der öffentliche Schlüssel (Endung ``-pub.pem``), der private
Schlüssel (Endung ``-key.pem``), und die Anfrage-Datei (Endung ``.csr``).
Die Anfrage-Datei mit der Endung ``.csr`` wird nicht weiter benötigt,
entscheidend sind die beiden ``.pem``-Dateien.

Die Zertifizierungsanfrage zertifikat.csr kann gelöscht werden -- sie wird nicht
mehr benötigt. Übrig bleiben Private Key und Public Key des neuen Zertifikats
(zertifikat-key.pem und zertifikat-pub.pem) sowie Private- und Public Key der CA
(ca-key.pem und ca-root.pem)


Den privaten Schlüssel benötigt der HTTP-Server um den Traffic zu verschlüsseln.
Dein Browser entschlüsselt das dann mit dem öffentlichen Schlüssel. Sendest du
nun weitere Anfragen (GET, POST, PUT, etc..) werden diese mit dem öffentlichen
Schlüssel verschlüsselt und der Server entschlüsselt diese mit dem Privaten.
Ohne privaten Schlüssel ist also keine Kommunikation möglich. 


.. openssl x509 -in cert.pem -text -noout
.. openssl x509 -in cert.cer -text -noout
.. openssl x509 -in cert.crt -text -noout




Der Inhalt derartiger Dateien beginnt stets mit ``-----BEGIN
CERTIFICATE-----`` und endet mit ``-----END CERTIFICATE-----``.

Nach dem Erstellen muss das Zertifikat entweder selbst oder von einer externen
Zertifizierungs-Stelle (CA) signiert werden.

.. code-block:: sh

    # Eigenes Zertifikat erstellen
    openssl x509


Man kann beide Schritte, also das Erstellen eines Schlüssels und eines
Zertifikats, auch mit nur einer einzigen Anweisung erreichen, indem man
``openssl req`` mit der zusätzlichen Option ``-x509`` aufruft und den Dateinamen
des zu erstellenden Schlüssels mittels der Option ``-keyout`` angibt:

.. code-block:: sh

    openssl req -new -x509 -keyout example-one.de.pem \
                -out example-one.de.pem -days 365 -nodes

.. ``openssl req`` kennt auch die Option ``-new -x509 -newkey -rsa:2048 -keyout cakey.pem -out cacert.pem -days 3650``.


Zertifikate aktivieren
----------------------

Die Zertifikats-Stellen, denen der eigene Rechner vertraut, sind üblicherweies
im Verzeichnis ``/usr/share/ca-certificates`` abgelegt. Zertifikate, die mittels
dieser CAs erstellt wurden, werden von ``openssl`` im Verzeichnis
``/etc/ssl/certs`` abgelegt und dort zusätzlich in der Datei
``/etc/ssl/ca-certificates.crt`` zusammengefasst.

Welchen Zertifizierungs-Stellen vertraut wird, kann mittels ``dpkg-reconfigure
ca-certificates`` neu konfiguriert werden:

.. code-block:: sh

    sudo dpkg-reconfigure ca-certificates

Insbesondere kann somit das CA-Zertifikat als vertrauenswürdig eingestuft
werden.


.. Wir empfehlen bei jeder Verlängerung einen neuen Schlüssel zu generieren.


.. To use a local certificate authority, you'll should install your certificate
.. root into /usr/local/share/ca-certificate it will neeed to be named <useful
.. name>.crt in the share/ca-certificate directory. When it gets symlinked into
.. /etc/ssl/certs, it will be renamed as <useful name>.pem.

.. Run

.. $ update-ca-certificates

.. to install the certificate into /etc/ssl/certs.

.. Once your certificate is ready you should update nslcd.conf to use your
.. certificate authority.


Links
-----

* `OpenSSL Online Manpage (en.) <https://www.openssl.org/docs/manmaster/man1/openssl.html>`__



