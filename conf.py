import sys, os
import sphinx_rtd_theme
import datetime

#import recommonmark
import myst_parser
#from recommonmark.transform import AutoStructify

from sphinx.highlighting import lexers
from pygments.lexers.web import PhpLexer
from pygments.lexers.web import HtmlLexer
from pygments.lexers.web import JsonLexer

from datetime import datetime

lexers['php'] = PhpLexer(startinline=True)
lexers['php-annotations'] = PhpLexer(startinline=True)
lexers['html'] = HtmlLexer(startinline=True)
lexers['json'] = JsonLexer(startinline=True)

extensions = [
  #'recommonmark',
  'myst_parser',
  'sphinx_rtd_theme',
  'sphinx_copybutton',
  'sphinx_markdown_tables',
]

source_suffix = ['.rst', '.md']
master_doc = 'index'

project = 'Warden'
today = datetime.today()

copyright = '2019-' + str(today.year) + ' by David Alger.'
author = 'David Alger, Navarr Barnier, Taras Shabatyn'
version = '0.13.3'
release = ''

exclude_patterns = ['_build']

html_theme = "sphinx_rtd_theme"
html_theme_path = [sphinx_rtd_theme.get_html_theme_path()]
html_show_sourcelink = False

html_static_path = ['_static']
templates_path = ['_templates']
html_extra_path = ['_redirects']

myst_enable_extensions = [
  "html_admonition",
  "strikethrough",
  "colon_fence",
]

#def setup(app):
  #app.add_config_value('myst_parser_config', {
  #  
  #}, True)
    #app.add_config_value('recommonmark_config', {
    #    'auto_toc_tree_section': ['Table of Contents'],
    #    'enable_math': False,
    #    'enable_inline_math': False,
    #    'enable_eval_rst': True,
    #}, True)
    #app.add_transform(AutoStructify)
