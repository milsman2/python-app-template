"""Main entry point for weather.gov astronomical data display.

Orchestrates loading and displaying astronomical data.
"""

import json
import sys

import httpx
from pydantic import ValidationError

from sample_python_app.core import (
    display_astronomical_data,
    setup_logger,
    weather_settings,
)
from sample_python_app.services import fetch_astronomical_data_from_api

logger = setup_logger(mode="silent")


def run_app():
    """Run the application."""
    lat, lon = weather_settings.LOCATION.latitude, weather_settings.LOCATION.longitude
    logger.info(f"Using input latitude: {lat}, longitude: {lon}")
    try:
        astro = fetch_astronomical_data_from_api(lat, lon)
    except httpx.HTTPStatusError as e:
        logger.error(f"HTTP status error: {e}")
        sys.exit(1)
    except httpx.RequestError as e:
        logger.error(f"Network error: {e}")
        sys.exit(1)
    except ValidationError as e:
        logger.error(f"Validation error: {e}")
        sys.exit(1)
    except json.JSONDecodeError as e:
        logger.error(f"JSON decode error: {e}")
        sys.exit(1)
    display_astronomical_data(astro)


if __name__ == "__main__":  # pragma: no cover
    run_app()
