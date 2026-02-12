"""
Handles loading and validating weather.gov astronomical data from file.
"""

from pydantic import ValidationError

from sample_python_app.core import setup_logger
from sample_python_app.models import WeatherGovFeature
import httpx


def fetch_astronomical_data_from_api(lat: float, lon: float):
    logger = setup_logger(mode="silent")
    url = f"https://api.weather.gov/points/{lat},{lon}"
    headers = {"User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"}
    try:
        response = httpx.get(url, headers=headers)
        response.raise_for_status()
        data = response.json()
        model = WeatherGovFeature.model_validate(data)
        astro = model.properties.astronomical_data
        logger.info("AstronomicalData fetched and validated from API.")
        return astro
    except ValidationError as e:
        logger.error(f"Data validation error: {e}")
        raise
    except httpx.HTTPError as e:
        logger.error(f"Failed to fetch or validate data from API: {e}")
        raise
