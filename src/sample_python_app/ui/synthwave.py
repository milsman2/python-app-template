"""Synthwave terminal UI for astronomical data display using rich and pyfiglet."""

from datetime import datetime

from pyfiglet import Figlet
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from sample_python_app.core import Settings, setup_logger
from sample_python_app.models import AstronomicalData


def synthwave_display(astro: AstronomicalData, settings: Settings):
    """Display astronomical data in a synthwave terminal UI."""
    logger = setup_logger(mode="silent")
    console = Console()
    logger.info("Rendering synthwave terminal UI for astronomical data.")
    header = Figlet(font="slant", width=120).renderText("SYNTHWAVE SUNRISE 🌅")
    logger.info("Header rendered as figlet art.")
    header_text = Text(header)
    header_text.stylize("bold magenta")

    sunrise_local = astro.sunrise.astimezone(settings.tz)
    sunset_local = astro.sunset.astimezone(settings.tz)
    logger.info(f"Local sunrise: {sunrise_local}, Local sunset: {sunset_local}")
    date_str = sunrise_local.strftime("%A, %B %d, %Y")
    date_art = Figlet(font="mini", width=150).renderText(date_str)
    logger.info(f"Date rendered as figlet: {date_str}")
    date_text = Text(date_art)
    date_text.stylize("bold cyan")

    sun_art = Figlet(font="starwars", width=120).renderText("SUNRISE")
    sun_set_art = Figlet(font="starwars", width=120).renderText("SUNSET")
    sun_text = Text(sun_art)
    sun_text.stylize("bold yellow")
    sunrise_time_str = sunrise_local.strftime("%I:%M:%S %p")
    logger.info(f"Sunrise time (figlet): {sunrise_time_str}")
    sunrise_time_art = Figlet(font="big", width=100).renderText(sunrise_time_str)
    sunrise_time_text = Text(sunrise_time_art)
    sunrise_time_text.stylize("bold yellow")

    sun_set_text = Text(sun_set_art)
    sun_set_text.stylize("bold blue")
    sunset_time_str = sunset_local.strftime("%I:%M:%S %p")
    logger.info(f"Sunset time (figlet): {sunset_time_str}")
    sunset_time_art = Figlet(font="big", width=100).renderText(sunset_time_str)
    sunset_time_text = Text(sunset_time_art)
    sunset_time_text.stylize("bold blue")

    # Table with color-coded events
    astro_table = Table(show_header=True, header_style="bold magenta", box=None)
    astro_table.add_column("Event", style="bold #ff00cc")
    astro_table.add_column("Local Time", style="bold #00eaff")
    tz = settings.tz
    time_fmt = "%I:%M:%S %p %Z"
    event_colors = {
        "sunrise": "#ffe066",
        "sunset": "#5dade2",
        "transit": "#ffb347",
        "civil twilight begin": "#f7cac9",
        "civil twilight end": "#92a8d1",
        "nautical twilight begin": "#f9d423",
        "nautical twilight end": "#6a89cc",
        "astronomical twilight begin": "#b388ff",
        "astronomical twilight end": "#2e86c1",
    }
    for name, dt in astro.as_local(tz).items():
        label = name.replace("_", " ").title()
        if isinstance(dt, datetime):
            value = dt.strftime(time_fmt)
        else:
            value = str(dt)
        color = event_colors.get(label.lower(), "#e17055")
        logger.info(f"Event: {label}, Time: {value}, Color: {color}")
        astro_table.add_row(
            f"[{color}]{label}[/{color}]", f"[{color}]{value}[/{color}]"
        )

    sun_figlet_row = Columns(
        [
            Group(Align.center(sun_text), Align.center(sunrise_time_text)),
            Group(Align.center(sun_set_text), Align.center(sunset_time_text)),
        ],
        align="center",
        expand=True,
    )

    panel_content = Group(
        Align.center(header_text),
        Align.center(date_text),
        sun_figlet_row,
        Align.center(astro_table),
    )
    console.print(
        Panel(
            panel_content,
            title="[bold #ff6ec7]Synthwave Astronomical Events[/bold #ff6ec7]",
            border_style="#ff00cc",
            padding=(1, 2),
        )
    )
