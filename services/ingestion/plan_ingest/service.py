from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for plan_ingest.

    Responsibilities:
    - Plan ingestion steps, including pre-chunking decisions for large files.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Plan ingestion steps, including pre-chunking decisions for large files..
        return OutputSchema.success(payload)
