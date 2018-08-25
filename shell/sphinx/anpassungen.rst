.. _Gestalterische Anpassungen:

Gestalterische Anpassungen
==========================

Für die Grundwissen-Webseite nutze ich das Sphinx-Standard-Theme mit einigen
Anpassungen. Ich nutze dafür eine :ref:`virtuellen Umgebung <Virtuelle
Umgebungen>`, in der einige Sphinx-Dateien geändert werden. Zum Einrichten
einer solchen virtuellen Umgebung kann man folgendes eingeben:

# Im Basis-Ordner des Sphinx-Projekts:
python

Diese habe ich als Super-User direkt am zentralen
Installationspfad
(in meinem Fall ``/usr/local/lib/python3.5/dist-packages/sphinx``) vorgenommen,
so dass sie global für alle Dokumentations-Projekte gleichermaßen gelten. Als
(empfehlenswertere) Alternative hierzu kann Sphinx mittels einer
lokal im Ordner des Benutzers
installiert und dort auch ohne Super-User-Rechte angepasst werden. Die im
folgenden Abschnitt aufgelisteten Datei-Änderungen beziehen sich dabei stets auf
den jeweiligen Installationspfad.


.. _Kontakt-Link auf jeder HTML-Seite hinzufügen:

.. rubric:: Kontakt-Link auf jeder HTML-Seite hinzufügen

In der Fußnotenzeile der Webseite wollte ich ein Link auf Kontakt/Impressum
eingefügen. Dies kann in in der Datei ``themes/basic/layout.html`` festgelegt
werden:

.. code-block:: jinja
    :emphasize-lines: 4,12,13

    VORHER:

    {%- if last_updated %}
      {% trans last_updated=last_updated|e %}Last updated on {{ last_updated }}.
      {% endtrans %}
    {%- endif %}

    NACHHER:

    {%- if last_updated %}
      {% trans last_updated=last_updated|e %}Last updated on {{ last_updated }}.
      <a href='http://grund-wissen.de/impressum.html'>Kontakt/Impressum</a>
      {% endtrans %}
    {%- endif %}


.. _Zeilenumbruch bei langen HTML-Navigationszeilen ermöglichen:

.. rubric:: Zeilenumbruch bei langen HTML-Navigationszeilen ermöglichen

In der obersten Zeile einer jeden mit Sphinx erstellten HTML-Seite wird eine
Navigations-Leiste angezeigt. Bei einer umfangreichen Dokumentation mit vielen
Unterabschnitten kann es vorkommen, dass auf kleinen Bildschirmen hierbei ein
Zeilenumbruch nötig ist -- der letzte Listeneintrag wird also in eine neue
Zeile geschrieben. In der Grundversion wird hierbei die Seitenüberschrift
verschoben. Um dies zu vermeiden, muss folgender Eintrag in der Datei
``themes/basic/static/basic.css_t`` ergänzt werden:

.. code-block:: css
    :emphasize-lines: 16,17,18

    VORHER:

    div.related ul {
        margin: 0;
        padding: 0 0 0 10px;
        list-style: none;
        }


    NACHHER:

    div.related ul {
        margin: 0;
        padding: 0 0 0 10px;
        list-style: none;
        min-height: 2em;
        height: auto;
        overflow: hidden;
        }

Durch den Eintrag ``height: auto`` wird die Höhe der Navigations-Leiste
automatisch angepasst. Der Eintrag ``overflow: hidden;`` fügt anschließend bei
Bedarf automatisch eine (wieder ganz von links beginnende) neue Zeile ein.


.. _Tabellen zentrieren:

.. rubric:: Tabellen zentrieren

.. Normalerweise stellt Sphinx Tabellen im LaTeX-Output linksbündig dar. Persönlich
.. sind mir zentrierte Tabellen lieber. Daher habe ich die (umfangreiche) Datei
.. ``writers/latex.py``, speziell die Funktion ``depart_table(self, node)``, etwas
.. abgeändert:

