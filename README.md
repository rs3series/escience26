# RS3 eScience 2026 Workshop Site

This repository contains the Sphinx documentation site for the
`rs3-eScience-2026` workshop:

Workshop on Research Software Supply Chain Security (RS3)

The site uses `sphinx-book-theme`, Markdown content via MyST, and GitHub Pages
deployment through GitHub Actions.

## Local development

Create a virtual environment and install the documentation dependencies:

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

Build the site:

```bash
.venv/bin/sphinx-build -b html docs docs/_build/html
```

Open `docs/_build/html/index.html` in a browser to preview the result.

## Publishing on GitHub Pages

1. Push this repository to GitHub, ideally as `rs3-eScience-2026`.
2. In GitHub, enable Pages and set the source to `GitHub Actions`.
3. The workflow in `.github/workflows/pages.yml` will build and deploy the site
   on pushes to `main`.

## Content status

The initial pages are based on the current workshop proposal. A few items are
left intentionally marked as `TBD`, including:

- final workshop date and venue details
- submission deadline and notification dates
- EasyChair or conference submission link
- confirmed keynote and panelists

