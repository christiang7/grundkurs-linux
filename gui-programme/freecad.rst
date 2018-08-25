
.. index:: FreeCAD
.. _FreeCAD:

Erstellen von 3D-Modellen mit ``freecad``
=========================================

FreeCAD ist, wie der Name schon sagt, ein freies Programm zum Erstellen von
dreidimensionalen Modellen ("Computer Animated Design"). Mit FreeCAD lassen sich
beispielsweise relativ einfach mechanische Modelle oder Architekturmodelle mit
genauen Abmessungen erstellen.

Einen guten Einblick in die Funktionen von FreeCAD gibt beispielsweise die
deutschsprachige `FreeCAD-Videoreihe auf Youtube
<https://www.youtube.com/user/BPLRFE/videos>`_.


.. _FreeCAD-Installation:

.. rubric:: Installation

FreeCAD kann unter Ubuntu über folgendes Paket installiert werden:

.. code-block:: sh

    sudo aptitude install freecad

Möchte man allerdings stets auch an den neuesten Entwicklungen teilhaben, so ist
es empfehlenswert, die Paket-Quellen des Entwickler-Teams mit aufzunehmen:

.. code-block:: sh

    sudo add-apt-repository ppa:freecad-maintainers/freecad-daily
    sudo apt-get update
    sudo apt-get upgrade
    sudo apt-get install freecad-daily freecad-daily-doc

Freecad kann anschließend über das Start-Menü oder aus einer Shell heraus
mittels ``freecad`` für die Standard-Version beziehungsweise ``freecad-daily``
für die aktuellste Entwickler-Version gestartet werden.

.. _Werkbank:
.. _Arbeitsfläche:

.. rubric:: Arbeitsflächen ("Werkbänke")

