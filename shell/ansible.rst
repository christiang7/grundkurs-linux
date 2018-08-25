
.. _ansible:
.. _Konfigurations-Verwaltung mittels ansible:

Konfigurations-Verwaltung mittels ``ansible``
=============================================

`Ansible <https://www.ansible.com/>`__ ist ein
Konfigurations-Verwaltungs-Programm, mit dessen Hilfe es möglich ist, von einem
Computer aus Installations- und Konfigurations-Routinen simultan auf beliebig
vielen anderen Rechnern auszuführen. Die Voraussetzung dafür ist lediglich, dass
der auf dem Tower angemeldete Benutzer sich via :ref:`SSH <SSH>` auf den anderen
Rechnern anmelden kann und dort gegebenenfalls SuperUser-Rechte bekommen kann.
Auf den Clients selbst muss keine weitere Software installiert werden.

.. _Tower:

Der grundlegende Workflow von Ansible ist also folgender:

* Auf einem Hauptrechner ("Tower") werden einzelne Routinen ("Tasks")
  definiert, die dann auf den Zielrechnern ("Hosts") ausgeführt werden sollen.
* Die einzelnen Hosts werden beim Aufruf von Ansible via :ref:`SSH <SSH>`
  kontaktiert. Anstelle der manuellen Eingabe von Passwörtern werden dabei meist
  :ref:`SSH-Schlüssel <Anmeldung mit Public Key anstelle eines Passworts>`
  verwendet.

Ein Vorteil von Ansible ist es, dass es erst die vorliegenden Bedingungen prüft,
bevor es irgendwelche Routinen aufruft. Sind beispielsweise die gewünschten
Programme bereits installiert oder die entsprechenden Konfigurationsdateien
angepasst, so bedeutet dies, dass ein erneuter Aufruf einer Ansible-Task keine
weiteren Veränderungen mit sich bringt (beispielsweise kann so vermieden werden,
dass Server-Dienste erneut gestartet werden, wenn sie bereits aktiv sind). Wegen
derartiger Features wird Ansible häufig bei der Server-Verwaltung eingesetzt, es
kann allerdings auch auf üblichen Computern genutzt werden.

Unter Debian/Ubuntu/LinuxMint kann Ansible folgendermaßen installiert werden:

.. code-block:: sh

    sudo aptitude install ansible


.. _Zielrechner festlegen:

Zielrechner festlegen
---------------------

Das Verzeichnis ``/etc/ansible`` enthält eine vollständige Basis-Konfiguration
für ein Ansible-Projekt; unter anderem befindet sich in der Konfigurationsdatei
``/etc/ansible/hosts`` eine Beispiel-Liste von Rechnern, auf denen
Installationen beziehungsweise Konfigurationen vorgenommen werden sollen. Die
einzelnen Ziel-Rechner können optional (mittels einer einfachen `YAML
<https://de.wikipedia.org/wiki/YAML>`__-Syntax) gruppiert und mit einem Label
versehen werden. Eine solche Rechner-Liste kann beispielsweise folgendermaßen
aussehen:

.. ``/etc/hosts`` ist ein Verzeichnis, das eine vollständige
.. Ansible-Beispiel-Konfiguration enthält

.. code-block:: yaml

    [myweb]
    192.168.2.11
    192.168.2.12

.. Mit dieser einfachen Form können alle aufgelisteten Netzwerk-Adressen unter der
.. Sammel-Bezeichnung ``servers`` angesprochen werden; im realen Einsatz müssen die
.. obigen Netzwerk-Adressen durch die tatsächlichen Netzwerk-Adressen ersetzt
.. werden.

Für die Festlegung der Zielrechner und der einzelnen Tasks ist es
empfehlenswert, ein eigenes lokales Verzeichnis anzulegen, das auch ohne
SuperUser-Rechte verwaltet werden kann:

.. code-block:: sh

    mkdir ~/ansible
    cp -R /etc/ansible ~/ansible

Beim Aufruf von ``ansible`` kann der Pfad der gewünschten Hosts-Datei mittels
der Option ``-i hostfile`` explizit angegebenen werden. Möchte man allerdings,
dass Ansible standardmäßig auf die Host-Datei im Verzeichnis ``~/ansible``
zurückgreift, so kann man folgende Zeile in einer Shell eingeben (oder diese am
Ende der Konfigurationsdatei ``~/.bashrc`` beziehungsweise ``~/.zshrc``
einfügen):

.. code-block:: sh

    export ANSIBLE_HOSTS=~/ansible/hosts

