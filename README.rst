Sphinx Theme Bernard
====================

http://bernardphp.com source files.

Build with:

.. code-block:: bash

    $ sphinx-build . _build

Installation
------------

Download the package or add it to your ``requirements.txt`` file:

.. code:: bash

    $ pip install sphinx_bernard_theme

In your ``conf.py`` file:

.. code:: python

     import sphinx_bernard_theme

     html_theme = "sphinx_bernard_theme"
     html_theme_path = [sphinx_bernard_theme.get_html_theme_path()]

