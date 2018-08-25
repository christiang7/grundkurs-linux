.. index:: Sphinx
.. _Sphinx:

Das Dokumentations-System ``sphinx``
====================================

`Sphinx <http://www.sphinx-doc.org>`__ ist ein in Python geschriebenes
Shell-Programm, das aus einer bzw. mehreren Textdateien mit
RestructuredText-Syntax auf dem lokalen Rechner wahlweise eine PDF-Datei oder
eine beziehungsweise mehrere HTML-Dateien erzeugen kann. [#]_

Da die RestructuredText-Syntax minimal und leicht erlernbar ist, ermöglicht es 
Sphinx, Dokumente mit nicht einmal dem halben gewöhnlichen Aufwand in einer
Online-Version für Webbrowser sowie in einer (druckbaren) PDF-Version zu
publizieren.


.. _Dursuchen von RST-Dateien:

.. rubric:: Dursuchen von RST-Dateien

Die Quelldateien eines Sphinx-Projekts sind reine Textdateien mit der Endung
``.rst`` (für RestructuredText); diese lassen sich schnell und einfach nach
Inhalten durchsuchen. Persönlich habe ich mir dazu folgende Abkürzung in der
Konfigurationsdatei ``~/.zshrc`` definiert:

.. code-block:: bash

    alias rstgrep='find ./ -name "*.rst" | xargs grep'

In einer Shell kann damit mittels ``rstgrep Suchbegriff`` nach einem Begriff
oder einem regulären Ausdruck in allen ``rst``-Dateien eines Projekts (inklusive
aller Unterverzeichnisse) gesucht werden; als Ergebnis bekommt man jede Zeile
einer ``rst``-Datei angezeigt, die den Suchbegriff enthält. Durch die Verwendung
von :ref:`grep <grep>`  können auch reguläre Ausdrücke genutzt werden;
beispielsweise würde ``rstgrep "^Hallo *"`` jede Zeile ausgeben, die mit "Hallo"
beginnt. Zusätzliche ``grep``-Optionen können ebenfalls wie üblich genutzt
werden, würde ``rstgrep -li Suchbegriff`` ("list", "ignore-case") anstelle der
zutreffenden Zeilen nur die Namen der Dateien auflisten, die den Suchbegriff 
ohne Berücksichtigung der Groß-/Kleinschreibung enthalten.


.. _Installation von Sphinx:

.. rubric:: Installation von Sphinx

Sphinx sowie einige nützliche Zusatz-Pakete können unter Linux folgendermaßen
installiert werden:

.. code-block:: bash

    sudo aptitude install python3-setuptools python3-numpy \ 
        python3-matplotlib python3-docutils dvipng latexmk

    sudo pip3 install Sphinx

Mit ``sudo pip3 install -U Sphinx`` ("Update") kann Sphinx jederzeit auf den
aktuellsten Stand gebracht werden.

Zur Erzeugung von PDF-Druckversionen genügt bereits ein minimales LaTeX-System,
wie es nach Installation der oben genannten Pakete automatisch vorhanden ist. Um
beispielsweise in naturwissenschaftlichen Publikationen einen umfangreichen
mathematischen Formelsatz nutzen zu können, sollte bei Bedarf ein :ref:`volles
LaTeX-System <gwil:LaTeX>` installiert werden.


.. toctree::
    :maxdepth: 2

    quickstart-und-programmaufruf.rst
    restructuredtext-tutorial.rst
    anpassungen.rst
    tinkerer.rst
    links.rst


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkung:

.. [#]  Um die erzeugten HTML-Dateien im Internet zu publizieren, müssen sie
    lediglich in einen gemeinsamen Ordner auf einem Webserver kopiert werden.
    Weist man diesem Ordner anschließend über einen Domain-Anbieter eine feste
    Webadresse (URL) zu, so ist die Seite bereits fertig!

..  `Filezilla <http://wiki.ubuntuusers.de/FileZilla>`_ oder Midnight Commander

