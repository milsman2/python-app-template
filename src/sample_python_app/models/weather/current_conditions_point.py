"""Model for weather.gov current_conditions_sample.json point metadata response."""

from typing import Annotated, Any

from pydantic import BaseModel, Field

from sample_python_app.models.weather.weather_common import NWR, AstronomicalData


class RelativeLocationProperties(BaseModel):
    """Properties for a relative location."""

    city: Annotated[str, Field(default="")]
    state: Annotated[str, Field(default="")]
    distance: dict[str, Any]
    bearing: dict[str, Any]


class RelativeLocation(BaseModel):
    """Relative location feature with geometry and properties."""

    type: Annotated[str, Field(default="")]
    geometry: Annotated[dict[str, Any], Field(default_factory=dict)]
    properties: RelativeLocationProperties


class CurrentConditionsProperties(BaseModel):
    """Top-level properties for a weather.gov point feature."""

    id_: Annotated[str, Field(..., alias="@id")]
    type_: Annotated[str, Field(..., alias="@type")]
    cwa: str
    type: str
    forecast_office: Annotated[str, Field(..., alias="forecastOffice")]
    grid_id: Annotated[str, Field(..., alias="gridId")]
    grid_x: Annotated[int, Field(default=0, alias="gridX")]
    grid_y: Annotated[int, Field(default=0, alias="gridY")]
    forecast: Annotated[str, Field(...)]
    forecast_hourly: Annotated[str, Field(..., alias="forecastHourly")]
    forecast_grid_data: Annotated[str, Field(..., alias="forecastGridData")]
    observation_stations: Annotated[str, Field(..., alias="observationStations")]
    relative_location: Annotated[
        RelativeLocation,
        Field(..., alias="relativeLocation"),
    ]
    forecast_zone: Annotated[str, Field(..., alias="forecastZone")]
    county: Annotated[str, Field(...)]
    fire_weather_zone: Annotated[str, Field(..., alias="fireWeatherZone")]
    time_zone: Annotated[str, Field(..., alias="timeZone")]
    radar_station: Annotated[str, Field(..., alias="radarStation")]
    astronomical_data: Annotated[
        AstronomicalData,
        Field(..., alias="astronomicalData"),
    ]
    nwr: Annotated[NWR, Field(..., alias="nwr")]


class CurrentConditionsFeature(BaseModel):
    """Feature model for current conditions point metadata."""

    context: Annotated[Any, Field(alias="@context")]
    id: str
    type: str
    geometry: Annotated[dict[str, Any], Field(default_factory=dict)]
    properties: CurrentConditionsProperties
