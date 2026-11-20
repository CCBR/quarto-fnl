# FNL Themes for Quarto

This is a Quarto template that assists you in creating a report, document, or
presentation using the [FNLCR branding
guidelines](https://nih.sharepoint.com/sites/NCI-Fred/Communications/Branding).

## Creating a New Document

To create a new document, use the following command:

```bash
quarto use template CCBR/quarto-fnl
```

This will install the extension and create an example qmd file that you can use as a starting place

## Installation For Existing Document

You may also use this format with an existing Quarto project or document. From the quarto project or document directory, run the following command to install this format:

```bash
quarto add extension CCBR/quarto-fnl
```

## Usage

To use the format, you can use the format names `fnl-html`, `fnl-revealjs`, or `fnl-dashboard`. For example:

```bash
quarto render report.qmd --to fnl-html
```

or in your document yaml or `_quarto.yml` file:

```yaml
format:
  fnl-html
```

### Report format

`quarto add extension CCBR/quarto-fnl` also installs a second, independent
extension, `fnl-report`. It provides the `fnl-report-html` format for
reports with a title banner, styled buttons, tab themes, author/affiliation
cards, and table styles:

```yaml
format:
  fnl-report-html
```

All assets are bundled with the extension, so documents render offline with no
calls to Google Fonts or GitHub. Bundled assets include:

- Roboto and Roboto Mono fonts
- Font Awesome icons
- the banner image
- the stylesheets

The report styles only load for `fnl-report-html`, so `fnl-html`,
`fnl-revealjs`, and `fnl-dashboard` documents are unaffected.

See [template-report.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template-report.qmd)
for the available components, such as `.btn-primary`, `.btn-outline-github`,
`.panel-tabset .theme-ccbr-poppy`, and `.ccbr-footer`.

## Templates

| Format | Quarto Source | Rendered Example |
|--------|--------------|-----------------|
| HTML | [template.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template.qmd) | [View HTML](https://ccbr.github.io/quarto-fnl/template.html) |
| report HTML | [template-report.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template-report.qmd) | [View report](https://ccbr.github.io/quarto-fnl/template-report.html) |
| revealjs | [template-revealjs.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template-revealjs.qmd) | [View revealjs](https://ccbr.github.io/quarto-fnl/template-revealjs.html) |
| dashboard | [template-dashboard.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template-dashboard.qmd) | [View dashboard](https://ccbr.github.io/quarto-fnl/template-dashboard.html) |

## See also

[quarto-version-selector](https://github.com/CCBR/quarto-version-selector) - extension providing a version dropdown menu for quarto websites

## Examples

See this theme in action!

| Format | URL |
|------|-----|
| website | <https://ccbr.github.io/quarto-fnl> |
| website | <https://ccbr.github.io/Tools> |
| website | <https://ccbr.github.io/actions> |
| website | <https://ccbr.github.io/HowTos/> |
| revealjs | <https://ccbr.github.io/reproducible-toolchain/slides/abcs-tech-workshop-2026-05.html> |
