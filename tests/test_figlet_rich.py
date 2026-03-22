"""Test for minimal figlet output using Rich and pyfiglet."""

from pyfiglet import Figlet
from rich.console import Console


def test_figlet_rich_output(capfd):
    """Test Rich and pyfiglet output to stdout."""

    def test_figlet_rich_empty_string(capfd):
        """Test Rich and pyfiglet output with empty string."""
        """Test Rich and pyfiglet output with empty string."""
        console = Console()
        f = Figlet(font="slant")
        ascii_art = f.renderText("")
        console.print(f"[bold magenta]{ascii_art}[/bold magenta]")
        out, _ = capfd.readouterr()
        # Output should still be a string, possibly just newlines
        assert isinstance(out, str)

    """Test Rich and pyfiglet output to stdout."""
    console = Console()
    f = Figlet(font="slant")
    ascii_art = f.renderText("Hello, Synthwave!")
    console.print(f"[bold magenta]{ascii_art}[/bold magenta]")
    out, _ = capfd.readouterr()
    # Check for a distinctive substring from the ASCII art output
    assert "__  __" in out or "/ / / /__" in out
