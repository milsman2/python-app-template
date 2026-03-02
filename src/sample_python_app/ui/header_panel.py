"""Header panel for synthwave dashboards."""

from pyfiglet import Figlet
from rich.align import Align
from rich.console import Group
from rich.panel import Panel
from rich.text import Text

from sample_python_app.core import Settings
from sample_python_app.models import AstronomicalData


def build_header_panel(
    astro: AstronomicalData, settings: Settings, *, preferred_height: int | None = None
) -> Panel:
    """Build the compact header panel used by dashboards.

    The optional ``preferred_height`` is informational and intended to be
    used by callers when placing the panel into a ``rich.layout.Layout``.
    The panel itself remains flexible and does not enforce a fixed height.
    """
    sunrise_local = astro.sunrise.astimezone(settings.tz)
    # Render as three stacked lines: SYNTHWAVE, SUNRISE, then the date
    header_main = Figlet(font="slant", width=80).renderText("SYNTHWAVE")
    header_main_text = Text(header_main, style="bold magenta")
    header_sub = Figlet(font="small", width=80).renderText("SUNRISE")
    header_sub_text = Text(header_sub, style="bold yellow")
    date_str = sunrise_local.strftime("%A, %B %d, %Y")
    date_text = Text(date_str, style="bold cyan")
    content = Group(
        Align.center(header_main_text),
        Align.center(header_sub_text),
        Align.center(date_text),
    )
    # Vertically center the header + date within the panel
    return Panel(
        Align(content, align="center", vertical="middle"),
        title="[bold #ff6ec7]Synthwave[/bold #ff6ec7]",
        border_style="#ff00cc",
        padding=(0, 1),
    )
