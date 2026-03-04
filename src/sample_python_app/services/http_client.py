"""Shared HTTP client wrapper for service modules.

Provides a thin wrapper around `httpx.Client` so callers can share
common headers (like `User-Agent`) at instantiation and use a single
session for multiple requests.
"""

from __future__ import annotations

from typing import Any

import httpx

from sample_python_app.core import setup_logger

logger = setup_logger(mode="silent")


class CustomHTTPClient:
    """Simple HTTP client wrapper around httpx.Client.

    Args:
        headers: Optional default headers to include on each request.
        timeout: Request timeout in seconds.

    """

    def __init__(
        self,
        headers: dict | None = None,
        timeout: float = 10.0,
        base_url: str | None = None,
    ) -> None:
        """Initialize the HTTP client wrapper.

        Args:
            headers: Optional default headers to include on each request.
            timeout: Request timeout in seconds.
            base_url: Optional base URL for relative request paths.

        """
        self.headers = headers or {"User-Agent": "(milsman2, milsman2@gmail.com)"}
        client_kwargs: dict = {"headers": self.headers, "timeout": timeout}
        if base_url is not None:
            client_kwargs["base_url"] = base_url
        self._client = httpx.Client(**client_kwargs)

    def get(self, url: str, **kwargs: Any) -> httpx.Response:
        """Perform a GET request and return the Response.

        Accepts either absolute URLs or relative paths when a `base_url` is set.
        """
        logger.info("HTTP GET %s", url)
        return self._client.get(url, **kwargs)

    def get_json(self, url: str, **kwargs: Any) -> Any:
        """GET the given URL and return the parsed JSON body.

        Raises an HTTPStatusError on non-2xx responses.
        """
        # Accept either absolute URLs or relative paths when base_url is set.
        resp = self.get(url, **kwargs)
        resp.raise_for_status()
        return resp.json()

    def close(self) -> None:
        """Close the underlying httpx client."""
        try:
            self._client.close()
        except Exception:
            logger.exception("Error closing HTTP client")

    def __enter__(self) -> CustomHTTPClient:
        """Context manager enter returns the client instance."""
        return self

    def __exit__(self, exc_type, exc, tb) -> None:  # type: ignore[override]
        """Context manager exit closes the underlying client."""
        self.close()
