"""Handles loading and validating weather.gov astronomical data from file and API."""

from __future__ import annotations

from pydantic import ValidationError

from sample_python_app.core import setup_logger, weather_settings
from sample_python_app.models import (
    AstronomicalData,
    ForecastFeature,
    WeatherGovFeature,
)
from sample_python_app.services.http_client import CustomHTTPClient

weather_client = CustomHTTPClient(
    headers=weather_settings.WEATHER_HEADERS, base_url=weather_settings.WEATHER_API_BASE
)


def resolve_point_metadata(
    lat: float, lon: float, client: CustomHTTPClient
) -> WeatherGovFeature:
    """Resolve and return the WeatherGovFeature for the given lat/lon.

    This calls the `/points/{lat},{lon}` endpoint and returns the
    validated `WeatherGovFeature` model. Other functions can call this
    to discover grid coordinates or forecast URLs.
    """
    logger = setup_logger(mode="silent")
    api_client = client or weather_client
    points_path = f"/points/{lat},{lon}"
    logger.info(
        "Resolving point metadata for coordinates %s,%s: %s", lat, lon, points_path
    )
    points_data = api_client.get_json(points_path)
    point_model = WeatherGovFeature.model_validate(points_data)
    logger.info(
        "Resolved point metadata: grid=%s x=%s y=%s",
        point_model.properties.grid_id,
        point_model.properties.grid_x,
        point_model.properties.grid_y,
    )
    return point_model


def fetch_astronomical_data_from_api(
    lat: float, lon: float, client: CustomHTTPClient
) -> AstronomicalData:
    """Fetch and validate astronomical data from weather.gov API for given coordinates.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        client (HTTPClient, optional): HTTP client to use for requests. If
            not provided the module-level `weather_client` will be used.

    Returns:
        AstronomicalData: Validated astronomical data from API response.

    Raises:
        ValidationError: If the API response fails validation.
        httpx.HTTPError: If the API request fails.

    """
    logger = setup_logger(mode="silent")
    points_path = f"/points/{lat},{lon}"
    client = client or weather_client
    logger.info("Fetching astronomical data from: %s", points_path)
    try:
        data = client.get_json(points_path)
        model = WeatherGovFeature.model_validate(data)
        astro = model.properties.astronomical_data
        logger.info("AstronomicalData fetched and validated from API.")
        return astro
    except ValidationError as e:
        logger.error("Data validation error: %s", e)
        raise


def fetch_hourly_forecast_from_api(
    lat: float, lon: float, client: CustomHTTPClient
) -> ForecastFeature:
    """Fetch hourly forecast Feature for the given coordinates.

    This function first queries the `/points/{lat},{lon}` endpoint to resolve
    the appropriate grid URL, then requests the hourly forecast and validates
    it against `ForecastFeature`.

    Args:
        lat (float): Latitude of the location.
        lon (float): Longitude of the location.
        client (HTTPClient, optional): HTTP client to use for requests. If
            not provided the module-level `weather_client` will be used.

    Returns:
        ForecastFeature: Parsed and validated hourly forecast feature.

    Raises:
        httpx.HTTPError: If an HTTP request fails.
        ValidationError: If the response fails pydantic validation.

    """
    logger = setup_logger(mode="silent")
    client = client or weather_client

    # Resolve point metadata to find the hourly forecast URL
    point_model = resolve_point_metadata(lat, lon, client=client)
    forecast_url = point_model.properties.forecast_hourly
    logger.info("Fetching hourly forecast from: %s", forecast_url)

    # forecast_url is often an absolute URL returned by the API; httpx
    # client with a base_url accepts absolute URLs as well, so pass through.
    forecast_data = client.get_json(forecast_url)

    forecast_model = ForecastFeature.model_validate(forecast_data)
    logger.info("Hourly forecast fetched and validated.")
    return forecast_model


def fetch_hourly_forecast_by_grid(
    grid_id: str, grid_x: int, grid_y: int, client: CustomHTTPClient
) -> ForecastFeature:
    """Fetch hourly forecast Feature directly from grid coordinates.

    Builds the gridpoints URL (for example `HGX/59,98`) and fetches the
    hourly forecast Feature at
    `/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly`.

    Args:
        grid_id: Grid identifier (e.g. "HGX").
        grid_x: Grid X coordinate (e.g. 59).
        grid_y: Grid Y coordinate (e.g. 98).
        client (HTTPClient, optional): HTTP client to use for requests. If
            not provided the module-level `weather_client` will be used.

    Returns:
        ForecastFeature: Parsed and validated hourly forecast feature.

    """
    logger = setup_logger(mode="silent")
    client = client or weather_client

    path = f"/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly"
    logger.info("Fetching hourly forecast by grid from: %s", path)
    data = client.get_json(path)

    model = ForecastFeature.model_validate(data)
    logger.info("Hourly forecast (grid) fetched and validated.")
    return model
