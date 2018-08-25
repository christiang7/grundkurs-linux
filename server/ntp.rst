.. index:: NTP
.. _NTP:
.. _ntpd:
.. _ntpdate:
.. _Zeitabgleich mit NTP:

Zeitabgleich mit ``ntp``
========================
.. {{{

Auf Desktop-Rechnern und Notebooks ist auf dem Mainboard üblicherweise eine
CMOS-Uhr eingebaut. Diese wird von einer eigenen Batterie gespeist und läuft
auch weiter, wenn der Rechner ausgeschaltet ist. Wenn man ohne Verbindung zum
Internet nach einiger Zeit den Rechner wieder anschaltet, so bekommt man
weiterhin eine augenscheinlich korrekte Uhrzeit angezeigt.

Für viele Zwecke ist die CMOS-Uhr ausreichend genau. Es gibt allerdings durchaus
auch Anwendungen, bei denen die Systemzeit *exakt* stimmen sollte --
beispielsweise, wenn ein bidirektionales Synchronisierungs-Programm wie
:ref:`bsync <bsync>` auf zwei verschiedenen Rechnern prüfen möchte, auf welchem
der beiden eine bestimmte Datei zuletzt geändert wurde.

.. localet

In einem Netzwerk ist es allgemein sinnvoll, dass alle Rechner-Uhren aufeinander
abgestimmt sind. Hierfür bietet sich das "Network Time Protocol" (NTP) an. Der
entsprechende Hintergrund-Dienst ``ntpd`` kann unter Debian/Ubuntu/LinuxMint
folgendermaßen installiert werden:

.. code-block:: sh

    sudo aptitude install ntp ntpdate

Mittels ``ntpdate`` kann die aktuelle Zeit des Rechners mit einem
externen Rechner-Netzwerk synchronisiert werden. Diese Anweisung sollte
einmalig ausgeführt werden, bevor der eigentliche Hintergrund-Dienst
genutzt wird.

Da der Dienst ``ntpd`` bereits oftmals im Rahmen der Installation automatisch
gestartet wird, ist es empfehlenswert, diesen zwischenzeitlich zu beenden:

.. code-block:: sh

    # NTP stoppen:
    sudo systemctl stop ntp

    # Rechnerzeit aktualisieren:
    sudo ntpdate de.pool.ntp.org

    # NTP wieder starten:
    sudo systemctl start ntp

Der Grund für das zwischenzeitliche Deaktivieren des NTP-Dienstes liegt darin,
dass die Systemzeit nicht sprunghaft geändert werden sollte -- dies kann
beispielsweise bei Mailservern oder Logging-Diensten zu Komplikationen führen. 
Der Dienst ``ntpd`` vergleicht daher kontinuierlich die Systemzeit mit den
Zeiten des externen Rechner-Pools, und lässt bei Bedarf die eigene CMOS-Uhr
etwas schneller beziehungsweise langsamer laufen, bis die Zeiten wieder
möglichst exakt übereinstimmen.

Die Abweichungen der aktuellen Systemzeit von den Zeiten der anderen Rechner im
NTP-Pool kann man sich folgendermaßen anzeigen lassen:

.. code-block:: sh

    sudo ntpq -p

    # Mögliches Ergebnis:
         remote           refid      st t when poll reach   delay   offset  jitter
    ==============================================================================
     0.ubuntu.pool.n .POOL.          16 p    -   64    0    0.000    0.000   0.000
    +spacys.de       36.224.68.195    2 u   27   64   37   32.067   -1.310   2.473
    +alpha.rueckgr.a 130.149.17.8     2 u   32   64   37   33.030   -2.245   1.659
    #news01.nierle.c 192.53.103.108   2 u   26   64   37   33.003    2.832   1.444
    #re.uni-paderbor 131.234.137.63   2 u   26   64   37   37.210   -8.801   0.833
    +muenchen.kumi.s 131.188.3.220    2 u   18   64   37   37.077   -2.460   0.848

Entscheidend ist hierbei vor allem die Spalte ``offset``, welche die Abweichung
von der Systemzeit der anderen Rechnern in Millisekunden angibt. Liegt der
aktuelle Wert dort über 1000 (was einer Sekunde enstspricht), so sollte die
Systemzeit wie oben beschrieben mittels ``ntpdate`` manuell synchronisiert
werden.

.. Man kann anstelle eines Pools auch einen lokalen Server verwenden.
.. Dieser sollte in den Konfigurationsdateien /etd/ntp.conf und 
.. /etc/default/ntpdate identisch sein.

.. # Test, ob NTP beim Start automatisch geladen wird:
.. sudo systemctl is-enabled ntp

.. # Bei Bedarf: NTP beim Systemstart automatisch laden:
.. sudo systemctl enable ntp


.. }}}

