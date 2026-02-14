"""Handles formatting and displaying astronomical data using rich and pyfiglet."""

from sample_python_app.core.config import settings


def display_astronomical_data(astro):
    """Display astronomical data using the synthwave terminal UI."""
    from sample_python_app.ui.synthwave import synthwave_display

    synthwave_display(astro, settings)
