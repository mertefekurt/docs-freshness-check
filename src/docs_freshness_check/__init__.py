"""Public API for docs-freshness-check."""

from docs_freshness_check.core import audit_records, read_records
from docs_freshness_check.models import AuditReport, Finding, Rule

__all__ = ["AuditReport", "Finding", "Rule", "audit_records", "read_records"]
__version__ = "0.1.0"