.. .. code-block:: python
..     :emphasize-lines: 4,5,7,8,12,13,15,16,21,27,28,33,34,36,37,39,40,45

..     VORHER:

..     if not self.table.longtable and self.table.caption is not None:
..         self.body.append(u'\n\\begin{threeparttable}\n'
..                          u'\\capstart\\caption{%s}\n' % self.table.caption)
..     elif self.table.has_verbatim:
..         self.body.append('\n\\begin{tabular}')
..         endmacro = '\\end{tabular}\n'
..     elif self.table.has_problematic and not self.table.colspec:
..         # if the user has given us tabularcolumns, accept them and use
..         # tabulary nevertheless
..         self.body.append('\n\\begin{tabular}')
..         endmacro = '\\end{tabular}\n'
..     else:
..         self.body.append('\n\\begin{tabulary}{\\linewidth}')
..         endmacro = '\\end{tabulary}\n'

..     [...]

..     if not self.table.longtable and self.table.caption is not None:
..         self.body.append('\\end{threeparttable}\n')


..     NACHHER:

..     if not self.table.longtable and self.table.caption is not None:
..         self.body.append(u'\n\n\\begin{table}\\centering\n'
..                          u'\\capstart\\caption{%s}\n' % self.table.caption)
..     if self.table.longtable:
..         self.body.append('\n\\begin{longtable}')
..         endmacro = '\\end{longtable}\n\n'
..     elif self.table.has_verbatim:
..         self.body.append('\n\\begin{center}\\begin{tabular}')
..         endmacro = '\\end{tabular}\\end{center}\n\n'
..     elif self.table.has_problematic and not self.table.colspec:
..         self.body.append('\n\\begin{center}\\begin{tabular}')
..         endmacro = '\\end{tabular}\\end{center}\n\n'
..     else:
..         self.body.append('\n\\begin{center}\\begin{tabulary}{\\linewidth}')
..         endmacro = '\\end{tabulary}\\end{center}\n\n'

..     [...]

..     if not self.table.longtable and self.table.caption is not None:
..         self.body.append('\\end{table}\n\n')


.. ..
..     *   Zusätzlich nach folgendem suchen:

..     .. code-block:: python

