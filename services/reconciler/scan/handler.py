"""Python Lambda stub for scan.
Responsibilities:
- Scan for stuck processing, orphaned OpenAI files, and incomplete deletes.
Failure modes:
- Raises KnownError for expected failures and returns structured error codes.
- Raises Exception for unexpected failures to trigger retries.
"""
from __future__ import annotations

from .service import Service
from .errors import KnownError


def handler(event, context):
    """Entry point for scan."""
    service = Service()
    try:
        return service.handle(event)
    except KnownError as exc:
        return exc.to_response()
