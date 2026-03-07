"""Prometheus metrics for astronomical data fetches."""

from prometheus_client import Counter, Histogram, start_http_server

FETCH_COUNTER = Counter(
    "fetch_all_total",
    "Total number of astronomical data fetches",
)
FETCH_ERRORS = Counter(
    "fetch_errors_total",
    "Total number of astronomical data fetch errors",
)
FETCH_DURATION = Histogram(
    "fetch_duration_seconds",
    "Duration of astronomical data fetches in seconds",
)
HTTP_REQUESTS = Counter(
    "http_requests_total",
    "Total HTTP requests made",
    ["method", "host", "path", "status_code"],
)
HTTP_REQUEST_EXCEPTIONS = Counter(
    "http_request_exceptions_total",
    "Total HTTP request exceptions",
    ["method", "host", "path", "exception_type"],
)
HTTP_REQUEST_DURATION = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "host", "path"],
)
__all__ = [
    "FETCH_COUNTER",
    "FETCH_ERRORS",
    "FETCH_DURATION",
    "HTTP_REQUESTS",
    "HTTP_REQUEST_EXCEPTIONS",
    "HTTP_REQUEST_DURATION",
    "start_http_server",
]
