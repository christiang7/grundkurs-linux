
Single-Sign-On mit PAM und Kerberos
===================================

Die meisten modernen Linux-Distributionen, auch Debian/Ubuntu/LinuxMint,
verwenden das sogenannte "Pluggable Authentication Module", kurz PAM, zur
Authentifizierung von Benutzern. PAM kann man sich als Schnittstelle zwischen
einzelnen Anwendungen, die eine Authentifizierung erfordern, und möglichen
Authentifizierungs-Mechanismen vorstellen.


Möchte sich beispielsweise ein Benutzer an einem Linux-System anmelden, so prüft
PAM üblicherweise zunächst anhand der Datei ``/etc/passwd``, ob überhaupt ein
Benutzer mit dem angegebenen Namen existiert, und testet anschließend, ob das
angegebene Passwort mit dem in der Datei ``/etc/shadow`` verschlüsselt
hinterlegten Passwort übereinstimmt; erst nach beiden Tests wird der Benutzer
zugelassen oder mit einer Fehlermeldung abgelehnt. Bei entsprechender
Konfiguration kann PAM anstelle der Einträge in den Dateien ``/etc/passwd``
beziehungsweise ``/etc/shadow`` allerdings auch beispielsweise ein
LDAP-Verzeichnis zur Authentifizierung nutzen und/oder mit Kerberos
zusammenarbeiten.



Grundlegende Funktionsweise von PAM
-----------------------------------

Für viele Dienste, die PAM nutzen, gibt es eine eigene Konfigurationsdatei im
Verzeichnis ``/etc/pam.d``. Existiert für einen Dienst keine eigene
Konfigurationsdatei, so werden die Einstellungen aus ``/etc/pam.d/other``
verwendet.

Jede der Dateien in ``/etc/pam.d`` enthält ausführliche Kommentare, deren Zeilen
jeweils mit ``#`` beginnen. Ansonsten bestehen die Dateien aus Abfolgen
einzelner Regeln, wobei für jede Regel eine neue Zeile begonnen wird. Überlange
Zeilen können mit ``\`` beendet und mit einer Einrückung (Tab) in der folgenden
Zeile fortgesetzt werden.

Die allgemeine Syntax hierbei lautet:

::

    type control module-path module-arguments

Neben ``@include``-Anweisungen, die auf Debian-basierten Systemen üblich sind
und zum Einbinden weiterer PAM-Dateien an der jeweiligen Stelle genutzt werden,
beginnen also alle Zeilen mit einem "Modul-Typ". Die vier möglichen Typen sind:

* ``account``: Hiermit wird unabhängig von einer Authorisierung geprüft, ob ein
  Zugriff auf einen Dienst für einen Benutzer erlaubt ist -- beispielsweise in
  Abhängigkeit von der Uhrzeit, der Anzahl der bereits angemeldeten Benutzer,
  der Existenz eines Benutzer-Accounts, oder der Gültigkeit eines Benutzers an
  einer bestimmten Stelle (beispielsweise ``root``-Login via SSH).

* ``auth``: Hiermit wird ein Mechanismus für eine Benutzer-Authentifizierung
  festgelegt: Die seitens des aufrufenden Programms erfolgte Passwort-Abfrage
  wird geprüft. Gegebenenfalls können daraufhin Rechte freigeschaltet werden.

* ``password``: Hiermit werden Regeln für das Ändern von Passwörtern festgelegt,
  beispielsweise ein Prüfen der Länge des angegebenen Passworts.

* ``session``: Hiermit wird festgelegt, welche Aktionen zu Beginn oder am Ende
  einer Sitzung ausgeführt werden sollen -- beispielsweise das Einhängen eines
  Home-Verzeichnisses, Logging, usw.

.. Limits, Berechtigungen ... während des Zugriffs.

.. Die Module werden vor und nach der Authentifizierung gestartet um etwas zu
.. protokolieren und dem Benutzer seine eigene Umgebung zuzuweisen.

.. (z.B. Homeverzeichnis)

Der darauf folgende ``control``-Parameter gibt an, wie sich PAM verhalten soll,
wenn das angegebene Authentifizierungs-Modul erfolgreich oder mit einem Fehler
beendet wird. Die klassischen Parameter hierbei sind:

.. Modulsteuerung

* ``required``: Das angegebene Modul muss mit Erfolg enden. Tritt ein Fehler
  auf, so werden die weiteren Module abgearbeitet.

* ``requisite``: Das angegebene Modul muss mit Erfolg enden. Tritt ein Fehler
  auf, so werden keine weiteren Module abgearbeitet.

