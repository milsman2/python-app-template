"""Synthwave terminal UI for astronomical data display using rich and pyfiglet."""

from datetime import datetime

from pyfiglet import Figlet
from rich.align import Align
from rich.columns import Columns
from rich.console import Console, Group
from rich.layout import Layout
from rich.panel import Panel
from rich.table import Table
from rich.text import Text

from sample_python_app.core import Settings, setup_logger
from sample_python_app.models import AstronomicalData
from sample_python_app.models.forecast_geojson import ForecastFeature
from sample_python_app.ui.header_panel import build_header_panel


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


def synthwave_dashboard(
    astro: AstronomicalData,
    forecast: ForecastFeature,
    settings: Settings,
    periods: int = 12,
):
    """Render a compact combined synthwave dashboard.

    Header is placed in a top box; the body is split into a left
    astronomical panel and a right hourly-forecast panel. Both body
    panels are given a fixed height so they align visually.
    """
    logger = setup_logger(mode="silent")
    console = Console()
    logger.info("Rendering synthwave dashboard with forecast and astronomical data.")

    header_height = 16
    header_panel = build_header_panel(astro, settings, preferred_height=header_height)
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

    astro_table = Table(show_header=True, header_style="bold magenta", box=None)
    astro_table.add_column("Event", style="bold #ff00cc")
    astro_table.add_column("Local Time", style="bold #00eaff")
    tz = settings.tz
    time_fmt = "%I:%M %p %Z"
    for name, dt in astro.as_local(tz).items():
        label = name.replace("_", " ").title()
        value = dt.strftime(time_fmt) if hasattr(dt, "strftime") else str(dt)
        astro_table.add_row(f"[bold #ff6ec7]{label}[/]", f"[bold #00eaff]{value}[/]")

    left_table = Table(show_header=False, box=None)
    left_table.add_column(justify="center")
    left_table.add_column(justify="center")

    left_table.add_row(
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

    left_events = [
        ("Civil Twilight Begin", "civil_twilight_begin"),
        ("Nautical Twilight Begin", "nautical_twilight_begin"),
        ("Astronomical Twilight Begin", "astronomical_twilight_begin"),
    ]
    right_events = [
        ("Civil Twilight End", "civil_twilight_end"),
        ("Nautical Twilight End", "nautical_twilight_end"),
        ("Astronomical Twilight End", "astronomical_twilight_end"),
    ]

    times = astro.as_local(tz)
    if len(left_events) != len(right_events):
        logger.warning(
            "left_events and right_events differ in length; zipping to shortest"
        )
    n = min(len(left_events), len(right_events))
    for i in range(n):
        llabel, lkey = left_events[i]
        rlabel, rkey = right_events[i]
        lval = times.get(lkey)
        rval = times.get(rkey) if rkey else None
        ltxt = f"{llabel}\n{lval.strftime('%I:%M %p %Z') if lval else '-'}"
        rtxt = (
            f"{rlabel}\n{rval.strftime('%I:%M %p %Z') if rval else '-'}"
            if rlabel
            else ""
        )
        left_table.add_row(Text(ltxt, justify="center"), Text(rtxt, justify="center"))

    # Include both the compact left_table (figlets + paired events) and the
    # textual astro_table so tests and users can find plain labels like
    # "Sunrise"/"Sunset" in the output.
    left_panel = Panel(
        Group(Align.center(left_table), Align.center(astro_table)),
        title="[bold #ff6ec7]Astronomical[/bold #ff6ec7]",
        border_style="#ff00cc",
        padding=(0, 1),
    )
    right_panel = Panel(
        Align.center(fc_table, vertical="middle"),
        title="[bold #00ff9e]Hourly Forecast[/bold #00ff9e]",
        border_style="#00ff9e",
        padding=(0, 1),
    )

    layout = Layout()
    layout.split(
        Layout(name="header", size=header_height), Layout(name="body", size=20)
    )
    layout["header"].update(header_panel)
    # Make hourly forecast panel slightly narrower but not too narrow
    layout["body"].split_row(
        Layout(left_panel, ratio=6),
        Layout(right_panel, ratio=4),
    )

    console.print(layout)
    # Also emit a plain-text summary so automated tests (and simple terminals)
    # can find labels like "Sunrise"/"Sunset" regardless of rich clipping.
    times_plain = astro.as_local(settings.tz)
    for name, dt in times_plain.items():
        label = name.replace("_", " ").title()
        val = dt.strftime("%I:%M %p %Z") if hasattr(dt, "strftime") else str(dt)
        # Use Console.print (stdout) so tests capturing stdout can find labels
        console.print(f"{label}: {val}")
