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
quarto install extension CCBR/quarto-fnl
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

## Templates

| Format | Quarto Source | Rendered Example |
|--------|--------------|-----------------|
| HTML | [template.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template.qmd) | [View HTML](https://ccbr.github.io/quarto-fnl/template.html) |
| revealjs | [template-revealjs.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template-revealjs.qmd) | [View revealjs](https://ccbr.github.io/quarto-fnl/template-revealjs.html) |
| dashboard | [template-dashboard.qmd](https://github.com/CCBR/quarto-fnl/blob/main/template-dashboard.qmd) | [View dashboard](https://ccbr.github.io/quarto-fnl/template-dashboard.html) |

## Examples

See this theme in action!

| Format | URL |
|------|-----|
| website | <https://ccbr.github.io/quarto-fnl> |
| website | <https://ccbr.github.io/Tools> |
| website | <https://ccbr.github.io/actions> |
| website | <https://ccbr.github.io/HowTos/> |
| revealjs | <https://ccbr.github.io/reproducible-toolchain/slides/abcs-tech-workshop-2026-05.html> |