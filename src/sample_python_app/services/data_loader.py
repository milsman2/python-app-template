"""Handles loading and validating weather.gov astronomical data from file and API."""

import httpx
from pydantic import ValidationError

from sample_python_app.core import setup_logger
from sample_python_app.models import (
    AstronomicalData,
    ForecastFeature,
    WeatherGovFeature,
)


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
    headers = {"User-Agent": "(milsman2, milsman2@gmail.com)"}
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


def fetch_hourly_forecast_from_api(lat: float, lon: float) -> ForecastFeature:
    """Fetch hourly forecast Feature for the given coordinates.

    This function first queries the `/points/{lat},{lon}` endpoint to resolve
    the appropriate grid URL, then requests the hourly forecast and validates
    it against `ForecastFeature`.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.

    Returns:
        ForecastFeature: Parsed and validated hourly forecast feature.

    Raises:
        httpx.HTTPError: If an HTTP request fails.
        ValidationError: If the response fails pydantic validation.

    """
    logger = setup_logger(mode="silent")
    headers = {"User-Agent": "(milsman2, milsman2@gmail.com)"}

    # Resolve point metadata to find the hourly forecast URL
    points_url = f"https://api.weather.gov/points/{lat},{lon}"
    logger.info(f"Resolving grid for coordinates {lat},{lon}: {points_url}")
    resp = httpx.get(points_url, headers=headers)
    resp.raise_for_status()
    points_data = resp.json()

    point_model = WeatherGovFeature.model_validate(points_data)
    forecast_url = point_model.properties.forecast_hourly
    logger.info(f"Fetching hourly forecast from: {forecast_url}")

    resp2 = httpx.get(forecast_url, headers=headers)
    resp2.raise_for_status()
    forecast_data = resp2.json()

    forecast_model = ForecastFeature.model_validate(forecast_data)
    logger.info("Hourly forecast fetched and validated.")
    return forecast_model


def fetch_hourly_forecast_by_grid(
    grid_id: str, grid_x: int, grid_y: int
) -> ForecastFeature:
    """Fetch hourly forecast Feature directly from grid coordinates.

    Builds the gridpoints URL (for example `HGX/59,98`) and fetches the
    hourly forecast Feature at
    `/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly`.

    Args:
        grid_id: Grid identifier (e.g. "HGX").
        grid_x: Grid X coordinate (e.g. 59).
        grid_y: Grid Y coordinate (e.g. 98).

    Returns:
        ForecastFeature: Parsed and validated hourly forecast feature.

    """
    logger = setup_logger(mode="silent")
    headers = {"User-Agent": "(milsman2, milsman2@gmail.com)"}

    url = (
        "https://api.weather.gov/gridpoints/ "
        f"{grid_id}/{grid_x},{grid_y}/forecast/hourly"
    )
    logger.info(f"Fetching hourly forecast by grid from: {url}")
    resp = httpx.get(url, headers=headers)
    resp.raise_for_status()
    data = resp.json()

    model = ForecastFeature.model_validate(data)
    logger.info("Hourly forecast (grid) fetched and validated.")
    return model
