# FNL Theme for Quarto

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

You can view a preview of the rendered templates:

- HTML:
- revealjs:
- dashboard: