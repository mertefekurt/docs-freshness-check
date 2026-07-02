# docs-freshness-check

> Audit docs inventories for stale owners, old updates, and broken review cadence.

## Review card Overview

Audit docs inventories for stale owners, old updates, and broken review cadence. It solves review drift by turning plain-text plans into deterministic CI-friendly findings.

## Input Contract 25

Accepts documentation inventory. The reader supports plain text, JSON, JSONL, and CSV so the
tool can fit into scripts, CI jobs, and review exports.

## CLI Walkthrough 25

```bash
python -m pip install -e ".[dev]"
docs-freshness-check examples/sample.txt
docs-freshness-check examples/sample.txt --json --fail-on medium
python -m docs_freshness_check --help
```

## Rule Surface 25

| Rule | Severity | Meaning |
|---|---:|---|
| `unknown-owner` | high | doc owner missing |
| `stale-doc` | medium | doc appears stale |
| `no-review` | low | review cadence missing |

## Validation Notes 25

```bash
ruff check .
pytest
python -m docs_freshness_check --help
```

Example risky input:

```text
doc api-auth owner unknown updated 2023 review none
```

Architecture: `cli.py` handles arguments, `core.py` reads and evaluates records, and
`rules.py` keeps the project-specific policy explicit.

License: MIT.
