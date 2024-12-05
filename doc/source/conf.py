# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'Jeu du pendu, documentation'
copyright = '2024, Fiona Mordenti'
author = 'Fiona Mordenti'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'sphinx.ext.autodoc',   # Génère automatiquement la documentation à partir des docstrings Python
    'sphinx.ext.napoleon',  # Supporte les styles de docstrings NumPy et Google
    'sphinx.ext.viewcode',  # Ajoute des liens vers le code source dans la documentation générée
    'sphinx.ext.intersphinx',  # Permet de créer des liens vers la documentation d'autres projets externes
    "sphinx_autodoc_typehints"  # Inclut automatiquement les annotations de types Python dans la documentation
]

templates_path = ['_templates']
exclude_patterns = []



# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']

import os
import sys

sys.path.insert(0, os.path.abspath('../../'))

napoleon_google_docstring = True
napoleon_numpy_docstring = False

add_module_names = False