Beim ersten Programmstart von FreeCAD erscheint ein fast leerer Bildschirm. Dies
liegt daran, dass noch keine "Werkbank" ausgewählt ist; als solche werden in
FreeCAD für bestimmte Zwecke zusammengestellte Icon-Leisten bezeichnet. Wählt
man im mittleren Auswahlmenü beispielsweise die Arbeitsfläche/Werkbank
``Sketcher``, so werden die für das Erstellen und Bemaßen von 2D-Skizzen
nützlichen Werkzeuge als anklickbare Icons eingeblendet. [#]_

Folgende Arbeitsflächen in FreeCAD mit der Grundversion verfügbar:

* Der Arbeitsbereich ``Start`` dient als Einstiegshilfe in das Programm und
  bietet einige Tips sowie Links zu Tutorials (beispielsweise Youtube oder
  das FreeCAD-Handbuch).
* Der Arbeitsbereich ``Sketcher`` ist für das Erstellen von Skizzen mit Rand-
  bzw. Zwangsbedingungen ausgelegt.
* Der Arbeitsbereich ``PartDesign`` bietet Werkzeuge für die Erstellung von
  3D-Körpern aus 2D-Skizzen sowie die Weiterbearbeitung von 3D-Körpern mittels
  zusätzlicher Skizzen.
* Der Arbeitsbereich ``Part`` wird zur Erstellung von geometrischen Grundkörpern
  verwendet; zudem können beliebige geometrische Körper weiter bearbeitet
  werden.

* Der Arbeitsbereich ``Complete`` beinhaltet alle Werkzeuge der anderen
  Arbeitsbereiche. Die Symbolleiste ist dadurch stark gefüllt; die einzelnen
  Symbol-Gruppen können jedoch nach eigenen Vorstellungen platziert werden,
  indem man je eine Gruppe mit gedrückter linker Maustaste an eine andere Stelle
  in der Symbolleiste bewegt.

.. * Der Arbeitsbereich ``Draft`` für die Arbeit mit Skizzen aus ebenen
..   Konstruktionselementen wie Linien, Kreisen, Text, Maßketten und Schraffuren.
.. * Der Arbeitsbereich ``Mesh`` für die Arbeit mit Oberflächennetzen. Aktuell sind
..   dies vor allem polygonale Dreiecks- und Vierecksnetze.
.. * Der Arbeitsbereich ``Bild`` für die Arbeit mit Bitmap-Bildern.
.. * Der Arbeitsbereich ``Rendering`` für die Erstellung von fotorealistischen
..   Bildern von Körpermodellen (Ray-Tracing).
.. * Der Arbeitsbereich ``Drawing`` für die Ausgabe der erstellten
..   Konstruktionselemente und Körpermodelle auf einem Zeichnungsblatt mit Titel.
.. * Der Arbeitsbereich ``Robot`` für das Simulieren von Roboterbewegungen.

Zu Beginn sind die wohl wichtigsten Arbeitsflächen die PartDesign- und die
Part-Werkbank, die in den folgenden Abschnitten vorgestellt werden. Weitere
Arbeitsflächen können als Addons hinzugefügt werden.


.. _Fenster-Ansichten:

.. rubric:: Fenster-Ansichten

In FreeCAD ist die aktuelle 3D-Ansicht im Hauptfenster mittig platziert. Da
mehrere Dateien gleichzeitig geöffnet werden können, ist zur Übersicht und für
ein einfaches Wechseln der Fenster unmittelbar unter dem Hauptfenster eine
entsprechende Tab-Leiste angebracht.

Links davon ist üblicherweise eine so genannte "Combo-Ansicht" eingeblendet:

* Der obere Teil der Combo-Ansicht enthält im oberen Teil eine Art
  Inhaltsverzeichnis ("Modell-Baum") des aktuellen Projekts, im dem einzelne
  Objekte ausgewählt werden können (mit gedrückter ``Ctrl``-Taste auch mehrere
  auf einmal). Zudem können in diesem Fenster auch Bauteile gruppiert sowie
  durch Drücken der Leertaste aus beziehungsweise wieder eingeblendet werden
  können.

  Der obere Teil der Combo-Box hat zusätzlich eine zweite anwählbare Rubrik
  namens "Aufgaben". Sofern eine Bearbeits-Funktion es erfordert, wechselt die
  Combo-Box automatisch in diese Rubrik und ermöglicht es die einzelnen
  Funktions-Parameter einzustellen.

* Der untere Teil der Combo-Ansicht enthält ebenfalls zwei Rubriken mit jeweils
  editierbaren Tabellen. In der Rubrik "Ansicht" kann das Aussehen eines Objekts
  (Liniendicke, Selektierbarkeit usw.) festgelegt werden, in der Rubrik "Daten"
  kann die Positionierung sowie die Größe eines Objekts durch Zahlenwerte genau
  festgelegt werden.


Über dem Hauptfenster sind eine oder mehrere Symbol-Leisten zu finden, wobei je
nach ausgewählter Werkbank die verschiedene Icon-Gruppen angezeigt werden.

Unter dem Hauptfenster befindet sich standardmäßig ein Ausgabefenster (unter
anderem für Fehler und Warnungen) sowie eine Python-Konsole; diese beiden
Fenster können anfangs guten Gewissens geschlossen werden, um auf dem Bildschirm
mehr Platz für die 3D-Ansicht zu bekommen. Bei Bedarf können die geschlossenen
Fenster wieder über das Menü ``Ansicht -> Ansichten -> Ausgabefenster``
beziehungsweise ``Ansicht -> Ansichten -> Python-Konsole`` wieder eingeblendet
werden.

.. _Navigation:
.. rubric:: Navigation

In FreeCAD können viele Arbeitsschritte mit der Maus vorgenommen werden.
Standardmäßig haben die einzelnen Tasten folgende Bedeutung:


* ``Linke Maustaste``: Objekt auswählen. Mit gedrückter ``Ctrl``-Taste können
  durch einen Klick auf die linke Maustaste weitere Objekte zur Auswahl
  hinzugefügt werden; durch einen Klick ins Leere wird die aktuelle Auswahl
  aufgehoben.

  Mit den Standard-Einstellungen leuchten auswählbare Punkte, Kanten und Flächen
  in FreeCAD automatisch gelb auf, sobald sich der Maus-Cursor über ihnen
  befindet. Wählt man eine solche Kante oder Fläche durch einen Klick mit der
  linken Maustaste aus, so wird sie automatisch grün eingefärbt.

* ``Rechte Maustaste``: Durch einen Rechtsklick wird im 3D-Fenster ein Menü mit
  verschiedenen Darstellungs- und Bearbeitsoptionen geöffnet.

* ``Mausrad``: Dreht man am Mausrad, so wird die Ansicht im 3D-Fenster
  vergrößert beziehungsweise verkleinert ("Zoom"). Hält man die mittlere Maustaste
  gedrückt, so kann die Ansicht verschoben werden ("Pan").

  Hält man das Mausrad gedrückt *und* drückt dann wahlweise die linke oder
  rechte Maustaste, so kann man die Ansicht um den Maus-Cursor als Drehzentrum
  drehen, bis man die linke beziehungsweise rechte Maustaste wieder los lässt.

Ist man von einem ähnlichen Programm eine andere Belegung der Maustasten
gewöhnt, so kann man im Menü ``Bearbeiten -> Einstellungen`` unter der Rubrik
``Anzeige`` auch andere vordefinierte Tastenbelegungen auswählen: Neben der
standardmäßigen "CAD-Navigation" ist auch eine Navigation wie in den Programmen
"Blender3D" oder "Inventor" sowie speziell für Touchpads ausgelegte Navigation
wählbar. Klickt man nach der Auswahl auf das daneben platzierte ``Maus``-Icon,
so wird die Tasten-Belegung für den jeweiligen Stil eingeblendet.

Die Maus-Navigation kann man leicht ausprobieren, indem man zur
``Part``-Werkbank wechselt und oben links in der Symbolleiste auf das
Würfel-Icon klickt; hierdurch wird ein neuer Würfel mit Standard-Maßen im
Ursprung des Koordinatensystems eingefügt.

Zusätzlich zur Maus-Navigation kann auch das NumPad der Tastatur zur Navigation
genutzt werden:

* Mit der Taste ``Numpad-0`` wechselt die Ansicht in eine schräge
  ("axometrische") 3D-Ansicht von vorne.

* Mit der Taste ``Numpad-1`` wird in eine Frontal-Ansicht des Objekts gewechselt
  (:math:`x-z`-Ebene). Die Taste ``Numpad-4`` liefert die zugehörige Ansicht von
  hinten.

* Mit der Taste ``Numpad-2`` wird in die Vogelperspektive gewechselt
  (:math:`x-y`-Ebene). Die Taste ``Numpad-5`` liefert die zugehörige Ansicht von
  unten.

* Mit der Taste ``Numpad-3`` wird in eine Seiten-Ansicht des Objekts gewechselt
  (:math:`y-z`-Ebene, rechte Seite). Die Taste ``Numpad-6`` liefert die
  zugehörige Ansicht von der linken Seite.

Klickt man mit der rechten Maustaste in das 3D-Fenster und wählt im
erscheinenden Menü ``Einpassen`` aus, so wechselt die aktuelle Ansicht in eine
axometrische Ansicht, die alle in der geöffneten Datei existierenden Objekte
beinhaltet.

Zusätzlich kann die Darstellungsweise der Objekte im 3D-Fenster geändert werden,
indem man  mit der rechten Maustaste in das 3D-Fenster klickt und im Menü auf
``Zeichenstil`` klickt. Wechselt man in diesem Untermenü beispielsweise auf
"Drahtgitter", so werden die Objekte nur noch anhand ihrer Konturen dargestellt,
jedoch ohne feste Flächen (kann beispielsweise beim Erstellen von zusätzlichen
Skizzen auf bestehenden Objekten hilfreich sein).

Für die obigen Navigations-Funktionen existieren jeweils auch Icons, die
standardmäßig in der obersten Symbol-Leiste ganz links zu finden sind.

.. _Einstellungen:

.. rubric:: Einstellungen

FreeCAD bietet eine Vielzahl an Anpassungsmöglichkeiten, sowohl was die
Bedienung als auch das Aussehen der Arbeitsflächen anbelangt. Die Einstellungen
können allgemein über das Menü ``Bearbeiten -> Einstellungen`` vorgenommen
werden. Gewöhnungsbedürftig, aber auch nicht unpraktisch ist es, dass hierbei
Einstellungsmöglichkeiten nur für diejenigen Arbeitsbereiche eingeblendet
werden, die in der aktuellen Sitzung bereits einmal durch eine entsprechende
Auswahl in der Haupt-Symbolleiste aktiviert wurden.

Für einen besseren Kontrast ist es beispielsweise empfehlenswert, kurz in den
PartDesign-Arbeitsbereich zu wechseln und dann unter ``Bearbeiten ->
Einstellungen -> Anzeige`` in der Rubrik ``Skizze`` die Kantenfarbe von weiß auf
schwarz umzuschalten.

Zudem ist es empfehlenswert, in der Rubrik ``Part Design`` in der Rubrik
``Allgemein -> Modelleinstellungen`` alle drei Häkchen bei "Modell automatisch
nach Boolescher Operation überprüfen", "Modell automatisch nach Boolescher
Operation verfeinern" und "Verfeinere Modell nach Skizzenoperation automatisch"
zu setzen.

.. Häufig benutzte Befehle:

.. Werkzeuge -> Benutzerdefiniert, Rubrik ``Tastatur``:
.. Wählt man dann im linken Auswahlmenü "Skizze" aus, so kann man den einzelnen
.. Funktionen des Sketchers eigene Tastenkombinationen zuweisen.
.. Somit Shortcuts für jeden einzelnen Arbeitsbereich möglich

.. _Bauteil mit der PartDesign-Werkbank erstellen:

Bauteil mit der PartDesign-Werkbank erstellen
----------------------------------------------

Um ein neues Bauteil zu erstellen, sollte zunächst eine zweidimensionale Skizze
des Grundrisses erstellt werden. Klickt man bei aktiver PartDesign-Werkbank auf
das Skizze-Symbol in der Symbolleiste, so werden die entsprechenden Funktionen
des Sketchers aktiviert. [#]_

Bei einer neuen Skizze wählt man zunächst aus, für welche Ebene die Skizze
gedacht ist. Die Auswahl lässt sich zwar nachträglich jederzeit korrigieren, da
das entstehende Bauteil gedreht werden kann, es ist jedoch beispielsweise für
die Erstellung einer Bodenplatte durchaus hilfreich, die zugehörige Skizze von
vornherein waagrecht in die :math:`x-y`-Ebene zu legen.


.. _Zeichenelemente in Skizze aufnehmen:

.. rubric:: Zeichenelemente in Skizze aufnehmen

Um Zeichenelemente in die Skizze aufzunehmen, genügt ein Klick auf das
entsprechende Icon in der Symbolleiste; bewegt man den Maus-Cursor über die
einzelnen Symbole, so wird am unteren Bildschirmrand eine Kurzbeschreibung der
jeweiligen Funktion eingeblendet.

Nachdem die Formen in der Skizze festgelegt sind, kann mit der Ausrichtung und
Dimensionierung der einzelnen Elemente begonnen werden. Hierin unterscheidet
sich FreeCAD deutlich von manuell erstellten Skizzen: Die Zeichnung muss nicht
von Anfang an mit Präzision angefertigt werden; Objekte können auch im
Nachhinein ausgerichtet und mit Zusatz-Bedingungen versehen werden.

.. Erst Formen einzeichnen, dann darauf achten, dass Linienzüge geschlossen sind
.. (beispielsweise mittels Koinzidenz-Beschränkungen)

.. zuerst "offensichtliche" Beschränkungen: Horizontal und Vertikal, Tangential,
.. Symmetrie, Gleichheit

.. _Längen und Symmetrien festlegen:

.. rubric:: Längen und Symmetrien festlegen

FreeCAD vergibt in der Skizze automatisch, sofern möglich, Beschränkungen
("Constraints"). Beispielsweise erhalten beim Zeichnen eines Rechtecks die
einzelnen Seiten automatisch Vertikal- beziehungsweise
Horizontal-Beschschränkungen.

Hat man das ein Rechteck fertig gezeichnet, so ist dieses in seiner Bemaßung und
Platzierung noch nicht eindeutig festgelegt; es hat noch so genannte
"Freiheitsgrade". Legt man zwei Werte für Länge und Breite sowie einen Abstand
zur :math:`x`- sowie zur :math:`y`-Achse fest, so ist das Rechteck hingegen
eindeutig festgelegt. Hat eine Zeichnung keine Freiheitsgrade mehr, so spricht
man von einer "vollständig eingeschränkten Skizze"; in diesem Fall wird die
komplette Skizze grün hervorgehoben.

.. todo

.. Skizze auf Fläche erstellen: Beispielsweise Rechteck als "Hilfslinien"
.. erstellen; dann durch Klick auf das entsprechende Icon in den
.. Konstruktions-Modus wechseln; dadurch werden die Linien der bisherigen Skizze
.. blau; sie verlieren dadurch ihre eigentlichen Funktionen (beispielsweise für
.. Aufpolsterungen oder Taschen) und werden zu Hilfslinien.


Mehr Infos zu den Funktionen des Sketchers finden sich im `FreeCAD-Manual
<https://www.freecadweb.org/wiki/index.php?title=Sketcher_Workbench>`__.


.. _Skizze zu einem 3D-Objekt aufpolstern:

.. rubric:: Skizze zu einem 3D-Objekt "aufpolstern"

Ist man mit dem Erstellen der Skizze fertig, so kann man anschließend die Skizze
mittels der entsprechenden Funktion in der Symbolleiste "aufpolstern"; so
entsteht aus einer zwei-dimensionalen Skizze ein drei-dimensionales Objekt.

Wählt man bei einem Objekt durch einen Klick mit der linken Maustaste eine
einzelne Fläche aus, so kann durch ein erneutes Anklicken des Skizze-Symbols in
der Symbolleiste eine neue Skizze auf dieser Fläche erzeugt werden. FreeCAD
dreht dabei automatisch die Ansicht so, dass die ausgewählte Fläche von oben als
Unterlage der Skizze betrachtet wird. Hat man wiederum eine Skizze fertig
erstellt, so sind zweierlei Funktionen möglich:

* Mittels der "Taschen"-Funktion in der Symbolleiste kann man eine Bohrung
  beziehungsweise Ausfräsung durch das Objekt bewirken; hierbei kann die Bohr-
  beziehungsweise Frästiefe entweder durch Bemaßung oder über logische
  Beziehungen (beispielsweise "Bis zur nächsten Oberfläche" oder "Durch alles")
  angegeben werden.

* Mittels der "Aufpolstern"-Funktion in der Symbolleiste kann man aus der Skizze
  einen neuen 3D-Körper erstellen, der dann senkrecht zur bestehenden Fläche
  ausgerichtet ist. Auf diese Weise lassen sich auch komplexe Geometrien
  schichtweise aufbauen.

Eine Besonderheit der "Aufpolstern"-Funktion des PartDesign-Arbeitsbereics liegt
darin, dass als Resultat stets ein einzelnes Objekt entsteht. Im Modellbaum
entsteht somit eine Hierarchie der Bearbeitungsschritte: Die Grundkörper sind
oben angeordnet, die später hinzukommenden Aufpolsterungen und/oder Taschen
werden jeweils unten angefügt. Im Modellbaum bleiben die Original-Objekte also
erhalten, während sie in der 3D-Hauptansicht von FreeCAD automatisch
ausgeblendet werden. [#]_


.. _Farben festlegen:

.. rubric:: Farben festlegen

Um ein Objekt einzufärben, klickt man im Modellbaum (oberer Teil der Combo-Box)
mit der rechten Maustaste auf das gewünschte Objekt und wählt im erscheinenden
Menü den Eintrag "Darstellung" aus. Die Combo-Box wird hierdurch zu einem
Eingabe-Formular für die Kanten- und Flächenfarben des Objekts.

.. Auswahl-Menü öffnen und "Legen Sie Farben fest" anklicken. Dann entweder
.. einzelnen Oberflächen anklicken und Farbe festlegen, oder ``Box Selection``
.. anklicken und ein Auswahl-Fenster über die gewünschten Flächen ziehen.

Weitere Infos zur PartDesign-Werkbank finden sich im `FreeCAD-Manual
<https://www.freecadweb.org/wiki/index.php?title=PartDesign_Workbench>`__.


.. _Bauteile mit der Part-Werkbank erstellen:

Bauteile mit der Part-Werkbank erstellen
----------------------------------------

In der ``Part``-Werkbank können einerseits dreidimensionale geometrische
Grundkörper wie Würfel, Kugel, Zylinder oder Kegel durch ein einfaches Anklicken
des jeweiligen Icons in der Symbolleiste hinzugefügt werden; andererseits können
bereits bestehende 3D-Objekte beispielsweise mittels logischen Operatoren oder
speziellen Funktionen weiter bearbeitet werden.

Einen neuen 3D-Grundkörper kann man durch Anklicken des jeweiligen Icons in der
Symbolleiste erstellen. Das neue Objekt wird dabei mit einstellbaren
Standard-Maßen am Koordinaten-Ursprung eingefügt. Da das neue Objekt zudem
automatisch ausgewählt wird, können die Standard-Maße bei Bedarf sogleich in der
unteren Hälfte der Combo-Box abgeändert werden.

Neben den Längen-Maßen kann in der unteren Hälfte der Combo-Box auch die
Platzierung eines Objekts geändert werden. Hat man ein Objekt ausgewählt, so
erscheint als erster Eintrag im Datenfeld der Combo-Box die Eigenschaft
"Placement". Klickt man auf das Icon mit den drei Punkten in der gleichen Zeile,
so ändert sich die Combo-Box in ein Bearbeitungsfenster für exakt angegebene
Positionierungen:

* Unter der Rubrik "Verschiebung" kann vorgegeben werden, um wie weit das
  ausgewählte Objekt in die :math:`x`, :math:`y` beziehungsweise :math:`z` Achse
  verschoben werden soll.

* Unter der Rubrik "Drehpunkt" kann, wie der Name schon sagt, ein Punkt als
  Drehzentrum festgelegt werden. Dies ist allerdings nur von Bedeutung, sofern
  die Drehung um einen einzelnen Punkt erfolgen soll.

  Soll eine Drehung um eine Achse erfolgen, so können die Drehpunkt-Koordinaten
  beim Wert Null belassen werden; dafür kann in der unteren Hälfte Teil des
  Bearbeitungsfensters eine Achse ausgewählt sowie ein Drehwinkel festgelegt
  werden.

In welche Richtung die einzelnen Koordinaten bei der aktuellen 3D-Ansicht
zeigen, kann man an dem kleinen Achsenkreuz erkennen, das rechts unten im
Hauptfenster eingeblendet ist.

Setzt man zudem einen Haken bei der Option "Änderungen an Objektplacement
inkrementell übernehmen", so kann man schrittweise Änderungen, beispielsweise
Verschiebungen entlang einer Achse vornehmen, und bekommt diese jeweils nach
einem Klick auf "Anwenden" unmittelbar angezeigt. Ohne diese Option muss die
gesamte Transformation als ein einziger Prozess-Schritt vorgenommen werden.

.. rubric:: Boolesche Operationen

Im Part-Arbeitsbereich werden nur diejenigen Icons für boolesche Operationen
farbig angezeigt, die auf die aktuelle Auswahl angewendet werden können.
Beispielsweise kann die Operation "Schnittmenge" nur dann angewendet werden,
wenn (mindestens) zwei Objekte ausgewählt sind. Dabei muss unter Umständen auf
die Auswahl-Reihenfolge geachtet werden: Bei der booleschen Operation
"Differenz" wird beispielsweise das als zweites ausgewählte Objekt aus dem
zuerst ausgewählten Objekt ausgeschnitten.


... to be continued ...

.. _FreeCAD-Links:

Links
-----


* `FreeCAD Projektseite (en.) <https://www.freecadweb.org>`__
* `FreeCAD Wiki (en.) <https://www.freecadweb.org/wiki/Manual:Introduction>`__
* `FreeCAD All workbenches at a glance (en.)
  <https://www.freecadweb.org/wiki/Manual:All_workbenches_at_a_glance>`__
* `A FreeCAD Manual (en., auch PDF)
  <https://www.gitbook.com/book/yorikvanhavre/a-freecad-manual/details>`__
* `FreeCAD-Videoreihe auf Youtube (de.)
  <https://www.youtube.com/user/BPLRFE/videos>`__
* `FreeCAD 0.17 Release Notes
  <https://www.freecadweb.org/wiki/Release_notes_0.17>`__


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Welche Arbeitsfläche standardmäßig ausgewählt sein soll, wenn FreeCAD
    gestartet wird, kann über das Menü ``Bearbeiten -> Einstellungen``
    festgelegt werden.

.. [#] Die Skizze kann wahlweise auch mittels der ``Sketcher``-Werkbank erstellt
    und erst anschließend in der ``PartDesign``-Werkbank weiter bearbeitet
    werden.

    Viele Elemente der ``Sketcher``-Werkbank sind allerdings auch auf der
    ``PartDesign``-Arbeitsfläche verfügbar, so dass oftmals bereits diese zum
    Erstellen von Skizzen ausreichend ist.

.. [#] Dies ist auch der Grund, weshalb es in FreeCAD keine einfache Möglichkeit
    gibt, die Objekte im Modell-Baum neu anzuordnen: Bei Objekten, die mit Hilfe
    des PartDesign-Arbeitsbereichs erstellt wurden, könnte so die
    Objekt-Historie verloren gehen, was zu unerwarteten Ergebnissen führen
    könnte.

    Als Workaround ist es für eine Neuordnung des Modellbaums allerdings
    möglich, im Anschluss an eine Sicherheitskopie eine neue Gruppe im
    Modellbaum zu erstellen (Rechtsklick im oberen Teil der Combo-Box, "Gruppe
    erstellen" anklicken) und die gewünschten Objekte in der Soll-Reihenfolge
    per Drag-and-Drop in diese Gruppe zu ziehen. Löscht man die Gruppe
    anschließend wieder, so bleibt die Reihenfolge der Objekte in der Gruppe
    erhalten.

    Macht man dies mit Objekten aus dem PartDesign-Arbeitsbereich, so muss
    allerdings geprüft werden, ob dadurch Fehler entstanden sind; notfalls muss
    man die vorherigen Arbeitsschritte rückgängig machen.

