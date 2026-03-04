"""Runner module for the sample Python app.

Handles fetching, validation, and display of astronomical data.
"""

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
from sample_python_app.services import (
    fetch_astronomical_data_from_api,
    fetch_hourly_forecast_from_api,
)
from sample_python_app.services.http_client import CustomHTTPClient
from sample_python_app.ui import display_astronomical_data

logger = setup_logger("normal")


class AstroFetcher:
    """Fetches astronomical data and displays only once per day.

    Accepts an `HTTPClient` to use for all outbound requests so the
    runner can own the client's lifecycle and tests can inject mocks.
    """

    def __init__(self, client: CustomHTTPClient) -> None:
        """Initialize the AstroFetcher with an optional HTTP client."""
        self._last_displayed_day: str | None = None
        self.client = client

    def fetch(self, *, exit_on_error: bool = True) -> None:
        """Fetch astronomical data and display if not already displayed today."""
        lat = weather_settings.LOCATION.latitude
        lon = weather_settings.LOCATION.longitude
        logger.info(f"Using latitude={lat} longitude={lon}")
        start = time.time()
        try:
            astro = fetch_astronomical_data_from_api(lat, lon, client=self.client)
            forecast = fetch_hourly_forecast_from_api(lat, lon, client=self.client)
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
        today_str = date.today().isoformat()
        if self._last_displayed_day != today_str:
            display_astronomical_data(astro, forecast)
            self._last_displayed_day = today_str

    def reset_display(self):
        """Reset the last displayed day so display will occur again."""
        self._last_displayed_day = None

    def close(self) -> None:
        """Close the associated HTTP client if present.

        This allows the runner to delegate shutdown responsibility to the
        fetcher when it owns the client's lifecycle.
        """
        if hasattr(self, "client") and self.client is not None:
            try:
                self.client.close()
            except Exception:
                logger.exception("Error closing HTTP client in AstroFetcher")

    def _handle_fetch_error(self, exc: Exception, exit_on_error: bool) -> None:
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


runner_client = CustomHTTPClient(
    headers=weather_settings.WEATHER_HEADERS,
    base_url=weather_settings.WEATHER_API_BASE,
)
fetcher = AstroFetcher(client=runner_client)


def shutdown_runner() -> None:
    """Shutdown helper to close long-lived resources owned by the runner.

    Call this from application shutdown hooks to ensure the HTTP client is
    properly closed and connections are released.
    """
    try:
        fetcher.close()
    except Exception:
        logger.exception("Error during runner shutdown")
