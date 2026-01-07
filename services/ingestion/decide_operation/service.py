from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for decide_operation.

    Responsibilities:
    - Determine whether the command is UPLOAD, UPDATE, DELETE, or NOOP.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Determine whether the command is UPLOAD, UPDATE, DELETE, or NOOP..
        return OutputSchema.success(payload)
