# Treasurer handbook site

A public, single-file training site for UCT society treasurers, with one numbered section per finance form (MM010 complete, SD004 placeholder). No encryption, no server.

## Build

    pip install markdown
    python3 build.py

Writes `dist/index.html`. Put that one file in a GitHub Pages repo (or anywhere static) and it works as is.

## Edit

- Pages are Markdown files in `content/`. Filename order is page order; the `group` in the frontmatter names the section. A group containing a colon (for example `MM010: purchase order request`) is a form section and its pages are numbered; any other group is plain. To add a form, create its pages with a new `FORMCODE: description` group.
- Custom blocks: `:::watch ... :::` for a callout, `:::chain` with `Who | What` lines for a numbered process, `:::reveal Title ... :::` for a hidden answer.
- `<div id="vendor-search"></div>` and `<div id="builder"></div>` are where the two interactive tools render.
- The vendor list is `data/vendors.json` (vendor number, registered name, town, telephone, categories), built from Treasury's workbook. Regenerate it from a new workbook with `python3 extract_vendors.py All_Vendors_UCT.xlsx`.
- Styles, the vendor search and the MM010 builder live in `template.html`.
