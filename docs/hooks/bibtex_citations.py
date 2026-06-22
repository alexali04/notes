"""
Render inline BibTeX entries as formatted citations (no metadata, no deps).

Drop a BibTeX entry anywhere in the markdown -- optionally as a `- ` list item --
and this hook replaces it in place with a one-line reference:

    - @misc{betancourt2018conceptualintroductionhamiltonianmonte,
          title={A Conceptual Introduction to Hamiltonian Monte Carlo},
          author={Michael Betancourt},
          year={2018},
          eprint={1701.02434},
          archivePrefix={arXiv},
          url={https://arxiv.org/abs/1701.02434},
      }

becomes

    - Michael Betancourt. *A Conceptual Introduction to Hamiltonian Monte Carlo*. 2018. arXiv:1701.02434. [link](https://arxiv.org/abs/1701.02434)

Brace-balanced, so braces inside field values (e.g. {BERT}) are handled. One
entry per block. Non-BibTeX text is left untouched.
"""

import re

ENTRY_START = re.compile(r'@(\w+)\s*\{\s*([^,\s]+)\s*,')
FIELD_RE = re.compile(r'(\w+)\s*=\s*')


def _read_value(s, i):
    """Read a field value at index i; return (value, next_index)."""
    while i < len(s) and s[i].isspace():
        i += 1
    if i >= len(s):
        return '', i
    if s[i] == '{':                                   # {balanced ... braces}
        depth, start = 0, i
        while i < len(s):
            if s[i] == '{':
                depth += 1
            elif s[i] == '}':
                depth -= 1
                if depth == 0:
                    return s[start + 1:i], i + 1
            i += 1
        return s[start + 1:], i
    if s[i] == '"':                                   # "quoted value"
        start = i + 1
        i += 1
        while i < len(s) and s[i] != '"':
            i += 1
        return s[start:i], i + 1
    start = i                                         # bare value
    while i < len(s) and s[i] not in ',}':
        i += 1
    return s[start:i].strip(), i


def _parse_fields(body):
    fields, i = {}, 0
    while True:
        m = FIELD_RE.search(body, i)
        if not m:
            break
        val, i = _read_value(body, m.end())
        val = ' '.join(val.split()).replace('{', '').replace('}', '')
        fields[m.group(1).lower()] = val
    return fields


def _format_authors(raw):
    out = []
    for a in re.split(r'\s+and\s+', raw):
        a = a.strip()
        if not a:
            continue
        if ',' in a:                                  # "Last, First" -> "First Last"
            last, first = (p.strip() for p in a.split(',', 1))
            out.append(f'{first} {last}'.strip())
        else:
            out.append(a)
    if len(out) > 1:
        return ', '.join(out[:-1]) + ' and ' + out[-1]
    return out[0] if out else ''


def _format_entry(etype, f):
    etype = etype.lower()
    parts = []
    if 'author' in f:
        parts.append(f'{_format_authors(f["author"])}.')
    elif 'editor' in f:
        parts.append(f'{_format_authors(f["editor"])} (ed.).')
    if 'title' in f:
        parts.append(f'*{f["title"]}*.')

    venue = (f.get('journal') if etype == 'article'
             else f.get('booktitle') if etype in ('inproceedings', 'incollection')
             else f.get('publisher') if etype == 'book'
             else f.get('institution') if etype == 'techreport'
             else f.get('school') if etype in ('phdthesis', 'mastersthesis')
             else None)
    if venue:
        parts.append(f'{venue}.')
    if 'year' in f:
        parts.append(f'{f["year"]}.')
    if 'eprint' in f:
        prefix = 'arXiv:' if f.get('archiveprefix', '').lower() == 'arxiv' else ''
        parts.append(f'{prefix}{f["eprint"]}.')

    cite = ' '.join(parts).strip()
    if 'url' in f:
        cite += f' [link]({f["url"]})'
    elif 'doi' in f:
        cite += f' [doi](https://doi.org/{f["doi"]})'
    return cite


def on_page_markdown(markdown, page, config, files):
    out, last_end = [], 0
    for m in ENTRY_START.finditer(markdown):
        if m.start() < last_end:                      # inside an entry we already took
            continue
        brace = markdown.index('{', m.start())
        depth, j = 0, brace
        while j < len(markdown):
            if markdown[j] == '{':
                depth += 1
            elif markdown[j] == '}':
                depth -= 1
                if depth == 0:
                    break
            j += 1
        if depth != 0:                                # unbalanced -> leave as-is
            continue
        end = j + 1

        body = markdown[brace + 1:j]
        body = body[body.index(',') + 1:]             # drop the cite key
        cite = _format_entry(m.group(1), _parse_fields(body))

        # preserve leading indentation / list marker on the entry's line
        line_start = markdown.rfind('\n', 0, m.start()) + 1
        pm = re.match(r'^(\s*)(?:([-*+])\s+)?', markdown[line_start:m.start()])
        bullet = f'{pm.group(1)}{pm.group(2)} ' if pm.group(2) else pm.group(1)

        out.append(markdown[last_end:line_start])
        out.append(bullet + cite)
        last_end = end

    out.append(markdown[last_end:])
    return ''.join(out)