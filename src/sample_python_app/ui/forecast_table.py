"""Module for building a rich Table to display forecast data."""

from rich.table import Table

from sample_python_app.core import Settings
from sample_python_app.models.forecast_geojson import ForecastFeature


def build_forecast_table(forecast: ForecastFeature, settings: Settings, periods=12):
    """Build a rich Table for the hourly forecast data."""
    fc_table = Table(show_header=True, header_style="bold magenta", box=None)
    fc_table.add_column("Time", style="bold #00eaff")
    fc_table.add_column("T", style="bold #ffdd57")
    fc_table.add_column("POP", style="bold #ff6ec7")
    fc_table.add_column("Wind", style="bold #00ff9e")
    fc_table.add_column("Short", style="bold #ffffff")

    count = 0
    for p in forecast.properties.periods:
        if count >= periods:
            break
        t = p.start_time.astimezone(settings.tz).strftime("%I %p")
        temp = (
            f"{p.temperature}°{p.temperature_unit or ''}"
            if p.temperature is not None
            else "-"
        )
        pop = (
            f"{int(p.probability_of_precipitation.value)}%"
            if p.probability_of_precipitation
            and p.probability_of_precipitation.value is not None
            else "-"
        )
        wind = p.wind_speed or "-"
        short = p.short_forecast or ""
        fc_table.add_row(t, temp, pop, wind, short)
        count += 1
    return fc_table
