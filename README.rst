
Grundkurs Linux
===============

In dieser Dokumentation aus der `Grund-Wissen <https://www.grund-wissen.de>`_
-Reihe geht es um Linux, Open Source, Shell-Anweisungen, Shell-Scripting, den
Text-Editor Vim, und weitere damit zusammen hängende Themen.

Das Projekt verwendet `Sphinx <http://sphinx-doc.org/>`_ als Programm zum
Erstellen der HTML- bzw. PDF-Dokumente. Die Dokumentation wird kontinuierlich
ausgebaut, Unterstützung bei der Weiterentwicklung ist gerne willkommen.

Eine HTML-Version dieser Seite ist unter folgender Adresse abrufbar:

https://www.grund-wissen.de/linux


Lokale Kopien und eigene Änderungen
-----------------------------------

Um lokale Kopien der Dokumentation zu erstellen, müssen einige Pakete
installiert sein. Unter Debian, Ubuntu oder Linux Mint können diese
folgendermaßen installiert werden:

.. code-block:: bash

    aptitude install python3-pip

	pip3 install -U Sphinx

Anschließend kann das Repository heruntergeladen werden:

.. code-block:: bash

    git clone https://github.com//grund-wissen/grundkurs-linux.git

Im Projektverzeichnis können dann aus den Quelldateien wahlweise HTML-Seiten
oder ein PDF-Dokument erstellt werden:

.. code-block:: bash

    # HTML-Seiten erzeugen:
    make html

    # PDF-Dokument erzeugen:
    make latexpdf

**Update:** Seit Anfang 2018 bin ich auf separate Verzeichnisse für den
Source-Code und die Builds umgestiegen -- das erleichtert die Synchronisation,
und hat zusätzlich den Vorteil, man kann einem lokalen Apache-Webserver einfach
Lese-Rechte für dieses Build-Verzeichnis einräumen kann.

Befindet sich der Source-Code beispielsweise im Verzeichnis ``~/source/linux``,
so werden die HTML- beziehungsweise LaTeX-Builds damit in den Verzeichnissen
``~/build/linux/html`` beziehungsweise ``~/build/linux/latex`` abgelegt.

Sollen eigene, lokale Änderungen an der Dokumentation in dieses Repository
übernommen werden, so wird um einen entsprechenden Pull-Request gebeten.


Herzlichen Dank an alle Mitwirkenden!


