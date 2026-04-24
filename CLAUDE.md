# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

Static workshop website for the **RS3 at IEEE eScience 2026** workshop (Workshop on Research Software Supply Chain Security), built with Sphinx + MyST Markdown and deployed to GitHub Pages via GitHub Actions.

## Development setup

```bash
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt
```

## Common commands

| Task | Command |
|------|---------|
| Build site | `make html` or `.venv/bin/sphinx-build -b html docs docs/_build/html` |
| Clean build | `make clean` |
| Preview | open `docs/_build/html/index.html` in a browser |

## Architecture

All content lives in `docs/` as Markdown files (`.md`). Sphinx configuration is in `docs/conf.py`. The build outputs to `docs/_build/html/` (gitignored).

- `docs/conf.py` — Sphinx config; sets theme, extensions, `GITHUB_REPOSITORY` env var for the repo button
- `docs/index.md` — landing page with MyST grid cards and the `toctree`
- `docs/call-for-papers.md`, `program.md`, `organizers.md`, `logistics.md` — the four workshop content pages
- `docs/_static/custom.css` — site-wide CSS overrides
- `docs/_static/rs3-logo.png` — logo used as both `html_logo` and `html_favicon`

**Extensions in use:** `myst_parser` (Markdown), `sphinx_design` (grid/card directives), `sphinx.ext.todo`. MyST colon-fence and deflist extensions are enabled.

## Deployment

Pushing to `main` triggers `.github/workflows/pages.yml`, which builds with Python 3.12 and deploys to GitHub Pages automatically. No manual deployment step is needed.

## Content status

Several fields are intentionally marked `TBD` pending confirmation: final workshop date/venue, submission deadlines, notification dates, and the EasyChair/submission link.
