# Contributing

Thank you for your interest in improving this wiki. Please read the [Wiki Charter](WIKI_CHARTER.md) before contributing — it defines scope, content standards, and the boundary between physics and philosophy.

## Content standards

- **Originality.** All contributions must be original writing. Do not reproduce passages from copyrighted textbooks or papers. Paraphrase, cite with DOI or arXiv, and explain in your own words.
- **Sources.** Every claim that is not standard mathematical background must cite a primary or peer-reviewed source. Use DOI or arXiv links in the node's `sources` frontmatter field.
- **Separation of physics and philosophy.** Physics concepts must not depend on Advaita nodes. Comparative links belong only in the optional philosophy layer and must state their limits explicitly.
- **Review status.** New and modified nodes must carry `review_status: draft`. Only the maintainer may promote content to `approved`.

## Workflow

1. **Open an issue first** for anything beyond a typo fix. Use the provided issue templates.
2. **Fork the repo** and create a branch from `main`.
3. **Make your changes** and run `make validate` locally to confirm the graph is valid.
4. **Open a pull request** using the PR template checklist.
5. The maintainer reviews and merges. CI must pass before merge.

## Running validation locally

```bash
# Requires Python 3.11+
make validate       # validate the wiki graph
make index          # rebuild concept and example indexes
```

## Copyright

Contributions are accepted under [CC BY 4.0](LICENSE). By submitting a pull request you confirm that your contribution is your own original work and that you agree to license it under CC BY 4.0.
