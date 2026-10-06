#!/usr/bin/env python3
"""Build the MM010 walkthrough site into a single HTML file.

Reads content/*.md (with a small frontmatter block), converts them to HTML,
embeds the vendor list from data/vendors.json, and writes dist/index.html.
No encryption: the site is public.
"""
import json, re, html
from pathlib import Path
import markdown

ROOT = Path(__file__).parent
CONTENT = ROOT / "content"
DIST = ROOT / "dist"
DIST.mkdir(exist_ok=True)

def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", text, re.S)
    meta = {}
    for line in m.group(1).splitlines():
        k, _, v = line.partition(":")
        meta[k.strip()] = v.strip()
    return meta, m.group(2)

def custom_blocks(md):
    """Turn :::watch / :::chain / :::reveal Title blocks into HTML before markdown runs."""
    def chain(m):
        rows = []
        for line in m.group(1).strip().splitlines():
            who, _, what = line.partition("|")
            rows.append(f'<li><span class="who">{html.escape(who.strip())}</span><span class="what">{markdown.markdown(what.strip())[3:-4]}</span></li>')
        return '<ol class="chain">' + "".join(rows) + "</ol>\n"
    md = re.sub(r":::chain\n(.*?):::", chain, md, flags=re.S)

    def watch(m):
        inner = markdown.markdown(m.group(1).strip(), extensions=["tables"])
        return f'<aside class="watch">{inner}</aside>\n'
    md = re.sub(r":::watch\n(.*?):::", watch, md, flags=re.S)

    def reveal(m):
        title = m.group(1).strip()
        inner = markdown.markdown(m.group(2).strip(), extensions=["tables"])
        return f'<details class="reveal"><summary>{html.escape(title)}</summary><div>{inner}</div></details>\n'
    md = re.sub(r":::reveal (.*?)\n(.*?):::", reveal, md, flags=re.S)
    return md

pages = []
for f in sorted(CONTENT.glob("*.md")):
    meta, body = frontmatter(f.read_text())
    body = custom_blocks(body)
    body_html = markdown.markdown(body, extensions=["tables", "md_in_html", "attr_list"])
    slug = f.stem.split("-", 1)[1]
    pages.append({"slug": slug, "title": meta["title"], "group": meta["group"], "html": body_html})

vendors = json.loads((ROOT / "data" / "vendors.json").read_text())
template = (ROOT / "template.html").read_text()

nav_groups = {}
for p in pages:
    nav_groups.setdefault(p["group"], []).append(p)

# Groups whose pages are numbered steps: the per-form walkthroughs.
NUMBERED = lambda g: ":" in g

nav_html = ""
for group, items in nav_groups.items():
    gclass = "navgroup form" if NUMBERED(group) else "navgroup"
    nav_html += f'<div class="{gclass}"><h2>{html.escape(group)}</h2>'
    cls = "steps" if NUMBERED(group) else "plain"
    nav_html += f'<ol class="{cls}">'
    for p in items:
        nav_html += f'<li><a href="#{p["slug"]}" data-page="{p["slug"]}">{html.escape(p["title"])}</a></li>'
    nav_html += "</ol></div>"

sections = ""
order = [p["slug"] for p in pages]
for i, p in enumerate(pages):
    prev_ = pages[i - 1] if i > 0 else None
    next_ = pages[i + 1] if i < len(pages) - 1 else None
    footer = '<nav class="pager">'
    footer += f'<a class="prev" href="#{prev_["slug"]}">{html.escape(prev_["title"])}</a>' if prev_ else "<span></span>"
    footer += f'<a class="next" href="#{next_["slug"]}">{html.escape(next_["title"])}</a>' if next_ else "<span></span>"
    footer += "</nav>"
    sections += f'<section class="page" id="page-{p["slug"]}" data-group="{html.escape(p["group"])}" hidden>{p["html"]}{footer}</section>\n'

out = (template
       .replace("<!--NAV-->", nav_html)
       .replace("<!--PAGES-->", sections)
       .replace("/*VENDORS*/", json.dumps(vendors, separators=(",", ":"), ensure_ascii=False))
       .replace("/*ORDER*/", json.dumps(order)))
(DIST / "index.html").write_text(out)
print(f"built dist/index.html: {len(out)//1024} KB, {len(pages)} pages, {len(vendors)} vendors")