Diese Hosts-Datei kann nun auch ohne SuperUser-Rechte nach Belieben angepasst
werden. Zu Test-Zwecken kann man beispielsweise auch ein virtuelles
Betriebsystem einrichten und die Ansible-Tasks auf diesem ablaufen lassen.
Hierzu sollte die Rechner-Liste um folgenden Eintrag ergänzt werden:

.. code-block:: yaml

    [local]
    127.0.0.1

.. Die Adresse ``127.0.0.1`` steht für den Localhost.

Auf diese Weise kann man Ansible ausprobieren, ohne Änderungen auf anderen
Rechnern durchzuführen. Die Anmeldung auf dem virtuellen Betriebsystem erfolgt
allerdings mittels Benutzername und Passwort, nicht mittels SSH-Schlüsseln.


.. _Tasks und Playbooks:
.. _Task:
.. _Playbook:

Tasks und Playbooks
-------------------

Bei der Verwendung von Ansible wird angegeben, welchen "Status" das Zielsystem
haben sollte. Ansible führt dann (und nur dann) einzelne Routinen aus, bis der
Soll-Status erreicht ist.

Die auszuführenden Tasks können ebenfalls in einer YAML-Datei ('Playbook')
abgelegt werden. So kann man beispielsweise eine Datei
``~/ansible/upgrade-servers.yml`` mit folgendem Inhalt anlegen:

.. code-block:: yaml

    - hosts: myweb
      sudo: true
      tasks:
        - name: update apt sources
          apt:  update_cache=yes

       - name: upgrade apt packages
         apt:  upgrade=yes

Hat man Netzwerk-Zugriff auf den/die Host-Computer Netzwerk-Zugriff und kann auf
diesen SuperUser-Rechte erlangen, so kann man anschließend Ansible mit folgender
Anweisung aufrufen:

.. code-block:: sh

    ansible-playbook ~/ansible/upgrade-server.yml -u -K

Durch die Option ``-u`` wird der Benutzer auf dem entfernten Rechner festgelegt,
durch die Option ``-K`` wird nach dem jeweiligen Passwort gefragt.

.. ansible-playbook update-servers.yml --ask-sudo-pass
.. https://techsomnia.net/2013/11/ansible-apt-get-updateupgrade/

.. Ansible unterstützt dabei sowohl das beispielsweise unter Debian, Ubuntu und
.. Linux Mint übliche Paketverwaltungs-Programm :ref:`apt <apt>` wie auch den in
.. Python geschriebenen Paket-Manager ``yum``.

Ansible-Module
--------------

Zum Durchführen der einzelnen Tasks bietet Ansible einige Module, die jeweils
Funktion für bestimmte Aufgaben bereitstellen. Das wohl einfachste Modul heißt
``command``, und erlaubt das Ausführen einer gewöhnlichen Shell-Anweisung. Auch
ohne Definition eines Playbooks kann man dies beispielsweise folgendermaßen
nutzen:

.. code-block:: sh

    # Shell-Anweisung via Ansible ausführen:
    ansible myweb -m command -a "uptime"

.. -u root

Durch die Option ``-m`` wird ein Modulname angegeben, mit ``-a`` wird ein
Kommandozeilen-Argument für dieses Modul übergeben (mittels ``-u username``
könnte zudem wiederum ein Benutzername angegeben werden, mit dem man sich via
SSH bei den Zielrechnern anmelden möchte).

Anstelle einer einzelnen Anweisung kann man auch ein Shell-Skript mittels Ansible
ausführen lassen. Ein solches könnte beispielsweise folgenden Inhalt haben:

.. code-block:: sh

    #!/bin/bash

    # Filename: script-example.sh

    uptime
    echo "Hello World!"

Speichert man dieses Mini-Skript als Datei ``script-example.sh``, so kann man
das Ansible-Modul ``script`` nutzen, um es auf den Zielrechnern auszuführen:

.. code-block:: sh

    # Shell-Skript via Ansible ausführen:
    ansible myweb -m script -a script-example.sh

Wiederum wird mit der Option ``-m`` der Modulname angegeben, und mit der Option
``-a`` der Name des Skripts als zusätzliches Argument.





... to be continued ...

.. rubric:: Links

* `Ansible Tutorial (en.)
  <https://serversforhackers.com/c/an-ansible-tutorial>`__
* `Ansible Modules Documentation (en.) <http://docs.ansible.com/ansible/modules_by_category.html>`__
* `Ansible Python API (en.)
  <http://docs.ansible.com/ansible/latest/dev_guide/developing_api.html>`__
* `Jinja2 Documentation (en.) <http://jinja.pocoo.org/docs/2.9/>`__


.. Relevant für Backups!?:
.. http://docs.ansible.com/ansible/copy_module.html
.. http://docs.ansible.com/ansible/fetch_module.html


