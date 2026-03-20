"""Tests for the forecast GeoJSON Pydantic models.

Assumes Pydantic v2 and that `ForecastFeature.model_validate` is available.
"""

import json
from datetime import datetime

from sample_python_app.models import ForecastFeature


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
