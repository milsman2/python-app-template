"""Runner module for the sample Python app.

Handles fetching, validation, and display of astronomical data.
"""

import time
from datetime import date

from loguru import logger

from sample_python_app.core import (
    FETCH_COUNTER,
    FETCH_DURATION,
    weather_settings,
)
from sample_python_app.exceptions import AppError
from sample_python_app.services import (
    CustomHTTPClient,
    fetch_hourly_forecast_from_api,
    fetch_weather_point_data,
    set_next_hour_forecast_temperature,
)
from sample_python_app.ui import display_astronomical_data


def extract_astronomical_data(weather_point_data):
    """Extract the astronomical data from a WeatherPointDataFeature object."""
    if hasattr(weather_point_data, "properties") and hasattr(
        weather_point_data.properties, "astronomical_data"
    ):
        return weather_point_data.properties.astronomical_data
    raise AttributeError("Input does not have properties.astronomical_data")


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
        """Fetch astronomical data and display if not already shown today."""
        lat = weather_settings.LOCATION.latitude
        lon = weather_settings.LOCATION.longitude

        logger.info("Using latitude={} longitude={}", lat, lon)

        start = time.time()

        try:
            weather_point_data = fetch_weather_point_data(lat, lon, client=self.client)
            forecast = fetch_hourly_forecast_from_api(lat, lon, client=self.client)
            set_next_hour_forecast_temperature(forecast, location=f"{lat},{lon}")
            FETCH_COUNTER.inc()
        except AppError as exc:
            logger.error("Weather fetch failed: {}", exc)
            if exit_on_error:
                raise SystemExit(1) from None
            return
        finally:
            FETCH_DURATION.observe(time.time() - start)

        today = date.today().isoformat()

        if self._last_displayed_day != today:
            astro_data = extract_astronomical_data(weather_point_data)
            display_astronomical_data(astro_data, forecast)
            self._last_displayed_day = today

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


runner_client = CustomHTTPClient(
    headers=weather_settings.WEATHER_HEADERS,
    base_url=weather_settings.WEATHER_API_BASE,
)
fetcher = AstroFetcher(client=runner_client)


def shutdown_runner() -> None:
    """Shutdown helper to close long-lived resources owned by the runner.

    Call this from application shutdown hooks to ensure the HTTP client is
    properly closed and resources are released.
    """
    fetcher.close()
