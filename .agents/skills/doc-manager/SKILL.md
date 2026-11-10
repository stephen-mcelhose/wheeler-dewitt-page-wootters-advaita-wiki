---
name: doc-manager
description: Maintain this wiki and its governing charter
---
# Local Doc Manager
`WIKI_CHARTER.md` is mandatory governing project context: complete it before source research, source selection, or content production. The validator requires its minimum headings. If it changes mid-project, record the decision first; update affected sources, nodes, examples, redirects, indexes, and version/change notes before validation.

Run `python3 scripts/build_index.py .` after edits and `python3 scripts/validate.py .` before packaging. See `references/example-taxonomy.md`.
