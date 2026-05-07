import os

project = "RS3 eScience 2026"
author = (
    "James C. Davis, George K. Thiruvathukal, "
    "Alexandra Harris-Watson, Jeffrey C. Carver"
)
copyright = "2026, RS3 Workshop Organizers"
repository = os.environ.get("GITHUB_REPOSITORY", "OWNER/rs3-eScience-2026")

extensions = [
    "sphinx.ext.todo",
    "myst_parser",
    "sphinx_design",
]

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

source_suffix = {
    ".md": "markdown",
    ".rst": "restructuredtext",
}

myst_enable_extensions = [
    "colon_fence",
    "deflist",
]

todo_include_todos = True

html_theme = "sphinx_book_theme"
html_title = "RS3 at IEEE eScience 2026"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_show_sourcelink = False
html_logo = "_static/rs3-logo.png"
html_favicon = "_static/rs3-logo.png"

html_theme_options = {
    "path_to_docs": "docs",
    "repository_url": f"https://github.com/{repository}",
    "use_repository_button": True,
    "use_edit_page_button": False,
    "use_issues_button": False,
    "show_navbar_depth": 2,
    # "announcement": "The Call for Papers is now open! Submit at <URL>.",
}
