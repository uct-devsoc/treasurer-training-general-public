#!/usr/bin/env python3
"""Rebuild data/vendors.json from Treasury's vendor workbook.

    python3 extract_vendors.py All_Vendors_UCT.xlsx

Expects a "Vendors ALL" sheet first, then one sheet per category. Keeps only
vendor number, registered name, town, telephone and category; drops the
clerk names and email addresses in the workbook.
"""
import sys, json, openpyxl
wb = openpyxl.load_workbook(sys.argv[1], read_only=True)
cats = {}
for ws in wb.worksheets[1:]:
    title = ws.title.replace('Hiring& Deco', 'Hiring & Deco')
    for i, r in enumerate(ws.iter_rows(values_only=True)):
        if i and r[0]: cats.setdefault(str(r[0]).strip(), set()).add(title)
out, seen = [], set()
for i, r in enumerate(wb.worksheets[0].iter_rows(values_only=True)):
    if i == 0: continue
    v = str(r[0]).strip() if r[0] else ''
    if not v or v in seen: continue
    seen.add(v)
    name = ' '.join(x for x in [str(r[1] or '').strip(), str(r[2] or '').strip()] if x)
    out.append({'v': v, 'n': name, 'c': str(r[3] or '').strip().title(), 't': str(r[4] or '').strip(), 'k': sorted(cats.get(v, []))})
json.dump(out, open('data/vendors.json', 'w'), separators=(',', ':'), ensure_ascii=False)
print(len(out), 'vendors written')
