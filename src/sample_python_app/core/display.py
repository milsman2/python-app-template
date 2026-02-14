"""Handles formatting and displaying astronomical data using rich and pyfiglet."""

from datetime import datetime

from pyfiglet import Figlet
from rich.align import Align
from rich.console import Console
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from sample_python_app.core.config import settings
from sample_python_app.core.logging import setup_logger


def display_astronomical_data(astro):
    """Format and display astronomical data using rich and pyfiglet.

    Args:
        astro: AstronomicalData object containing sunrise, sunset, and formatted values.

    Returns:
        None

    """
    logger = setup_logger(mode="silent")
    console = Console()
    # Synthwave color palette (no longer used)

    header = Figlet(font="slant", width=120).renderText("SYNTHWAVE SUNRISE 🌅")
    logger.info("Displaying Synthwave Sunrise header.")
    header_text = Text(header)
    header_text.stylize("bold magenta")

    sunrise_local = astro.sunrise.astimezone(settings.tz)
    sunset_local = astro.sunset.astimezone(settings.tz)
    date_art = Figlet(font="mini", width=150).renderText(
        sunrise_local.strftime("%A, %B %d, %Y")
    )
    logger.info(f'Displaying date: {sunrise_local.strftime("%A, %B %d, %Y")})')
    date_text = Text(date_art)
    date_text.stylize("bold cyan")

    # Stylized sunrise/sunset
    sun_art = Figlet(font="starwars", width=120).renderText("SUNRISE")
    sun_set_art = Figlet(font="starwars", width=120).renderText("SUNSET")
    sun_text = Text(sun_art)
    sun_text.stylize("bold yellow")
    # Sunrise time as figlet
    sunrise_time_art = Figlet(font="big", width=100).renderText(
        sunrise_local.strftime("%H:%M:%S")
    )
    sunrise_time_text = Text(sunrise_time_art)
    sunrise_time_text.stylize("bold yellow")

    sun_set_text = Text(sun_set_art)
    sun_set_text.stylize("bold blue")
    # Sunrise time as figlet with AM/PM
    sunrise_time_str = sunrise_local.strftime("%I:%M:%S %p")
    sunrise_time_art = Figlet(font="big", width=100).renderText(sunrise_time_str)
    sunrise_time_text = Text(sunrise_time_art)
    sunrise_time_text.stylize("bold yellow")

    sun_set_text = Text(sun_set_art)
    sun_set_text.stylize("bold blue")
    # Sunset time as figlet with AM/PM
    sunset_time_str = sunset_local.strftime("%I:%M:%S %p")
    sunset_time_art = Figlet(font="big", width=100).renderText(sunset_time_str)
    sunset_time_text = Text(sunset_time_art)
    sunset_time_text.stylize("bold blue")

    astro_table = Table(show_header=True, header_style="bold magenta", box=None)
    astro_table.add_column("Event", style="bold #ff00cc")
    astro_table.add_column("Local Time", style="bold #00eaff")
    tz = settings.tz
    time_fmt = "%I:%M:%S %p %Z"
    # Color mapping for event types
    event_colors = {
        "sunrise": "#ffe066",  # yellow
        "sunset": "#5dade2",  # blue
        "transit": "#ffb347",  # orange
        "civil twilight begin": "#f7cac9",  # pink
        "civil twilight end": "#92a8d1",  # light blue
        "nautical twilight begin": "#f9d423",  # gold
        "nautical twilight end": "#6a89cc",  # purple-blue
        "astronomical twilight begin": "#b388ff",  # violet
        "astronomical twilight end": "#2e86c1",  # deep blue
    }
    for name, dt in astro.as_local(tz).items():
        label = name.replace("_", " ").title()
        if isinstance(dt, datetime):
            value = dt.strftime(time_fmt)
        else:
            value = str(dt)
        logger.info(f"Displaying {label}: {value}")
        # Pick color based on event type
        color = event_colors.get(label.lower(), "#e17055")  # fallback: coral
        astro_table.add_row(
            f"[{color}]{label}[/{color}]", f"[{color}]{value}[/{color}]"
        )

    # Compose all parts into a single renderable for the panel
    from rich.columns import Columns
    from rich.console import Group

    # Combine sunrise and sunset figlet art and times in the same row
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
