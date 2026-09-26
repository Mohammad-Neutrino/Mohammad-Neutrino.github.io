# Mohammad Ful Hossain Seikh — Personal Website

Personal academic website designed for GitHub Pages. The main portfolio pages are static HTML to preserve the custom design. Quarto is used for the Notes/blog workflow so new posts can be written in Markdown.

## Recommended repository

Create the GitHub repository `Mohammad-Neutrino.github.io` under the `Mohammad-Neutrino` account and place these files at the repository root.

## Local preview

The static pages can be opened directly in a browser. For the complete Quarto site including Notes:

```bash
quarto preview
```

## Add a new Note

Copy `posts/_template/` to a new folder, for example:

```text
posts/2026-10-radio-neutrinos/index.qmd
```

Update the title, date, description, categories, and set `draft: false` when ready to publish.

## Deployment

The included GitHub Actions workflow renders Quarto and deploys `_site` to GitHub Pages on pushes to `main`. In the GitHub repository, set **Settings → Pages → Source** to **GitHub Actions**.
