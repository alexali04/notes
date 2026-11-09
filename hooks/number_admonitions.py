"""
Auto-number theorem-like admonitions AND opt-in display equations, both scoped
to h3 sections, derived from the same h2/h3 counts your CSS uses (no metadata).

Admonitions  -- shared counter, reset per ## / ### section:
    !!! info "Definition: UMP"               -> Definition 3.2.1: UMP
    !!! tip  "Theorem: Neyman-Pearson Lemma" -> Theorem 3.2.2: Neyman-Pearson Lemma

Equations -- separate counter, OPT-IN via the \eqnum marker:
    $$ x = y \eqnum $$                                 -> x = y                  (3.2.1)
    $$ \begin{gather*} ... \eqnum ... \end{gather*} $$ -> number on that row    (3.2.2)

Put \eqnum anywhere inside a display block ($$...$$, single- or multi-line) to
give it the next sectional number; the hook swaps it for \tag{...}. Blocks
without \eqnum are left untouched. One \eqnum per block.
"""

import re

ADMONITION_LABELS = {
    'info': 'Definition',
    'tip': 'Theorem',
    'question': 'Lemma',
    'success': 'Proposition',
    'warning': 'Corollary',
    'example': 'Example',
}
SHARED = {'info', 'tip', 'question', 'success', 'warning'}  # one shared counter
OWN = {'example'}                                           # its own counter
SKIP_NUMBERING = {'quote'}                                  # Proof, unnumbered

ADMON_RE = re.compile(r'^(\s*)!!!\s+(\w+)\s+"([^"]*)"')
HEADING_RE = re.compile(r'^(#{1,6})\s+\S')
DELIM_RE = re.compile(r'^\s*\$\$\s*$')                 # a lone $$ delimiter line
ONELINE_RE = re.compile(r'^(\s*)\$\$(.+?)\$\$\s*$')    # $$ ... $$ on one line

EQ_MARKER = r'\eqnum'


def on_page_markdown(markdown, page, config, files):
    h2 = h3 = 0
    shared = example = eq = 0

    def prefix():
        if h3 > 0:
            return f'{h2}.{h3}'
        if h2 > 0:
            return f'{h2}'
        return '1'

    def tag_block(text):
        """Replace the first \eqnum with a sectional \tag; strip any extras."""
        nonlocal eq
        eq += 1
        text = text.replace(EQ_MARKER, f'\\tag{{{prefix()}.{eq}}}', 1)
        return text.replace(EQ_MARKER, '')   # safety: no stray markers reach MathJax

    lines = markdown.split('\n')
    out = []
    i = 0
    while i < len(lines):
        line = lines[i]

        # --- headings: bump section counters, reset everything per section ---
        h = HEADING_RE.match(line)
        if h:
            level = len(h.group(1))
            if level == 2:
                h2 += 1; h3 = 0; shared = example = eq = 0
            elif level == 3:
                h3 += 1; shared = example = eq = 0
            out.append(line); i += 1; continue

        # --- admonitions ---
        m = ADMON_RE.match(line)
        if m:
            indent, kind, title = m.group(1), m.group(2), m.group(3)
            if kind in SKIP_NUMBERING or kind not in ADMONITION_LABELS:
                out.append(line); i += 1; continue
            if kind in OWN:
                example += 1; num = example
            else:
                shared += 1; num = shared
            label = ADMONITION_LABELS[kind]
            if ':' in title:
                name = title.split(':', 1)[1].strip()
                out.append(f'{indent}!!! {kind} "{label} {prefix()}.{num}: {name}"')
            else:
                out.append(f'{indent}!!! {kind} "{label} {prefix()}.{num}"')
            i += 1; continue

        # --- one-line display equation with marker ---
        om = ONELINE_RE.match(line)
        if om and EQ_MARKER in om.group(2):
            body = tag_block(om.group(2)).strip()
            out.append(f'{om.group(1)}$$ {body} $$')
            i += 1; continue

        # --- multi-line display block ---
        if DELIM_RE.match(line):
            block = [line]
            j = i + 1
            while j < len(lines) and not DELIM_RE.match(lines[j]):
                block.append(lines[j]); j += 1
            if j < len(lines):
                block.append(lines[j])          # closing delimiter
            inner = '\n'.join(block)
            if EQ_MARKER in inner:
                inner = tag_block(inner)
            out.append(inner)
            i = j + 1; continue

        out.append(line); i += 1; continue

    return '\n'.join(out)