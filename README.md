# Docs Freshness Check

> A small command-line review pass for documentation health.

![Docs Freshness Check cover](assets/readme-cover.svg)

Audit docs inventories for stale owners, old updates, and broken review cadence. The idea is simple: give Docs Freshness Check the local file or fixture, get a readable result, and decide what needs attention before the next handoff.

## Signals in plain English

- `unknown-owner` (high): doc owner missing. Fix: assign documentation owner.
- `stale-doc` (medium): doc appears stale. Fix: review and update doc.
- `no-review` (low): review cadence missing. Fix: add review cadence.

## Input and report

The reader accepts text, JSON, JSONL, or CSV. The default report is readable in a terminal or pull request; `--json` keeps the same findings available to automation.

## Demo

```bash
git clone https://github.com/mertefekurt/docs-freshness-check.git
cd docs-freshness-check
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
docs-freshness-check examples/sample.txt
docs-freshness-check examples/sample.txt --json
```

## Sanity checks

```bash
ruff check .
pytest
python -m docs_freshness_check --help
```
