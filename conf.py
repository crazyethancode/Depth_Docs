# -- Project information -----------------------------------------------------
project = 'Depth'
copyright = '2025, Suzanna_Ethan'
author = 'Suzanna_Ethan'
release = '0.1'
version = '0.1.0'

# -- Internationalization ---------------------------------------------------
language = 'en'
locale_dirs = ['locales/']
gettext_compact = False
gettext_uuid = True

# -- Source processing ------------------------------------------------------
source_suffix = {
    ".rst": "restructuredtext",
    ".md": "markdown",
}

# -- General configuration ---------------------------------------------------
extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
]

templates_path = ['_templates']
exclude_patterns = ['_build', 'Thumbs.db', '.DS_Store']

# -- HTML Output ------------------------------------------------------------
html_theme = 'furo'
html_static_path = ['_static']
html_title = f"{project} {version} Documentation"

# Theme options
html_theme_options = {
    "sidebar_hide_name": False,
    "navigation_with_keys": True,
    "top_of_page_button": "edit",
    #"announcement": "<em>Silent Hill: Fog City Documentation</em>",
    "light_logo": "logo-light.png",  # добавьте свои логотипы
    "dark_logo": "logo-dark.png",
}

# Правильные настройки sidebar
html_sidebars = {
    "**": [
        "sidebar/scroll-start.html",
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/navigation.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

# Myst Parser
myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "dollarmath",
]