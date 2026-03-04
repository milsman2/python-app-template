"""Render an astronomical summary table with figlets and times.

This module builds a two-column Rich table containing large figlet
art for sunrise/sunset, followed by an "Event | Local Time" header
row and the corresponding event times converted to the app timezone.
"""

from pyfiglet import Figlet
from rich.align import Align
from rich.console import Group
from rich.table import Table
from rich.text import Text

from sample_python_app.core import Settings
from sample_python_app.models import AstronomicalData


def build_astro_table(astro: AstronomicalData, settings: Settings):
    """Build a rich Table for the astronomical data.

    The table renders large figlets first, then a manual header row
    "Event  |  Local Time" immediately below the figlets so the
    column labels appear under the art.
    """
    astro_table = Table(show_header=False, box=None)

    sunrise_local = astro.sunrise.astimezone(settings.tz)
    sun_art = Figlet(font="small", width=60).renderText("SUNRISE")
    sun_set_art = Figlet(font="small", width=60).renderText("SUNSET")
    sun_text = Text(sun_art, style="bold yellow")
    sun_set_text = Text(sun_set_art, style="bold blue")
    sunrise_time_art = Figlet(font="mini", width=60).renderText(
        sunrise_local.strftime("%I:%M %p")
    )
    sunset_time_art = Figlet(font="mini", width=60).renderText(
        astro.sunset.astimezone(settings.tz).strftime("%I:%M %p")
    )
    sunrise_time_text = Text(sunrise_time_art, style="bold yellow")
    sunset_time_text = Text(sunset_time_art, style="bold blue")

    astro_table.add_row(
        Align(
            Group(Align.center(sun_text), Align.center(sunrise_time_text)),
            align="center",
            vertical="middle",
        ),
        Align(
            Group(Align.center(sun_set_text), Align.center(sunset_time_text)),
            align="center",
            vertical="middle",
        ),
    )

    astro_table.add_row(
        Text("Event", style="bold magenta", justify="center"),
        Text("Local Time", style="bold magenta", justify="center"),
    )

    tz = settings.tz
    time_fmt = "%I:%M %p %Z"
    for name, dt in astro.as_local(tz).items():
        label = name.replace("_", " ").title()
        value = dt.strftime(time_fmt) if hasattr(dt, "strftime") else str(dt)
        astro_table.add_row(f"[bold #ff6ec7]{label}[/]", f"[bold #00eaff]{value}[/]")

    return astro_table
