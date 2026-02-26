"""Runner module for the sample Python app.

Handles fetching, validation, and display of astronomical data.
"""

# app/runner.py
import json
import time
from datetime import date

import httpx
from pydantic import ValidationError

from sample_python_app.core import (
    FETCH_COUNTER,
    FETCH_DURATION,
    FETCH_ERRORS,
    setup_logger,
    weather_settings,
)
from sample_python_app.exceptions import AppError
from sample_python_app.services import fetch_astronomical_data_from_api
from sample_python_app.ui import display_astronomical_data

logger = setup_logger("normal")


class AstroFetcher:
    """Fetches astronomical data and displays only once per day."""

    def __init__(self) -> None:
        """Initialize the AstroFetcher with no last displayed day."""
        self._last_displayed_day: str | None = None

    def fetch(self, *, exit_on_error: bool = True) -> None:
        """Fetch astronomical data and display if it is new day's data."""
        lat = weather_settings.LOCATION.latitude
        lon = weather_settings.LOCATION.longitude
        logger.info(f"Using latitude={lat} longitude={lon}")

        start = time.time()

        try:
            astro = fetch_astronomical_data_from_api(lat, lon)
            FETCH_COUNTER.inc()
        except (
            httpx.HTTPStatusError,
            httpx.RequestError,
            ValidationError,
            json.JSONDecodeError,
            AppError,
        ) as exc:
            self._handle_fetch_error(exc, exit_on_error)
            return
        finally:
            FETCH_DURATION.observe(time.time() - start)

        # Only display once per day
        today_str = date.today().isoformat()
        if self._last_displayed_day != today_str:
            display_astronomical_data(astro)
            self._last_displayed_day = today_str

    def _handle_fetch_error(self, exc: Exception, exit_on_error: bool) -> None:
        """Handle errors during the fetch operation."""
        FETCH_ERRORS.inc()
        if isinstance(exc, httpx.HTTPStatusError):
            logger.error("HTTP status error: %s", exc)
        elif isinstance(exc, httpx.RequestError):
            logger.error("Network error: %s", exc)
        elif isinstance(exc, ValidationError):
            logger.error("Validation error: %s", exc)
        elif isinstance(exc, json.JSONDecodeError):
            logger.error("JSON decode error: %s", exc)
        else:
            logger.exception("Unexpected error")

        if exit_on_error:
            raise SystemExit(1) from exc

        raise AppError(str(exc)) from exc


fetcher = AstroFetcher()
