
.. index:: Z-Shell, zsh
.. _zsh:
.. _Z-Shell:
.. _Die Z-Shell:

Die Z-Shell
===========

Die Z-Shell kann als Weiterentwicklung der Standard-Shell ``bash`` angesehen
werden: Man braucht zur Nutzung der Z-Shell nicht "umlernen", sie bietet
vielmehr ein paar zusätzliche Features, die das alltägliche Arbeiten etwas
erleichtern.

Unter Debian/Ubuntu/LinuxMint kann die Z-Shell folgendermaßen installiert
werden:

.. code-block:: sh

    sudo aptitude install zsh

Anschließend kann die Z-Shell folgendermaßen in einem Shell-Fenster gestartet
werden:

.. code-block:: sh

    zsh

Um die ``bash`` allgemein als Standard-Shell durch die Z-Shell zu ersetzen (also
beim Öffnen eines Shell-Fensters standardmäßig die Z-Shell zu laden), kann man
folgendes eingeben: [#]_

.. code-block:: sh

    # Einstellung für das aktuelle Benutzerkonto vornehmen:
    chsh -s /usr/bin/zsh

    # Einstellung für ein anderes Benutzerkonto vornehmen:
    sudo chsh -s /usr/bin/zsh username

Diese Änderung wird allerdings erst nach einem erneuten Login des Benutzers
wirksam.

.. _Unmittelbare Vorteile der zsh:

Unmittelbare Vorteile der ``zsh``
---------------------------------

Die Z-Shell bringt standardmäßig einige kleine Vorteile mit sich:

* Die Z-Shell kennt neben dem :ref:`Dateimuster <Dateimuster>`  ``*``, das für
  eine beliebig lange Folge von Zeichen in einem Dateinamen steht, auch das
  Muster ``**``, das für eine beliebige Zeichenfolge auch über
  Unterverzeichnisse hinweg steht. Man kann somit beispielsweise mit ``vim
  **.rst`` alle RestructuredText-Dateien des aktuellen Verzeichnisses inklusive
  aller Unterverzeichnisse öffnen.

  Ein zusätzliches nützliches Dateimuster ist ``(foo|bar)``, das wahlweise auf
  ``foo`` oder ``bar`` zutrifft. Beispielsweise können so mit ``ls *.(txt|rst)``
  alle ``.txt``- und ``.rst``-Dateien des aktuellen Verzeichnisses aufgelistet
  werden.

* Die Z-Shell akzeptiert so genannte "globale" :ref:`alias
  <alias>`-Definitionen. Damit sind Ersetzungen gemeint, die an einer beliebigen
  Stelle in der Eingabezeile vorkommen können (und nicht nur am Zeilenanfang).
  Ein solches Alias kann beispielsweise folgendermaßen definiert werden:

  .. code-block:: sh

      alias -g G='| grep -i'

  Damit kann man künftig beispielsweise anstelle von ``ls | grep foo`` kürzer
  ``ls G foo`` eingeben, um alle Dateien aufzulisten, die ``foo`` in ihrem
  Dateinamen enthalten.

* Um in ein anderes Verzeichnis zu wechseln, muss nicht ein ``cd pfadname``
  eingegeben werden; es genügt stattdessen ``pfadname``. Dies ist insbesondere
  hilfreich, wenn man beispielsweise mittels :ref:`locate <locate>` nach Dateien
  sucht und anschließend per Copy-and-Paste den Zielpfad in die Eingabezeile
  kopiert. [#]_

  Die Z-Shell bietet außerdem eine Art "Eingabe-Korrektur" bei Pfadangaben;
  beispielsweise korrigiert sie automatisch die Groß-/Kleinschreibung, wenn der
  angegebene Pfad nicht existiert.

* Beim Drücken der ``Tab``-Taste werden ebenfalls die möglichen Ergänzungen
  aufgelistet; durch erneutes Drücken der ``Tab``-Taste kann man zwischen diesen
  wechseln (``Shift Tab`` wechselt in die umgekehrte Richtung); nach Belieben
  können zur Auswahl auch die Pfeiltasten genutzt werden. Durch eine Eingabe von
  ``Enter`` wird die Vervollständigung übernommen.

  Die Z-Shell unterstützt standardmäßig auch eine ``Tab``-Vervollständigung für
  Kommandozeilen-Argumente; gibt man beispielsweise ``python3 -`` ein und drückt
  die ``Tab``-Taste, so bekommt man eine Liste aller möglichen Argumente
  aufgelistet.


Weitere Vorteile der Z-Shell, die tendenziell eher das Shell-Scripting
betreffen, sind beispielsweise auf `dieser Seite
<https://michael-prokop.at/computer/tools_zsh_liebhaber.html>`__ aufgelistet.


.. _Oh-my-ZSH:
.. _Konfiguration mittels Oh-my-ZSH:

Konfiguration mittels Oh-my-ZSH
-------------------------------

Die Konfiguration der Z-Shell erfolgt, ähnlich wie bei der ``bash``, über die
Konfigurationsdatei ``~/.zshrc``. Dort können beispielsweise wie üblich
:ref:`alias <alias>`-Definitionen erfolgen, Variablen gesetzt und Funktionen
definiert werden.

Die Z-Shell bietet allerdings auch Plugins, Themes, und zusätzliche
Konfigurationsmöglichkeiten. Eine simple Variante, um diese nutzen zu können,
bietet das Paket `Oh-my-ZSH <http://ohmyz.sh/>`__. Dieses kann folgendermaßen
installiert werden kann:

.. https://github.com/robbyrussell/oh-my-zsh/

.. code-block:: sh

    curl -L https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh | sh

Kopiert man die obige Anweisungs-Zeile in ein Shell-Fenster und führt diese aus,
so wird einerseits die Oh-my-ZSH-Umgebung in das Verzeichnis ``~/.oh-my-zsh``
kopiert, und andererseits ein gut kommentiertes Template für die
Konfigurationsdatei ``~/.zshrc`` angelegt. Öffnet man einen neues ZSH-Fenster,
so werden in diesem automatisch die neuen Konfigurationen wirksam.

* Anstelle des Benutzernamens und der kompletten Pfadangabe wird bei den
  Standard-Einstellungen von Oh-my-ZSH nur der Name der letzten Verzeichnisebene
  angezeigt; dies macht die Eingabe-Zeile "übersichtlicher" (den vollständigen
  Pfad kann man sich bei Bedarf mittels ``pwd`` anzeigen lassen; ich habe mir
  dafür schließlich ein ``alias p='pwd'`` definiert).

* Standardmäßig zeigt die "neue" Eingabe-Zeile dafür an, ob man sich in einem
  Git-Repository befindet.

Öffnet man die automatisch generierte Konfigurationsdatei ``~/.zshrc``, so kann
man weitere Optionen nach Belieben aktivieren. Das Aussehen der Eingabe-Zeile
kann beispielsweise durch eine simple Auswahl eines anderen `Themes
<https://github.com/robbyrussell/oh-my-zsh/wiki/Themes>`__ über die angepasst
werden; hierzu muss lediglich der Standard-Wert der Option
``ZSH_THEME="robbyrussell"`` durch einen anderen Theme-Namen ersetzt werden.

Ebenso einfach können zahlreiche `Plugins
<https://github.com/robbyrussell/oh-my-zsh/wiki/Plugins>`__ aktiviert werden,
indem in der ``~/.zshrc`` die ``plugins=``-Variable um die jeweiligen Einträge
ergänzt wird, beispielsweise:

.. code-block:: sh

    plugins=(gitfast pyenv tmux vi-mode wd)

.. _wd:

Das ``wd``-Plugin stellt beispielsweise gleichnamige Shell-Anweisung bereit, mit
deren Hilfe sich Verzeichnis-Bookmarks ("Warp-Points") setzen beziehungsweise
wieder aufrufen lassen. Um einen Warp-Point für das aktuelle Verzeichnis zu
setzen, gibt man einfach ``wd add kuerzel`` ein; mittels ``wd kuerzel`` kann
dann künftig wieder in das entsprechende Verzeichnis gewechselt werden. Mit ``wd
list`` können alle Warp-Points aufgelistet werden, mit ``wd rm kuerzel`` kann
ein Eintrag wieder entfernt werden. Persönlich nutze ich inzwischen ``wd`` so
häufig, dass ich mir kurzerhand mittels ``alias wda='wd add'`` und ``alias
wdl='wd list | sort'`` zwei Abkürzungen in der ``~/.zshrc`` definiert habe.

Weitere Plugins können via :ref:`git <git>` in das Verzeichnis ``$ZSH_CUSTOM``
(üblicherweise ``~/.oh-my-zsh/custom/``) heruntergeladen und nach dem gleichen
Prinzip aktiviert werden.

.. _Auto-Suggestions:

.. rubric:: Auto-Suggestions

Ein solches zusätzliches, meiner Ansicht nach durchaus nützliches Plugin nennt
sich `auto-suggestions <https://github.com/zsh-users/zsh-autosuggestions>`__.
Es bewirkt, dass bei der Eingabe einer Anweisung in einem Shell-Fenster mit
dunkelgrauer Schrift bereits ein Vervollständigungs-Vorschlag anhand der
bisherigen Eingaben eingeblendet wird; drückt man die rechte Pfeiltaste, so wird
dieser Vorschlag übernommen.

Das Plugin ist nicht im Standard-Umfang von Oh-my-ZSH enthalten, kann allerdings
folgendermaßen einfach installiert werden:

.. code-block:: sh

    git clone git://github.com/zsh-users/zsh-autosuggestions $ZSH_CUSTOM/plugins/zsh-autosuggestions

Anschließend muss noch die ``plugins``-Liste in der Konfigurationsdatei
``~/.zshrc`` um den Eintrag ``zsh-autosuggestions`` ergänzt werden.


.. rubric:: Links

* `Z-Shell Reference Card (en.)
  <http://www.bash2zsh.com/zsh_refcard/refcard.pdf>`__
* `Oh-my-ZSH Projektseite (en.) <http://ohmyz.sh/>`__
* `ZSH-Lovers -- Tips, Tricks and Examples for the Z-Shell (en.)
  <http://grml.org/zsh/zsh-lovers.html>`__


.. raw:: html

    <hr />

.. only:: html

    .. rubric:: Anmerkungen:

.. [#] Man kann jederzeit in einem Shell-Fenster durch eine simple Eingabe von
    ``bash`` zurück zur "alten" Shell wechseln. Die Pfade zum Setzen der
    Standard-Shell mittels ``chsh -s`` lassen sich beispielsweise mittels der
    Anweisung ``which zsh`` herausfinden.

.. [#] Nutzt man allerdings auch bei der Z-Shell die ``cd``-Anweisung und gibt
    als Zielpfad ``cd verzeichnis/datei`` an, so gelangt man in das
    Verzeichnis ``verzeichnis``, mit dem Vermerk, dass es sich bei ``datei`` um
    eine Datei handelt. Bei der ``bash`` würde die ``cd``-Anweisung lediglich
    eine Fehlermeldung zurückgeben, dass ``datei`` kein Verzeichnis sei (und
    keinen Verzeichnis-Wechsel ausführen).

.. https://github.com/robbyrussell/oh-my-zsh/tree/master/plugins/vi-mode
.. https://github.com/tmuxinator/tmuxinator