* ``sufficient``: Wenn das angegebene Modul erfolgreich endet, so genügt dies
  bereits. Es werden keine weiteren Module abgearbeitet.

* ``optional``: Das Ergebnis dieses Moduls findet keine Beachtung -- außer, es
  ist das einzige für einen Modul-Typ.


Komplexere ``control``-Parameter können mit folgender Syntax angegeben werden:

::

    [wert1=aktion1 wert2=aktion2 ...]

Als Wert ist ``success`` möglich, oder einer von vielen möglichen Fehlern wie
``perm_denied``, ``system_err``, ``service_err``, ``auth_err``,
``user_unknown``, usw. Als Aktionen sind folgende möglich:

.. Mögliche Werte:

.. success, open_err, symbol_err, service_err, system_err, buf_err, perm_denied,
.. auth_err, cred_insufficient, authinfo_unavail, user_unknown, maxtries,
.. new_authtok_reqd, acct_expired, session_err, cred_unavail, cred_expired,
.. cred_err, no_module_data, conv_err, authtok_err, authtok_recover_err,
.. authtok_lock_busy, authtok_disable_aging, try_again, ignore, abort,
.. authtok_expired, module_unknown, bad_item, conv_again, incomplete, default.

.. default means "all values not mentioned explicitly".

.. Note, the full list of PAM errors is available in
.. ``/usr/include/security/_pam_types.h``. The ``actionN`` can take one of the
.. following forms:

ignore
    Der Rückgabewert des Moduls ist für das Endergebnis der gesamten Modul-Kette
    ohne Bedeutung.

bad
    Der Rückgabewert des Moduls wird als Fehler interpretiert; die weiteren
    Module werden jedoch weiter abgearbeitet.

die
    Der Rückgabewert des Moduls wird -- ebenso wie ``bad`` -- als Fehler
    interpretiert; es werden keine weiteren Module mehr abgearbeitet.

ok
    Der Rückgabewert des Moduls wird als Erfolg interpretiert, die weiteren
    Module werden abgearbeitet. Tritt kein Fehler mehr auf, so wird die
    Modul-Kette am Ende damit insgesamt als "erfolgreich durchlaufen" angesehen.

    Gab es jedoch bereits vorab einen Rückgabewert, der mit ``bad`` bewertet
    wurde, so wird die Einschätzung, dass ein Fehler vorliegt, durch das ``ok``
    nicht revidiert.

done
    Der Rückgabewert des Moduls wird -- ebenso wie ``ok`` -- als Erfolg
    interpretiert. Es werden allerdings keine weiteren Module mehr abgearbeitet,
    stattdessen erfolgt ein Sprung zum Ende der Modul-Kette.

n (Zahlenwert)
    Der Rückgabewert des Moduls wird -- ebenso wie ``ok`` -- als Erfolg
    interpretiert; zudem werden die nächsten ``n`` Module der Kette übersprungen.
    ``n=0`` ist nicht erlaubt -- dies wäre identisch mit ``ok``.

reset
    Hiermit werden alle vorherigen Ergebnis-Interpretationen zurückgesetzt. Die
    weiteren Module werden regulär abgearbeitet.

Die "klassischen" ``control``-Parameter lassen sich gemäß der folgenden Tabelle
mittels der obigen, komplexeren Steuer-Anweisungen ausdrücken:

    +-----------------------+----------------------------------------------------------------+
    | Klassischer Parameter | Entsprechende Wert-Aktions-Liste                               |
    +-----------------------+----------------------------------------------------------------+
    | ``required``          | ``[success=ok new_authtok_reqd=ok ignore=ignore default=bad]`` |
    +-----------------------+----------------------------------------------------------------+
    | ``requisite``         | ``[success=ok new_authtok_reqd=ok ignore=ignore default=die]`` |
    +-----------------------+----------------------------------------------------------------+
    | ``sufficient``        | ``[success=done new_authtok_reqd=done default=ignore]``        |
    +-----------------------+----------------------------------------------------------------+
    | ``optional``          | ``[success=ok new_authtok_reqd=ok default=ignore]``            |
    +-----------------------+----------------------------------------------------------------+

