.. _Sphinx-Quickstart:

Sphinx-Quickstart
=================

Um ein neues Sphinx-Projekt zu starten, kann man entweder einen bestehenden
Projekt-Ordner kopieren und modifizieren, oder ein neues Verzeichnis anlegen und
in diesem mittels der Shell-Anweisung ``sphinx-quickstart`` ein neues
Grundgerüst erstellen:



.. code-block:: sh

    mkdir projektordner && cd projektordner

    sphinx-quickstart

Sphinx erstellt daraufhin einige notwendige Hilfsdateien, beispielsweise eine
:ref:`Makefile <Makefile>` und eine Konfigurationsdatei namens ``conf.py``,
in der auch zu einem späteren Zeitpunkt Einstellungen für das jeweilige Projekt
festgelegt werden können.

Beim Aufruf von ``sphinx-quickstart`` erscheinen zunächst einige
Benutzer-Abfragen, mit denen der Name des Projekts sowie andere grundlegende
Einstellungen vorgenommen werden können:

* Bei der ersten Abfrage soll der Nutzer angeben, in welchem Pfad das Projekt
  initiiert werden soll. Üblicherweise startet man ``sphinx-quickstart`` bereits
  im Projekt-Verzeichnis, so dass kein expliziter Pfad angegeben werden muss,
  sondern die Vorgabe ``[.]`` durch Drücken der ``Enter``-Taste bestätigt werden
  kann:

.. code-block:: rst

    Welcome to the Sphinx 1.6.2 quickstart utility.

    Please enter values for the following settings (just press Enter to
    accept a default value, if one is given in brackets).

    Enter the root path for documentation.
    > Root path for the documentation [.]:

* Bei den beiden nächsten Abfragen geht es darum, ob für die Quelldateien ein
  eigener Ordner angelegt werden soll und wie besondere Ordner, die
  beispielsweise Logos oder Templates beinhalten, gekennzeichnet werden sollen.
  Bei beiden Fragen sind meiner Meinung nach die Standard-Vorgaben
  empfehlenswert, es genügt somit jeweils eine Bestätigung mit der
  ``Enter``-Taste.

  Die Quelltexte der Webseite werden bei diesen Standard-Einstellungen im
  Projektverzeichnis beziehungsweise in Unterverzeichnissen abgelegt; der von
  Sphinx erzeugte HTML- beziehungsweise LaTeX-Code wird hingegen in die
  separaten Unterverzeichnisse ``_build/html`` beziehungsweise ``_build/latex``
  geschrieben.

* Bei den nächsten Abfragen muss der Projekt- sowie der Autorname der
  Dokumentation angegeben werden; die Angabe einer Versionsnummer ist optional
  und kann auch zu einem späteren Zeitpunkt in der Konfigurationsdatei
  ``conf.py`` vorgenommen werden.

  Als Sprache kann wahlweise ``en`` für Englisch, ``de`` für Deutsch, oder ein
  anderes Sprach- beziehungsweise Länderkürzel gesetzt werden (eine Übersicht
  über die unterstützten Sprachen gibt es `hier
  <http://www.sphinx-doc.org/en/stable/config.html#confval-language>`__).

* Bei den beiden nächsten Abfragen wird eine Datei-Endung für die
  Quelltext-Dateien sowie der Name der grundlegenden Index-Datei festgelegt.
  Auch hier ist es empfehlenswert die jeweiligen Vorgaben mit der
  ``Enter``-Taste zu bestätigen.

  Die Datei ``index.rst`` im Projekt-Verzeichnis beinhaltet im Wesentlichen ein
  Inhaltsverzeichnis ("toctree"), welcher die Einhänge-Punkte der übrigen
  Quelltext-Dateien festlegt.

* Bei der nächsten Abfrage wird festgelegt, ob ein Epub-Builder gewünscht ist
  oder nicht. Gewöhnlich kann hier die Vorgabe ``[n]`` mit der ``Enter``-Taste
  bestätigt werden.

