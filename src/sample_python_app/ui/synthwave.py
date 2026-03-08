"""Synthwave terminal UI for astronomical data display using rich and pyfiglet."""

from rich.align import Align
from rich.console import Console
from rich.layout import Layout
from rich.panel import Panel

from sample_python_app.core import Settings, setup_logger
from sample_python_app.models import AstronomicalData, ForecastFeature
from sample_python_app.ui.astro_table import build_astro_table
from sample_python_app.ui.forecast_table import build_forecast_table
from sample_python_app.ui.header_panel import build_header_panel


def synthwave_dashboard(
    astro: AstronomicalData,
    forecast: ForecastFeature,
    settings: Settings,
):
    """Render a compact combined synthwave dashboard.

    Header is placed in a top box; the body is split into a left
    astronomical panel and a right hourly-forecast panel. Both body
    panels are given a fixed height so they align visually.
    """
    logger = setup_logger("SILENT")
    console = Console()
    logger.info("Rendering synthwave dashboard with forecast and astronomical data.")

    header_height = 16
    header_panel = build_header_panel(astro, settings, preferred_height=header_height)

    forecast_table = build_forecast_table(forecast, settings)

    astro_table = build_astro_table(astro, settings)

    left_panel = Panel(
        Align.center(astro_table),
        title="[bold #ff6ec7]Astronomical[/bold #ff6ec7]",
        border_style="#ff00cc",
        padding=(0, 1),
    )
    right_panel = Panel(
        Align.center(forecast_table, vertical="middle"),
        title="[bold #00ff9e]Hourly Forecast[/bold #00ff9e]",
        border_style="#00ff9e",
        padding=(0, 1),
    )

    layout = Layout()
    layout.split(
        Layout(name="header", size=header_height), Layout(name="body", size=20)
    )
    layout["header"].update(header_panel)
    layout["body"].split_row(
        Layout(left_panel, ratio=6),
        Layout(right_panel, ratio=4),
    )

    console.print(layout)
