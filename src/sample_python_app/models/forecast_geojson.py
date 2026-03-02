"""Pydantic models for hourly forecast GeoJSON returned by weather.gov."""

from datetime import datetime
from typing import Any

from pydantic import BaseModel, Field

from sample_python_app.models.weather_gov import Distance


class PolygonGeometry(BaseModel):
    """Polygon geometry (GeoJSON) for forecast area."""

    type: str
    coordinates: list[list[list[float]]]


class Period(BaseModel):
    """Individual forecast period with detailed weather information."""

    number: int
    name: str
    start_time: datetime = Field(..., alias="startTime")
    end_time: datetime = Field(..., alias="endTime")
    is_daytime: bool = Field(..., alias="isDaytime")
    temperature: int | None
    temperature_unit: str | None = Field(None, alias="temperatureUnit")
    temperature_trend: Any | None = Field(None, alias="temperatureTrend")
    probability_of_precipitation: Distance | None = Field(
        None, alias="probabilityOfPrecipitation"
    )
    dewpoint: Distance | None
    relative_humidity: Distance | None = Field(None, alias="relativeHumidity")
    wind_speed: str | None = Field(None, alias="windSpeed")
    wind_direction: str | None = Field(None, alias="windDirection")
    icon: str | None
    short_forecast: str | None = Field(None, alias="shortForecast")
    detailed_forecast: str | None = Field(None, alias="detailedForecast")


class ForecastProperties(BaseModel):
    """Properties of the forecast GeoJSON feature."""

    units: str
    forecast_generator: str = Field(..., alias="forecastGenerator")
    generated_at: datetime = Field(..., alias="generatedAt")
    update_time: datetime = Field(..., alias="updateTime")
    valid_times: str = Field(..., alias="validTimes")
    elevation: Distance
    periods: list[Period]


class ForecastFeature(BaseModel):
    """Root model for forecast GeoJSON Feature."""

    context: list[Any] = Field(..., alias="@context")
    type: str
    geometry: PolygonGeometry
    properties: ForecastProperties
