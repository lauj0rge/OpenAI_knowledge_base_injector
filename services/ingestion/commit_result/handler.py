"""Python Lambda stub for commit_result.
Responsibilities:
- Commit final status to DynamoDB and write tombstones for deletes.
Failure modes:
- Raises KnownError for expected failures and returns structured error codes.
- Raises Exception for unexpected failures to trigger retries.
"""
from __future__ import annotations

from .service import Service
from .errors import KnownError


def handler(event, context):
    """Entry point for commit_result."""
    service = Service()
    try:
        return service.handle(event)
    except KnownError as exc:
        return exc.to_response()
