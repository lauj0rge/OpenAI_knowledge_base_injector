"""Python Lambda stub for prechunk_dispatch.
Responsibilities:
- Dispatch ECS pre-chunk tasks for large files.
Failure modes:
- Raises KnownError for expected failures and returns structured error codes.
- Raises Exception for unexpected failures to trigger retries.
"""
from __future__ import annotations

from .service import Service
from .errors import KnownError


def handler(event, context):
    """Entry point for prechunk_dispatch."""
    service = Service()
    try:
        return service.handle(event)
    except KnownError as exc:
        return exc.to_response()
