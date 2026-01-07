from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for normalize_event.

    Responsibilities:
    - Normalize and enrich raw ingestion events for idempotent processing.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Normalize and enrich raw ingestion events for idempotent processing..
        return OutputSchema.success(payload)