Die eigentlichen PAM-Module werden in jeder Zeile als drittes Argument
angegeben. Wahlweise können hierbei absolute Pfade zu den Modulen angegeben
werden (beginnend mit ``/``), oder es werden Dateinamen relativ zum Verzeichnis
``/lib/security`` angegeben -- dort sind die einzelnen PAM-Module üblicherweise
hinterlegt.


               +------------------+-------------------------------------------------------------+
               | pam_securetty    | Login als root nur an "sicheren" Terminals                  |
               |                  | (definiert in /etc/securetty)                               |
               +------------------+-------------------------------------------------------------+
               | pam_env          | Setzen/Löschen von Umgebunsvariablen                        |
               |                  | (definiert in /etc/security/pam_env.conf)                   |
               +------------------+-------------------------------------------------------------+
               | pam_nologin      | falls /etc/nologin existiert, nur noch Login als root       |
               |                  | erlauben                                                    |
               +------------------+-------------------------------------------------------------+
               | pam_krb5         | Authentisierung via Kerberos V5                             |
               |                  | (Konfiguration in /etc/krb5.conf)                           |
               +------------------+-------------------------------------------------------------+
               | pam_unix         | Authentisierung via traditioneller Unix-Mittel              |
               |                  | (Passwort-Hashes - md5/crypt)                               |
               |                  | beeinflusst durch /etc/nsswitch.conf                        |
               +------------------+-------------------------------------------------------------+
               | pam_deny         | liefert immer Misserfolg                                    |
               +------------------+-------------------------------------------------------------+
               | pam_login_access | Zugangsvoraussetzungen in                                   |
               |                  | /etc/login.access (auch pam_access)                         |
               +------------------+-------------------------------------------------------------+
               | pam_limits       | Einstellen von Limits   definiert in                        |
               |                  | /etc/security/limits.conf                                   |
               +------------------+-------------------------------------------------------------+
               | pam_console      | Übertragen/Entziehen von Berechtigungen des Konsole-Nutzers |
               |                  | definiert in etc/security/console.apps                      |
               |                  | und /etc/security/console.perms                             |
               +------------------+-------------------------------------------------------------+

* zahlreiche Module gehören zum Paketumfang von Linux-PAM; siehe
  http://www.kernel.org/pub/linux/libs/pam/Linux-PAM-html/Linux-PAM_SAG.html

  - pam_listfile
        Zugangssteuerung auf Basis von ASCII-Files 

  - pam_userdb
        zusätzliche lokale Passwort-Datenbasis auswerten 

  - pam_mkhomedir
        HOME-Verzeichnis bei erster Anmeldung des Nutzers einrichten 

  - pam_time 
        zeitabhängige Zugangssteuerung 

* einige PAM-Module als eigenständige Projekte, teilweise in Paketform in
  Distributionen integriert

  - pam_krb5
        Original-Quelle: http://people.redhat.com/nalin/pam_krb5/ 
  - pam_ldap, pam_ccreds
        Original-Quelle: http://www.padl.com/Contents/OpenSourceSoftware.html 
  - pam_login_access
        https://www-user.tu-chemnitz.de/~mibe/sw/OpenPBS/#pam_login_access 


.. To configure just LDAP authentication on your client install the pam & nsswitch
.. modules

.. apt-get install libpam-ldapd libnss-ldapd

.. The LDAPd debconf scripts helpfully prompt for several of the important
.. configuration options.

.. libpam-ldapd

.. /usr/share/pam-configs/mkhomedir

.. libpam-ldapd uses the same backend (nslcd) as libnss-ldapd, and thus also shares
.. the same configuration file (/etc/nslcd.conf) for LDAP connection parameters.

.. dpkg-reconfigure libpam-runtime

.. Datei ``/usr/share/pam-configs/mkhomedir``:

.. Name: Create home directory during login
.. Default: yes
.. Priority: 900
.. Session-Type: Additional
.. Session:
..         required        pam_mkhomedir.so umask=0027 skel=/etc/skel

.. and run command

.. .. code-block:: sh

..     sudo pam-auth-update


.. Die PAM-Module befinden sich meist im Verzeichnis ``/lib/security``.

.. NIS (Network Information Service) wird als Verzeichnisdienst immer mehr durch
.. Kerberos und LDAP ersetzt

.. Guter Test:
.. Base-DN anzeigen:
.. ldapsearch -h localhost -x -s base | grep '^dn:'

.. # LDIF für neue Gruppe:
.. dn: ou=users, dc=emile, dc=aux
.. objectClass: organizationalUnit
.. objectClass: top
.. ou: users
..
.. dn: ou=groups, dc=emile, dc=aux
.. objectClass: organizationalUnit
.. objectClass: top
.. ou: groups

