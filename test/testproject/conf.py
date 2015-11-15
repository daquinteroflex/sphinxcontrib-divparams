# -*- coding: utf-8 -*-

import sys
import six

# noinspection PyPackageRequirements
import sphinxcontrib.divparams as divparams

six.print_(">>> This python version is ", sys.version)

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc',
              'sphinxcontrib.divparams']

# Add any paths that contain templates here, relative to this directory.
templates_path = [divparams.get_templates_path()]

# The suffix of source filenames.
source_suffix = '.rst'

# The encoding of source files.
source_encoding = 'utf-8-sig'

# The master toctree document.
master_doc = 'index'

divparams_exclude_sources = ['excluded']

# General information about the project.
project   = 'sphinxcontrib.divparams.testproject'

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
html_theme = 'default'

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = [divparams.get_static_path()]
