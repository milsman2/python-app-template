"""Unit tests for sample_python_app.core.config module.

Covers Settings and WeatherSettings instantiation, properties, and model_config.
"""

from sample_python_app.core.config import settings, weather_settings


def test_settings_fields():
    """Test settings fields for expected values."""
    assert settings.APP_NAME == "python-app-template"
    assert settings.DATE_FORMAT
    assert settings.TIMEZONE


def test_settings_tz_property():
    """Test settings.tz property returns correct timezone."""
    tz = settings.tz
    # ZoneInfo does not have a 'zone' attribute; use 'key' for the timezone name
    assert tz.key == settings.TIMEZONE


def test_weather_settings_location():
    """Test weather_settings.LOCATION returns correct coordinates."""
    loc = weather_settings.LOCATION
    assert loc.latitude == 29.8469
    assert loc.longitude == -95.4689


def test_settings_instantiation_and_model_config():
    """Test explicit instantiation and model config of settings classes."""
    # Explicitly instantiate settings classes
    s = type(settings)()
    ws = type(weather_settings)()
    # Access model_config (should exist and be a dict-like object)
    assert hasattr(s, "model_config")
    assert hasattr(ws, "model_config")
    # Access tz property again for coverage
    assert isinstance(s.tz, type(settings.tz))
