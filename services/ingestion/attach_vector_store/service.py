from __future__ import annotations

from .errors import KnownError
from .schema import InputSchema, OutputSchema


class Service:
    """Service layer for attach_vector_store.

    Responsibilities:
    - Attach uploaded files to the OpenAI vector store.
    - Emit deterministic results for idempotent orchestration.
    """

    def handle(self, payload: dict) -> dict:
        InputSchema.validate(payload)
        # TODO: Implement Attach uploaded files to the OpenAI vector store..
        return OutputSchema.success(payload)
