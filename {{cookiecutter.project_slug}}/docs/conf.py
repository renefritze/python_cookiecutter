#!/usr/bin/env python
#
# {{cookiecutter.repository_url}} documentation build configuration file, created by
# sphinx-quickstart on Fri Jun  9 13:47:02 2017.
#
# This file is execfile()d with the current directory set to its
# containing dir.
#
# Note that not all possible configuration values are present in this
# autogenerated file.
#
# All configuration values have a default; values that are commented out
# serve to show the default.

# If extensions (or modules to document with autodoc) are in another
# directory, add these directories to sys.path here. If the directory is
# relative to the documentation root, use os.path.abspath to make it
# absolute, like shown here.
#
import sys
import os
from pathlib import Path

this_dir = Path(__file__).resolve().parent
root_dir = (this_dir / '..').resolve()
sys.path.insert(0, str(root_dir))
sys.path.insert(0, str(this_dir))

import {{cookiecutter.__module_name}}

# -- General configuration ---------------------------------------------

# If your documentation needs a minimal Sphinx version, state it here.
#
# needs_sphinx = '1.0'

# Add any Sphinx extension module names here, as strings. They can be
# extensions coming with Sphinx (named 'sphinx.ext.*') or your custom ones.
extensions = ['sphinx.ext.autodoc', 'sphinx.ext.viewcode', "autoapi", "myst_nb",
                  "sphinx.ext.coverage",
    "sphinx.ext.autosummary",
    "sphinx.ext.linkcode",
    "sphinx.ext.intersphinx",
    "sphinx.ext.mathjax"]
# this enables:
# substitutions-with-jinja2, direct-latex-math and definition-lists
# ref: https://myst-parser.readthedocs.io/en/latest/using/syntax-optional.html
myst_enable_extensions = [
    "dollarmath",
    "amsmath",
    "deflist",
    "html_image",
    "colon_fence",
    "smartquotes",
    "replacements",
    "substitution",
]
myst_url_schemes = ["http", "https", "mailto"]
# auto genereated link anchors
myst_heading_anchors = 2
import substitutions  # noqa

myst_substitutions = substitutions.myst_substitutions
nb_execute_notebooks = "cache"
nb_execution_timeout = 240  # there is an interpolation test
# print tracebacks to stdout
nb_execution_show_tb = True
nb_execution_mode = "cache"
# Add any paths that contain templates here, relative to this directory.
templates_path = ['_templates']

# The suffix(es) of source filenames.
# You can specify multiple suffix as a list of string:
#
source_suffix = {
    '.rst': 'restructuredtext',
    '.ipynb': 'myst-nb',
    '.md': 'myst-nb',
}

# The master toctree document.
master_doc = 'index'

# General information about the project.
project = '{{cookiecutter.project_slug}}'
copyright = "2023, {{cookiecutter.author}}"
author = "{{cookiecutter.author}}"

# The version info for the project you're documenting, acts as replacement
# for |version| and |release|, also used in various other places throughout
# the built documents.
#
# The short X.Y version.
version = {{cookiecutter.__module_name}}.__version__
# The full version, including alpha/beta/rc tags.
release = {{cookiecutter.__module_name}}.__version__

# The language for content autogenerated by Sphinx. Refer to documentation
# for a list of supported languages.
language = "en"

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This patterns also effect to html_static_path and html_extra_path
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# The name of the Pygments (syntax highlighting) style to use.
pygments_style = 'sphinx'

# If true, `todo` and `todoList` produce output, else they produce nothing.
todo_include_todos = True


# -- Options for HTML output -------------------------------------------

html_theme = "furo"
html_theme_options = {}
# Custom sidebar templates, maps document names to template names.
# all: "**": ["logo-text.html", "globaltoc.html", "localtoc.html", "searchbox.html"]
# refer to https://github.com/pradyunsg/furo/blob/main/src/furo/theme/furo/theme.conf
# for available ones
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "sidebar/scroll-end.html",
        "sidebar/variant-selector.html",
    ]
}

# Theme options are theme-specific and customize the look and feel of a
# theme further.  For a list of options available for each theme, see the
# documentation.
#
# html_theme_options = {}

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ['_static']

# Pngmath should try to align formulas properly.
pngmath_use_preview = True

autoapi_python_use_implicit_namespaces = True
autoapi_dirs = [root_dir / 'src'/ '{{cookiecutter.__module_name}}']
autoapi_type = 'python'
# allows incremental build
autoapi_keep_files = True
autoapi_template_dir = this_dir / '_templates' / 'autoapi'

coverage_ignore_modules = r"""
    """.split()
coverage_ignore_functions = r"""
    test($|_) (some|all)true bitwise_not cumproduct pkgload
    generic\.
    """.split()
coverage_ignore_classes = r"""
    """.split()

coverage_c_path = []
coverage_c_regexes = {}
coverage_ignore_c_items = {}

# autodoc_default_flags = ['members', 'undoc-members', 'show-inheritance']

# PyQt5 inventory is only used internally, actual link targets PySide2
intersphinx_mapping = {
    "python": ("https://docs.python.org/3", None),
    "numpy": ("https://numpy.org/doc/stable/", None),
    "PyQt5": ("https://www.riverbankcomputing.com/static/Docs/PyQt5", None),
    "scipy": ("https://docs.scipy.org/doc/scipy/reference", None),
    "matplotlib": ("https://matplotlib.org", None),
    "Sphinx": (" https://www.sphinx-doc.org/en/master/", None),
}


def linkcode_resolve(domain, info):
    if domain == "py":
        if not info["module"]:
            return None
        filename = info["module"].replace(".", "/")
        baseurl = "{{cookiecutter.repository_url}}"
        branch = os.environ.get("CI_COMMIT_REF_NAME", "main")
        return f"{baseurl}/-/tree/{branch}/src/{filename}.py"
    return None
