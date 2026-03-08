"""Handles loading and validating weather.gov astronomical data."""

from __future__ import annotations

from datetime import UTC, datetime, timedelta

from pydantic import ValidationError

from sample_python_app.core import (
    FORECAST_NEXT_HOUR_TEMPERATURE,
    weather_settings,
)
from sample_python_app.exceptions import AppError, NetworkError, ServiceError
from sample_python_app.models import (
    AstronomicalData,
    ForecastFeature,
    WeatherGovFeature,
)
from sample_python_app.services.http_client import CustomHTTPClient

weather_client = CustomHTTPClient(
    headers=weather_settings.WEATHER_HEADERS,
    base_url=weather_settings.WEATHER_API_BASE,
)


def resolve_point_metadata(
    lat: float, lon: float, client: CustomHTTPClient | None = None
) -> WeatherGovFeature:
    """Resolve grid metadata for coordinates."""
    client = client or weather_client
    path = f"/points/{lat},{lon}"

    try:
        data = client.get_json(path)
        return WeatherGovFeature.model_validate(data)
    except (NetworkError, ServiceError) as exc:
        raise AppError("Failed to resolve point metadata") from exc
    except ValidationError as exc:
        raise AppError("Invalid metadata returned from weather service") from exc


def fetch_astronomical_data_from_api(
    lat: float,
    lon: float,
    client: CustomHTTPClient | None = None,
) -> AstronomicalData:
    """Fetch astronomical data for coordinates."""
    client = client or weather_client
    path = f"/points/{lat},{lon}"

    try:
        data = client.get_json(path)
        model = WeatherGovFeature.model_validate(data)
        return model.properties.astronomical_data
    except (NetworkError, ServiceError) as exc:
        raise AppError("Weather API request failed") from exc
    except ValidationError as exc:
        raise AppError(
            "Invalid astronomical data returned from weather service"
        ) from exc


def fetch_hourly_forecast_from_api(
    lat: float,
    lon: float,
    client: CustomHTTPClient | None = None,
) -> ForecastFeature:
    """Fetch hourly forecast for coordinates."""
    client = client or weather_client

    try:
        point = resolve_point_metadata(lat, lon, client)
        forecast_url = point.properties.forecast_hourly
        data = client.get_json(forecast_url)
        return ForecastFeature.model_validate(data)
    except (NetworkError, ServiceError) as exc:
        raise AppError("Weather API request failed") from exc
    except ValidationError as exc:
        raise AppError("Invalid forecast returned from weather service") from exc


def fetch_hourly_forecast_by_grid(
    grid_id: str,
    grid_x: int,
    grid_y: int,
    client: CustomHTTPClient | None = None,
) -> ForecastFeature:
    """Fetch hourly forecast using grid coordinates."""
    client = client or weather_client
    path = f"/gridpoints/{grid_id}/{grid_x},{grid_y}/forecast/hourly"

    try:
        data = client.get_json(path)
        return ForecastFeature.model_validate(data)
    except (NetworkError, ServiceError) as exc:
        raise AppError("Weather API request failed") from exc
    except ValidationError as exc:
        raise AppError("Invalid forecast returned from weather service") from exc


def set_next_hour_forecast_temperature(
    forecast: ForecastFeature, location: str = "default"
) -> None:
    """Set the Prometheus metric for the 1-hour-ahead forecast temperature."""
    now = datetime.now(UTC)
    one_hour_later = now + timedelta(hours=1)
    next_period = None
    for period in forecast.properties.periods:
        if period.start_time >= one_hour_later:
            next_period = period
            break
    if next_period and next_period.temperature is not None:
        FORECAST_NEXT_HOUR_TEMPERATURE.labels(location=location).set(
            next_period.temperature
        )
    else:
        FORECAST_NEXT_HOUR_TEMPERATURE.labels(location=location).set(float("nan"))
