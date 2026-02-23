"""Main configuration file for the API."""

from zoneinfo import ZoneInfo

from pydantic_extra_types.coordinate import Coordinate, Latitude, Longitude
from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import SecretStr


class WeatherSettings(BaseSettings):
    """Weather-related settings."""

    LOCATION: Coordinate = Coordinate(Latitude(29.8469), Longitude(-95.4689))

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
