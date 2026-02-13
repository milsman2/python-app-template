"""
Main entry point for weather.gov astronomical data display.
Orchestrates loading and displaying astronomical data.
"""

import json

import httpx
from pydantic import ValidationError

from sample_python_app.core import (
    display_astronomical_data,
    fetch_astronomical_data_from_api,
    weather_settings,
)


def run_app():
    lat, lon = weather_settings.LOCATION.latitude, weather_settings.LOCATION.longitude
    try:
        astro = fetch_astronomical_data_from_api(lat, lon)
    except httpx.HTTPStatusError as e:
        print(f"HTTP error: {e.response.status_code} {e.response.reason_phrase}")
        return
    except httpx.RequestError as e:
        print(f"Network error: {e}")
        return
    except ValidationError as e:
        print(f"Validation error: {e}")
        return
    except json.JSONDecodeError as e:
        print(f"JSON decode error: {e}")
        return
    display_astronomical_data(astro)


if __name__ == "__main__":  # pragma: no cover
    run_app()