..         if not self.table.longtable and self.table.caption is not None:
..         self.body.append(u'\n\n\\begin{threeparttable}\\centering\n'

..     und durch folgendes ersetzen:

..     .. code-block:: python

..         if not self.table.longtable and self.table.caption is not None:
..             self.body.append(u'\n\n\\begin{table}\\centering\n'
..                  u'\\caption{%s}\n' % self.table.caption)

..     und entsprechend (einfach nach threeparttable suchen)

..     .. code-block:: python

..         if not self.table.longtable and self.table.caption is not None:
..             self.body.append('\\end{table}\n\n')


Tabellen werden von Sphinx bei Verwendung der Grundeinstellungen automatisch
zentriert; Persönlich möchte ich in der HTML-Darstellung allerdings die
Fußnoten, die via CSS ebenfalls als Tabellen gesetzt werden, linksbündig
ausrichten. Um dies zu erreichen, habe ich in der Datei
``themes/basic/static/basic.css_t`` den Eintrag ``table.docutils``
folgendermaßen ergänzt:

.. code-block:: css
    :emphasize-lines: 2,4-5,8-16

    table.docutils {
        border: 1px solid gray;
        border-collapse: collapse;
        margin-left: auto;
        margin-right: auto;
    }

    table.docutils.footnote, table.docutils.citation {
        border: 0px;
        border-collapse: collapse;
        margin-left: 0;
    }

    table.docutils.footnote td, table.docutils.citation td {
        border: 0px;
    }


.. _Maximalbreite der HTML-Dokumentation festlegen:

.. rubric:: Maximalbreite der HTML-Dokumentation festlegen

In den letzten Jahren sind Computer-Monitore immer breiter geworden. Im
Vergleich zu einer DinA4-Seite sind somit, sofern keine Beschränkungen
festgelegt werden, auch wesentlich längere Textzeilen möglich.

Mittels einer entsprechenden CSS-Option kann erreicht werden, dass auch bei sehr
breiten Monitoren ein als kleiner Absatz geschriebener Text als eine einzige
Zeile erscheint -- das Layout der HTML-Seite bleibt somit der Druckversion
ähnlich. Dies gilt nicht nur für Text, sondern auch für Graphiken, die mit einer
prozentualen Breitenangabe eingebunden werden: In LaTeX ist die Zeilenbreite des
Texts als Referenzwert üblich, in HTML standardmäßig die Breite des
Browserfensters; auf breiten Monitoren werden Graphiken in einem
Vollbild-Browser entsprechend groß dargestellt.

Bei der Grund-Wissen-Seite wird das Theme ``sphinxdoc`` verwendet; die
entsprechende CSS-Datei ist ``themes/sphinxdoc/static/sphinxdoc.css_t``. Hier
muss zur Begrenzung der HTMl-Seitenbreite folgende Änderung vorgenommen werden:

.. code-block:: css
    :emphasize-lines: 15,16,17

    NACHHER:

    body {
        font-family: 'Lucida Grande', 'Lucida Sans Unicode', 'Geneva',
                     'Verdana', sans-serif;
        font-size: 14px;
        letter-spacing: -0.01em;
        line-height: 150%;
        text-align: center;
        background-color: #BFD1D4;
        color: black;
        padding: 0;
        border: 1px solid #aaa;

        margin: auto;
        min-width: 740px;
        max-width: 1200px;
    }

Mit den obigen Einstellungen wird die Webseite mit der angegebenen Breite
zentriert dargestellt; der Rest des Browserfensters durch einen neutralen
Hintergrund ausgefüllt.



.. _Kopfzeile in der Druckversion entfernen:

.. rubric:: Kopfzeile in der Druckversion entfernen

Normalerweise erscheint in der mittels LaTeX erzeugten PDF-Datei in der
Kopfzeile jeder Seite ein Versionshinweis. Um dies zu deaktivieren, muss die
Datei ``texinputs/sphinx.sty`` an zwei Stellen abgeändert werden. Zum einen muss
die ``\fancyhead``-Zeile, die den Versions-Eintrag erzeugt, mit einem
``%``-Zeichen auskommentiert werden. Zum anderen kann der Strich zwischen
Kopfzeile und erster Textzeile entfernt werden, indem ihr Wert auf ``0.0``
gesetzt wird:

.. code-block:: tex
    :emphasize-lines: 17-21

    VORHER:

    \fancypagestyle{normal}{
      \fancyhf{}
      \fancyfoot[LE,RO]{{\py@HeaderFamily\thepage}}
      \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
      \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
      \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}
      \renewcommand{\headrulewidth}{0.4pt}
      \renewcommand{\footrulewidth}{0.4pt}


    NACHHER:

    \fancypagestyle{normal}{
      \fancyhf{}
      \fancyfoot[CE,CO]{{\py@HeaderFamily\thepage}}
    % \fancyfoot[LO]{{\py@HeaderFamily\nouppercase{\rightmark}}}
    % \fancyfoot[RE]{{\py@HeaderFamily\nouppercase{\leftmark}}}
    % \fancyhead[LE,RO]{{\py@HeaderFamily \@title, \py@release}}
      \renewcommand{\headrulewidth}{0.0pt}
      \renewcommand{\footrulewidth}{0.4pt}

Soll nicht zwischen geraden und ungeraden Seitenanzahlen (``even``, ``odd``)
unterschieden werden (LaTeX-Option :ref:`oneside <gwil:oneside>`), so sollte
hier anstelle ``CE,CO`` besser ``C`` gesetzt werden. Dies sollte dann auch bei
den entsprechenden Einträgen für ``plain`` berücksichtigt werden, also für
Seiten auf denen ein neues Kapitel beginnt.


.. rubric:: Darstellung von Verbatim-Boxen anpassen

Um Code-Beispiele in LaTeX besser hervorzuheben, habe ich in der Datei
``texinputs/sphinx.sty`` die Farben für die Verbatim-Umgebung und ihre
Umrandung etwas angepasst:

.. code-block:: tex
    :emphasize-lines: 8,9

    VORHER:

    \definecolor{VerbatimColor}{rgb}{1,1,1}
    \definecolor{VerbatimBorderColor}{rgb}{1,1,1}

    NACHHER:

    \definecolor{VerbatimColor}{rgb}{0.97,0.97,1}
    \definecolor{VerbatimBorderColor}{rgb}{0.75,0.75,1}

Die Boxen werden so in einem schwachen Blau mit einem ebenfalls leicht blauen
Rahmen gedruckt.



.. .. rubric:: Darstellung von Subparagraphen und Rubriken anpassen

.. Bei umfangreichen Dokumentationen mit vielen ineinander geschachtelten
.. Abschnitten können auch Sub-Paragraphen als Überschriften vorkommen. [#]_ Damit
.. diese -- wie andere Überschriften auch -- in LaTeX ebenfalls in blauer
.. Schriftfarbe gedruckt werden, ist die Datei ``texinputs/sphinx.sty`` hinter um
.. folgenden Eintrag zu ergänzen:


.. .. code-block:: tex

..     VORHER:

..     \titleformat{\section}{\Large\py@HeaderFamily}%
..         {\py@TitleColor\thesection}{0.5em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\subsection}{\large\py@HeaderFamily}%
..         {\py@TitleColor\thesubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\subsubsection}{\py@HeaderFamily}%
..         {\py@TitleColor\thesubsubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\paragraph}{\small\py@HeaderFamily}%
..         {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}


..     NACHHER:

..     \titleformat{\section}{\Large\py@HeaderFamily}%
..         {\py@TitleColor\thesection}{0.5em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\subsection}{\large\py@HeaderFamily}%
..         {\py@TitleColor\thesubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\subsubsection}{\py@HeaderFamily}%
..         {\py@TitleColor\thesubsubsection}{0.5em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\paragraph}{\small\py@HeaderFamily}%
..         {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}
..     \titleformat{\subparagraph}{\small\py@HeaderFamily}%
..         {\py@TitleColor}{0em}{\py@TitleColor}{\py@NormalColor}

.. .. [#] Das gilt insbesondere auch für mit ``.. rubric:: Titel`` erzeugte
..     Rubriken. Diese werden ohne die obigen Anpassungen in schwarzer Farbe und
..     größer als die Paragraphen-Überschriften dargestellt.


.. _Titelseite gestalten:

.. rubric:: Titelseite gestalten

Nach persönlichem Geschmack habe ich die Titelseite etwas abgewandelt --
insbesondere wollte ich dort einen Link auf die URL der Homepage einfügen.
Hierbei habe ich in der Datei ``texinputs/sphinxmanual.cls`` die Funktion
``\maketitle`` folgendermaßen angepasst;

.. code-block:: tex
    :emphasize-lines: 19,28

    \renewcommand{\maketitle}{%
      \let\spx@tempa\relax
      \ifHy@pageanchor\def\spx@tempa{\Hy@pageanchortrue}\fi
      \hypersetup{pageanchor=false}% avoid duplicate destination warnings
      \begin{titlepage}%
        \let\footnotesize\small
        \let\footnoterule\relax
        \noindent\rule{\textwidth}{1pt}\par
          \begingroup % for PDF information dictionary
           \def\endgraf{ }\def\and{\& }%
           \pdfstringdefDisableCommands{\def\\{, }}% overwrite hyperref setup
           \hypersetup{pdfauthor={\@author}, pdftitle={\@title}}%
          \endgroup
        \begin{flushright}%
          \sphinxlogo
          \py@HeaderFamily
          {\Huge \@title \par}
          {\itshape\LARGE \py@release\releaseinfo \par}
          {\itshape Aktualisiert am \@date \par}
          \vfill
          {\LARGE
            \begin{tabular}[t]{c}
              \@author
            \end{tabular}
            \par}
          \vfill\vfill
          {\Large
          \url{http://www.grund-wissen.de} \par
           \vfill
           \py@authoraddress \par
          }%
        \end{flushright}%\par
        \@thanks
      \end{titlepage}%

      \setcounter{footnote}{0}%
      \let\thanks\relax\let\maketitle\relax
      %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
      \if@openright\cleardoublepage\else\clearpage\fi
      \spx@tempa
    }


Zwischen ``\end{titlepage}`` und ``\setcounter{footnote{0}`` habe ich zusätzlich
folgenden Text hinzugefügt, der bei jeder meiner Dokumentationen auf der zweiten
Seite des Dokuments, also unmittelbar vor dem Inhaltsverzeichnis, erscheinen
soll: [#]_

.. code-block:: tex
    :emphasize-lines: 21-63

    VORHER:

    [...]

    \end{titlepage}%

    \setcounter{footnote}{0}%
      \let\thanks\relax\let\maketitle\relax
      %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
      \if@openright\cleardoublepage\else\clearpage\fi
      \spx@tempa
    }


    NACHHER:

    [...]

    \end{titlepage}%

    Dieses Buch wird unter der
    \href{http://de.wikipedia.org/wiki/Creative_Commons}{Creative Commons
    License (Version 3.0, by-nc-sa)} ver\"{o}ffentlicht. Alle Inhalte d\"{u}rfen
    daher in jedem beliebigen Format vervielf\"{a}ltigt und/oder
    weiterverarbeitet werden, sofern die Weitergabe nicht kommerziell ist, unter
    einer gleichen Lizenz erfolgt, und das Original als Quelle genannt wird.
    Siehe auch:

    \href{https://creativecommons.org/licenses/by-nc-sa/3.0}{Erl\"{a}uterung der
        Einschr\"{a}nkung by-nc-sa} \\
    \href{https://irights.info/wp-content/uploads/userfiles/CC-NC_Leitfaden_web.pdf}{Leitfaden
        zu Creative-Commons-Lizenzen}

    Unabh\"{a}ngig von dieser Lizenz ist die Nutzung dieses Buchs f\"{u}r
    Unterricht und Forschung \href{http://dejure.org/gesetze/UrhG/52a.html}{(\S
    52a UrhG)} sowie zum privaten Gebrauch
    \href{http://dejure.org/gesetze/UrhG/53.html}{(\S 53 UrhG)} ausdr\"{u}cklich
    erlaubt.

    Der Autor erhebt mit dem Buch weder den Anspruch auf Vollst\"{a}ndigkeit
    noch auf Fehlerfreiheit; insbesondere kann f\"{u}r inhaltliche Fehler keine
    Haftung \"{u}bernommen werden.

    Die Quelldateien dieses Buchs wurden unter
    \href{http://grund-wissen.de/linux/index.html}{Linux} mittels
    \href{http://grund-wissen.de/linux/tools/vim/index.html}{Vim} und
    \href{http://grund-wissen.de/linux/tools/sphinx/index.html}{Sphinx}, die
    enthaltenen Graphiken mittels
    \href{http://grund-wissen.de/linux/tools/inkscape.html}{Inkscape} erstellt.
    Der Quellcode sowie die Original-Graphiken  k\"{o}nnen \"{u}ber die
    Projektseite heruntergeladen werden:

    \textbf{http://www.grund-wissen.de}
    \\[3pt]

    Bei Fragen, Anmerkungen und Verbesserungsvorschl\"{a}gen bittet der Autor um
    eine kurze Email an folgende Adresse:

    \textbf{info@grund-wissen.de}
    \\[5pt]

    Augsburg, den \today. \\[6pt]
    \@author

    \setcounter{footnote}{0}%
      \let\thanks\relax\let\maketitle\relax
      %\gdef\@thanks{}\gdef\@author{}\gdef\@title{}
      \if@openright\cleardoublepage\else\clearpage\fi
      \spx@tempa
    }

Zusätzlich habe ich in der Datei ``writers/latex.py`` beide Vorkommnisse der
Bezeichnung "Release" durch "Version" ersetzt.

.. _Mehrspaltige Aufzählungen (hlist) in LaTeX:

.. rubric:: Mehrspaltige Aufzählungen (hlist) in LaTeX

Mit der ``hlist``-Umgebung kann man mit Sphinx mehrspaltige Tabellen erstellen.
Der Code dafür sieht etwa so aus:

.. code-block:: rst

    .. hlist::
        :columns: 2

        * Item 1
        * Item 2
        * ...

Während die HTML-Ausgabe ausgezeichnet funktioniert, werden ``hlist``-Umgebungen
vom LaTeX-Übersetzer wie "normale" Listen behandelt. Persönlich verwende ich
in den allermeisten Fällen zweispaltige ``hlists``, so dass ich mir in der Datei
``writers/latex.py`` mit folgendem Trick Abhilfe für den erstellten LaTeX-Code
geschaffen habe:

.. code-block:: python
    :emphasize-lines: 19,28

    VORHER:

    def visit_hlist(self, node):
        self.compact_list += 1
        self.body.append('\\begin{itemize}\\setlength{\\itemsep}{0pt}'
                         '\\setlength{\\parskip}{0pt}\n')

    [...]

    def depart_hlist(self, node):
        self.compact_list -= 1
        self.body.append('\\end{itemize}\n')


    NACHHER:

    def visit_hlist(self, node):
        self.compact_list += 1
        self.body.append('\\begin{multicols}{2}')
        self.body.append('\\begin{itemize}\\setlength{\\itemsep}{0pt}'
                         '\\setlength{\\parskip}{0pt}\n')

    [...]

    def depart_hlist(self, node):
        self.compact_list -= 1
        self.body.append('\\end{itemize}\n')
        self.body.append('\\end{multicols}')

Damit dies funktioniert, muss in der Konfigurationsdatei ``conf.py`` des
jeweiligen Projekts eine Ergänzung der LaTeX-Präambel vorgenommen werden:

.. code-block:: python

    latex_elements = {
        'preamble':  '''\usepagckage{multicol}'''
        # ...
        }

Mit der obigen Einstellung werden alle ``hlists`` in der Druckversion als
zweispaltige Aufzählungen dargestellt. [#]_



.. _Linkcheck bei URLs mit Umlauten:

.. rubric:: Linkcheck bei URLs mit Umlauten

In der derzeit von mir genutzten Sphinx-Version 1.7.1 bleibt der Linkcheck
(``make linkcheck``) bei manchen Projekten hängen, wenn dieser in der
``Makefile`` mittels mittels der Option ``SPHINXBUILD   = python3 -msphinx``
aufgerufen wird. Abhilfe ist dadurch möglich, dass in der Datei
``builders/linckcheck.py`` folgende Ersetzung vorgenommen wird:

.. code-block:: python
    :emphasize-lines: 13

    VORHER:

    # handle non-ASCII URIs
    try:
        req_url.encode('ascii')
    except UnicodeError:
        req_url = encode_uri(req_url)

    NACHHER:

    # handle non-ASCII URIs
    try:
        req_url.encode('utf-8')
    except UnicodeError:
        req_url = encode_uri(req_url)

Damit funktioniert ``make linkcheck`` auch, wenn auf URLS verlinkt wird, die
Sonderzeichen enthalten (wie es beispielsweise bei Wikipedia häufig der Fall
ist).


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Hierbei muss das LaTeX-Paket ``multicol`` installiert sein. Sollte dies
    nicht der Fall sein, kann es von der `CTAN-Projektseite
    <http://www.ctan.org/tex-archive/macros/latex/required/tools>`_ herunter
    geladen werden und gemäß dem üblichen :ref:`Installations-Schema
    <CTAN-Zusatzpakete installieren>` nachinstalliert werden.

.. [#] Diese Lösung ist nicht elegant, erfüllt aber ihren Zweck. Für
    Verbesserungshinweise bin ich dankbar. ;-)

