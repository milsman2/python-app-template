"""
Handles formatting and displaying astronomical data using rich and pyfiglet.
"""

from pyfiglet import Figlet
from rich.console import Console

from sample_python_app.core import settings, setup_logger


def display_astronomical_data(astro):
    logger = setup_logger(mode="silent")
    console = Console()
    header = Figlet(font="small", width=100).renderText("Astronomical Data")
    logger.info("Displaying Astronomical Data header.")
    console.print(f"[bold magenta]{header}[/bold magenta]")
    sunrise_local = astro.sunrise.astimezone(settings.tz)
    date_art = Figlet(font="mini", width=150).renderText(
        sunrise_local.strftime("%A, %B %d, %Y")
    )
    logger.info(f'Displaying date: {sunrise_local.strftime("%A, %B %d, %Y")}')
    console.print(f"[bold cyan]{date_art}[/bold cyan]")
    for name, value in astro.formatted(settings.tz, settings.DATE_FORMAT).items():
        label = name.replace("_", " ").title()
        logger.info(f"Displaying {label}: {value}")
        console.print(f"[bold cyan]{label}: [white]{value}[/white]")
