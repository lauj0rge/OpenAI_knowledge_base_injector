from __future__ import annotations


class InputSchema:
    """Validates input payloads for deterministic behavior."""

    @staticmethod
    def validate(payload: dict) -> None:
        if not isinstance(payload, dict):
            raise ValueError("payload must be a dict")


class OutputSchema:
    """Standard response wrapper to keep state machine contracts stable."""

    @staticmethod
    def success(payload: dict) -> dict:
        return {"status": "ok", "payload": payload}
