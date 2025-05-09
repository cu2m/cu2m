# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

import os
import sys
from typing import Any

sys.path.insert(0, os.path.abspath(".."))
sys.path.insert(0, os.path.abspath("../tests"))


project = "CU^2M Test Documentation"
copyright = "2025, TEAM A11"
author = "TEAM A11"

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    "sphinx_needs",
    "sphinxcontrib.test_reports",
    "sphinxcontrib.plantuml",
    "sphinx.ext.autodoc",
    "sphinx.ext.viewcode",
]

templates_path = ["_templates"]
exclude_patterns = []


# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = "alabaster"
html_static_path = ["_static"]

tr_report_template = "_templates/report.rst"

exclude_tags = ["file", "style"]

needs_layouts: dict[str, Any] = {
    "custom_layout": {
        "grid": "simple",
        "layout": {
            "head": [
                '<<meta("type_name")>>: **<<meta("title")>>** <<meta_id()>>  <<collapse_button("meta", collapsed="icon:arrow-down-circle", visible="icon:arrow-right-circle", initial=False)>>'
            ],
            "meta": [
                f"<<meta_all(prefix='**', postfix='**', exclude={exclude_tags}, no_links=True)>>",
                f"<<meta_links_all(prefix='**', postfix='**', exclude=None)>>",
            ],
        },
    }
}


needs_default_layout = "custom_layout"
