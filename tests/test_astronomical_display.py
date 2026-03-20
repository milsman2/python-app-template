"""Tests for astronomical data display functionality.

Uses sample file and real API call.
"""

import json
from pathlib import Path

import httpx

from sample_python_app.app.scheduler import start_scheduler
from sample_python_app.models import WeatherPointDataFeature


def test_display_with_sample_file(capsys):
    """Test display of astronomical data from sample file."""
    sample_path = (
        Path(__file__).parent.parent
        / "data"
        / "weather"
        / "current_conditions_sample.json"
    )
    with open(sample_path, encoding="utf-8") as f:
        data = json.load(f)
    model = WeatherPointDataFeature.model_validate(data)
    astro = model.properties.astronomical_data
    assert astro.sunrise is not None
    # Use scheduler in test mode to avoid infinite loop
    start_scheduler(test_mode=True)
    out = capsys.readouterr().out
    # Check for synthwave dashboard box-drawing header
    assert "Synthwave" in out


def test_display_with_real_api(capsys):
    """Test display of astronomical data from real API call."""
    url = "https://api.weather.gov/points/29.8469,-95.4689"
    response = httpx.get(
        url, headers={"User-Agent": "(myweatherapp.com, contact@myweatherapp.com)"}
    )
    assert response.status_code == 200
    data = response.json()
    model = WeatherPointDataFeature.model_validate(data)
    astro = model.properties.astronomical_data
    assert astro.sunrise is not None
    # Use scheduler in test mode to avoid infinite loop and NameError
    start_scheduler(test_mode=True)
    out = capsys.readouterr().out
    assert "Synthwave" in out
