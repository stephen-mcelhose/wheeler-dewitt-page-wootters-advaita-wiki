# Time, Quantum Cosmology, and Advaita: An Explorable Wiki

A physics-student-first learning hub. It begins with mathematical foundations, proceeds to constrained dynamics and canonical gravity, then studies relational time via the Page–Wootters mechanism. An optional philosophical layer — bounded comparisons with selected Advaita Vedānta concepts — follows only after the physics curriculum is complete.

**Requires Python 3.11+**

## Build steps

| Command        | What it does                                                                                      |
| -------------- | ------------------------------------------------------------------------------------------------- |
| `make explore` | Starts a local HTTP server and opens the interactive wiki explorer at `http://localhost:8000`     |
| `make validate`| Validates the wiki graph: schema, controlled vocabulary, review-status, and relationship rules    |
| `make index`   | Rebuilds `concept-index.md` and `example-index.md` from the source graph                         |
| `make package` | Full release build — clean → index → validate → zip the wiki to `../wheeler-dewitt-page-wootters-advaita-wiki.zip` |
| `make clean`   | Removes `__pycache__` directories and the generated `viewer/wiki-data.json`                       |

### Run tests

```bash
python3 scripts/test_annotation_transform.py
```

The test suite uses stdlib `unittest` and requires no external dependencies.

### CI

GitHub Actions runs `make validate` and the test suite on every push and pull request to `main`. Merging to `main` requires the CI job to pass and at least one review approval.

## Repository layout

```
mathematics/        Hilbert spaces, Dirac notation, constrained systems, quantization
physics/            ADM gravity, Wheeler–DeWitt, superspace, problem of time
page-wootters/      Relational time, clock states, conditional states, finite clocks
philosophy/         Optional Advaita layer (comes after physics)
definitions/        Short reusable term definitions linked from concept bodies
examples/           Worked examples (do not define concepts)
viewer/             Self-contained HTML explorer (index.html + generated wiki-data.json)
scripts/            Tooling: annotation transform, packaging, smoke tests
.agents/            AI-assisted development tooling (skills and build scripts)
```

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md). All contributions must be original writing; no verbatim reproduction from copyrighted texts. Content is licensed [CC BY 4.0](LICENSE).
