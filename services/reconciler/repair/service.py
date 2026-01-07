from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for repair.

    Responsibilities:
    - Repair discrepancies using compensating deletes and retries.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Repair discrepancies using compensating deletes and retries..
        return OutputSchema.success(payload)
