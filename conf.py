# import sys, os
extensions = [
    'sphinx.ext.intersphinx',
    'sphinx.ext.imgmath',
    'sphinx.ext.ifconfig',
    'sphinx.ext.todo',
    'sphinx.ext.viewcode',
    ]

# 'sphinx.ext.todo',
# 'sphinx.ext.imgmath',
# 'sphinx.ext.autodoc',
# 'sphinx.ext.coverage',

templates_path = ['_templates']
source_suffix  = '.rst'
master_doc     = 'index'

project = 'Linux und Open Source'
copyright = "2011-2018, Bernhard Grotz"

version = '0.3.0a'
release = '0.3.0a'

language = 'de'

exclude_patterns = ["notes.rst", "*/notes.rst", "**/notes.rst","todos.rst", "README.rst"]
linkcheck_ignore = [r"https://wiki.ubuntuusers.de/PCMan.*",
                    r"https://wiki.ubuntuusers.de/LXD.*"]

pygments_style = 'sphinx'

html_theme = 'sphinxdoc'
html_static_path = ['_static']
html_additional_pages = {'home': 'home.html'}
html_title        = 'Linux und Open Source'
html_short_title  = 'Linux und Open Source'
htmlhelp_basename = 'Linux und Open Source'
html_show_sourcelink = True
html_show_copyright  = False
html_show_sphinx     = False
html_last_updated_fmt = '%d.%m.%Y'
today_fmt = '%d.%m.%Y'

html_favicon = 'favicon.ico'
html_logo    = 'logo.png'
latex_logo   = 'logo_print.png'
# html_search_language = 'de'
# html_search_options = {'type': 'default'}


trim_footnote_reference_space = True
todo_include_todos = False

latex_show_pagerefs = False
latex_preamble = r"""
\usepackage[T1]{fontenc}
\usepackage[version=3]{mhchem}
\usepackage{shadow}
\usepackage{amsmath, units, cancel}
\usepackage{amsfonts, amssymb,color}
\usepackage{multicol,pifont,mdframed,lscape}
\usepackage{nicefrac,marvosym,wasysym, textcomp, gensymb}
\usepackage[draft]{minted}
\fvset{breaklines=true}
\setlength{\headheight}{15pt}
\setcounter{secnumdepth}{-1}
\setcounter{tocdepth}{2}
\clubpenalty  = 10000 % Disable single lines at the start of a page ("Schusterjungen")
\widowpenalty = 10000 % Disable single lines at the end   of a page ("Hurenkinder")
\displaywidowpenalty = 10000
\usepackage{hyperref,url}
\hypersetup{
pdftitle={Grundkurs Linux und Open Source},
pdfsubject={Ein Tutorial zu Linux und einigen Open-Source-Programmen},
pdfauthor={Bernhard Grotz},
pdfkeywords={Linux} {Tutorial} {Einf\"uhrung} {Tipps} {Shell} {tmux} {Vim} {Mutt} {Sphinx},
}
"""

# % Make '_' a mathrm macro:
# \catcode`_=\active
# \newcommand_[1]{\ensuremath{\sb{\mathrm{#1}}}}
# \newenvironment{hinweis}
#   {\par\begin{mdframed}[linewidth=1.5pt,linecolor=blue]%
#     \begin{list}{}{\leftmargin=1cm
#                    \labelwidth=\leftmargin}\item[\Large\ding{43}]}
#   {\end{list}\end{mdframed}\par}
# %\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}

imgmath_latex_preamble = latex_preamble
imgmath_image_format = 'png'

latex_elements = {
    'preamble': latex_preamble,
    'classoptions': 'oneside,openany,',
    'papersize': 'a4paper,',
    'pointsize': '12pt,',
    'fontpkg': '',
    'geometry': '\\usepackage[left=2.5cm, right=2.5cm, top=2.5cm, bottom=2.5cm]{geometry}',
    'babel':    '\\usepackage[ngerman]{babel}',
    'fncychap': '',
}

latex_documents = [
    ('index', 'grundkurs-linux.tex', "Grundkurs Linux",
        "Bernhard Grotz", 'manual'),
    ]

texinfo_documents = [
  ('index', 'Linux und Open Source', "Grundkurs Linux",
   "Bernhard Grotz", "Linux und Open Source", "Grundkurs Linux",
   ''),
]

intersphinx_mapping = {
    'sphinx': ('http://www.sphinx-doc.org/en/stable', None),
    'gw':('http://grund-wissen.de/', None),
    'gwc':('http://grund-wissen.de/chemie/', None),
    'gwe':('http://grund-wissen.de/elektronik/', None),
    'gwl':('http://grund-wissen.de/linux/', None),
    'gwm':('http://grund-wissen.de/mathematik/', None),
    'gwp': ('http://grund-wissen.de/physik/', None),
    'gwv': ('http://grund-wissen.de/vegan/', None),
    'gwic': ('http://grund-wissen.de/informatik/c', None),
    'gwil': ('http://grund-wissen.de/informatik/latex', None),
    'gwip': ('http://grund-wissen.de/informatik/python', None),
}

