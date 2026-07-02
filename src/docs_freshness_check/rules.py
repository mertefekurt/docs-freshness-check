from __future__ import annotations

from docs_freshness_check.models import Rule

PROJECT_NAME = 'docs-freshness-check'
SUMMARY = 'Audit docs inventories for stale owners, old updates, and broken review cadence.'
SAMPLE_RISK = 'doc api-auth owner unknown updated 2023 review none'
SAMPLE_CLEAN = 'doc api-auth owner dx updated 2026 review quarterly'
TEXT_FIELDS = ("text", "content", "description", "summary", "body", "notes", "message")
SUBJECT_FIELDS = ("id", "name", "path", "service", "endpoint", "field", "event")

RULES = (
    Rule(
        code='unknown-owner',
        severity='high',
        pattern='owner\\s+(unknown|none|missing)',
        message='doc owner missing',
        recommendation='assign documentation owner',
    ),
    Rule(
        code='stale-doc',
        severity='medium',
        pattern='updated\\s+20(1[0-9]|2[0-4])',
        message='doc appears stale',
        recommendation='review and update doc',
    ),
    Rule(
        code='no-review',
        severity='low',
        pattern='review\\s+(none|missing|unknown)',
        message='review cadence missing',
        recommendation='add review cadence',
    ),
)
