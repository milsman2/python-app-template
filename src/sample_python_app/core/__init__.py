"""Export core modules for use in other modules."""

from sample_python_app.core.config import Settings, settings, weather_settings
from sample_python_app.core.logging import setup_logger
from sample_python_app.core.metrics import (
    FETCH_COUNTER,
    FETCH_DURATION,
    FETCH_ERRORS,
)

__all__ = [
    "settings",
    "weather_settings",
    "setup_logger",
    "Settings",
    "FETCH_COUNTER",
    "FETCH_DURATION",
    "FETCH_ERRORS",
]
