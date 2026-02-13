from sample_python_app.core.config import settings, weather_settings


def test_settings_fields():
    assert settings.APP_NAME == "python-app-template"
    assert settings.DATE_FORMAT
    assert settings.TIMEZONE


def test_settings_tz_property():
    tz = settings.tz
    # ZoneInfo does not have a 'zone' attribute; use 'key' for the timezone name
    assert tz.key == settings.TIMEZONE


def test_weather_settings_location():
    loc = weather_settings.LOCATION
    assert loc.latitude == 29.8469
    assert loc.longitude == -95.4689


def test_settings_instantiation_and_model_config():
    # Explicitly instantiate settings classes
    s = type(settings)()
    ws = type(weather_settings)()
    # Access model_config (should exist and be a dict-like object)
    assert hasattr(s, "model_config")
    assert hasattr(ws, "model_config")
    # Access tz property again for coverage
    assert isinstance(s.tz, type(settings.tz))
