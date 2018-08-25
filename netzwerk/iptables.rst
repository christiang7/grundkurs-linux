
Firewalls mit ``iptables``
==========================

Bei `iptables <https://wiki.ubuntuusers.de/iptables2>`__ handelt es sich weniger
um ein "Programm", sondern eher um ein Interface zur "Netfilter"-Firewall des
Linux-Kernels.

Ist ``iptables`` aktiv, so werden alle eingehenden IP-Pakete geprüft, bevor sie
an die Ziel-Anwendungen weitergeleitet werden; ebenso werden alle ausgehenden
Daten-Pakete geprüft, bevor sie den Rechner verlassen. Bei entsprechenden
Einstellungen kann ``iptables`` die Pakete sogar verändern.

.. Die Paketprüfung und die mit iptables zu erstellenden Filterregeln sind
.. dreistufig aufgebaut. Es gibt (hierarchisch von oben nach unten):
 
.. * Tabellen
.. * sogenannte "Chains" (Ketten)
.. * die eigentliche Filterregeln

.. Trifft eine in einer Tabelle und Chain definierte Regel zu, so wird die in der
.. Regel hinterlegte Aktion ausgeführt. Sollte keine Regel zutreffen (was durchaus
.. nichts ungewöhnliches ist), so wird die in der Tabelle hinterlegte, allgemein
.. gültige Policy angewendet.


.. Agiert der Rechner als Router (z.B. in einem Netzwerk), so werden die Pakete
.. während der Weiterleitung geprüft. 

... to be continued ...


