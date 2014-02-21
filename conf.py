# Sets the theme to the package embedded
html_theme = 'sphinx_bernard_theme'
html_theme_path = ['_themes']

project = u'Bernard'
copyright = u'MIT'

master_doc = 'index'

templates_path = ['_templates']

exclude_patterns = ['demo', 'README.rst']

html_static_path = ['_static']
html_additional_pages = {
    'index' : 'index.html'
}
