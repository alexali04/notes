"""
Auto-number admonitions with section-based counters.

Renders: "Definition 1.3: σ-algebra" where 1 = h2 section number, 3 = definition count within that section.

Supported admonition types:
  !!! info "Definition: name"       -> Definition 1.1: name
  !!! tip "Theorem: name"           -> Theorem 1.1: name
  !!! question "Lemma: name"        -> Lemma 1.1: name
  !!! success "Proposition: name"   -> Proposition 1.1: name
  !!! warning "Corollary: name"     -> Corollary 1.1: name
  !!! example "Example: name"       -> Example 1.1: name
  !!! quote "Proof"                 -> Proof (no numbering)

The name part is optional:
  !!! info "Definition"             -> Definition 1.1
"""

import re

# Map admonition types to their display labels
ADMONITION_LABELS = {
    'info': 'Definition',
    'tip': 'Theorem',
    'question': 'Lemma',
    'success': 'Proposition',
    'warning': 'Corollary',
    'example': 'Example',
}

# Types that should NOT be numbered
SKIP_NUMBERING = {'quote'}


def on_page_markdown(markdown, page, config, files):
    h2_count = 0
    counters = {}  # per-type counters, reset each h2

    lines = markdown.split('\n')
    result = []

    admonition_pattern = re.compile(
        r'^(\s*)!!!\s+(\w+)\s+"([^"]*)"'
    )
    h2_pattern = re.compile(r'^##\s+[^#]')

    for line in lines:
        # Detect h2 headings — reset counters
        if h2_pattern.match(line):
            h2_count += 1
            counters = {}
            result.append(line)
            continue

        m = admonition_pattern.match(line)
        if m:
            indent = m.group(1)
            kind = m.group(2)
            title_text = m.group(3)

            if kind in SKIP_NUMBERING:
                result.append(line)
                continue

            if kind not in ADMONITION_LABELS:
                result.append(line)
                continue

            # Increment counter for this type
            counters[kind] = counters.get(kind, 0) + 1
            num = counters[kind]
            section = h2_count if h2_count > 0 else 1

            label = ADMONITION_LABELS[kind]

            # Parse title: "Label: name" or "Label" or just "name"
            # If title starts with the expected label, extract the name after ":"
            if ':' in title_text:
                parts = title_text.split(':', 1)
                name = parts[1].strip()
                new_title = f'{label} {section}.{num}: {name}'
            else:
                # No colon — could be just "Definition" or a custom title
                new_title = f'{label} {section}.{num}'

            result.append(f'{indent}!!! {kind} "{new_title}"')
            continue

        result.append(line)

    return '\n'.join(result)