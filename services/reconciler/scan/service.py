from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for scan.

    Responsibilities:
    - Scan for stuck processing, orphaned OpenAI files, and incomplete deletes.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Scan for stuck processing, orphaned OpenAI files, and incomplete deletes..
        return OutputSchema.success(payload)
