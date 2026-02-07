"""
Main entry point for the python-app-template project.
"""

from pyfiglet import Figlet
from rich.console import Console

from sample_python_app.core import settings, setup_logger


def run_app():
    console = Console()
    f = Figlet(font="slant")
    ascii_art = f.renderText(f"Welcome to {settings.APP_NAME}!")
    console.print(f"[bold magenta]{ascii_art}[/bold magenta]")
    logger = setup_logger(mode="silent")
    logger.info(f"Starting {settings.APP_NAME}...")
    logger.info("Hello from python-app-template!")


if __name__ == "__main__":  # pragma: no cover
    run_app()
