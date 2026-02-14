"""Pydantic models for weather.gov API response.

including astronomical data utilities.
"""

from datetime import datetime
from typing import Annotated, Any
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field


class Distance(BaseModel):
    """Represents a distance value with unit code."""

    unit_code: Annotated[str, Field(..., alias="unitCode")]
    value: float


class Bearing(BaseModel):
    """Represents a bearing value with unit code."""

    unit_code: Annotated[str, Field(..., alias="unitCode")]
    value: float


class RelativeLocationProperties(BaseModel):
    """Properties for a relative location including.

    city, state, distance, and bearing.
    """

    city: str
    state: str
    distance: Distance
    bearing: Bearing


class RelativeLocationGeometry(BaseModel):
    """Geometry for a relative location (type and coordinates)."""

    type: str
    coordinates: list[float]


class RelativeLocation(BaseModel):
    """Relative location feature with geometry and properties."""

    type: str
    geometry: RelativeLocationGeometry
    properties: RelativeLocationProperties


class AstronomicalData(BaseModel):
    """Astronomical event times for a given location.

    With timezone conversion and formatting methods.
    """

    sunrise: datetime
    sunset: datetime
    transit: datetime
    civil_twilight_begin: Annotated[datetime, Field(..., alias="civilTwilightBegin")]
    civil_twilight_end: Annotated[datetime, Field(..., alias="civilTwilightEnd")]
    nautical_twilight_begin: Annotated[
        datetime, Field(..., alias="nauticalTwilightBegin")
    ]
    nautical_twilight_end: Annotated[datetime, Field(..., alias="nauticalTwilightEnd")]
    astronomical_twilight_begin: Annotated[
        datetime, Field(..., alias="astronomicalTwilightBegin")
    ]
    astronomical_twilight_end: Annotated[
        datetime, Field(..., alias="astronomicalTwilightEnd")
    ]

    def as_local(self, tz: ZoneInfo) -> dict[str, datetime]:
        """Return astronomical event times converted to the given timezone."""
        return {name: value.astimezone(tz) for name, value in self.__dict__.items()}

    def formatted(self, tz: ZoneInfo, fmt: str) -> dict[str, str]:
        """Return formatted astronomical event times as strings.

        For the given timezone and format.
        """
        return {name: dt.strftime(fmt) for name, dt in self.as_local(tz).items()}


class NWR(BaseModel):
    """NOAA Weather Radio transmitter info."""

    transmitter: str
    same_code: Annotated[str, Field(..., alias="sameCode")]
    area_broadcast: Annotated[str, Field(..., alias="areaBroadcast")]
    point_broadcast: Annotated[str, Field(..., alias="pointBroadcast")]


class Properties(BaseModel):
    """Top-level properties for a weather.gov point feature."""

    id: Annotated[str, Field(..., alias="@id")]
    type_: Annotated[str, Field(..., alias="@type")]
    cwa: str
    type: str
    forecast_office: Annotated[str, Field(..., alias="forecastOffice")]
    grid_id: Annotated[str, Field(..., alias="gridId")]
    grid_x: Annotated[int, Field(..., alias="gridX")]
    grid_y: Annotated[int, Field(..., alias="gridY")]
    forecast: Annotated[str, Field(..., alias="forecast")]
    forecast_hourly: Annotated[str, Field(..., alias="forecastHourly")]
    forecast_grid_data: Annotated[str, Field(..., alias="forecastGridData")]
    observation_stations: Annotated[str, Field(..., alias="observationStations")]
    relative_location: Annotated[RelativeLocation, Field(..., alias="relativeLocation")]
    forecast_zone: Annotated[str, Field(..., alias="forecastZone")]
    county: str
    fire_weather_zone: Annotated[str, Field(..., alias="fireWeatherZone")]
    time_zone: Annotated[str, Field(..., alias="timeZone")]
    radar_station: Annotated[str, Field(..., alias="radarStation")]
    astronomical_data: Annotated[AstronomicalData, Field(..., alias="astronomicalData")]
    nwr: NWR


class Geometry(BaseModel):
    """Geometry for a weather.gov feature (type and coordinates)."""

    type: str
    coordinates: list[float]


class WeatherGovFeature(BaseModel):
    """Root model for weather.gov point feature response."""

    context: Annotated[list[Any], Field(..., alias="@context")]
    id: str
    type: str
    geometry: Geometry
    properties: Properties
