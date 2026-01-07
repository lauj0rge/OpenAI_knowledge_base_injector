from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for notify.

    Responsibilities:
    - Publish notifications without blocking ingestion completion.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Publish notifications without blocking ingestion completion..
        return OutputSchema.success(payload)
