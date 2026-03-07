"""Custom exceptions for the sample_python_app project."""


class HTTPTimeoutError(Exception):
    """Raised when an HTTP request times out."""

    def __init__(self, message: str) -> None:
        """Initialize the HTTPTimeoutError with a message."""
        super().__init__(message)


class NetworkError(Exception):
    """Raised when a network-level error occurs.

    (connection refused, DNS failure, etc.).
    """

    def __init__(self, message: str) -> None:
        """Initialize the NetworkError with a message."""
        super().__init__(message)


class ServiceError(Exception):
    """Raised when the HTTP response returns an error status (4xx or 5xx)."""

    def __init__(self, status_code: int, body: str | None = None) -> None:
        """Initialize the ServiceError with status code and optional response body."""
        self.status_code = status_code
        self.body = body
        msg = f"Service returned status {status_code}"
        if body:
            msg += f": {body}"
        super().__init__(msg)


class AppError(Exception):
    """Base exception for the application."""

    pass
