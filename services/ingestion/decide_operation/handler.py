"""Python Lambda stub for decide_operation.
Responsibilities:
- Determine whether the command is UPLOAD, UPDATE, DELETE, or NOOP.
Failure modes:
- Raises KnownError for expected failures and returns structured error codes.
- Raises Exception for unexpected failures to trigger retries.
"""
from __future__ import annotations

from .service import Service
from .errors import KnownError


def handler(event, context):
    """Entry point for decide_operation."""
    service = Service()
    try:
        return service.handle(event)
    except KnownError as exc:
        return exc.to_response()
