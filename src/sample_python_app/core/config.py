"""
Main configuration file for the API
"""

from zoneinfo import ZoneInfo

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """Application settings display."""

    APP_NAME: str = "python-app-template"
    DATE_FORMAT: str = "%Y-%m-%d %I:%M:%S %p %Z"
    TIMEZONE: str = "America/Chicago"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        case_sensitive=False,
    )

    @property
    def tz(self) -> ZoneInfo:
        return ZoneInfo(self.TIMEZONE)


settings = Settings()
