.. _Bedienung:

Bedienung
=========

.. {{{

Vim wird meist komplett über die Tastatur gesteuert. Damit es bei einer
begrenzten Anzahl an Tasten möglich ist schnell durch Dateien zu navigieren,
Text einzugeben sowie Editierbefehle auszuführen, wurden verschiedene Ebenen
("Modi") eingeführt. Je nach aktivem Modus haben die Tasten verschiedene
Bedeutungen.

* Beim Start von Vim befindet man sich im Normalmodus.
* In einen anderen Modus gelangt man durch Drücken einer entsprechenden Taste.
* Durch Drücken von ``ESC`` gelangt man in den Normalmodus zurück.

Um Vim zu beenden, kann man im Normalmodus ``ZQ`` (schließen, Änderungen
verwerfen) beziehungsweise ``ZZ`` (schließen, Änderungen speichern) eingeben.

.. _Einfügemodus:

.. }}}

Einfügemodus
------------
.. {{{

Der Einfügemodus dient -- wie der Name schon sagt -- zum Einfügen von Text in
die aktuelle Datei. Hier gleicht Vim einem "normalen" Editor: Alle Buchstaben,
Zahlen, etc. erscheinen nach der Eingabe an der aktuellen Position auf dem
Bildschirm.

Ausgehend vom Normalmodus gelangt man in den Einfügemodus durch Drücken einer
der folgenden Tasten:

.. list-table::
    :widths: 10 60 30
    :header-rows: 0

    * - ``i``
      - Text einfügen vor  der momentanen Position
      - (*insert*)
    * - ``I``
      - Text einfügen zu Beginn der momentanen Zeile
      -
    * - ``a``
      - Text einfügen nach der momentanen  Position
      - (*append*)
    * - ``A``
      - Text einfügen am Ende der  momentanen Zeile
      -
    * - ``o``
      - Text einfügen unter der aktuellen Zeile
      - (*open a new line*)
    * - ``O``
      - Text einfügen über der aktuellen  Zeile
      -

Auch mit ``s, S, c, C, r, R`` gelangt man in den Einfügemodus. Hierbei wird
jedoch bestehender Text ersetzt.

Gibt man beispielsweise ``10i`` gefolgt von etwas Text ein, so wird nach Beenden
der Eingabe mit ``Esc`` das 10-fache des eingegebenen Textes eingefügt.

Im Einfügemodus gibt es standardmäßig folgende Tastenkombinationen:

.. list-table::
    :widths: 20 60 20
    :header-rows: 0

    * - ``Ctrl n`` bzw. ``Ctrl p``
      - Vervollständigung des aktuellen Wortes anhand eines bereits vorkommenden
        Wortes
      - (*next* bzw. *previous word*)
    * - ``Ctrl x  Ctrl l``
      - Vervollständigung der aktuellen Zeile anhand einer bereits vorkommenden
        Zeile
      - (*line-completion*)
    * - ``Ctrl x  Ctrl f``
      - Vervollständigung der Eingabe von Dateinamen und Pfaden
      - (*file-completion*)


.. index:: Snippets (Vim)
.. _Vim-Snippets:

.. rubric:: Snippets

Durch die Verwendung von so genannten "Snippets" kann viel Tipparbeit gespart
werden. Das Prinzip hierbei ist sehr einfach: Man definiert sich frei wählbare
Abkürzungen, die dann nach einem Drücken der ``Tab``-Taste (oder einer anderen
frei wählbaren Taste) ein ganzes Template ausrollen können, so dass nur noch an
einzelnen Stellen Text eingefügt werden muss.

Das meiner Meinung nach beste Snippet-Plugin ist :ref:`Ultisnips <Ultisnips>`;
man kann damit je nach Dateityp beziehungsweise Endung einer Datei
unterschiedliche Abkürzungen definieren. Die Abkürzungen liegen allesamt in
einem gemeinsamen Ordner und sind jeweils mit ``dateityp.snippets`` benannt.
Beispielsweise kann man sich so sowohl für C-Dateien als auch für Python-Dateien
je ein Snippet mit der Abkürzung ``ife`` definieren, das dann nach einem Drücken
der ``Tab``-Taste im jeweiligen Dateityp eine ``if-else``-Abfrage mit
Sprungmarken zu den jeweiligen Eingabestellen erstellt.

Besonders praktisch sind Snippets für ein Arbeiten mit :ref:`LaTeX <gwil:LaTeX>` -Dateien: So kann
man beispielsweise ein Snippet namens ``art`` definieren, das eine gesamte
Standard-Präambel für die Dokumentklasse ``article`` definiert. So genügt es
dann, eine leere ``.tex``-Datei zu öffnen, im Einfügemodus ``art`` und ``Tab``
einzugeben, und man kann bereits mit dem Schreiben des eigentlichen Dokuments
beginnen. :-)

.. only:: html

    *Snippets-Beispieldateien:*

    * :download:`LaTeX-Snippets <tex.snippets>`
    * :download:`LaTeX-Math-Snippets <texmath.snippets>`
    * :download:`LaTeX-Template-Snippets <tex.snippets>`
    * :download:`RestructuredText-Snippets <rst.snippets>`

.. only:: latex

    Snippet-Beispieldateien sind auf der :ref:`Grund-Wissen <Grund-Wissen>`-Seite verlinkt.


.. _Normalmodus:

.. }}}

