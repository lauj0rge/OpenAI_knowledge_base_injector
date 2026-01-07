"""Python Lambda stub for command_ledger.
Responsibilities:
- Create or reject command ledger entries using conditional writes for idempotency.
Failure modes:
- Raises KnownError for expected failures and returns structured error codes.
- Raises Exception for unexpected failures to trigger retries.
"""
from __future__ import annotations

from .service import Service
from .errors import KnownError


def handler(event, context):
    """Entry point for command_ledger."""
    service = Service()
    try:
        return service.handle(event)
    except KnownError as exc:
        return exc.to_response()
