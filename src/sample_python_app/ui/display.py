"""Handles formatting and displaying astronomical data using rich and pyfiglet."""

from sample_python_app.core.config import settings
from sample_python_app.models import AstronomicalData, ForecastFeature

from .synthwave import synthwave_dashboard


def display_astronomical_data(astro: AstronomicalData, forecast: ForecastFeature):
    """Display astronomical and hourly forecast data.

    Combined synthwave dashboard will be shown.
    """
    synthwave_dashboard(astro, forecast, settings)