Normalmodus
-----------
.. {{{

.. {{{

Der Normalmodus dient der Navigation durch die geöffnete(n) Datei(en) und der
Bearbeitung von deren Inhalt. Jede Taste besitzt hier ihre eigene Funktion. Ein
`Spickzettel <http://tnerual.eriogerg.free.fr/vimqrc-ge.pdf>`_ kann in der
Lernphase hilfreich sein!

Eigene Zuweisungen von beliebigen Funktionen auf Tasten(kombinationen) lassen
sich mittels :ref:`Mappings <Mappings>` definieren.


.. _Bewegen:
.. _Bewegungsanweisungen:

.. }}}

Bewegen
^^^^^^^
.. {{{

Die folgenden Tasten(kombinationen) bewirken im Normalmodus eine Bewegung des
Cursors.

``hjkl`` kann alternativ zu den Pfeiltasten genutzt werden:

.. list-table::
    :widths: 20 20 60
    :header-rows: 0

    * - ``j``
      - :math:`\downarrow`
      - Gehe eine Zeile nach unten
    * - ``k``
      - :math:`\uparrow`
      - Gehe eine Zeile nach oben
    * - ``h``
      - :math:`\leftarrow`
      - Gehe eine Stelle nach links
    * - ``l``
      - :math:`\rightarrow`
      - Gehe eine Stelle nach rechts

``Ctrl f`` und ``Ctrl b`` entsprechen ``PageDOWN`` und ``PageUp``:

.. todo: move in long lines!

.. list-table::
    :widths: 40 60
    :header-rows: 0

    * - ``Ctrl f`` oder ``PageDOWN``
      - Gehe eine Seite nach unten
    * - ``Ctrl b`` oder ``PageUP``
      - Gehe eine Seite nach oben

Um zu einer bestimmten Zeile zu gelangen, gibt es folgende Tastenkürzel:

.. list-table::
    :widths: 40 60
    :header-rows: 0

    * - ``gg``
      - Gehe zum Anfang der Datei
    * - ``G``
      - Gehe ans Ende der Datei

Mit der Eingabe von ``nG`` oder ``ngg`` springt man zur ``n``-ten Zeile.
Beispielsweise gelangt man durch die Eingabe von ``3gg`` beziehungsweise ``3G``
zur dritten Zeile.

.. _Navigation innerhalb einer Zeile:

.. rubric:: Navigation innerhalb einer Zeile

Mit ``0`` und ``$`` gelangt man schnell an den Anfang oder das Ende der
aktuellen Zeile. Einzelne Buchstaben lassen sich gezielt mit ``f`` und ``t``
ansteuern: [#]_

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``^`` oder ``0``
      - Gehe an den Anfang der Zeile
    * - ``$``
      - Gehe an das Ende der Zeile
    * - ``f`` ``Buchstabe``
      - Gehe zu dem nächsten Vorkommen von ``Buchstabe`` (exakt)
    * - ``F`` ``Buchstabe``
      - Gehe zu dem vorherigen Vorkommen von ``Buchstabe`` (exakt)
    * - ``t`` ``Buchstabe``
      - Gehe zu dem nächsten Vorkommen von ``Buchstabe`` (eine Stelle vorher)
    * - ``T`` ``Buchstabe``
      - Gehe zu dem vorherigen Vorkommen von ``Buchstabe`` (eine Stelle vorher)
    * - ``;`` (Strichpunkt)
      - Wiederhole die letzte Buchstabensuche in gleicher Richtung
    * - ``,`` (Komma)
      - Wiederhole die letzte Buchstabensuche in umgekehrter Richtung


Um von einem Wort zum nächsten zu gelangen, gibt es folgende Tastenkürzel:

.. list-table::
    :widths: 5 45 5 45
    :header-rows: 0

    * - ``w``
      - Gehe an den Anfang des nächsten Wortes
      - ``W``
      - wie ``w``, jedoch ohne Rücksicht auf Satzzeichen
    * - ``e``
      - Gehe an das Ende des aktuellen Wortes
      - ``E``
      - wie ``e``, jedoch ohne Rücksicht auf Satzzeichen
    * - ``b``
      - Gehe an den Anfang des vorherigen Wortes
      - ``B``
      - wie ``b``, jedoch ohne Rücksicht auf Satzzeichen
    * - ``ge``
      - Gehe an das Ende des vorherigen Wortes
      -
      -

.. _Navigation zwischen Sätzen und Abschnitten:

.. rubric:: Navigation zwischen Sätzen und Abschnitten

Für Sprünge zum nächsten beziehungsweise vorherigen Satz oder  Abschnitt  lassen  sich  die
Klammer-Symbole verwenden:

.. list-table::
    :widths: 5 45 5 45
    :header-rows: 0

    * - ``(``
      - Gehe an den Anfang des aktuellen Satzes
      - ``)``
      - Gehe an den Anfang des nächsten  Satzes
    * - ``{``
      - Gehe zu der vorherigen leeren Zeile
      - ``}``
      - Gehe zu der nächsten leeren Zeile
    * - ``[[``
      - Gehe zu der vorherigen Überschrift
      - ``]]``
      - Gehe zu der nächsten Überschrift

.. TODO Für Programmierer: Fehlen passende Gegenstücke, so können ungeschlossene Klammern leicht gefunden werden:

.. ``[(`` bzw. ``[)``   | gehe zu der vorherigen öffnenden bzw. schließenden runden Klammer
.. ``](`` bzw. ``])``   | gehe zu der nächsten öffnenden bzw. schließenden runden Klammer
.. ``[\{`` bzw. ``]\{`` | gehe zu der vorherigen öffnenden bzw. schließenden geschweiften Klammer
.. ``[\{`` bzw. ``]\}`` | gehe zu der nächsten öffnenden bzw. schließenden geschweiften Klammer

Innerhalb des aktuellen Bildschirms kann man sich wie folgt bewegen:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``H``
      - Gehe zu der obersten Zeile des Bildschirms
    * - ``M``
      - Gehe zu der mittleren Zeile des Bildschirms
    * - ``L``
      - Gehe zu der untersten Zeile des Bildschirms

Hierbei gelangt man mit z.B. ``5H`` zur fünften Zeile des aktuellen Bildschirms,
mit ``2L`` zur vorletzten.


Manchmal (z.B. beim Aufnehmen von :ref:`Makros`)  finden  auch  folgende  Tasten
Verwendung:

.. list-table::
    :widths: 15 80
    :header-rows: 0

    * - ``+``
      - Gehe zum ersten Zeichen der folgenden Zeile
    * - ``-``
      - Gehe zum ersten Zeichen der vorherigen Zeile
    * - ``n|``
      - Gehe zum ``n``-ten Zeichen der aktuellen Zeile
    * - ``gm``
      - Gehe zur Fenstermitte (horizontal)
    * - ``%``
      - Gehe zum passenden Gegenstück einer Klammer
    * - ``Ctrl d``
      - Gehe eine halbe Seite nach unten
    * - ``Ctrl u``
      - Gehe eine halbe Seite nach oben
    * - ``Ctrl e``
      - Scrolle den Bildschirm eine Zeile nach oben (der Cursor bleibt
        unverändert)
    * - ``Ctrl y``
      - Scrolle den Bildschirm eine Zeile nach unten (der Cursor bleibt
        unverändert)
    * - ``zt``
      - Scrolle den Cursor an das obere Ende des Bildschirms
    * - ``zb``
      - Scrolle den Cursor an das untere Ende des Bildschirms
    * - ``zz``
      - Scrolle den Cursor in die Mitte des Bildschirms

.. _Weitere Navigationsmöglichkeiten:

.. rubric:: Weitere Navigationsmöglichkeiten

Folgende Tastenkombinationen sind im Normalmodus ebenfalls oftmals hilfreich:

.. list-table::
    :widths: 10 90
    :header-rows: 0

    * - ``gf``
      - Öffne die Datei unter dem Cursor
    * - ``gx``
      - Öffne den Link unter dem Cursor im Standard-Webbrowser (beispielsweise
        Firefox)

Beide Tastenkombinationen funktionieren nur, wenn sich der Cursor aktuell über
einem existierenden Dateipfad oder einer Web-Adresse befindet.


.. _Suchen:
.. _Suchanweisungen:

.. }}}

Suchen
^^^^^^
.. {{{

Im Normalmodus kann man mit ``/`` beziehungsweise ``?`` die aktuelle Datei
vorwärts beziehungsweise rückwärts nach Textstellen durchsuchen:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``/`` ``Suchbegriff``
      - Gehe zu dem nächsten Vorkommen von ``Suchbegriff``
    * - ``?`` ``Suchbegriff``
      - Gehe zu dem vorherigen Vorkommen von ``Suchbegriff``
    * - ``*``
      - Gehe zu dem nächsten Vorkommen des Worts unter dem Cursor
    * - ``#``
      - Gehe zu dem vorherigen Vorkommen des Worts unter dem Cursor
    * - ``gd``
      - Gehe zu dem ersten Vorkommen des Worts unter dem Cursor (*go [to the] definition*)

Ist die Option ``hlsearch`` in der :ref:`Konfigurationsdatei` gesetzt, so werden
die Treffer farblich hervorgehoben. Mittels ``:nohl`` ("no-highlight") oder
einem entsprechenden :ref:`Mapping <Mappings>` kann die Hervorhebung wieder
aufgehoben werden.

Zu dem jeweils nächsten Treffer gelangt man mit ``n``:

.. list-table::
    :widths: 15 80
    :header-rows: 0

    * - ``n``
      - Gehe zum nächsten Treffer
    * - ``N``
      - Gehe zum nächsten Treffer (umgekehrte Richtung)

Mit ``gD`` kann auch nach einer globalen Definition (in allen geöffneten Buffern
gesucht werden.


.. _Bearbeiten:
.. _Bearbeitungsanweisungen:

.. }}}

Bearbeiten
^^^^^^^^^^
.. {{{

Im Normalmodus gibt es folgende Anweisungen, um Text zu kopieren, löschen,
abzuändern, oder einzufügen:


.. list-table::
    :widths: 15 60 25
    :header-rows: 0

    * - ``y``
      - Kopieren
      - (*yank*)
    * - ``d``
      - Löschen bwz. Ausschneiden
      - (*delete*)
    * - ``c``
      - Ändern
      - (*change*)
    * - ``p``
      - Einfügen
      - (*paste*)

Damit lassen sich beliebige Mengen an Text bearbeiten:

.. list-table::
    :widths: 35 15 20 20
    :header-rows: 0

    * - Text
      - kopieren
      - ändern
      - löschen
    * - wortweise vorwärts
      - ``yw``
      - ``cw``
      - ``dw``
    * - wortweise rückwärts
      - ``yb``
      - ``cb``
      - ``db``
    * - bis zum Zeilenanfang
      - ``y0``
      - ``c0``
      - ``d0``
    * - bis zum Zeilenende
      - ``y$``
      - ``c$`` oder ``C``
      - ``d$`` oder ``D``
    * - die ganze Zeile
      - ``yy``
      - ``cc``
      - ``dd``

**Tip**: Mir erscheint es logisch, mit ``Y`` alles bis zum Zeilenende zu
kopieren. Da dies nicht standardmäßig der Fall ist, habe ich mir ein
eigenes Mapping in der :ref:`Konfigurationsdatei` so definiert.

Natürlich lassen sich die Anweisungen wieder beliebig multiplizieren, ``c3W``
oder ``3cW`` ändert die nächsten drei Wörter ohne Rücksicht auf
Satzzeichen, ``y3y`` oder ``3yy`` löscht die nächsten drei Zeilen. Bei
umfassenderen Textmengen empfiehlt es sich, diese zuerst im :ref:`visuellen
Modus <Visueller Modus>` zu markieren, und dann die entsprechende Taste für
die gewünschte Bearbeitungsfunktion zu drücken.

Will man nur einzelne Buchstaben oder Ziffern abändern, so kann man folgende
Funktionen nutzen:

.. list-table::
    :widths: 5 70 10
    :header-rows: 0

    * - ``x``
      - Lösche das Zeichen unter dem Cursor
      -
    * - ``~``
      - Ändere Kleinbuchstaben in Großbuchstaben und umgekehrt
      -
    * - ``gu``
      - Ändere Buchstaben in Kleinbuchstaben (auch visuell markierte Bereiche)
      -
    * - ``gU``
      - Ändere Buchstaben in Großbuchstaben (auch visuell markierte Bereiche)
      -
    * - ``r``
      - Ändere das Zeichen unter dem Cursor, danach weiter im Normal-Mode
      - (*replace*)
    * - ``R``
      - Überschreibe eine beliebige Anzahl an Zeichen ("Replace"-Mode, zurück mit ``ESC``)
      -
    * - ``s``
      - Ändere das Zeichen unter dem Cursor, weiter im Insert-Mode
      - (*substitute*)
    * - ``S``
      - Ändere die ganze Zeile
      -

Bei jeder Bearbeitungsanweisung wird der entsprechende Textteil in die
Zwischenablage kopiert. Von dort aus kann er mittels ``p`` wieder eingefügt
werden:

.. list-table::
    :widths: 10 90

    * - ``p``
      - Füge Inhalt des Zwischenspeichers *hinter* dem Cursor ein
    * - ``P``
      - Füge Inhalt des Zwischenspeichers *vor* dem Cursor ein

Im Einfügemodus kann Text aus der systemweiten Zwischenablage mittels
``Shift Insert`` (Einfüge-Taste) oder durch Klick auf die mittlere
Maustaste (gleichzeitiges Klicken von linker und rechter Taste bei
zweitastigen Mäusen und Notebooks) eingefügt werden.

Im Normalmodus kann Text aus der systemweiten Zwischenablage mittels des
:ref:`Registers <Register>` ``*`` genutzt, also mittels ``"*p`` beziehungsweise
``"*P`` eingefügt werden.

.. _Undo und Redo:

.. }}}

Undo und Redo
^^^^^^^^^^^^^
.. {{{

Änderungen können mit ``u`` rückgängig gemacht beziehungsweise mit ``Ctrl r``
wiederhergestellt werden:

.. list-table::
    :widths: 20 50 40

    * - ``u``
      - Mache die letzte Änderung rückgängig
      - (*undo*)
    * - ``U``
      - Mache alle Änderungen in der aktuellen Zeile rückgängig
      -
    * - ``Ctrl r``
      - Stelle eine rückgängig gemachte Änderung wieder her
      - (*redo*)
    * - ``.``
      - Wiederhole die zuletzt getätigte Texteingabe, Textbearbeitung,
        Formatierung, etc.
      -


.. _Marker:

.. }}}

Marker
^^^^^^
.. {{{

Muss man öfters innerhalb einer Datei hin- und herspringen, so schaffen
Markierungshilfen (*Marker*) Abhilfe.

Im Normalmodus kann man die Stelle, an der sich der Cursor gerade befindet,  mit
``m`` gefolgt von einem beliebigen Buchstaben markieren:

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - ``m`` ``Kleinbuchstabe``
      - Setze  eine lokale Markierung (gilt nur in der aktuellen Datei)
    * - ``m`` ``Großbuchstabe``
      - Setze eine globale Markierung

Mit Hilfe der globalen Markierungen lassen sich häufig genutzte Dokumente
schnell laden, egal wo man sich gerade befindet.

*Beispiel:* Man kann man mit ``'G`` zu genau der Stelle wechseln, die man
vorhergehend mit ``mG`` markiert hat. Liegt der Marker dabei in einer anderen
Datei, so bleibt der ursprüngliche Buffer im Hintergrund geöffnet (ein
:ref:`Wechsel zwischen den geöffneten Dateien <Buffer wechseln>` ist
beispielsweise mit dem :ref:`Minibuf-Explorer`-Plugin leicht möglich).

Mit ``'`` (einfaches Anführungszeichen), gefolgt von dem angegebenen
Buchstaben, gelangt man von wieder zu der entsprechenden Zeile, mittels
````` (Apostroph) sogar in die entsprechende Spalte. Mittels ``''``
beziehungsweise `````` gelangt man zur zuletzt bearbeiteten Zeile
beziehungsweise Position zurück.

*Tipp:* Mittels ``'.`` gelangt man zu der zuletzt editierten Stelle, mit
``'^`` zur letzten Einfüge-Stelle, und mit ``'"`` zur Position beim letzten
Beenden zurück!

Ein weiteres Springen zwischen verschiedenen Änderungen und deren Positionen ist
mittels ``Ctrl o`` beziehungsweise ``Ctrl i`` möglich:

.. list-table::
    :widths: 15 80
    :header-rows: 0

    * - ``Ctrl o``
      - Gehe zurück zur letzten Änderung (beziehungsweise zur zuletzt geänderten
        Datei)
    * - ``Ctrl i``
      - Gehe vorwärts zur letzten Änderung (umgekehrte Richtung)

``Ctrl o`` beziehungsweise ``Ctrl i`` können auch mehrfach hintereinander
gedrückt werden, um weiter zurück beziehungsweise vor in der Positions-History
zu springen.

.. _Register:

.. }}}

Register
^^^^^^^^
.. {{{

Vim besitzt nicht nur *eine* Zwischenablage, sondern kann Textelemente und
:ref:`Makros` jedem beliebigen Kleinbuchstaben zuweisen. Ein Register ist quasi
eine benannte Zwischenablage.

Im Normalmodus kann man mit ``"`` ``Buchstabe`` auf einen Register zugreifen:

.. list-table::
    :widths: 40 60
    :header-rows: 0

    * - ``"`` ``Kleinbuchstabe`` ``Bearbeitungsanweisung``
      - Kopiere in/aus das Register ``Buchstabe`` hinein/heraus
    * - ``"`` ``Großbuchstabe`` ``Bearbeitungsanweisung``
      - Füge Text oder Code hinten an das Register ``Buchstabe`` an

*Beispiel:* Mittels ``"hyy`` kann die aktuelle Zeile in die Ablage ``h`` kopiert
werden. Deren Inhalt kann mit ``"hp`` wieder an anderer Stelle eingefügt werden.
So abgelegte Inhalte bleiben auch beim Schließen von Vim erhalten!

Mit ``:reg`` erhält man eine Übersicht, welcher Inhalt in welchem Register
abgelegt ist:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``:reg``
      - Zeige den Inhalt aller Register an

Die normale, Vim-interne (namenlose) Zwischenablage kann explizit über das
Register ``"`` angewählt werden. Ein anderes, spezielles Register ist die
systemweite Zwischenablage ``*``, mittels der ein Kopieren von beziehungsweise
in andere(n) Programme(n) möglich ist:

.. list-table::
    :widths: 35 65
    :header-rows: 0

    * - ``"*y`` ``Bewegung``
      - Kopiere in die Zwischenablage
    * - ``"*p`` ``Bewegung``
      - Füge aus der Zwischenabage ein

Eine weitere systemweite Zwischenablage ist ``~``, in welcher der zuletzt mit
der Maus ausgewählte Text abgespeichert ist.

Unter Linux werden Bereiche bereits durch ein einfaches Markieren
(:ref:`Visueller Modus`) in die systemweiten Zwischenablagen kopiert. An anderer
Stelle können sie dann mit ``Shift Ins`` (Einfüge-Taste) oder durch einen Klick
auf die mittlere Maustaste wieder eingefügt werden.

Auch im Einfüge- und im Kommandozeilenmodus kann auf die Inhalte der einzelnen
Register zugegriffen werden: Durch eine aufeinander folgende Eingabe von
``<c-r>`` und einem Registerbuchstaben beziehungsweise -Symbol wird der Inhalt des
entsprechenden Registers an der Cursorposition eingefügt:

.. list-table::
    :widths: 20 70
    :header-rows: 0

    * - ``<c-r>"``
      - Füge den Inhalt des namenlosen Registers an der Cursorpostition ein
    * - ``<c-r>%``
      - Füge den aktuellen Dateinamen (Register ``%``) an der Cursorposition ein
    * - ``<c-r>a``, ``<c-r>b`` usw.
      - Füge den Inhalt des Registers ``a``, ``b``, usw. an der Cursorposition
        ein

Weitere Informationen über die verschiedenen Register aus den Vim-Hilfeseiten
können mittels ``:h <c-r>`` aufgerufen werden.


.. _Makros:

.. }}}

Makros
^^^^^^
.. {{{

Es kann nicht nur Text in einem :ref:`Register` abgelegt werden, sondern auch
jede beliebige Anweisungssequenz. Wie bei einem Kassettenrecorder können
Anweisungen mit aufgezeichnet, und als "Makro" später beliebig oft wieder
abgespielt werden:

Im Normalmodus werden Makros mit ``q`` ``Buchstabe`` aufgezeichnet und mit
``@`` ``Buchstabe`` wiedergegeben:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``q`` ``Kleinbuchstabe``
      - Nehme eine Anweisungssequenz bis zum nächsten Drücken von ``q`` auf
    * - ``q`` ``Großbuchstabe``
      - Hänge eine Anweisungssequenz an das Register ``Buchstabe`` an
    * - ``@`` ``Buchstabe``
      - Führe die im Register ``Buchstabe`` liegende Anweisungssequenz aus

Es kann durchaus nützlich sein, z.B. mittels ``10@Buchstabe`` eine
Anweisungskette 10fach auszuführen. Speziell gleichförmige Bearbeitungen
mehrerer Dateien sind so möglich, denn :ref:`Bufferwechsel <Buffer wechseln>`
können ja gleich mit "aufgenommen" werden.. :-)

*Tipp:* Der zuletzt ausgeführte Makro-Anweisung kann mit ``@@`` wiederholt werden.

..  Die unmittelbar letzte Anweisung (Eingabe von Text, usw.) kann man auch ohne Makro
..  im Normalmodus mittels ``.`` (*Punkt*) wiederholen.

.. _Faltungen:

.. }}}

Faltungen
^^^^^^^^^
.. {{{

Werden Text-Dateien infolge ihrer Länge zu unübersichtlich, können bestimmte
Bereiche ausgeblendet werden. Das kann entweder über Schlüsselworte,
Einrückungen oder über Symbole erfolgen.

Beispielsweise wird Python-Code häufig anhand von Einrückungen gefaltet, in
Datei-Vergleichen mittels :ref:`diff <vimdiff>` werden gleiche Textbereiche
weggefaltet, so dass nur die Unterschiede in den Dateien sichtbar bleiben.
Wird kein spezieller Faltungsmechanismus von einem Plugin geladen, so wird das
in der :ref:`Konfigurationsdatei` festgelegt Faltungsschema verwendet. Oft
werden dabei als Faltungsmarkierungen ``{{{`` und ``}}}`` genutzt, so dass alle
Textbereiche, die sich zwischen solchen Dreifach-Klammern befinden, gefaltet
werden.

Folgende Anweisungen können im Umgang mit Faltungen nützlich sein:

.. list-table::
    :widths: 10 30 10
    :header-rows: 0

    * - ``zf``
      - Erstelle eine Faltung
      -
    * - ``zo``
      - Öffne eine Faltung
      -  (*open*)
    * - ``zc``
      - Schließe eine Faltung
      - (*close*)
    * - ``zd``
      - Entferne eine Faltung
      - (*delete*)
    * - ``\rf``
      - Falte die Datei neu
      - (*refold*)

Um eine Faltung zu erstellen, wird der Bereich meist zuerst visuell
markiert, und dann mittels ``zf`` gefaltet.

Faltungen können auch ineinandergeschachtelt (*nested*) auftreten. Faltungen
unter dem Cursor können einzeln oder auf einmal mittels ``za`` beziehungsweise
``zA`` geöffnet und geschlossen werden.

.. list-table::
    :widths: 10 40
    :header-rows: 0

    * - ``za``
      - Öffne beziehungsweise schließe lokale Faltungen
    * - ``zA``
      - Öffne beziehungsweise schließe lokale Faltungen (rekursiv)

Ebenfalls nützlich sind folgende Faltungsanweisungen:

.. list-table::
    :widths: 10 50 10
    :header-rows: 0

    * - ``zr``
      - Reduziere die Anzahl der Faltungsebenen um eins
      -  (*reduce*)
    * - ``zm``
      - Erhöhe die Anzahl der Faltungsebenen um eins
      - (*more*)
    * - ``zR``
      - Öffne alle Faltungen
      -
    * - ``zM``
      - Schließe alle Faltungen
      -

Persönlich habe ich mir in der Konfigurationsdatei mittels ``nmap <space> za``
ein Mapping definiert, das beim Drücken der Leertaste ``za`` aufruft, und damit
die aktuelle Textebene faltet oder aber , falls man sich mit dem Cursor über
einer Faltung befindet, diese wiederum öffnet.

.. Nach Belieben können Faltungen gelegentlich auch komplett de- und reaktiviert
..  werden:

..  .. list-table::
    ..  :widths: 10 40
    ..  :header-rows: 0

    ..  * - ``zn``
      ..  - Faltung deaktivieren
    ..  * - ``zN``
      ..  - Faltung reaktivieren
    ..  * - ``zi``
      ..  - Wechsel zwischen ``zn`` und ``zN``

..   *   Mit   ''\rf''   werden   die   Faltungen   einer   Datei   aufgefrischt

.. _Fenster splitten:

.. }}}

Fenster splitten
^^^^^^^^^^^^^^^^
.. {{{

Vim kann mehrere Dateien optional in verschiedenen Tabs im oder in unterteilten
Fenstern öffnen:

* Mit ``:tabedit datei`` wird eine Datei in einem neuen Tab geöffnet.
  Zwischen den Tabs kann mit ``Ctrl PageUP`` und ``Ctrl PageDOWN``
  gewechselt werden. Infos findet man beispielsweise unter ``:h tabpage.txt``.
  [#]_

* Mit ``:[v]split`` beziehungsweise ``Ctrl W s`` oder ``Ctrl W v`` wird ein Fenster
  horizontal beziehungsweise vertikal geteilt. Manche Plugins wie
  :ref:`Minibuf-Explorer <Minibuf-Explorer>` oder :ref:`Tagbar <Tagbar>` nutzen
  diese Funktion, um auf der linken Seite beispielsweise ein Inhaltsverzeichnis
  ein- oder auszublenden.

Anweisungen zur Handhabung von geteilten Fenstern werden gewöhnlich mit ``Ctrl W``
eingeleitet. Mit folgenden Tastenkombinationen kann man zwischen den geöffneten
Fenstern wechseln:

.. list-table::
    :widths: 20 80
    :header-rows: 0

    * - ``Ctrl W w``
      -  Wechsle zum jeweils nächsten Fenster (im Uhrzeigersinn)
    * - ``Ctrl W h j k l``
      - Wechsle man zum nächsten Fenster auf der linken, unteren, oberen oder
        rechten Seite
    * - ``Ctrl W H J K L``
      -  Verschiebe das aktuelle Fenster in die jeweilige Richtung
    * - ``Ctrl W r`` bzw. ``Ctrl W R``
      - Verschiebe alle geöffnete Fenster der Reihenfolge nach, das letzte wird
        das erste

Mit folgenden Anweisungen lässt sich die Größe des aktuellen Fensters anpassen:

.. list-table::
    :widths: 15 50
    :header-rows: 0

    * - ``Ctrl W +``
      - Vergrößere das aktuelle Fenster um eine Zeile
    * - ``Ctrl W -``
      - Verkleinere das aktuelle Fenster um eine Zeile
    * - ``n Ctrl W |``
      - Setze die Breite des aktuellen Fensters auf ``n``
    * - ``Ctrl W _``
      - Maximiere das aktuelle Fenster
    * - ``Ctrl W =``
      - Richte alle Fenster auf die gleiche Größe aus

Zum Schließen des aktuellen beziehungsweise der übrigen Fenster gibt es folgende
Tastenkombinationen:

.. list-table::
    :widths: 10 25 10
    :header-rows: 0

    * - ``Ctrl W c``
      - Schließe das aktuelles Fenster
      - (*close*)
    * - ``Ctrl W o``
      - Schließe alle anderen Fenster
      - (*close other*)

Persönlich nutze ich Fenster-Aufteilungen nur, wenn :ref:`Plugins <Vim-Plugins>`
dies erforderlich machen, beispielsweise das :ref:`Minibuf-Explorer
<Minibuf-Explorer>`-Plugin. Ansonsten nutze ich grundsätzlich 
eigene :ref:`Buffer <Buffer>`, wenn innerhalb einer Vim-Sitzung mehrere Dateien
bearbeitet werden sollen.

.. rubric:: Quickfixleiste

Nutzt man den Vim als Programmier-Umgebung beziehungsweise compiliert aus dem
Vim heraus Quellcode, so bekommt man Fehlermeldungen in der sogenannten
"Quickfix-Leiste" angezeigt. Im Prinzip ist das ein gesplittetes Fenster, in
welchem zwischen den Fehlern navigiert werden kann. Durch Drücken von ``Enter``
gelangt man an die entsprechende Stelle im Hauptdokument. Von dort aus gelangt
man zum nächsten beziehungsweise vorherigen Fehler mittels ``:cn``
beziehungsweise ``:cp``.

Gesplittete Fenster werden häufig von Plugins genutzt, um beispielsweise am
linken Seitenrand ein :ref:`Inhaltsverzeichnis <Tagbar>`  oder am unteren einen
:ref:`Buffer-Browser <Minibuf-Explorer>` einzublenden.

.. , am rechten einen Datei-Browser

.. Normalerweise wird die Quickfix-Leiste mit
.. ``:copen`` geöffnet und mit ``:cclose`` geschlossen. Bei häufigerem
.. Gebrauch empfiehlt sich dafuer allerdings z.B. folgendes Makro von der
.. fuer die Konfigurationsdatei:
..
.. command -bang -nargs=? QFix call QFixToggle(<bang>0)
.. function! QFixToggle(forced)
.. if exists("g:qfix_win") && a:forced == 0
.. cclose
.. unlet g:qfix_win
.. else
.. copen 10
.. let g:qfix_win = bufnr("$")
.. endif
.. endfunction
..
.. Tastenkuerzel F6 dafuer festlegen:
.. nmap <silent> <F6> :QFix<CR>

.. index:: vimdiff
.. _vimdiff:

.. rubric:: Vimdiff

Das Linux-Programm ``vimdiff`` zeigt ebenfalls in gesplitteten Fenstern
Unterschiede zwischen zwei Dateien an. Auf diese Weise lassen sich verschiedenen
Versionen des gleichen Dokuments schnell und übersichtlich abgleichen
(abweichende Stellen werden automatisch markiert):

.. code-block:: bash

 vimdiff datei1 datei2

Bewegt man sich in einer Datei nach unten, so scrolled die Anzeige der anderen
Datei im gegenüberliegenden Fenster mit, so dass stets die entsprechenden zwei
Zeilen verglichen werden. Beide Dateien können editiert werden, der Abgleich
erfolgt automatisch.


.. _Kommandozeilen-Modus:

.. }}}

.. }}}

Kommandozeilen-Modus
--------------------
.. {{{

.. {{{

Im Kommandozeilen-Modus können sowohl Vim-Anweisungen als auch :ref:`externe
Systemanweisungen <Aufrufe von externen Programmen>` aufgerufen werden.

Ausgehend vom Normalmodus gelangt man mittels ``:`` in den Kommandozeilen-Modus,
mittels ``Esc`` wieder zurück.

.. % bedeutet: Aktuelle Datei
.. %:p bedeutet: Aktuelle Datei als ganzer Pfad
.. %:p:h bedeutet: Head dieses Pfads (Pfad ohne Dateiname)
.. mehrere Angaben von :h sind möglich!

.. _Buffer:
.. _Buffer öffnen:
.. _Buffer einlesen:

.. }}}

Buffer öffnen
^^^^^^^^^^^^^
.. {{{

Eine neue Datei kann mit ``:edit`` (oder kurz ``:e``) als neuer Buffer geöffnet
werden, wobei die bisherige Datei als eigener Buffer im Hintergrund geladen
bleibt.

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:e dateiname``
      - eine Datei  öffnen beziehungsweise neu erstellen
    * - ``:e %``
      - die aktuelle Datei (``%``) neu laden

Das Zeichen ``%`` hat im Kommandozeilen-Modus eine eigene Bedeutung: Es steht
für den Namen der aktuell geöffneten Datei. Die Ausgabe von ``%`` lässt sich
unter anderem folgendermaßen ändern:

.. list-table::
    :name: tab-filename
    :widths: 10 50

    * - ``%``
      - Aktueller Dateiname
    * - ``%:~``
      - Aktueller Dateiname (relativ zum Home-Verzeichnis)
    * - ``%:p``
      - Aktueller Dateiname (absoluter Pfad)
    * - ``%:p:h``
      - Aktuelles Verzeichnis ("Head" des absoluten Pfads)
    * - ``%:p:h:h``
      - Übergeordnetes Verzeichnis ("Head" des aktuellen Verzeichnisses)
    * - ``%:p:r``
      - Aktueller Dateiname ohne Endung (absoluter Pfad)
    * - ``%:e``
      - Endung der aktuellen Datei

Eine vollständige Beschreibung kann mittels ``:h filename-modifiers``
aufgerufen werden.

Der Inhalt einer anderen Datei kann mittels ``:read`` (oder kurz ``:r``) hinter
der momentanen Cursor-Position eingefügt werden:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:r dateiname``
      - Inhalt einer Datei vor dem Cursor einfügen


.. _Buffer speichern:
.. _Buffer wechseln:

.. }}}

Buffer speichern und/oder wechseln
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

Um Vim zu beenden oder einzelne Dateien beziehungsweise Fenster zu schließen,
gibt man folgendes ein:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:q``
      - Schließe den aktuellen Buffer schließen (und beende Vim, falls nur ein
        Fenster offen ist)
    * - ``:qa``
      - Schließe alle Buffer, beende Vim
    * - ``:q!``
      - Schließe den aktuellen Buffer, verwerfe ungespeicherte Änderungen
    * - ``:w``
      - Speichere Änderungen an der aktuellen Datei
    * - ``:wq``
      - Speichere die aktuelle Datei und schließe den Buffer
    * - ``:wqa``
      - Speichere alle geöffneten Dateien und beende Vim
    * - ``:w Dateiname``
      - Speichere den aktuellen Buffer als ``Dateiname``

Auch die Schreib-Anweisung kann nur auf einen bestimmten Textbereich angewendet
werden. Beispielsweise kann man mit ``:1,25w dateiname`` die ersten ``25``
Zeilen der Datei in den angegebenen Dateinamen schreiben, oder man kann einen
Text visuell markieren und dabei ``:w`` eingeben; in der Kommandozeile wird
dabei automatisch ``'<,'>w`` angezeigt, wobei ``'<,'>`` den visuell markierten
Bereich bezeichnet.

In Vim können mehrere Dateien auf einmal geöffnet sein. Im Umgang mit
diesen Buffern sind folgende Anweisungen hilfreich:

.. list-table::
    :widths: 15 40 20
    :header-rows: 0

    * - ``:ls``
      - Zeige eine Liste an geöffneten Dateien an
      - (identisch mit ``:buffers``)
    * - ``:bn``
      - Gehe zur nächsten offenen Datei
      - (*buffer next*)
    * - ``:bp``
      - Gehe zur vorherigen offenen Datei
      - (*buffer previous*)
    * - ``:bf``
      - Gehe zur ersten geöffneten Datei
      - (*buffer first*)
    * - ``:bl``
      - Gehe zur letzten geöffneten Datei
      - (*buffer last*)
    * - ``:b#``
      - Gehe zur zuletzt verwendeten Buffer
      -
    * - ``:b 1..99``
      - Gehe zur Datei Nr. ``1..99`` der Bufferliste
      -
    * - ``:bd``
      - Lösche die aktuelle Datei aus der Buffer-Liste
      - (*buffer delete*)

.. :wn : write file and move to next (SUPER)
.. :bd : remove file from buffer list (SUPER)
.. :sp fred.txt : open fred.txt into a split

Mittels ``:bufdo`` kann man eine (oder mehrere mittels ``|`` ("Pipe")
verknüpfte) Anweisung(en) auf alle geöffneten Dateien anwenden:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:bufdo Anweisung``
      - Führe eine ``Anweisung`` in allen geöffneten Buffern aus

Das Gleiche kann man allerdings auch (meist sicherer) mittels einer
:ref:`Makro-Aufzeichnung <Makros>` erreichen.

.. _Aufrufe von externen Programmen:

.. }}}

Externe Programme aufrufen
^^^^^^^^^^^^^^^^^^^^^^^^^^
.. {{{

Externe Programme können im Kommandozeilen-Modus integriert werden, indem dem
jeweiligen Aufruf ein ``!`` vorangesetzt wird, wie zum Beispiel:

.. list-table::
    :widths: 10 60
    :header-rows: 0

    * - ``:ls``
      - Zeige eine Liste der geoffneten Buffer an (Vim-interne Funktion!)
    * - ``:!ls``
      - Gebe den Inhalt des Arbeitsverzeichnisses aus (gewöhnliche
        Linux-Anweisung)
    * - ``:.!sh``
      - Ersetze die momentane Zeile (``.``) durch die Rückgabe der Shell

Wird ein beliebiger Bereich vor dem Ausrufezeichen angegeben (z.B. ``%`` für die
aktuelle Datei oder ``.`` für die aktuelle Zeile), so wird die Rückgabe der
aufgerufenen Anweisung an entsprechender Stelle in die Datei geschrieben.

Die Ausgabe eines externen Programms kann wiederum mittels ``:r`` unmittelbar
hinter der aktuellen Cursorposition eingelesen werden. Um beispielsweise die
Ausgabe von ``!ls`` in den Buffer aufzunehmen, kann man folgendes eingeben:

.. code-block:: vim

    :r !ls

Im Normalmodus kann auch ``!!`` anstelle von ``:!`` eingegeben werden, um
externe Programme aufzurufen.

..  % !!tr -d abcd     # Delete a,b,c,d from the current line

Externe Programme können unter anderem eingesetzt werden, um die aktuelle Datei
zu compilieren. Um beispielsweise eine aktuell geöffnete :ref:`LaTeX
<gwil:LaTeX>` -Datei in ein ``.pdf``-Dokument umzuwandeln, kann man folgendes
eingeben:

.. code-block:: vim

    :!pdflatex %

Für längere derartige Aufrufe können natürlich wiederum in der
:ref:`Konfigurationsdatei` entsprechende :ref:`Mappings` vergeben werden. Danach
genügt im Normal- oder Einfügemodus ein individuelles Tastenkürzel, und der
dadurch definierte Prozess wird ausgeführt.

Ebenso ist es möglich, externe Programme nur auf einen bestimmten Bereich (z.B.
im :ref:`visuellen Modus <Visueller Modus>`) anzuwenden:

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``'<,'> !sort``
      - Sortiere den visuell markierten Bereich (``'<`` bis ``'>``)
    * - ``'a,'b !grep Wort``
      - Lösche alle Zeilen zwischen den Markern ``a`` und ``b``, die nicht
        ``Wort`` enthalten
    * - ``:r !grep "Test" Datei``
      - Lese die Ausgabe von ``grep`` ein und füge sie nach der aktuellen Stelle
        in die ``Datei`` ein

Das externe Programm muss also nicht an erster Stelle in der Kommandozeile
erscheinen.

.. _Text ersetzen:

.. }}}

Text ersetzen
^^^^^^^^^^^^^
.. {{{

Gezieltes Ersetzen von Text erfolgt in Vim nach folgendem Schema:

.. code-block:: vim

    :Bereich s/Suchbegriff/Ersetzung/Optionen

Als Optionen stehen dabei zur Verfügung:

.. list-table::
    :widths: 5 55 10
    :header-rows: 0

    * - ``c``
      - Frage bei jedem Treffer nach
      - (*confirmation*)
    * - ``g``
      - Beachte alle Vorkommen des Suchbegriffs (nicht nur den ersten Treffer in
        jeder Zeile)
      - (*global*)
    * - ``i``
      - Ignoriere Groß- / Kleinschreibung
      - (*ignore case*)

Wird eine dieser Anweisungen auf einen visuell markierten Bereich angewandt, so
werden dessen Grenzen ``'<``, ``'>`` als Bereich angenommen. Ansonsten kann
jeder beliebige Zeilenbereich, mit Komma getrennt, angegeben werden. Möchte man
Ersetzungen in der ganzen Datei vornehmen, so steht dafür ``%`` als
Auswahlbereich zur Verfügung.

*Beispiel:*

.. list-table::
    :widths: 20 60
    :header-rows: 0

    * - ``:% s/alt/neu/g``
      - Ersetze ``alt`` durch ``neu`` in der ganzen Datei
    * - ``:1,20 s/alt/neu/g``
      - Ersetze ``alt`` durch ``neu`` in den ersten 20 Zeilen

Kommt der Schrägstrich selbst im Suchbegriff vor, kann auch jedes andere
Zeichen zur Trennung von Suchbegriff, Ersetzungen und Optionen gewählt
werden. Das erste Zeichen nach dem ``s`` wird dann als Trennzeichen
verwendet (z.B. ``:%s #/pfad/#irgendwas#`` ).

Bisweilen ist es auch hilfreich, "seltsame" Zeichen in einer Textdatei zu
ersetzen, beispielsweise wenn Text aus einer ``.pdf``-Datei mittels
``pdftotext`` in eine Textdatei extrahiert wird. Die zu löschenden Zeichen
können dann visuell markiert und mittels ``y`` in die Vim-interne Zwischenablage
kopiert werden. In der Kommandozeile kann der so kopierte Inhalt dann mittels
``<c-r> *`` wieder eingefügt werden.

.. _Reguläre Ausdrücke:

.. }}}

Reguläre Ausdrücke
^^^^^^^^^^^^^^^^^^
.. {{{

Das Suchen und Ersetzen von Textstücken lässt sich durch so genannte reguläre
Ausdrücke oft wesentlich erleichtern beziehungsweise beschleunigen. Hierzu können
spezielle Zeichen verwendet werden, die jeweils einem bestimmten Suchmuster
entsprechen.

Werden die folgenden Zeichen in einer Such- oder Ersetzungsanweisung verwendet,
so werden sie als reguläre Ausdrücke interpretiert. Möchte man das jeweilige
Zeichen in seiner Grundbedeutung interpretiert haben, so muss ein ``\``
(Backslash) davor platziert werden:

.. list-table::
    :widths: 10 50
    :header-rows: 0

    * - ``\``
      - Sonderbedeutung des nächsten Zeichens aufheben ("\\" entspricht einem Backslash)
    * - ``^``
      - Zeilenanfang
    * - ``$``
      - Zeilenende
    * - ``\r``
      - Zeilenende (carriage return)
    * - ``\t``
      - Tabulator
    * - ``.``
      - Ein beliebiges Zeichen
    * - ``*``
      - Multiplexer: Das vorhergehende Zeichen null mal oder beliebig oft
    * - ``[ ]``
      - Selektierer: Eines der Zeichen innerhalb der eckigen Klammern
    * - ``[^  ]``
      - Selektierer mit Negation: Ein Zeichen, das *nicht* in der eckigen Klammer vorkommt
    * - ``&``
      - Nur im Ersetzungsbereich: Textstelle, auf die das Suchmuster zutrifft.

..  ~ 	Matches last given substitute string.

Ebenso gibt es Zeichen, die in einer Such- oder Ersetzungsanweisung als
"normale" Zeichen interpretiert werden, jedoch durch Voranstellen eines ``\``
eine Sonderbedeutung bekommen:

.. list-table::
    :widths: 10 50
    :header-rows: 0

    * - ``\<``
      - Wortanfang
    * - ``\>``
      - Wortende
    * - ``\(   \)``
      - UND-Verknüpfung: Gruppierung mehrer Suchmuster zu einem Ausdruck
    * - ``\|``
      - ODER-Verknüpfung: Der links oder der rechts von ``\|`` stehende Ausdruck
    * - ``\_.``
      - Ein beliebigs Zeichen, auch Zeilenende-Zeichen (Suche über Zeilenumbrüche hinweg)
    * - ``\+``
      - Multiplexer: Das vorhergehende Zeichen einmal oder beliebig oft.
    * - ``\?``
      - Multiplexer: Das vorhergehende Zeichen null oder ein mal.

Teile eines regulären Ausdrucks, die beim Suchen mittels ``\(`` und ``\)``
gruppiert werden, können im neuen Ausdruck mittels ``\1``, ``\2``, ``\3`` usw.
wieder aufgegriffen werden, wobei beispielsweise ``\1`` den ersten gruppierten
Ausdruck bezeichnet. Die Textstelle, die beim Suchen auf den *gesamten*
regulären Ausdruck zutrifft, kann beim Ersetzen mittels ``\0`` referenziert
werden.

Weitere Infos zu regulären Ausdrücken in Vim gibt es unter anderem `hier
<http://vimregex.com/>`__, `hier <http://vim.wikia.com/wiki/Search_patterns>`__
und `hier
<http://www.softpanorama.org/Editors/Vimorama/vim_regular_expressions.shtml>`__.

.. http://www.jeetworks.org/node/86

.. definition greedy, beispiel

..  \{ 	Multi-item count match specification (greedy).
..  \{n,m} 	n to m occurrences of the preceding atom (as many as possible).
..  \{n} 	Exactly n occurrences of the preceding atom.
..  \{n,} 	At least n occurrences of the preceding atom (as many as possible).
..  \{,m} 	0 to n occurrences of the preceding atom (as many as possible).
..  \{} 	0 or more occurrences of the preceding atom (as many as possible).

..  \{- 	Multi-item count match specification (non-greedy).
..  \{-n,m} 	n to m occurrences of the preceding atom (as few as possible).
..  \{-n} 	Exactly n occurrences of the preceding atom.
..  \{-n,} 	At least n occurrences of the preceding atom (as few as possible).
..  \{-,m} 	0 to n occurrences of the preceding atom (as few as possible).
..  \{-} 	0 or more occurrences of the preceding atom (as few as possible).

.. Alle Leerzeilen am Ende von Zeilen löschen:
.. :%s/\s\+$//


.. _Visueller Modus:

.. }}}

.. }}}

Visueller Modus
---------------
.. {{{

Im visuellen Modus kann Text mittels :ref:`Bewegungsanweisungen
<Bewegungsanweisungen>` markiert werden, um ihn zu kopieren oder zu bearbeiten.

Aus dem Normal-Modus gelangt man wie folgt in den visuellen Modus:

.. list-table::
    :name: tab-visueller-modus
    :widths: 10 30 20

    * - ``v``
      - "normaler" visueller Modus
      -
    * - ``V``
      - zeilenweise visueller Modus
      - (*Visual Line*)
    * - ``Ctrl v``
      - spaltenweise visueller Modus
      - (*Visual Block*)

Im normalen visuellen Modus wird der gesamte Textbereich von der aktuellen
Position aus bis zu der Stelle, zu der man sich hinbewegt, markiert. Mit ``o``
("other") kann man an das andere Ende des visuell markierten Bereichs gelangen.

Im zeilenweise-visuellen Modus können mit den Navigationsanweisungen ``{`` und
``}`` oder mit Hilfe von Markierungen leicht ganze Paragraphen oder
Textabschnitte kopiert, verschoben oder anderweitig bearbeitet werden. Der
blockweise-visuelle Modus bietet speziell mit dem Vim-Plugin Align eine elegante
Möglichkeit zur Bearbeitung von Spalten einer Tabelle.

**Tipp:** Um Zeilen mit verschieden langen Inhalten am Ende mit Leerzeichen
aufzufüllen, um beispielsweise dahinter weiteren Text als eine neue Spalte
einfügen zu können, können jeweils die ersten Zeichen der Zeilen im visuellen
Blockmodus markiert werden und anschließend ``$`` gedrückt werden. Es wird
dadurch der gesamte Text markiert. Gibt man dann ``A <Leertaste>`` ein, so wird
am Ende der längsten Zeile ein Leerzeichen angefügt und alle kürzeren Zeilen bis
zur gleichen Breite mit Leerzeichen aufgefüllt.

Weiterhin gibt es im visuellen Modus Mappings für folgende Auswahl-Kriterien,
die wahlweise mit ``i`` ("inner") ohne umgebende Whitespaces oder mit ``a``
("outer") mitsamt umgebenden Whitespaces eingeleitet werden können:

.. list-table::
    :name: tab-auswahl-kriterien
    :widths: 15 60

    * - ``w``
      - Ein einzelnes Wort (siehe Option ``iskeyword``)
    * - ``s``
      - Ein einzelner Satz
    * - ``p``
      - Ein einzelner Paragraph (Absatz)
    * - ``t``
      - Ein HTML/XML-Tag
    * - ``"``, ``'``, `````
      - Durch Anführungszeichen begrenzter Text
    * - ``{``, ``[``, ``(``, ``<``
      - Durch Klammern begrenzter Text

Gibt man also beispielsweise im visuellen Modus ``ip`` ein, so wird der aktuelle
Absatz (ohne vorangehende und darauf folgende Leerzeile) ausgewählt; ebenso kann
Text innerhalb zwei runder Klammern mit ``a(`` inklusive der Klammern ausgewählt
werden, wenn sich der Cursor innerhalb der Klammern befindet.

**Tip**: Jede Bearbeitungsanweisung, die für gewöhnlich eine darauffolgende
Bewegungs- oder Auswahlanweisung erwartet, kann auch direkt einen markierten
Bereich angewandt werden.

.. }}}


.. rubric:: Links

* `Vim Cheatsheet <http://adam.garrett-harris.com/updated-vim-cheatsheet/>`__
* `What it feels like to use Vim :-) <http://adam.garrett-harris.com/what-it-feels-like-to-use-vim/>`__

.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Bei der aktuellen Version von Vim habe ich feststellen müssen, dass das
    ``,``-Mapping mit standardmäßig mitinstallierten Plugin "justify.vim"
    kollidiert; man muss, um dies zu beheben, mit SuperUser-Rechten die Datei
    ``/usr/share/vim/vim74/pack/dist/opt/justify/plugin/justify.vim`` editieren und
    folgende beiden Zeilen durch ein ``"``-Zeichen am Zeilanfang auskommentieren:

    .. code-block:: vim

        " nmap ,gq :%s/\s\+/ /g<CR>gq1G
        " vmap ,gq :s/\s\+/ /g<CR>gvgq

.. [#] Persönlich nutze ich anstelle von Tabs lieber verschiedene :ref:`Buffer
    <Buffer>`, insbesondere in Kombination mit dem :ref:`Minibuf-Explorer
    <Minibuf-Explorer>`.
