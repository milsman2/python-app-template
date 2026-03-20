"""Common models for weather.gov API response parsing."""

from datetime import datetime
from typing import Annotated
from zoneinfo import ZoneInfo

from pydantic import BaseModel, Field


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


class UnitAndValue(BaseModel):
    """Represents a distance value with unit code."""

    unit_code: Annotated[str, Field(..., alias="unitCode")]
    value: float
