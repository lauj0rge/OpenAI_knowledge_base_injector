from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for prechunk_dispatch.

    Responsibilities:
    - Dispatch ECS pre-chunk tasks for large files.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Dispatch ECS pre-chunk tasks for large files..
        return OutputSchema.success(payload)
