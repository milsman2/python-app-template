"""HTTP client abstraction for making requests with metrics and error handling."""

from __future__ import annotations

import time
from types import TracebackType
from typing import Any

import httpx
from loguru import logger

from sample_python_app.core import (
    HTTP_REQUEST_DURATION,
    HTTP_REQUEST_EXCEPTIONS,
    HTTP_REQUESTS,
)
from sample_python_app.exceptions import HTTPTimeoutError, NetworkError, ServiceError

JSONType = dict[str, object] | list[dict[str, object]]


class CustomHTTPClient:
    """HTTP client wrapper around httpx.Client."""

    def __init__(
        self,
        headers: dict | None = None,
        timeout: float = 10.0,
        base_url: str | None = None,
    ) -> None:
        """Initialize the CustomHTTPClient with optional headers, timeout, and base URL.

        Args:
            headers (dict, optional): HTTP headers to include in requests.
            timeout (float, optional): Request timeout in seconds. Defaults to 10.0.
            base_url (str, optional): Base URL for all requests. Defaults to None.

        """
        client_kwargs: dict[str, Any] = {
            "headers": headers or {"User-Agent": "sample-python-app"},
            "timeout": timeout,
        }

        if base_url:
            client_kwargs["base_url"] = base_url

        self._client = httpx.Client(**client_kwargs)
        self._host_label = "weather_api"
        self._last_response: httpx.Response | None = None

    def request_json(self, method: str, url: str, **kwargs: Any) -> JSONType:
        """Perform HTTP request and return parsed JSON."""
        path = url if url.startswith("/") else "/" + url
        start_time = time.time()

        try:
            response = self._client.request(method, url, **kwargs)
            self._last_response = response
        except httpx.TimeoutException as exc:
            HTTP_REQUEST_EXCEPTIONS.labels(
                method=method,
                host=self._host_label,
                path=path,
                exception_type="TimeoutException",
            ).inc()
            raise HTTPTimeoutError(str(exc)) from exc
        except httpx.RequestError as exc:
            HTTP_REQUEST_EXCEPTIONS.labels(
                method=method,
                host=self._host_label,
                path=path,
                exception_type=type(exc).__name__,
            ).inc()
            raise NetworkError(str(exc)) from exc

        duration = time.time() - start_time

        HTTP_REQUEST_DURATION.labels(
            method=method,
            host=self._host_label,
            path=path,
        ).observe(duration)
        HTTP_REQUESTS.labels(
            method=method,
            host=self._host_label,
            path=path,
            status_code=str(response.status_code),
        ).inc()

        full_url = str(response.request.url) if hasattr(response, "request") else url
        logger.info(
            "HTTP {method} {full_url} responded with status code "
            "{status_code} in {duration:.2f}s",
            method=method,
            full_url=full_url,
            status_code=response.status_code,
            duration=duration,
        )

        if not response.is_success:
            logger.error(
                "HTTP error status code: {}," "response body: {}",
                response.status_code,
                response.text,
            )
            logger.debug("HTTP error response body: {}", response.text)
            raise ServiceError(
                status_code=response.status_code,
                body=response.text,
            )

        try:
            return response.json()
        except ValueError as exc:
            raise ServiceError(
                status_code=response.status_code,
                body="Invalid JSON response",
            ) from exc

    def get_json(self, url: str, **kwargs: Any) -> JSONType:
        """Return parsed JSON from a GET request."""
        return self.request_json("GET", url, **kwargs)

    def close(self) -> None:
        """Close the underlying HTTP client."""
        self._client.close()

    def __enter__(self) -> CustomHTTPClient:
        """Support context manager entry."""
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        """Support context manager exit by closing the client."""
        self.close()
