from __future__ import annotations


class KnownError(Exception):
    """Base class for expected errors with explicit codes for Step Functions."""

    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code
        self.message = message

    def to_response(self) -> dict:
        return {"status": "error", "code": self.code, "message": self.message}


class ValidationError(KnownError):
    """Raised when input payloads are invalid or incomplete."""

    def __init__(self, message: str):
        super().__init__("VALIDATION_ERROR", message)
