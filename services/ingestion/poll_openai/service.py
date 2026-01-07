from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for poll_openai.

    Responsibilities:
    - Poll OpenAI processing until ready or timeout.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Poll OpenAI processing until ready or timeout..
        return OutputSchema.success(payload)
