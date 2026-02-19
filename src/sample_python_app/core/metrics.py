"""Prometheus metrics for astronomical data fetches."""

from prometheus_client import Counter, Histogram, start_http_server

FETCH_COUNTER = Counter(
    "astro_fetch_total",
    "Total number of astronomical data fetches",
)
FETCH_ERRORS = Counter(
    "astro_fetch_errors_total",
    "Total number of astronomical data fetch errors",
)
FETCH_DURATION = Histogram(
    "astro_fetch_duration_seconds",
    "Duration of astronomical data fetches in seconds",
)

__all__ = [
    "FETCH_COUNTER",
    "FETCH_ERRORS",
    "FETCH_DURATION",
    "start_http_server",
]
