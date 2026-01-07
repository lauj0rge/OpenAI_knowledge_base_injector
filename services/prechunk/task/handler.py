"""ECS task entry for deterministic pre-chunking.
Responsibilities:
- Deterministically chunk large files for ingestion.
Failure modes:
- Raises Exception for unexpected failures to allow retries.
"""
from __future__ import annotations


def handler(event=None, context=None):
    """Entry point for prechunk task."""
    return {"status": "ok", "message": "not implemented"}
