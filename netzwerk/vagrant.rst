
.. _Vagrant:

Virtuelle Systeme mittels ``vagrant``
=====================================

Computer-Netzwerke setzen mehrere Rechner voraus. Möchte man mit einem einzelnen
Rechner auf weitere Rechner als Test-Plattformen zugreifen, so kann man dies
mittels ``vagrant`` und virtuellen Betriebsystemen sehr einfach erreichen.

Als Shell-Anwendung greift ``vagrant`` auf die Virtualisierungs-Software
`VirtualBox <https://wiki.ubuntuusers.de/VirtualBox/>`__ zurück, vereinfacht
allerdings die Einrichtung und Nutzung des Zielsystems erheblich.

Mittels :ref:`aptitude <aptitude>` kann ``vagrant`` folgendermaßen installiert
werden:

.. code-block:: sh

    sudo aptitude install virtualbox virtualbox-dkms vagrant

Hierdurch wird auch Virtualbox automatisch mitinstalliert.


.. rubric:: Virtuelles Betriebsystem initialisieren

Um ein neues virtuelles Betriebsystem einzurichten, legt man zunächst ein
neues Verzeichnis für so genannte "Vagrantfiles" an:

.. code-block:: sh

    mkdir ~/playbooks 
    cd ~/playbooks

Alle folgenden ``vagrant``-Anweisungen müssen aus diesem Verzeichnis heraus
ausgeführt werden.

Zunächst wird festgelegt, welches Zielsystem installiert werden soll. Eine Liste
mit verfügbaren Systemen gibt es `hier
<https://app.vagrantup.com/boxes/search>`__. Um beispielsweise Ubuntu Xenial
(16.04 LTS) zu installieren, gibt man zunächst folgendes ein:

.. code-block:: sh

    # Virtuelles System hinzufügen:
    vagrant box add ubuntu/xenial64

Diese Anweisung bewirkt, dass im ``playbooks``-Verzeichnis eine Datei
namens ``Vagrantfile`` angelegt wird. Der überwiegende Teil dieser Datei besteht
aus Kommentar-Zeilen, die mit einem ``#``-Zeichen beginnen; der einzige
wesentliche Eintrag ist ``config.vm.box = "ubuntu/xenial64"``. Die eigentliche
Installation startet man wie folgt:

.. code-block:: sh

    # Virtuelles System installieren:
    vagrant init ubuntu/xenial64

Falls bei der Installation eine ``404``-er Fehlermeldung auftritt, so genügt es
ans Ende der ``Vagrantfile`` folgende Zeile einzufügen:

``Vagrant::DEFAULT_SERVER_URL.replace('https://vagrantcloud.com')``

Schließlich ist es noch empfehlenswert, folgendes Plugin zu installieren:

.. code-block:: sh

    vagrant plugin install vagrant-vbguest

.. libxslt-dev, libxml2-dev, and build-essential installed?

Damit ist die Installation abgeschlossen.


.. _Vagrant benutzen:

.. rubric:: Vagrant benutzen

Um das virtuelle Betriebsystem zu starten, genügt folgende Anweisung:

.. code-block:: sh

    vagrant up

Wiederum muss man sich für diesen Aufruf im ``playbooks``-Verzeichnis befinden.
Man erhält dabei etwa folgende Ausgabe:

::

    Bringing machine 'default' up with 'virtualbox' provider...
    ==> default: Checking if box 'ubuntu/xenial64' is up to date...
    ==> default: Clearing any previously set forwarded ports...
    ==> default: Clearing any previously set network interfaces...
    ==> default: Preparing network interfaces based on configuration...
        default: Adapter 1: nat
    ==> default: Forwarding ports...
        default: 22 (guest) => 2222 (host) (adapter 1)
    ==> default: Running 'pre-boot' VM customizations...
    ==> default: Booting VM...
    ==> default: Waiting for machine to boot. This may take a few minutes...
        default: SSH address: 127.0.0.1:2222
        default: SSH username: vagrant
        default: SSH auth method: private key
        default: Warning: Remote connection disconnect. Retrying...
    ==> default: Machine booted and ready!
    (...)

Nun kann man sich folgendermaßen via ``ssh`` mit der virtuellen Maschine
verbinden:

.. code-block:: sh

    vagrant ssh

Ein Dateiaustausch mit dem Host-System ist im virtuellen Betriebsystem über das
Verzeichnis ``/vagrant`` möglich. Jede Datei, die in diesem Verzeichnis erstellt
beziehungsweise dorhin kopiert wird, wird automatisch mit dem
``playbooks``-Verzeichnis des Host-Systems synchronisiert.

Mit ``exit`` kann die Sitzung wie jede gewöhnliche ``ssh``-Sitzung wieder
beendet werden. Anschließend kann ``vagrant`` in ähnlicher Form auch wieder
beendet werden:

.. code-block:: sh

    vagrant halt

Mit ``vagrant reload`` kann das virtuelle Betriebsystem bei Bedarf auch neu
gestartet werden. Soll das virtuelle Betriebsystem nicht nur heruntergefahren,
sondern komplett entfernt werden, ist dies mittels ``vagrant destroy`` möglich.

.. rubric:: Links:

* `Vagrant Docs: Getting Started (en.) <https://www.vagrantup.com/intro/getting-started/>`__

.. Docker Intro (de.) <https://gridscale.io/community/tutorials/docker-ubuntu/>__
.. Docker Documentation (en.) <https://docs.docker.com/engine/reference/commandline/login/>`__
.. Docker-Tutorial (de, ausführlich) <https://hosting.1und1.de/digitalguide/server/konfiguration/docker-tutorial-installation-und-erste-schritte/>`__