.. dn: cn=Bernhard Grotz, ou=users, dc=emile, dc=aux
.. cn: Bernhard Grotz
.. sn: Grotz
.. givenName: Bernhard
.. gecos: Bernhard Grotz
.. objectclass: top
.. objectclass: person
.. objectclass: inetOrgPerson
.. objectclass: organizationalPerson
.. objectclass: posixAccount
.. objectclass: shadowAccount
.. objectclass: top
.. uid: bgrotz
.. userpassword:{SSHA}MGIK2m78xFB1z7R6tJCsaFv46+JMFXpy
.. uidnumber: 1020
.. gidnumber: 1020
.. loginShell: /usr/bin/zsh
.. homeDirectory: /home/bgrotz

.. # LDIF für neuen Benutzer:

.. Achtung! posixgroup kann nicht in Verbindung mit inetorgperson verwendet werden!
.. (beides strukturelle Klassen)

.. person anstelle von inetorgperson reicht auch bereits.. will dann nur vor-
.. und nachnamen

.. ldapsearch -x  -LLL -b 'dc=emile,dc=aux' '(objectclass=*)'

.. cool: ldapsearch -x -LLL uid=bgrotz

.. It is possible to test authentication for an LDAP account with the
.. ``ldapwhoami`` command:

.. ldapwhoami -x -D uid=bgrotz,ou=users,dc=emile,dc=aux -W

.. ldapwhoami -x
.. Ergebnis: anonymous


.. Test, ob Kerberos installiert ist und läuft:
.. nmap -sU -sT -p U:88,464,T:464,749 desktop.emile.aux

.. Test, ob LDAP-Server im Netzwerk verfügbar ist
.. nmap -p 389 desktop.emile.aux

.. .. code-block:: sh

..     apt-get install ldap-utils libnss-ldap libpam-ldap nscd libsasl2-modules-gssapi-mit

.. During the installation procedure, certain questions will be asked about two of
.. these packages, first, about libnss-ldap. Answer them as follows:

.. LDAP server URI: ldap://kls1.example.com/ ldap://kls2.example.com/
.. Distinguished name of the search base: dc=example,dc=com
.. LDAP version to use: 3
.. Does the LDAP database require login? No
.. Special LDAP privileges for root? No
.. Make the configuration file readable/writeable by its owner only? No

.. These six questions are immediately followed by four more regarding
.. libpam-ldap. Answer them as follows:

.. Allow LDAP admin account to behave like local root? No
.. Does the LDAP database require login?: No
.. Local encryption algorithm to use for passwords: crypt

.. At this point, man-db also has a question that needs answering:

.. Should man and mandb be installed 'setuid man'? No

.. Finally, libpam-runtime asks a general PAM configuration question:

.. PAM profiles to enable: (leave only Kerberos and Unix authentication selected)

.. KRB5_TRACE


.. FQDN setzen:

.. * You'll want to edit ``/etc/hostname`` with your new hostname.
.. * Then, run ``sudo hostname $(cat /etc/hostname)``.
.. * Then, in ``/etc/resolvconf/resolv.conf.d/head``, you'll add then line search
..   your.domain.name (not your FQDN, just the domainname).
.. * Then, run ``sudo resolvconf -u`` to update your ``/etc/resolv.conf``
..   (alternatively, just reproduce the previous change into your
..   ``/etc/resolv.conf``).
.. * Finally, update your ``/etc/hosts`` file. There should be at least one line
..   starting with one of your IP (loopback or not), your FQDN and your hostname.
..   grepping out ipv6 addresses, your hosts file could look like this:

.. 127.0.0.1 localhost
.. 1.2.3.4 service.domain.com service

.. https://unix.stackexchange.com/questions/322883/how-to-correctly-set-hostname-and-domain-name




 Links
 -----

 * `OpenLDAP Administrator's Guide (en.) <http://www.openldap.org/doc/admin24/index.html>`__
 * `LDAP Guide and Reference (en.) <http://www.zytrax.com/books/ldap/>`__
 * `LDAP verstehen (de.) <http://www.mitlinx.de/ldap/>`__
* `Python LDAP3-Module Tutorial (en.) <http://ldap3.readthedocs.io/tutorial.html>`__

.. LDAP kann Cyrus SASL verwenden

.. https://www.cyrusimap.org/sasl/sasl/options.html#ldapdb

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Genau gehört jedes LDAP-Objekt *genau einer* ``STRUCTURAL``-Objektklasse
    an, die das Objekt im Wesentlichen charakterisiert. Zusätzlich können
    weitere ``AUXILIARY``-Objektklassen hinzugefügt werden, um weitere Attribute
    für das Objekt festzulegen.

    Um welchen dieser beiden Typen es sich bei einer Objektklasse handelt, kann
    aus der Definition der Objektklasse in der jeweiligen :ref:`Schema
    <LDAP-Schema>`-Datei entnommen werden.