* Bei der nächsten Abfrage kann man festlegen, welche Sphinx-Module für das
  Dokumentations-Projekt genutzt werden sollen; die Auswahl kann ebenfalls
  später in der Konfigurationsdatei ``conf.py`` überarbeitet werden.

  Bei mir persönlich würde die Modul-Abfrage folgendermaßen ausfallen:

  > autodoc: ``y``
        Dieses Modul ist für die Dokumentation von Python-Programmen gedacht --
        hierbei kann eine Dokumentation automatisch anhand der :ref:`Docstrings
        <gwip:Docstring>` der jeweiligen Funktionen beziehungsweise Module erstellt
        werden.

  > doctest: ``n``
        Python ermöglicht es, in die Docstrings von Funktionen Tests einzubauen.
        Ich persönlich verwende lieber :ref:`Unittests <gwip:Unittest>` und
        nutze dieses Feature daher nicht.

  > intersphinx: ``y``
        Intersphinx-Mappings ermöglichen es, von einer Sphinx-Dokumentation aus
        auf andere Sphinx-Dokumentationen zu verweisen.

        Hierbei wird in der Konfigurationsdatei ``conf.py`` unter dem Begriff
        ``intersphinx_mapping`` festgelegt, welche externen Projekte mit welchem
        Kürzel genutzt werden sollen. Ein solcher Eintrag könnte beispielsweise
        wie folgt aussehen:

        .. code-block:: python

            intersphinx_mapping = {
                'sphinx': ('http://www.sphinx-doc.org/en/stable', None),
                'gwm': ('http://grund-wissen.de/mathematik', None),
                'gwp': ('http://grund-wissen.de/physik', None),
            }

        Innerhalb der Dokumentation kann dann beispielsweise mittels
        ``:ref:`Mechanik <gwp:Mechanik>`` auf den :ref:`Mechanik
        <gwp:Mechanik>`-Teil der Physik-Dokumentation im Grund-Wissen-Projekt
        verwiesen werden. [#]_

    > todo: ``n``
        Dieses Modul ermöglicht es, Todo-Notizen in die Dokumentation
        aufzunehmen eine Übersichtsliste daraus zu erstellen. Persönlich
        vermerke ich mir Todos allerdings lieber als Kommentare, die dann im
        fertigen Dokument nicht erscheinen.

    > coverage: ``n``
        Dieses Modul ist ebenfalls für die Dokumentation von Python-Programmen
        gedacht, und ermöglicht eine Anzeige, wie viele der definierten
        Funktionen bereits über eine Dokumentation (einen Docstring) verfügen.

    > imgmath: ``y``
        Bei Verwendung dieses Moduls werden mathematische Formeln für die
        HTML-Version als ``png``-Dateien gerendert; diese werden dann an den
        jeweiligen Stellen automatisch eingefügt.

        Diese Option hat als Nachteil, dass bei technischen Dokumentationen
        unter Umständen viele (sogar tausende) ``png``-Dateien erstellt werden,
        was ein Hochladen des Projekts auf den Webserver verlangsamt. Der
        Vorteil ist hingegen, dass die Anzeige im Webbrowser auch ohne
        zusätzliche Javascript einwandfrei funktioniert.

    > mathjax: ``n``
        Bei Verwendung dieses Moduls werden mathematische Formeln in der
        HTML-Version so ausgegeben, dass sie erst im Browser des Lesers mittels
        Javascript gerendert werden.

        Je nach Vorlieben sollte man sich *entweder* für die ``imgmath``- oder für
        die ``mathjax``-Option entscheiden.

    > ifconfig: ``n``
        Dieses Modul ermöglicht es, bestimmte Inhalte nur dann in der
        Dokumentation zu berücksichtigen, wenn entsprechende Konfigurationen in
        der Datei ``conf.py`` vorliegen. Persönlich habe ich dieses Feature
        bislang nicht benötigt.

    > viewcode: ``y``
        Dieses Modul ermöglicht es, die Dokumentation von (Python-)Quellcode mit
        den jeweiligen Stellen des Quellcodes selbst zu verknüpfen; dies ist für
        die Dokumentation von Open-Source-Programmen durchaus nützlich.

* Bei der letzten Abfrage gibt man an, ob eine :ref:`Makefile <Makefiles>` (für
  Linux-Systeme) oder eine ``Commandfile`` (für Windows-Systeme) angelegt werden
  soll; diese Entscheidung muss je nach eingesetztem Betriebsystem individuell
  getroffen werden.

Anschließend wird das Projekt von Sphinx fertig angelegt und kann beliebig
gestaltet beziehungsweise mit Inhalten gefüllt werden.


.. _Aufruf von Sphinx:

Aufruf von Sphinx
=================

Ein bestehendes Projekt (beispielsweise ein selbst erstelltes oder ein
von `Github` geclontes) kann auf einfache Weise als Webseite oder PDF-Datei
ausgegeben werden. Hierzu wechselt man in einer Shell in das Projekt-Verzeichnis
und gibt folgendes ein:

.. code-block:: sh

    # HTML-Dateien erzeugen:
    make html

    # LaTeX-Code erzeugen:
    make latex

    # LaTeX-Code erzeugen und daraus eine PDF-Datei erstellen:
    make latexpdf

Treten aufgrund einer fehlerhaften RST-Syntax während des Übersetzens Fehler
auf, so werden diese mit einer kurzen Erläuterung und der Angabe der den Fehler
verursachenden Stelle auf dem Bildschirm ausgegeben.

Die neu erstellten Dateien werden vons ``sphinx`` bei Verwendung der oben
genannten Konfiguration im ``_build``-Verzeichnis innerhalb des Projektpfads
abgelegt. Je nach Ausgabe-Variante können die erstellten folgendermaßen
aufgerufen werden:

.. code-block:: sh

    # Erstellte HTML-Seiten mit Webbroswer "firefox" öffnen:
    firefox _build/html/index.html

    # Erstellte PDF-Datei mit PDF-Betrachter "evince" öffnen:
    evince _build/latex/projekttitel.pdf

Der Name des PDF-Dokuments wird in der Konfigurationsdatei ``conf.py``
unter der Rubrik ``latex_documents`` festgelegt.

Um den bestehenden Build eines Projekts zu entfernen, beispielsweise nach
einem Umbenennen mehrerer Quelldateien oder einer neuen Ordnerstruktur, kann
Folgendes eingegeben werden:

.. code-block:: sh

    make clean

Anschließend können mittels ``make html``, ``make latex`` oder ``make latexpdf``
neue Builds erstellt werden.


.. _Projekt auf nicht funktionierende Links prüfen:

.. rubric:: Projekt auf nicht funktionierende Links prüfen

Auf folgende Weise kann ein bestehendes Projekt hinsichtlich nicht
funktionierender Web-Links überprüft werden:

.. code-block:: sh

    make linkcheck

Dieser Aufruf gibt auf dem Bildschirm alle Links zu nicht mehr existierenden
oder permanent umgeleiteten Seiten aus. Dieses Feature sollte in regelmäßigen
Abständen genutzt werden, um den Besuchern der Seite unnötige ``404: Seite nicht
gefunden``-Fehlermeldungen zu ersparen; auch Suchmaschinen werten einen
möglichst hohen Anteil an funktionierenden Links als Kriterium für die
Aktualität einer Seite.

.. _Intersphinx-Mappings aktualisieren:

.. rubric:: Intersphinx-Mappings aktualisieren

Bei der Verwendung von Sphinx ist es möglich, Links auf Begriffe aus anderen
Sphinx-Dokumentationen zu setzen; dies wird als ``Intersphinx-Mapping``
bezeichnet.

Mit den normalen Einstellungen werden die Index-Kataloge der angegebenen
Projekte nur beim erstmaligen Erstellen eines Projekts geladen. Kommen bei den
externen Projekten weitere Begriffe hinzu, so kann also nur dann mittels eines
Intersphinx-Mappings darauf verwiesen werden, wenn explizit geprüft wird, ob
sich Änderungen in den angegebenen Projekten ergeben haben. Dies kann durch
folgende Änderung in der ``Makefile`` des Projekts erreicht werden:

.. code-block:: sh

    # Original
    # SPHINXOPTS =

    # Intersphinx-Seiten auf Änderungen prüfen:
    SPHINXOPTS = -E

Durch die ergänzende Angabe der Option ``-E`` werden beim Aufruf von ``make
html``, ``make latex`` oder ``make latexpdf`` alle externen Index-Kataloge neu
eingelesen. Dies kann den Übersetzungs-Prozess erheblich verlangsamen und sollte
daher nur bei Bedarf kurzzeitig geändert werden.


.. index:: rst2latex, docutils
.. _Einzelne Dateien mit rst2latex konvertieren:

Einzelne Dateien mit ``rst2latex`` konvertieren
===============================================

Hat man unter Linux das Paket ``python3-docutils`` installiert, so stehen neben
Sphinx auch die Konverter ``rst2html`` und ``rst2latex`` zur Verfügung, die
jeweils eine einzelne Quelldatei in ein HTML- beziehungsweise LaTeX-Dokument
übersetzen.

Für die Verwendung von ``rst2latex`` habe ich mir eine :ref:`Makefile
<Makefile>` mit folgendem Inhalt gebastelt:

.. code-block:: sh

    # Datei: rstmakefile

    %: %.rst
        rst2latex $< > $*.tex
        pdflatex $*.tex
        rm $*.aux $*.log $*.out

In einer Shell kann man dann im Projektordner folgendermaßen aus einer
``.rst``-Datei eine gleichnamige ``.tex``-Datei sowie das
zugehörige ``.pdf``-Dokument erzeugen:

.. code-block:: sh

    # RST-Datei dateiname.rst konvertieren:
    # (Dateiendung dabei weglassen!)
    make -f pfad-zur-rstmakefile dateiname

    # Ergebnis: dateiname.tex, dateiname.pdf

Diese Methode hat zwei sehr schöne Nebeneffekte: Erstens wird, anders als bei
Verwendung von Sphinx, ein "klassischer" LaTeX-Code ohne Extra-Konfigurationen
und besonderen Stil-Elementen generiert. Zweitens können über die
Konfigurationsdatei ``~/.docutils`` optional zusätzliche Pakete in die
:ref:`LaTeX-Präambel <gwil:Aufbau eines LaTeX-Dokuments>` geladen werden, um
beispielsweise das Seitenlayout anzupassen. Meine Konfigurationsdatei hat
beispielsweise folgenden Inhalt:

.. code-block:: tex

    [latex2e writer]
    latex_preamble: \usepackage{units,amsmath,amsfonts,amssymb,textcomp,gensymb,marvosym,wasysym}
                    \usepackage[left=2cm,right=2cm,top=1cm,bottom=1.5cm]{geometry}
                    \setlength{\parskip}{\baselineskip} % Extra line between paragraphs
                    \setlength{\parindent}{0pt} % No indent at the start of paragraphs
                    \pagestyle{empty}

Durch diese Einstellungen werden einerseits Zusatz-Pakete für mathematischen
Formelsatz eingebunden, zum anderen werden durch das ``geometry``-Paket die
Seitenränder auf ein Minimum reduziert, so dass beim Drucken einzelner
Notiz-Seiten kein Platz verschwendet wird.


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#] Die Angaben können zu jedem späteren Zeitpunkt in der
    Konfigurationsdatei ``conf.py`` geändert werden.

    Durch die Vergabe von Versionsnummern kann beispielsweise bei der
    Dokumentation von Software-Quellcode sichergestellt werden, dass eine
    Anleitung auch zur jeweiligen Software-Version passt. Auch bei allgemeinen
    Dokumentationsprojekten ist eine Versionsnummer sinnvoll, um den jeweiligen
    Entwicklungsstand aufzuzeigen; mit einem Versions-Upgrade können außerdem
    eine Rundmail über einen Verteiler, ein neuer Commit eines
    Versionsverwaltungs-Programms, ein Weblog-Eintrag o.ä. verbunden werden.

.. [#] Im Abschnitt :ref:`Sprungmarken und Referenzen <Sprungmarken und Referenzen>`.
    ist dies näher beschrieben.

