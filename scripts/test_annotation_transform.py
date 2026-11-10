#!/usr/bin/env python3
"""Source-only regression tests for inline-definition schemas and transforms.

The suite deliberately does not read, write, or publish the React explorer.
It retains the original five-page pilot regressions and adds an all-concept
source gate for schemas now declared in canonical Markdown frontmatter.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from annotation_transform import (  # noqa: E402
    EXPLICIT_RE,
    InlineDefinition,
    parse_frontmatter,
    transform,
    with_schema,
)

OUT = ROOT / ".agents" / "annotation-pilot-output"
CONTENT_DIRS = ("mathematics", "physics", "page-wootters", "philosophy")
TOKEN_RE = re.compile(r"\{\{def:([^|}]+)\|([^}]+)\}\}")
INLINE_MATH_RE = re.compile(r"\\\\\([\s\S]*?\\\\\)")
LINK_RE = re.compile(r"\[[^\]]*\]\([^)]*\)")
CODE_RE = re.compile(r"`[^`]*`")

# Original five-page pilot regression set, updated only to respect the final
# conservative semantic exclusions (notably inner-product space and anomaly freedom).
PILOTS = {
    "hilbert-spaces": [
        InlineDefinition("completeness", "Completeness"), InlineDefinition("norm", "norm"),
        InlineDefinition("cauchy-sequence", "Cauchy sequence"), InlineDefinition("ray", "ray"),
        InlineDefinition("normalization", "normalized"), InlineDefinition("orthogonality", "orthogonality"),
        InlineDefinition("born-rule", "Born rule"),
    ],
    "dirac-notation": [
        InlineDefinition("ket", "ket"), InlineDefinition("bra", "bra"), InlineDefinition("dual-vector", "dual vector"),
        InlineDefinition("overlap", "overlap"), InlineDefinition("norm", "norm"), InlineDefinition("discrete-basis", "discrete basis"),
        InlineDefinition("orthonormal-basis", "orthonormal"), InlineDefinition("kronecker-delta", "Kronecker delta"),
        InlineDefinition("resolution-of-identity", "resolution of the identity"), InlineDefinition("basis-expansion", "basis expansion"),
    ],
    "wheeler-dewitt-formalism": [InlineDefinition("functional-derivative", "functional derivatives")],
    "page-wootters-mechanism": [InlineDefinition("clock-system-factorization", "clock/system factorization")],
    "jon-projection-story": [
        InlineDefinition("ket", "ket"), InlineDefinition("dual-vector", "dual vector"),
        InlineDefinition("inner-product", "inner product"), InlineDefinition("projector", "projector"),
    ],
}


def concept_paths() -> list[Path]:
    return [path for directory in CONTENT_DIRS for path in sorted((ROOT / directory).glob("*.md"))]


def definition_ids() -> set[str]:
    result = set()
    for path in (ROOT / "definitions").glob("def-*.md"):
        metadata, _ = parse_frontmatter(path.read_text(encoding="utf-8"))
        result.add(metadata["id"].removeprefix("def-"))
    return result


def protected_tokens(body: str) -> list[str]:
    """Return annotations found in syntax that must never be annotated."""
    found: list[str] = []
    in_fence = in_display = False
    for line in body.splitlines():
        if line.startswith("```"):
            in_fence = not in_fence
            found.extend(TOKEN_RE.findall(line))
            continue
        if line == "\\[":
            in_display = True
        if in_fence or in_display or line.startswith("#") or line.startswith(">") or line.startswith("[^") or line.startswith("    "):
            found.extend(TOKEN_RE.findall(line))
        for fragment in (*INLINE_MATH_RE.findall(line), *CODE_RE.findall(line), *LINK_RE.findall(line)):
            found.extend(TOKEN_RE.findall(fragment))
        if line == "\\]":
            in_display = False
    return [definition_id for definition_id, _ in found]


class AnnotationTransformTests(unittest.TestCase):
    maxDiff = None

    def setUp(self) -> None:
        if OUT.exists():
            shutil.rmtree(OUT)
        OUT.mkdir(parents=True)

    def test_five_pilot_pages_transform_with_strong_invariants(self) -> None:
        manifest: dict[str, object] = {"tool": "annotation_transform.py", "pages": {}}
        for page_id, schema in PILOTS.items():
            with self.subTest(page_id=page_id):
                source_path = next(path for path in concept_paths() if parse_frontmatter(path.read_text(encoding="utf-8"))[0]["id"] == page_id)
                original = source_path.read_text(encoding="utf-8")
                _, original_body = parse_frontmatter(original)
                seeded = with_schema(original, schema)
                transformed, report = transform(seeded)
                _, transformed_body = parse_frontmatter(transformed)
                visible_body = TOKEN_RE.sub(r"\2", transformed_body)
                visible_body = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", visible_body)
                original_visible = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", original_body)
                self.assertEqual(visible_body, original_visible)
                self.assertEqual(report.unmatched, ())
                self.assertEqual(len(report.applied) + report.explicit_annotations, len(schema))
                self.assertEqual(protected_tokens(transformed_body), [])
                output_path = OUT / f"{page_id}.annotated.md"
                output_path.write_text(transformed, encoding="utf-8")
                manifest["pages"][page_id] = {
                    "source": str(source_path.relative_to(ROOT)),
                    "source_sha256": hashlib.sha256(original.encode()).hexdigest(),
                    "output_sha256": hashlib.sha256(transformed.encode()).hexdigest(),
                    "annotations": [item.definition_id for item in schema],
                }
        (OUT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")

    def test_all_concept_schemas_are_real_unique_matched_and_safe(self) -> None:
        definitions = definition_ids()
        schema_pages = 0
        declared_terms = 0
        for path in concept_paths():
            with self.subTest(path=path.relative_to(ROOT)):
                source = path.read_text(encoding="utf-8")
                metadata, body = parse_frontmatter(source)
                schema = metadata.get("inline_definitions", [])
                if not schema:
                    continue
                schema_pages += 1
                declared_terms += len(schema)
                ids = [item["definition_id"] for item in schema]
                self.assertEqual(len(ids), len(set(ids)), "Duplicate definition IDs per page are forbidden.")
                self.assertTrue(set(ids) <= definitions, "Every schema target must be a definition node.")
                explicit_ids = [definition_id for definition_id, _ in EXPLICIT_RE.findall(body)]
                self.assertTrue(set(explicit_ids) <= set(ids), "Explicit overrides must be declared by the schema.")
                transformed, report = transform(source)
                _, transformed_body = parse_frontmatter(transformed)
                self.assertEqual(report.unmatched, (), f"Unmatched schema: {report.unmatched}")
                output_ids = [definition_id for definition_id, _ in TOKEN_RE.findall(transformed_body)]
                self.assertEqual(len(output_ids), len(schema), "Each declared target must produce exactly one token, including an explicit override.")
                self.assertEqual(set(output_ids), set(ids))
                self.assertEqual(len(output_ids), len(set(output_ids)), "No target may be annotated twice.")
                self.assertEqual(protected_tokens(transformed_body), [], "Annotations must remain outside protected syntax.")
        # These totals are source-graph release fixtures. Update them only with
        # an intentional canonical-source addition and its matching tests.
        self.assertEqual(schema_pages, 36)
        self.assertEqual(declared_terms, 122)

    def test_explicit_override_is_retained_and_never_double_annotated(self) -> None:
        source = """---\n{\n  \"id\": \"fixture\",\n  \"title\": \"Fixture\",\n  \"inline_definitions\": [{\"definition_id\": \"ket\", \"term\": \"ket\", \"occurrence\": \"first\"}]\n}\n---\nA {{def:ket|ket}} is explicit. A later ket stays plain.\n"""
        transformed, report = transform(source)
        _, transformed_body = parse_frontmatter(transformed)
        _, original_body = parse_frontmatter(source)
        self.assertEqual(transformed_body, original_body)
        self.assertEqual(report.explicit_annotations, 1)
        self.assertEqual(report.unmatched, ())

    def test_bold_wrapped_explicit_override_is_structurally_preserved(self) -> None:
        source = """---\n{\n  \"id\": \"fixture\",\n  \"title\": \"Fixture\",\n  \"inline_definitions\": [{\"definition_id\": \"foliation\", \"term\": \"foliation\", \"occurrence\": \"first\"}]\n}\n---\nSpacetime is called a **{{def:foliation|foliation}}** here. A later foliation stays plain.\n"""
        transformed, report = transform(source)
        _, transformed_body = parse_frontmatter(transformed)
        _, original_body = parse_frontmatter(source)
        self.assertEqual(transformed_body, original_body)
        self.assertIn("**{{def:foliation|foliation}}**", transformed_body)
        self.assertEqual(TOKEN_RE.findall(transformed_body), [("foliation", "foliation")])
        self.assertEqual(report.explicit_annotations, 1)
        self.assertEqual(report.unmatched, ())
        self.assertEqual(protected_tokens(transformed_body), [])


if __name__ == "__main__":
    unittest.main(verbosity=2)
