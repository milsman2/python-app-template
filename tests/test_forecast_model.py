"""Tests for the forecast GeoJSON Pydantic models.

Assumes Pydantic v2 and that `ForecastFeature.model_validate` is available.
"""

import json
from datetime import datetime

import pytest

from sample_python_app.models import ForecastFeature


def test_forecast_feature_invalid_type():
    """Test ForecastFeature with invalid type for periods."""
    """Test ForecastFeature with invalid type for periods."""
    data = {
        "@context": [],
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": []},
        "properties": {
            "units": "us",
            "forecastGenerator": "HourlyForecastGenerator",
            "generatedAt": "2026-02-28T02:08:19+00:00",
            "updateTime": "2026-02-28T00:20:49+00:00",
            "validTimes": "2026-02-27T18:00:00+00:00/P7DT19H",
            "elevation": {"unitCode": "wmoUnit:m", "value": 24.0},
            "periods": "notalist",
        },
    }
    from pydantic import ValidationError

    with pytest.raises(ValidationError):
        ForecastFeature.model_validate(data)


def test_forecast_feature_empty_periods():
    """Test ForecastFeature with empty periods list."""
    data = {
        "@context": [],
        "type": "Feature",
        "geometry": {"type": "Polygon", "coordinates": []},
        "properties": {
            "units": "us",
            "forecastGenerator": "HourlyForecastGenerator",
            "generatedAt": "2026-02-28T02:08:19+00:00",
            "updateTime": "2026-02-28T00:20:49+00:00",
            "validTimes": "2026-02-27T18:00:00+00:00/P7DT19H",
            "elevation": {"unitCode": "wmoUnit:m", "value": 24.0},
            "periods": [],
        },
    }
    model = ForecastFeature.model_validate(data)
    assert model.properties.periods == []


def test_forecast_feature_parses_sample_file():
    """Load the sample hourly forecast JSON and validate the model."""
    with open("data/weather/forecast_hourly_sample.json", encoding="utf-8") as fh:
        data = json.load(fh)

    model = ForecastFeature.model_validate(data)
    assert model.properties.forecast_generator == "HourlyForecastGenerator"
    assert model.properties.periods and len(model.properties.periods) > 0

    first = model.properties.periods[0]
    assert isinstance(first.start_time, datetime)
    assert first.temperature is None or isinstance(first.temperature, int)
