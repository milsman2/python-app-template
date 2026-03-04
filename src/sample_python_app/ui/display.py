"""Handles formatting and displaying astronomical data using rich and pyfiglet."""

from sample_python_app.core import settings, setup_logger
from sample_python_app.models import AstronomicalData, ForecastFeature

from .synthwave import synthwave_dashboard


def display_astronomical_data(astro: AstronomicalData, forecast: ForecastFeature):
    """Display astronomical and hourly forecast data.

    Combined synthwave dashboard will be shown.
    """
    logger = setup_logger("normal")
    # Log plain-text summary for testability
    tz = settings.tz
    time_fmt = "%I:%M %p %Z"
    events = astro.formatted(tz, time_fmt)
    summary_keys = [
        "sunrise",
        "sunset",
        "astronomical_twilight_begin",
        "astronomical_twilight_end",
    ]
    for key in summary_keys:
        value = events.get(key)
        if value:
            label = key.replace("_", " ").title()
            logger.info(f"{label}: {value}")
    synthwave_dashboard(astro, forecast, settings)
