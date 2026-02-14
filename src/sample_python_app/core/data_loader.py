"""Handles loading and validating weather.gov astronomical data from file."""

import httpx
from pydantic import ValidationError

from sample_python_app.core.logging import setup_logger
from sample_python_app.models import AstronomicalData, WeatherGovFeature


def fetch_astronomical_data_from_api(lat: float, lon: float) -> AstronomicalData:
    """Fetch and validate astronomical data from weather.gov API for given coordinates.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.

    Returns:
        AstronomicalData: Validated astronomical data from API response.

    Raises:
        ValidationError: If the API response fails validation.
        httpx.HTTPError: If the API request fails.

    """
    logger = setup_logger(mode="silent")
    url = f"https://api.weather.gov/points/{lat},{lon}"
    headers = {"User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"}
    logger.info(f"Fetching astronomical data from URL: {url}")
    logger.info(f"Request headers: {headers}")
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
