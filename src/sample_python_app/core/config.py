"""
Main configuration file for the API
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    """
    Settings
    """

    APP_NAME: str = "python-app-template"

    model_config = SettingsConfigDict(
        env_file_encoding="utf-8",
        env_file=[".env"],
    )


settings = Settings()
