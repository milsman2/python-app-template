"""Main configuration file for the API."""

from zoneinfo import ZoneInfo

from pydantic import SecretStr
from pydantic_extra_types.coordinate import Coordinate, Latitude, Longitude
from pydantic_settings import BaseSettings, SettingsConfigDict


class WeatherSettings(BaseSettings):
    """Weather-related settings."""

    LOCATION: Coordinate = Coordinate(Latitude(29.8469), Longitude(-95.4689))
    WEATHER_API_BASE: str = "https://api.weather.gov"
    WEATHER_HEADERS: dict = {"User-Agent": "(milsman2, milsman2@gmail.com)"}

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )


class Settings(BaseSettings):
    """Application settings display."""

    TEST_MODE: bool = False
    APP_NAME: str = "python-app-template"
    DATE_FORMAT: str = "%Y-%m-%d %I:%M:%S %p %Z"
    TIMEZONE: str = "America/Chicago"
    PROMETHEUS_METRICS_PORT: int = 8000
    GF_SECURITY_ADMIN_PASSWORD: SecretStr = SecretStr("admin")
    LOG_LEVEL: str = "INFO"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @property
    def tz(self) -> ZoneInfo:
        """Return the configured timezone info."""
        return ZoneInfo(self.TIMEZONE)


settings = Settings()
weather_settings = WeatherSettings()
