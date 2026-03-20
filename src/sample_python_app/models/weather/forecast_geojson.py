"""Pydantic models for hourly forecast GeoJSON returned by weather.gov."""

from datetime import datetime
from typing import Annotated, Any

from pydantic import BaseModel, Field

from sample_python_app.models.weather.weather_common import UnitAndValue

# Model for the @context field in GeoJSON-LD
ContextType = Annotated[list[str | dict[str, Any]], Field(alias="@context")]


class PolygonGeometry(BaseModel):
    """Polygon geometry (GeoJSON) for forecast area."""

    type: str
    coordinates: list[list[list[float]]]


class Period(BaseModel):
    """Individual forecast period with detailed weather information."""

    number: int
    name: str
    start_time: Annotated[datetime, Field(..., alias="startTime")]
    end_time: Annotated[datetime, Field(..., alias="endTime")]
    is_daytime: Annotated[bool, Field(..., alias="isDaytime")]
    temperature: Annotated[int | None, Field(default=None)]
    temperature_unit: Annotated[
        str | None, Field(default=None, alias="temperatureUnit")
    ]
    temperature_trend: Annotated[
        Any | None, Field(default=None, alias="temperatureTrend")
    ]
    probability_of_precipitation: Annotated[
        UnitAndValue | None, Field(default=None, alias="probabilityOfPrecipitation")
    ]
    dewpoint: Annotated[UnitAndValue | None, Field(default=None)]
    relative_humidity: Annotated[
        UnitAndValue | None, Field(default=None, alias="relativeHumidity")
    ]
    wind_speed: Annotated[str | None, Field(default=None, alias="windSpeed")]
    wind_direction: Annotated[str | None, Field(default=None, alias="windDirection")]
    icon: Annotated[str | None, Field(default=None)]
    short_forecast: Annotated[str | None, Field(default=None, alias="shortForecast")]
    detailed_forecast: Annotated[
        str | None, Field(default=None, alias="detailedForecast")
    ]


class ForecastProperties(BaseModel):
    """Properties of the forecast GeoJSON feature."""

    units: str
    forecast_generator: Annotated[str, Field(..., alias="forecastGenerator")]
    generated_at: Annotated[datetime, Field(..., alias="generatedAt")]
    update_time: Annotated[datetime, Field(..., alias="updateTime")]
    valid_times: str = Field(..., alias="validTimes")
    elevation: UnitAndValue
    periods: list[Period]


class ForecastFeature(BaseModel):
    """Root model for forecast GeoJSON Feature."""

    context: ContextType
    type: str
    geometry: PolygonGeometry
    properties: ForecastProperties
