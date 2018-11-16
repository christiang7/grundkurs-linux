.. _Tinkerer:

Das Blog-System Tinkerer
========================

`Tinkerer <http://tinkerer.me/>`__ ist ein relativ junges Projekt, das auf
:ref:`Sphinx <Sphinx>` aufbaut und es erlaubt, ein statisches HTML-Weblog aus
einer beziehungsweise mehreren Textdateien mit `Restructured-Text
<https://de.wikipedia.org/wiki/ReStructuredText>`_-Syntax zu erzeugen.
"Statisch" soll hierbei bedeuten, dass es zwar keine Kommentier-Funktion und
kein Content-Management-System bietet, dafür allerdings ohne jede Datenbank und
serverseitige Skripte auskommt. Es genügt also bereits ein einfacher Webspace
ohne Extras, um das Weblog zu hosten.

Tinkerer kann folgendermaßen installiert werden:

.. code-block:: sh

    sudo pip3 install Tinkerer

Ruft man anscheinend in einer Shell ``tinker`` auf, so bekommt man eine kurze
Hilfeseite mit den wichtigsten Programm-Optionen angezeigt.


.. _Neues Weblog:
.. _Neues Weblog anlegen:
.. _Ein neues Weblog anlegen:

.. rubric:: Ein neues Weblog anlegen

Um mit Tinkerer ein Weblog zu generieren, legt man zunächst ein neues
Verzeichnis an; anschließend wechselt man ins Projektverzeichnis:

.. code-block:: sh

    # Blog-Verzeichnis anlegen:
    mkdir myblog

    cd myblog

Ähnlich wie Sphinx stellt auch Tinkerer eine Routine für das erstmalige
Erstellen eines Blogs bereit. Diese wird folgendermaßen gestartet:

.. code-block:: sh

    tinker --setup

Einige Basis-Einstellungen können anschließend in der neu erstellten Datei
``conf.py`` im Projektverzeichnis vorgenommen werden:

.. code-block:: python

    # Titel des Blogs festlegen:
    project = 'Mein Blog'

    # Zusatzzeile unter dem Blogtitel
    tagline = 'Eine zusätzliche Header-Zeile'

    # Kurze Beschreibung dse Blogs:
    description = 'Sinn dieses Weblogs'

    # Change this to your name
    author = 'Vorname Nachname'

    # Change this to your copyright string
    copyright = '2016, ' + author

    # Change this to your blog root URL (required for RSS feed)
    website = 'http://www.grund-wissen.de/blog/'

Der angegebene Webseiten-Pfad ist wichtig, damit die Seite mit einem RSS-Reader 
abonniert werden kann und die Abonnenten so automatisch über neue Artikel
informiert werden.

Gibt man in einer Shell ``tinker`` ohne weitere Angaben ein, so werden die
möglichen Aufruf-Optionen eingeblendet.


.. _Posting:
.. _Weblog-Eintrag:
.. _Einen neuen Weblog-Eintrag erstellen:

.. rubric:: Einen neuen Weblog-Eintrag erstellen

Um einen neuen Weblog-Eintrag ('Posting') zu erstellen, gibt man im Projektverzeichnis
folgendes ein:

.. code-block:: sh

    # Neuen Blog-Eintrag mit angegebenem Titel erstellen:
    tinker -p 'Titel des Weblog-Eintrags'

Hierdurch wird im Projektverzeichnis eine neue RestructuredText-Datei
beispielsweise unter ``2016/03/23/titel_des_weblog_eintrags.rst`` erstellt,
wobei die Verzeichnisangabe dem aktuellen Datum entspricht. Diese Datei kann mit
einem Texteditor geöffnet und mit Text gemäß der regulären
RestructuredText-Syntax gefüllt werden.

Gleichzeitig wird in der Datei ``master.rst`` im Projektverzeichnis ein Eintrag
ins dortige Inhalts-Verzeichnis aufgenommen:

.. code-block:: rst

    # Datei master.rst

    Sitemap
    =======

    .. toctree::
       :maxdepth: 1

       2016/03/23/titel_des_weblog_eintrags

Mag man beispielsweise nachträglich den Titel eines Eintrags ändern, so sollte
sowohl der Name der ``.rst``-Datei als auch die entsprechende Pfadangabe in der
Datei ``master.rst`` angepasst werden.


.. _Weblog-Seite:
.. _Neue Weblog-Seite erstellen:
.. _Eine neue Weblog-Seite erstellen:

.. rubric:: Eine neue Weblog-Seite erstellen

Um eine neue, statische Weblog-Seite zu erstellen, gibt man im
Projektverzeichnis folgendes ein:

.. code-block:: sh

    # Neue Blog-Seite mit angegebenem Titel erstellen:
    tinker --page 'Titel der Weblog-Seite'

Hierdurch wird im Projektverzeichnis eine neue RestructuredText-Datei
``pages/titel_der_weblog_seite.rst`` erstellt. Diese Datei kann wiederum mit
einem Texteditor geöffnet und mit Text gemäß der regulären
RestructuredText-Syntax gefüllt werden.

Auch in diesem Fall wird in der Datei ``master.rst`` im Projektverzeichnis ein Eintrag
ins dortige Inhalts-Verzeichnis aufgenommen:

.. code-block:: rst

    # Datei master.rst

    Sitemap
    =======

    .. toctree::
       :maxdepth: 1

       2016/03/23/titel_des_weblog_eintrags
       pages/titel_der_weblog_seite

Soll also nachträglich der Name einer Seite geändert werden, so sollte wiederum
sowohl der Name der ``.rst``-Datei als auch die entsprechende Pfadangabe in der
Datei ``master.rst`` angepasst werden.

Statische Seiten wie ein Impressum können beispielsweise verwendet werden, um
Informationen über den Autor sowie Kontaktmöglichkeiten zu hinterlegen.


.. _Weblog aus Quellcode-Dateien generieren:

.. rubric:: Weblog aus Quellcode-Dateien generieren

Um aus den ``.rst``-Quelldateien fertige HTML-Seiten zu erzeugen, gibt man im
Projektverzeichnis folgendes ein:

.. code-block:: sh

    # Weblog aus Quellcode bauen:
    tinker -b

Durch diesen Aufruf werden die fertigen HTMl-Dateien (bei Verwendung der
Standard-Optionen) im Unterverzeichnis ``blog`` innerhalb des
Projektverzeichnisses gespeichert. Von dort können sie mit einem
FTP-fähigen Dateimanager, beispielsweise :ref:`mc <mc>`, auf den zur Domain
gehörenden Webspace kopiert werden.

.. .. raw:: html

..     <hr />

.. .. only:: html

..     .. rubric:: Anmerkungen:

.. .. [#] **Tip:** Da das Projekt noch in Entwicklung ist, lohnt sich womöglich ein
..     Eintrag in der entsprechenden Googlegroup. Möchte man dafür jedoch kein
..     Google-Konto eröffnen, so genügt auch eine Email an:

..     ``tinkerer-dev+subscribe@googlegroups.com``

..     Dies funktioniert nach `dieser Anleitung
..     <https://www.mydigitallife.info/how-to-subscribe-or-join-goo
..     gle-groups-without-google-account/>`__ mit jeder Googlegroup.


.. Anker-Zeichen in Überschriften entfernen:

.. .. code-block:: sh

..     find ./ -iname "*.html" | xargs sed -i "s/¶//g"

