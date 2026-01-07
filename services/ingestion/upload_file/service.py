from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for upload_file.

    Responsibilities:
    - Upload files or chunks to OpenAI in a deterministic order.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Upload files or chunks to OpenAI in a deterministic order..
        return OutputSchema.success(payload)
