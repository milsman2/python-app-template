"""
Test for minimal figlet output using Rich and pyfiglet.
"""

from pyfiglet import Figlet
from rich.console import Console


def test_figlet_rich_output(capfd):
    console = Console()
    f = Figlet(font="slant")
    ascii_art = f.renderText("Hello, Synthwave!")
    console.print(f"[bold magenta]{ascii_art}[/bold magenta]")
    out, _ = capfd.readouterr()
    # Check for a distinctive substring from the ASCII art output
    assert "__  __" in out or "/ / / /__" in out
