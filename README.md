# Mohammad Ful Hossain Seikh | Personal Academic Website

Personal academic website of **Mohammad Ful Hossain Seikh**, Postdoctoral Researcher in Particle Astrophysics at the University of Kansas.

### [Visit the live website →](https://mohammad-neutrino.github.io/)

The site presents my research, scientific software, publications, invited talks, curriculum vitae, field work, and future research notes.

## Website Structure

The main portfolio pages use custom static HTML, CSS, and JavaScript to preserve the site's visual design and lightweight structure.

Current sections include:

- Home
- Research
- Projects
- Publications
- Talks
- Notes
- CV

Quarto is used for the **Notes** workflow so longer-form posts can be written in Markdown while remaining integrated with the rest of the website.

## Local Preview

Static HTML pages can be opened directly in a browser.

To preview the complete site, including Quarto-generated content:

```bash
quarto preview
```

## Adding a Note

New Notes are written as Quarto documents.

Copy the template directory:

```text
posts/_template/
```

to a new post directory, for example:

```text
posts/2026-10-radio-neutrinos/index.qmd
```

Update the title, date, description, categories, and content.

Set:

```yaml
draft: false
```

when the post is ready to publish.

## Curriculum Vitae

The CV source is maintained separately in the dedicated repository:

[github.com/Mohammad-Neutrino/CV](https://github.com/Mohammad-Neutrino/CV)

The CV workflow is automated:

```text
cv.tex
  → GitHub Actions
  → cv.pdf
  → website CV viewer
```

Updates pushed from Overleaf or Git to `cv.tex` automatically rebuild `cv.pdf`. The website then displays the latest generated PDF without requiring a manual website update.

## Deployment

The website is deployed through **GitHub Pages**.

The GitHub Actions workflow:

1. checks out the repository,
2. installs Quarto,
3. renders the site into `_site`,
4. uploads the Pages artifact,
5. deploys the site to GitHub Pages.

Deployment runs automatically on pushes to the `main` branch.

Live site:

**[https://mohammad-neutrino.github.io/](https://mohammad-neutrino.github.io/)**

## License and Reuse

The website source code and layout are available under the MIT License.

Personal and scholarly content is excluded from the software license. This includes, but is not limited to:

- photographs,
- CV and biographical material,
- research descriptions,
- talk slides and screenshots,
- publication imagery,
- personal branding,
- logos and third-party media.

If you adapt the website structure or design for your own academic site, attribution to **Mohammad Ful Hossain Seikh** and a link to this repository are appreciated.

See [`LICENSE`](LICENSE) for details.
