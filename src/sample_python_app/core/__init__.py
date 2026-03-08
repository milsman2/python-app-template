"""Export core modules for use in other modules."""

from sample_python_app.core.config import Settings, settings, weather_settings
from sample_python_app.core.logging import setup_logger
from sample_python_app.core.metrics import (
    FETCH_COUNTER,
    FETCH_DURATION,
    FETCH_ERRORS,
    FORECAST_NEXT_HOUR_TEMPERATURE,
    HTTP_REQUEST_DURATION,
    HTTP_REQUEST_EXCEPTIONS,
    HTTP_REQUESTS,
)

__all__ = [
    "settings",
    "weather_settings",
    "setup_logger",
    "Settings",
    "FETCH_COUNTER",
    "FETCH_DURATION",
    "FETCH_ERRORS",
    "HTTP_REQUESTS",
    "HTTP_REQUEST_EXCEPTIONS",
    "HTTP_REQUEST_DURATION",
    "FORECAST_NEXT_HOUR_TEMPERATURE",
]
